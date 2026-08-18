# -*- coding: utf-8 -*-
"""Capa de datos: series de 15 min de julio 2026 para FV (Santiago), eólico (Biobío) y BESS.
FV usa geometría solar real vía pvlib. Eólico usa Weibull + curva de potencia. BESS deriva del despacho."""
import pvlib, pandas as pd, numpy as np
from pvlib.location import Location

FREQ='15min'; PASO=0.25
def _idx(lat_tz): return pd.date_range('2026-07-01','2026-07-31 23:45',freq=FREQ,tz=lat_tz)

# ---------------- SOLAR FV — Santiago ----------------
def solar(seed=42):
    LAT,LON,ALT,TZ=-33.45,-70.67,570,'America/Santiago'
    idx=_idx(TZ); loc=Location(LAT,LON,TZ,ALT,'Santiago')
    cs=loc.get_clearsky(idx); sp=loc.get_solarposition(idx)
    rng=np.random.default_rng(seed)
    dk=pd.Index(idx.strftime('%Y-%m-%d')); ud=pd.unique(dk)
    f=pd.Series(np.clip(rng.normal(1.0,0.20,len(ud)),0.45,1.30),index=ud)
    ghi=(cs['ghi']*0.54*pd.Series(f.reindex(dk).values,index=idx)).clip(lower=0)
    e=pvlib.irradiance.erbs(ghi,sp['zenith'],idx)
    tr=pvlib.tracking.singleaxis(sp['apparent_zenith'],sp['azimuth'],0,0,max_angle=55,backtrack=True,gcr=0.35)
    poa=pvlib.irradiance.get_total_irradiance(tr['surface_tilt'].fillna(0),tr['surface_azimuth'].fillna(0),
        sp['apparent_zenith'],sp['azimuth'],e['dni'].fillna(0).clip(lower=0),ghi,e['dhi'].fillna(0).clip(lower=0),
        model='haydavies',dni_extra=pvlib.irradiance.get_extra_radiation(idx))
    POA=poa['poa_global'].fillna(0).clip(lower=0)
    doy=idx.dayofyear.values; hr=idx.hour.values+idx.minute.values/60
    tamb=pd.Series(14.0+8.5*np.cos(2*np.pi*(doy-15)/365)+6.5*np.sin(np.pi*np.clip((hr-7)/11,0,1)),index=idx)
    tc=pvlib.temperature.faiman(POA,tamb,wind_speed=2.0)
    PDC,PAC=156e3,120e3
    dc=PDC*(POA/1000)*(1+(-0.0035)*(tc-25))*(1-0.02-0.029-0.013-0.009)
    ac=(pd.Series(np.minimum(dc*0.985,PAC),index=idx).clip(lower=0)*(1-0.015-0.020-0.015))/1000  # MW
    return dict(tec='solar',idx=idx,pot=ac,PN=PAC/1000,POA=POA,ghi=ghi,tamb=tamb,tcell=tc,
                extra=dict(PDC=PDC/1000))

# ---------------- EÓLICO — Biobío ----------------
def eolico(seed=11):
    TZ='America/Santiago'; idx=_idx(TZ)
    rng=np.random.default_rng(seed)
    n=len(idx)
    # proceso autorregresivo -> Weibull(k=2.1, c=9.6) a altura de buje
    z=np.zeros(n); a=0.985
    for i in range(1,n): z[i]=a*z[i-1]+rng.normal(0,1)*np.sqrt(1-a*a)
    u=pd.Series(z,index=idx).rank(pct=True).clip(1e-4,1-1e-4)
    k,c=2.1,9.6
    v=c*(-np.log(1-u))**(1/k)
    # ciclo diurno leve (más viento de tarde/noche)
    hr=idx.hour.values+idx.minute.values/60
    v=v*(1+0.10*np.sin(2*np.pi*(hr-9)/24))
    v=pd.Series(v,index=idx).clip(0,28)
    # curva de potencia 4,5 MW: arranque 3, nominal 12, corte 25
    def cp(x):
        if x<3 or x>=25: return 0.0
        if x>=12: return 4.5
        return 4.5*((x**3-3**3)/(12**3-3**3))
    NT=24; PN=NT*4.5
    pot=v.map(cp)*NT
    rho=1.196+0.012*np.sin(2*np.pi*(idx.dayofyear.values)/365)
    pot=pot*(pd.Series(rho,index=idx)/1.225)**(1/3)
    # estela + pérdidas eléctricas
    pot=(pot*0.936*0.982).clip(0,PN)
    tamb=pd.Series(9.0+3.0*np.sin(np.pi*np.clip((hr-7)/11,0,1))+rng.normal(0,0.6,n),index=idx)
    return dict(tec='eolico',idx=idx,pot=pot,PN=PN,vel=v,tamb=tamb,
                extra=dict(NT=NT,rho=float(np.mean(rho))))

