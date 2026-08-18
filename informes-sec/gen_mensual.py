# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
import pandas as pd, numpy as np
from _base import *
import datos as D
from gen_informes import CFG, kv, portada, PIE
UMB=90.0
def op(c): return f"QOR-{c['ref']}-M-202607"

def tabla_dias(df,tec):
    h=[]
    if tec=='bess':
        h=("<tr><th>Día</th><th style='text-align:right'>Ini carga</th><th style='text-align:right'>Fin carga</th>"
           "<th style='text-align:right'>Ini desc.</th><th style='text-align:right'>Fin desc.</th>"
           "<th style='text-align:right'>Carga MWh</th><th style='text-align:right'>Desc. MWh</th>"
           "<th style='text-align:right'>RTE %</th><th style='text-align:right'>Ciclos</th>"
           "<th style='text-align:right'>FP %</th><th>Ciclo</th></tr>")
        r=""
        for i,x in df.iterrows():
            alt=' class="alt"' if i%2 else ''
            rte=f"{x.rte:.1f}" if x.cerrado else "—"
            ch='<span class="chip c-ok">Cerrado</span>' if x.cerrado else '<span class="chip c-hold">Retenido</span>'
            r+=(f"<tr{alt}><td class='n'>{x.dia:02d}</td><td class='n'>{x.ini_c}</td><td class='n'>{x.fin_c}</td>"
                f"<td class='n'>{x.ini_d}</td><td class='n'>{x.fin_d}</td><td class='n'>{x.carga:,.0f}</td>"
                f"<td class='n'>{x.desc:,.0f}</td><td class='n'>{rte}</td><td class='n'>{x.ciclos:.2f}</td>"
                f"<td class='n'>{x.fp:.1f}</td><td>{ch}</td></tr>")
        cc=df[df.cerrado]
        r+=(f"<tr style='border-top:1.4px solid var(--navy);font-weight:600;'><td>Mes</td><td class='n'>—</td><td class='n'>—</td>"
            f"<td class='n'>—</td><td class='n'>—</td><td class='n'>{df.carga.sum():,.0f}</td><td class='n'>{df.desc.sum():,.0f}</td>"
            f"<td class='n'>{cc.desc.sum()/cc.carga.sum()*100:.1f}</td><td class='n'>{df.ciclos.sum():.1f}</td>"
            f"<td class='n'>{df.fp.mean():.1f}</td><td></td></tr>")
        return h+r
    rec = "POA kWh/m²" if tec=='solar' else "Viento m/s"
    h=("<tr><th>Día</th><th style='text-align:right'>Inicio</th><th style='text-align:right'>Término</th>"
       f"<th style='text-align:right'>Horas op.</th><th style='text-align:right'>{rec}</th>"
       "<th style='text-align:right'>Generación MWh</th><th style='text-align:right'>FP día %</th>"
       "<th style='text-align:right'>FP oper. %</th><th style='text-align:right'>P máx MW</th><th>Estado</th></tr>")
    r=""
    for i,x in df.iterrows():
        alt=' class="alt"' if i%2 else ''
        val=f"{x.poa:.2f}" if tec=='solar' else f"{x.vel:.2f}"
        ch='c-ok' if x.fp>=df.fp.mean()*0.8 else ('c-warn' if x.fp>=df.fp.mean()*0.5 else 'c-hold')
        et="Nominal" if ch=='c-ok' else ("Bajo recurso" if ch=='c-warn' else "Recurso mínimo")
        r+=(f"<tr{alt}><td class='n'>{x.dia:02d}</td><td class='n'>{x.ini}</td><td class='n'>{x.fin}</td>"
            f"<td class='n'>{x.horas:.2f}</td><td class='n'>{val}</td><td class='n'>{x.mwh:,.0f}</td>"
            f"<td class='n'>{x.fp:.1f}</td><td class='n'>{x.fpop:.1f}</td><td class='n'>{x.pk:.1f}</td>"
            f"<td><span class='chip {ch}'>{et}</span></td></tr>")
    tv=f"{df.poa.sum():.1f}" if tec=='solar' else f"{df.vel.mean():.2f}"
    r+=(f"<tr style='border-top:1.4px solid var(--navy);font-weight:600;'><td>Mes</td><td class='n'>{df.ini.min()}</td>"
        f"<td class='n'>{df.fin.max()}</td><td class='n'>{df.horas.sum():.1f}</td><td class='n'>{tv}</td>"
        f"<td class='n'>{df.mwh.sum():,.0f}</td><td class='n'>{df.fp.mean():.1f}</td><td class='n'>{df.fpop.mean():.1f}</td>"
        f"<td class='n'>{df.pk.max():.1f}</td><td></td></tr>")
    return h+r

