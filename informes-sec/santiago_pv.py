# -*- coding: utf-8 -*-
"""Modelo FV Santiago (-33.45, -70.67) con pvlib. Reproducible: semilla fija."""
import pvlib, pandas as pd, numpy as np
from pvlib.location import Location
LAT,LON,ALT,TZ=-33.45,-70.67,570,'America/Santiago'
def run(seed=42):
    loc=Location(LAT,LON,TZ,ALT,'Santiago')
    idx=pd.date_range('2026-01-01','2026-12-31 23:00',freq='h',tz=TZ)
    cs=loc.get_clearsky(idx); sp=loc.get_solarposition(idx)
    kt={1:.83,2:.82,3:.79,4:.71,5:.58,6:.51,7:.54,8:.61,9:.69,10:.76,11:.81,12:.84}
    k=pd.Series(idx.month,index=idx).map(kt).astype(float)
    # variabilidad dia a dia (nubosidad), reproducible
    rng=np.random.default_rng(seed)
    dkey=pd.Index(idx.strftime('%Y-%m-%d'))
    ud=pd.unique(dkey)
    f=pd.Series(np.clip(rng.normal(1.0,0.20,len(ud)),0.45,1.30),index=ud)
    k=k*pd.Series(f.reindex(dkey).values,index=idx)
    ghi=(cs['ghi']*k).clip(lower=0)
    e=pvlib.irradiance.erbs(ghi,sp['zenith'],idx)
    dni=e['dni'].fillna(0).clip(lower=0); dhi=e['dhi'].fillna(0).clip(lower=0)
    tr=pvlib.tracking.singleaxis(sp['apparent_zenith'],sp['azimuth'],axis_tilt=0,axis_azimuth=0,
                                 max_angle=55,backtrack=True,gcr=0.35)
    poa=pvlib.irradiance.get_total_irradiance(tr['surface_tilt'].fillna(0),tr['surface_azimuth'].fillna(0),
         sp['apparent_zenith'],sp['azimuth'],dni,ghi,dhi,model='haydavies',
         dni_extra=pvlib.irradiance.get_extra_radiation(idx))
    POA=poa['poa_global'].fillna(0).clip(lower=0)
    # temperatura: hemisferio SUR -> enero calido, julio frio
    doy=idx.dayofyear.values; hr=idx.hour.values
    tamb=pd.Series(14.0+8.5*np.cos(2*np.pi*(doy-15)/365)+6.5*np.sin(np.pi*np.clip((hr-7)/11,0,1)),index=idx)
    tcell=pvlib.temperature.faiman(POA,tamb,wind_speed=2.0)
    PDC,PAC=156e3,120e3
    dc=PDC*(POA/1000)*(1+(-0.0035)*(tcell-25))*(1-0.02-0.029-0.013-0.009)
    ac=pd.Series(np.minimum(dc*0.985,PAC),index=idx).clip(lower=0)
    return dict(idx=idx,ghi=ghi,poa=POA,tamb=tamb,tcell=tcell,ac=ac,PAC=PAC,PDC=PDC)
if __name__=="__main__":
    r=run(); ghi,ac,POA,tamb,tcell=r['ghi'],r['ac'],r['poa'],r['tamb'],r['tcell']
    GA=ghi.sum()/1000
    print(f"GHI anual        : {GA:,.0f} kWh/m2   [Explorador Solar 1.750-1.900] {'OK' if 1750<=GA<=1900 else 'REVISAR'}")
    print(f"POA anual        : {POA.sum()/1000:,.0f} kWh/m2  (ganancia seguidor {POA.sum()/ghi.sum()-1:+.1%})")
    print(f"Generacion anual : {ac.sum()/1000:,.0f} MWh  CF {ac.sum()/(r['PAC']*8760)*100:.1f}%")
    print(f"Tamb enero med   : {tamb[r['idx'].month==1].mean():.1f} C   julio med: {tamb[r['idx'].month==7].mean():.1f} C  <- hemisferio sur OK")
    j=ac['2026-07']; gj=ghi['2026-07']; pj=POA['2026-07']
    print(f"\nJULIO: gen={j.sum()/1000:,.0f} MWh  CF={j.sum()/(r['PAC']*744)*100:.1f}%  GHI={gj.sum()/1000:.1f}  POA={pj.sum()/1000:.1f} kWh/m2")
    print(f"       Tamb {tamb['2026-07'].min():.1f} a {tamb['2026-07'].max():.1f} C | Tcelda max {tcell['2026-07'].max():.1f} C")
    d=(j.resample('D').sum()/1000)
    print(f"       diario MWh: min={d.min():.0f} max={d.max():.0f} media={d.mean():.0f}  (variabilidad {d.std()/d.mean()*100:.0f}%)")