# ---------------- BESS ----------------
def bess(seed=5):
    TZ='America/Santiago'; idx=_idx(TZ); rng=np.random.default_rng(seed)
    PN,CAP=200.0,800.0     # MW / MWh
    hr=idx.hour.values+idx.minute.values/60
    # carga 09-16 (excedente solar), descarga 18-23 (punta)
    carga=np.where((hr>=9)&(hr<16),1.0,0.0)
    desc =np.where((hr>=18)&(hr<23),1.0,0.0)
    jit=rng.normal(1.0,0.06,len(idx)).clip(0.8,1.2)
    p=(-carga*PN*0.62 + desc*PN*0.72)*jit      # negativo = carga
    p=pd.Series(p,index=idx)
    # SOC con eficiencias
    ec,ed=0.932,0.932
    soc=np.zeros(len(idx)); soc[0]=45.0
    for i in range(1,len(idx)):
        e=p.iloc[i]*PASO
        soc[i]=soc[i-1]+(-e*ec if e<0 else -e/ed)/CAP*100
        soc[i]=min(95.0,max(8.0,soc[i]))
    soc=pd.Series(soc,index=idx)
    # recortar potencia cuando SOC toca límites
    p=p.where(~((soc>=94.9)&(p<0)),0.0).where(~((soc<=8.1)&(p>0)),0.0)
    tamb=pd.Series(9.0+3.0*np.sin(np.pi*np.clip((hr-7)/11,0,1)),index=idx)
    track=pd.Series(np.clip(22+8*(p.abs()/PN)+rng.normal(0,1.0,len(idx)),16,36),index=idx)
    return dict(tec='bess',idx=idx,pot=p,PN=PN,soc=soc,tamb=tamb,track=track,
                extra=dict(CAP=CAP,ec=ec,ed=ed))

# ---------------- agregación diaria ----------------
def diario(d, umbral_frac=0.005):
    """Agregación diaria. Cada tecnología define su propia noción de 'operación'."""
    pot=d['pot']; PN=d['PN']; U=PN*umbral_frac; out=[]
    for day,g in pot.groupby(pot.index.date):
        if d['tec']=='bess':
            soc=d['soc'][d['soc'].index.date==day]
            car=-g[g<0].sum()*PASO; des=g[g>0].sum()*PASO
            gc=g[g<-U]; gd=g[g>U]
            ini_c=gc.index[0].strftime('%H:%M') if len(gc) else '—'
            fin_c=gc.index[-1].strftime('%H:%M') if len(gc) else '—'
            ini_d=gd.index[0].strftime('%H:%M') if len(gd) else '—'
            fin_d=gd.index[-1].strftime('%H:%M') if len(gd) else '—'
            soc_i,soc_f=soc.iloc[0],soc.iloc[-1]
            cerrado=abs(soc_f-soc_i)<=2.0          # regla de ciclo cerrado
            out.append(dict(dia=day.day,ini_c=ini_c,fin_c=fin_c,ini_d=ini_d,fin_d=fin_d,
                horas=round((len(gc)+len(gd))*PASO,2),carga=round(car,0),desc=round(des,0),
                rte=(round(des/car*100,1) if (car>0 and cerrado) else None),
                cerrado=bool(cerrado),soc_i=round(soc_i,1),soc_f=round(soc_f,1),
                ciclos=round(des/d['extra']['CAP'],2),soc_min=round(soc.min(),1),soc_max=round(soc.max(),1),
                fp=round(des/(PN*24)*100,1),pk=round(g.abs().max(),1)))
        elif d['tec']=='eolico':
            v=d['vel'][d['vel'].index.date==day]
            op=g[g>U]; mwh=g.sum()*PASO; horas=len(op)*PASO
            bajo=float((v<3.0).sum()*PASO); sobre=float((v>=25.0).sum()*PASO)
            out.append(dict(dia=day.day,ini=op.index[0].strftime('%H:%M') if len(op) else '—',
                fin=op.index[-1].strftime('%H:%M') if len(op) else '—',horas=round(horas,2),
                bajo=round(bajo,2),sobre=round(sobre,2),vel=round(v.mean(),2),
                mwh=round(mwh,0),fp=round(mwh/(PN*24)*100,1),
                fpop=round(mwh/(PN*horas)*100,1) if horas>0 else 0.0,pk=round(g.max(),1)))
        else:
            op=g[g>U]
            if len(op)==0: continue
            mwh=g.sum()*PASO; horas=len(op)*PASO
            poa=d['POA'][d['POA'].index.date==day].sum()*PASO/1000
            out.append(dict(dia=day.day,ini=op.index[0].strftime('%H:%M'),fin=op.index[-1].strftime('%H:%M'),
                horas=round(horas,2),poa=round(poa,2),mwh=round(mwh,0),fp=round(mwh/(PN*24)*100,1),
                fpop=round(mwh/(PN*horas)*100,1),pk=round(g.max(),1)))
    return pd.DataFrame(out)

if __name__=="__main__":
    for fn in (solar,eolico,bess):
        d=fn(); df=diario(d)
        print(f"\n=== {d['tec'].upper()} ===  PN={d['PN']:.0f} MW  días={len(df)}")
        print(df.head(3).to_string(index=False))
        if d['tec']=='bess':
            print(f"mes: carga={df.carga.sum():,.0f} desc={df.desc.sum():,.0f} RTE={df.desc.sum()/df.carga.sum()*100:.1f}% ciclos={df.ciclos.sum():.1f}")
        else:
            print(f"mes: gen={df.mwh.sum():,.0f} MWh  FP={df.fp.mean():.1f}%  horas op medias={df.horas.mean():.2f}")