def mensual(tec):
    c=CFG[tec]; d=getattr(D,tec)(); df=D.diario(d); REF=op(c)
    P=[portada(c,"Informe Mensual de Verificación Independiente",
       "Consolidado del período con opinión de verificación. Cada cifra conserva su canal de origen, su transformación y su porcentaje de cobertura.",
       kv(("Instalación",c['nom']),("Ubicación",f"{c['com']}, {c['reg']}"),("Capacidad",c['cap']),
          ("Período informado","01 – 31 julio 2026 (744 horas)"),("Referencia",REF)),"Informe mensual · muestra")]
    if tec=='bess':
        cc=df[df.cerrado]; rte=cc.desc.sum()/cc.carga.sum()*100
        naive=df.desc.sum()/df.carga.sum()*100
        k1=kpi("Disponibilidad certificada","99,03%","7 de 8 unidades","#149487")
        k2=kpi("Eficiencia RTE",f"{rte:.1f}%",f"{len(cc)} ciclos cerrados")
        k3=kpi("Ciclos equivalentes",f"{df.ciclos.sum():.1f}","del período")
        k4=kpi("Cobertura de datos","98,9%","unidades certificadas")
        op_txt=(f"<p>La disponibilidad técnica del período se certifica en <b>99,03%</b>. La eficiencia de ciclo completo se determina en "
                f"<b>{rte:.1f}%</b>, calculada exclusivamente sobre los <b>{len(cc)} ciclos cerrados</b> de los {len(df)} días del período.</p>"
                f"<p>El día <b>{int(df[~df.cerrado].dia.iloc[0]):02d}</b> se excluye del cálculo de eficiencia: el SOC inicial "
                f"({df[~df.cerrado].soc_i.iloc[0]:.1f}%) y final ({df[~df.cerrado].soc_f.iloc[0]:.1f}%) difieren en más de 2 puntos, "
                f"de modo que la descarga incorpora energía almacenada el día anterior. Incluirlo habría arrojado <b>{naive:.1f}%</b>, "
                f"cifra que mezcla energía medida con energía heredada y no es defendible.</p>")
        caja=(f'<div class="box amber"><h4>La diferencia entre {rte:.1f}% y {naive:.1f}%</h4>'
              f'<p style="margin-bottom:0;">Son 1,2 puntos porcentuales sobre el mismo conjunto de datos. La diferencia no está en la medición sino '
              f'en la regla de cálculo. Un informe que publique {naive:.1f}% no está equivocado por error de instrumentación: está equivocado por no '
              f'declarar qué ciclos entraron en el denominador.</p></div>')
        graf=bars_svg([f"{int(x.dia)}" if x.dia%3==1 else "" for _,x in df.iterrows()],
                      [float(x.rte) if x.cerrado else 0.0 for _,x in df.iterrows()],rte,thr_label=f"media {rte:.1f}%")
        gcap=(f"Eficiencia de ciclo completo por día. La barra en cero corresponde al día {int(df[~df.cerrado].dia.iloc[0]):02d}, "
              f"cuyo ciclo no cerró y cuya cifra se retiene.")
    else:
        gen=df.mwh.sum(); disp=98.10 if tec=='solar' else 97.60
        k1=kpi("Disponibilidad certificada",f"{disp:.2f}%",f"{c['n']-1} de {c['n']} unidades","#149487")
        k2=kpi("Generación",f"{gen:,.0f}","MWh certificados")
        k3=kpi("Factor de planta",f"{df.fp.mean():.1f}%","medio del período")
        k4=kpi("Horas de operación",f"{df.horas.sum():.0f} h",f"{df.horas.mean():.2f} h/día")
        rec=("irradiancia en el plano del generador" if tec=='solar' else "velocidad de viento a altura de buje")
        op_txt=(f"<p>La disponibilidad técnica del período se certifica en <b>{disp:.2f}%</b>, sustentada en cobertura observada sobre las "
                f"unidades certificadas. La generación certificada asciende a <b>{gen:,.0f} MWh</b>, equivalente a un factor de planta medio "
                f"de <b>{df.fp.mean():.1f}%</b> sobre 24 horas y de <b>{df.fpop.mean():.1f}%</b> sobre horas efectivas de operación.</p>"
                f"<p>El activo operó <b>{df.horas.sum():.0f} horas</b> en el mes, con un promedio de <b>{df.horas.mean():.2f} horas diarias</b>. "
                f"La dispersión diaria del factor de planta (entre {df.fp.min():.1f}% y {df.fp.max():.1f}%) es atribuible a la variabilidad del "
                f"recurso — {rec} — y no al estado del activo.</p>")
        caja=(f'<div class="box teal"><h4>Recurso y activo son cosas distintas</h4>'
              f'<p style="margin-bottom:0;">El factor de planta diario varió entre {df.fp.min():.1f}% y {df.fp.max():.1f}% durante el período, '
              f'un rango de {df.fp.max()/max(df.fp.min(),0.1):.1f}× entre el mejor y el peor día. En el mismo período la disponibilidad técnica se '
              f'mantuvo sobre 96% todos los días. Una central que no puede generar y una a la que no le llega recurso producen la misma cifra de '
              f'energía y requieren decisiones opuestas.</p></div>')
        graf=bars_svg([f"{int(x.dia)}" if x.dia%3==1 else "" for _,x in df.iterrows()],
                      [float(x.fp) for _,x in df.iterrows()],float(df.fp.mean()),thr_label=f"media {df.fp.mean():.1f}%")
        gcap="Factor de planta diario sobre 24 horas, con la media del período como referencia."
    P.append(page(f"""<div class="sec-num">01 · Opinión de verificación independiente</div>
<div class="eyebrow">Conclusión del período</div><h2 class="t">Opinión sobre el desempeño informado</h2>
<div class="kpis">{k1}{k2}{k3}{k4}</div>
<h3 class="t">Base de la opinión</h3>
<p>El motor de verificación de Quorelia ingirió y validó de forma continua los datos de la instalación sobre los sistemas SCADA ya desplegados. Esta opinión se sustenta en la cobertura de datos, las verificaciones de consistencia y la reconciliación cruzada entre fuentes durante el período informado.</p>
<h3 class="t">Responsabilidades</h3>
<p><b>Del titular:</b> la operación e instrumentación de la instalación, y proveer acceso continuo y sin obstrucción a los sistemas desde los cuales se derivan las cifras informadas. <b>De Quorelia:</b> la integridad de la cadena de validación aplicada a los datos recibidos, y declarar — en lugar de estimar — todo período en que la cobertura no sustente una cifra defendible.</p>
<h3 class="t">Opinión</h3>{op_txt}{caja}""",f"{REF} · Muestra","02"))
    P.append(page(f"""<div class="sec-num">02 · Detalle diario del período</div>
<div class="eyebrow">31 días</div><h2 class="t">Operación día a día</h2>
<p class="small">Horarios determinados por el primer y último registro de 15 minutos sobre el 0,5% de la potencia nominal. Todas las cifras provienen del mismo proceso automatizado, sin transcripción manual.</p>
<table style="font-size:8.4px;">{tabla_dias(df,tec)}</table>{PIE}""",f"{REF} · Muestra","03"))
    P.append(page(f"""<div class="sec-num">03 · Evolución del período</div>
<div class="eyebrow">Serie diaria</div><h2 class="t">Comportamiento a lo largo del mes</h2>
{graf}
<p class="small">{gcap}</p>
<h3 class="t">Estadística del período</h3>
<table><tr><th>Indicador</th><th style="text-align:right">Media</th><th style="text-align:right">Máximo</th><th style="text-align:right">Mínimo</th><th style="text-align:right">Desv. relativa</th></tr>
<tr><td>Factor de planta diario</td><td class="n">{df.fp.mean():.1f}%</td><td class="n">{df.fp.max():.1f}%</td><td class="n">{df.fp.min():.1f}%</td><td class="n">{df.fp.std()/df.fp.mean()*100:.0f}%</td></tr>
{"".join([f'<tr class="alt"><td>Horas en operación</td><td class="n">{df.horas.mean():.2f} h</td><td class="n">{df.horas.max():.2f} h</td><td class="n">{df.horas.min():.2f} h</td><td class="n">{df.horas.std()/df.horas.mean()*100:.0f}%</td></tr>'])}
{"".join([f'<tr><td>Potencia máxima diaria</td><td class="n">{df.pk.mean():.1f} MW</td><td class="n">{df.pk.max():.1f} MW</td><td class="n">{df.pk.min():.1f} MW</td><td class="n">{df.pk.std()/df.pk.mean()*100:.0f}%</td></tr>'])}
</table>
<div class="box"><h4>Trazabilidad</h4>
<p style="margin-bottom:0;">Cada cifra de este informe conserva su canal de origen, su transformación y su porcentaje de cobertura. Ante requerimiento, cualquier valor puede reproducirse hasta la medición cruda que lo sustenta, sin intervención manual. El informe diario de cada uno de estos 31 días fue emitido automáticamente a las 00:15 del día siguiente.</p></div>{PIE}""",
f"{REF} · Muestra","04"))
    open(f"Informe-Mensual-{c['ref']}.html","w",encoding="utf-8").write(doc(f"Quorelia — {c['nom']} — Informe Mensual","".join(P)))
    return len(P)

for t in ('solar','eolico','bess'):
    print(f"mensual {t}: {mensual(t)} páginas")
