# -*- coding: utf-8 -*-
import sys,json; sys.path.insert(0,'.')
import numpy as np, pandas as pd
from _base import *
DD=pd.read_json('/tmp/diario.json')
M=json.load(open('/tmp/pv.json'))
perf=np.load('/tmp/perf.npy'); perfh=np.load('/tmp/perfh.npy')
dia=np.load('/tmp/dia.npy'); poad=np.load('/tmp/poad.npy')
mens=np.load('/tmp/mens.npy'); ghim=np.load('/tmp/ghim.npy'); einv=np.load('/tmp/einv.npy')
REF="QOR-SEC-2026-08-PV-01"; PER="01 – 31 julio 2026"; H=744
NOM="Planta Solar Cerro Tinaja"; REG="Región Metropolitana de Santiago"
PAC=120.0; PDC=156.0; UMBRAL=90.0
COB=[99.1,98.8,99.1,98.6,99.1,97.9,99.1,98.5,99.1,98.7,51.2,99.0]
DIS=[98.6,98.1,99.0,97.4,98.5,96.2,98.9,97.6,98.4,97.7,None,98.7]
ids=[f"INV-{i:02d}" for i in range(1,13)]
E=list(einv[:10])+[None]+[einv[10]]
gen=int(sum(x for x in E if x))
GEN_TOT=int(M['gen15']); cob=np.mean([c for c in COB if c>=UMBRAL])
disp=np.mean([d for d in DIS if d]); PR=M['PR']; CF=M['CF']
P50=8650; desv=(gen-P50)/P50*100
MES=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
print(f"gen={gen} PR={PR:.1f} CF={CF:.1f} desv={desv:+.2f}")
P=[]
P.append(page(f"""<div class="page-in" style="min-height:9.6in;display:flex;flex-direction:column;">
<div style="font-family:var(--mono);font-size:16px;letter-spacing:.28em;font-weight:600;">QUORELIA</div>
<div style="font-family:var(--mono);font-size:8px;letter-spacing:.2em;color:var(--teal);margin-top:6px;">INTELIGENCIA EN ENERGÍA RENOVABLE</div>
<div style="margin-top:26px;"><span class="wm">Informe de muestra · recurso solar real de Santiago</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
<div style="font-family:var(--mono);font-size:9px;letter-spacing:.18em;color:var(--teal);margin-bottom:14px;">CENTRAL FOTOVOLTAICA · PV</div>
<h1 style="font-size:34px;line-height:1.12;font-weight:500;letter-spacing:-.03em;max-width:6.2in;">Informe de Verificación Independiente y Desempeño Operacional</h1>
<p style="color:var(--ink-2);font-size:11px;max-width:5.4in;margin-top:14px;">Perfil de recurso solar calculado para las coordenadas de Santiago (33,45° S · 70,67° O) mediante modelos NREL SPA e Ineichen, contrastado con el Explorador Solar del Ministerio de Energía.</p>
<table class="kv" style="margin-top:26px;max-width:5.6in;">
<tr><td style="color:var(--grey);">Instalación</td><td style="color:var(--ink);">{NOM}</td></tr>
<tr><td style="color:var(--grey);">Ubicación</td><td style="color:var(--ink);">{REG}, Chile</td></tr>
<tr><td style="color:var(--grey);">Capacidad</td><td style="color:var(--ink);">{PAC:.0f} MWac / {PDC:.0f} MWp</td></tr>
<tr><td style="color:var(--grey);">Período informado</td><td style="color:var(--ink);">{PER}</td></tr>
<tr><td style="color:var(--grey);">Referencia</td><td style="color:var(--ink);font-family:var(--mono);">{REF}</td></tr></table></div>
<p class="small" style="color:var(--grey);border-top:1px solid var(--line);padding-top:11px;">La instalación, el titular y los hallazgos son ilustrativos. El recurso solar es calculado a partir de la posición geográfica real de Santiago. © 2026 Quorelia.</p></div>""",
"Quorelia · Informe de muestra","01","cover"))

P.append(page(f"""<div class="sec-num">01 · Identificación del activo</div>
<div class="eyebrow">Antecedentes</div><h2 class="t">Identificación y recurso</h2>
<table class="kv">
<tr><td>Nombre de la central</td><td>{NOM} <span class="chip c-info">Entidad ficticia</span></td></tr>
<tr><td>Titular</td><td>Solar Cerro Tinaja SpA (ficticio)</td></tr>
<tr><td>Región / Comuna</td><td>{REG} / Til Til</td></tr>
<tr><td>Coordenadas de referencia</td><td>33,45° S · 70,67° O · 570 m s.n.m.</td></tr>
<tr><td>Tecnología</td><td>Fotovoltaica, seguidor de un eje N–S con backtracking, GCR 0,35</td></tr>
<tr><td>Capacidad instalada</td><td>{PAC:.0f} MWac / {PDC:.0f} MWp (ratio DC/AC {PDC/PAC:.2f})</td></tr>
<tr><td>Inversores monitoreados</td><td>12 unidades de 10 MWac</td></tr>
<tr><td>Período informado</td><td>{PER} ({H} horas)</td></tr>
<tr><td>Resolución de muestreo</td><td>15 minutos · 2.976 muestras esperadas por canal</td></tr></table>
<div class="box teal"><h4>Origen del recurso solar de este informe</h4>
<p>A diferencia de las cifras de desempeño del activo, que son ilustrativas, <b>el recurso solar de este informe no es inventado</b>. La irradiancia se calcula para las coordenadas reales de Santiago mediante:</p>
<table style="margin:8px 0 0;"><tr><th>Componente</th><th>Modelo aplicado</th></tr>
<tr><td>Posición solar</td><td>NREL Solar Position Algorithm (SPA)</td></tr>
<tr class="alt"><td>Irradiancia de cielo despejado</td><td>Ineichen–Perez con turbidez de Linke climatológica</td></tr>
<tr><td>Descomposición directa / difusa</td><td>Erbs</td></tr>
<tr class="alt"><td>Irradiancia en plano inclinado</td><td>Hay–Davies, con seguimiento y backtracking</td></tr>
<tr><td>Temperatura de celda</td><td>Faiman</td></tr></table>
<p class="small" style="margin:8px 0 0;"><b>Validación:</b> la irradiancia global horizontal anual resultante es de <b>{M['ghia']:,.0f} kWh/m²</b>, dentro del rango de <b>1.750 a 1.900 kWh/m²/año</b> que el Explorador Solar del Ministerio de Energía documenta para Santiago. El factor de planta anual del modelo es {M['cfa']:.1f}%, coherente con plantas con seguidor en la zona central.</p></div>
<h3 class="t">Contexto anual — el mes informado es el de menor recurso</h3>
{bars_svg(MES,[round(float(v),0) for v in ghim],None)}
<p class="small">Irradiancia global horizontal mensual, kWh/m². Julio es el mes de mínimo recurso del año en Santiago. Cualquier lectura de la generación de este período debe hacerse contra esa base estacional, no contra el promedio anual.</p>""",
f"{REF} · Muestra ilustrativa","02"))

P.append(page(f"""<div class="sec-num">02 · Opinión de verificación independiente</div>
<div class="eyebrow">Conclusión</div><h2 class="t">Opinión sobre el desempeño informado</h2>
<div class="kpis">
{kpi("Disponibilidad certificada",f"{disp:.2f}%","11 de 12 inversores","#149487")}
{kpi("Performance Ratio",f"{PR:.1f}%","corregido por temperatura")}
{kpi("Cobertura de datos",f"{cob:.1f}%","unidades certificadas")}
{kpi("Generación",f"{gen:,}","MWh certificados")}</div>
<h3 class="t">Opinión</h3>
<p>La disponibilidad técnica del período se certifica en <b>{disp:.2f}%</b>, sustentada en cobertura observada de <b>{cob:.1f}%</b> sobre las unidades certificadas. El Performance Ratio determinado es de <b>{PR:.1f}%</b>, conforme a IEC 61724-1, corregido por irradiancia en el plano del generador y temperatura de módulo.</p>
<p>La generación certificada asciende a <b>{gen:,} MWh</b>, un <b>{desv:+.1f}%</b> respecto de la expectativa P50 del estudio de energía para el mes. El inversor <b>INV-11 se retiene</b> por cobertura de 51,2%, inferior al umbral de {UMBRAL:.0f}%. Véase Sección 05, Hallazgo H-01.</p>
<div class="box amber"><h4>Por qué un PR de {PR:.1f}% no es un error en invierno</h4>
<p style="margin-bottom:0;">El Performance Ratio es estacional. La temperatura media ambiente del período fue de <b>{M['tmed']:.1f} °C</b> y la temperatura máxima de celda alcanzó <b>{M['tcmax']:.1f} °C</b>, por debajo de los 25 °C de condiciones estándar. Con un coeficiente térmico de −0,35 %/°C, operar bajo la temperatura de referencia <b>eleva</b> el rendimiento del módulo. Un PR invernal alto acompañado de una generación baja es el comportamiento esperado: el recurso cae, la eficiencia sube. Confundir ambos indicadores lleva a conclusiones opuestas sobre el estado del activo.</p></div>
<h3 class="t">Separación entre desviación de recurso y desviación de activo</h3>
<table><tr><th>Componente</th><th style="text-align:right">Contribución</th><th>Naturaleza</th></tr>
<tr><td>Irradiancia medida vs. serie del estudio</td><td class="n">-2,8%</td><td>Recurso — fuera del control del titular</td></tr>
<tr class="alt"><td>Ensuciamiento sobre lo previsto</td><td class="n">-1,1%</td><td>Activo — accionable</td></tr>
<tr><td>Indisponibilidad de equipos</td><td class="n">-0,5%</td><td>Activo — accionable</td></tr>
<tr class="alt"><td>Vertimiento por instrucción del Coordinador</td><td class="n">-0,2%</td><td>Sistémico — documentado aparte</td></tr>
<tr><td>No asignado</td><td class="n">{desv+4.6:+.1f}%</td><td>Dentro de la incertidumbre de medición</td></tr>
<tr style="border-top:1.2px solid var(--navy);font-weight:600;"><td>Desviación total vs. P50</td><td class="n">{desv:+.1f}%</td><td></td></tr></table>
<p class="small">Sin esta descomposición, una central mal mantenida en un mes de buen recurso resulta indistinguible de una central bien operada. Es la razón por la cual una cifra de generación, aislada, no permite fiscalizar el desempeño de un activo.</p>""",
f"{REF} · Muestra ilustrativa","03"))

rows=""
for i,(uid,cv,dp,e) in enumerate(zip(ids,COB,DIS,E)):
    alt=' class="alt"' if i%2 else ''
    if cv>=UMBRAL:
        prx=PR*(e/np.mean([x for x in E if x]))
        rows+=f'<tr{alt}><td>{uid}</td><td class="n">2.976</td><td class="n">{cv:.1f}</td><td class="n">{dp:.1f}</td><td class="n">{prx:.1f}</td><td class="n">{int(e):,}</td><td><span class="chip c-ok">Aprobado</span></td></tr>'
    else:
        rows+=f'<tr{alt}><td>{uid}</td><td class="n">1.524</td><td class="n">{cv:.1f}</td><td class="n">—</td><td class="n">—</td><td class="n">—</td><td><span class="chip c-hold">Retenido</span></td></tr>'
P.append(page(f"""<div class="sec-num">03 · Datos de desempeño</div>
<div class="eyebrow">Perfil real de generación</div><h2 class="t">Curva diaria media del período</h2>
<p class="small">Potencia media horaria entregada, MW. Perfil calculado con la geometría solar real de Santiago para julio: salida efectiva cerca de las 08:00, máximo en torno a las 13:00 y caída a las 18:00. La asimetría del perfil refleja la declinación solar invernal en latitud 33° S.</p>
{bars_svg([f"{int(h):02d}" for h in perfh],[round(float(v),1) for v in perf],None)}
<div class="kpis">
{kpi("Potencia máxima media",f"{max(perf):.1f}","MW · hora 13")}
{kpi("Horas con generación",f"{M['horas']}","h del período")}
{kpi("POA medio diario",f"{M['poamed']:.2f}","kWh/m²/día")}
{kpi("Factor de planta",f"{CF:.1f}%","mes de mínimo recurso")}</div>
<h3 class="t">Generación diaria del período</h3>
{line_svg([float(v) for v in dia],labels=["01","07","14","21","28"],ylab="MWh/día")}
<p class="small">Variabilidad diaria de {np.std(dia)/np.mean(dia)*100:.0f}% respecto de la media, entre {min(dia):,.0f} y {max(dia):,.0f} MWh. Esta dispersión es atribuible a nubosidad y corresponde al recurso, no al activo: la disponibilidad técnica se mantuvo sobre 96% en todos los días del período.</p>""",
f"{REF} · Muestra ilustrativa","04"))

P.append(page(f"""<div class="sec-num">03 · Datos de desempeño</div>
<div class="eyebrow">Detalle por inversor</div><h2 class="t">Desempeño por unidad</h2>
<table><tr><th>Unidad</th><th style="text-align:right">Muestras</th><th style="text-align:right">Cobertura %</th><th style="text-align:right">Disponib. %</th><th style="text-align:right">PR %</th><th style="text-align:right">Energía MWh</th><th>Veredicto</th></tr>{rows}
<tr style="border-top:1.4px solid var(--navy);font-weight:600;"><td>Total certificado</td><td class="n">—</td><td class="n">{cob:.1f}</td><td class="n">{disp:.2f}</td><td class="n">{PR:.1f}</td><td class="n">{gen:,}</td><td></td></tr></table>
<h3 class="t">Cobertura de datos por inversor</h3>
{bars_svg([i.replace("INV-","") for i in ids],COB,UMBRAL,thr_label=f"umbral {UMBRAL:.0f}%")}
<h3 class="t">Variables ambientales medidas</h3>
<table><tr><th>Variable</th><th style="text-align:right">Media</th><th style="text-align:right">Máx</th><th style="text-align:right">Mín</th><th>Fuente</th></tr>
<tr><td>Irradiancia POA</td><td class="n">{M['poamed']:.2f} kWh/m²/d</td><td class="n">{max(poad):.2f}</td><td class="n">{min(poad):.2f}</td><td>Estación en sitio (2 sensores)</td></tr>
<tr class="alt"><td>Irradiancia GHI</td><td class="n">{M['ghi']/31:.2f} kWh/m²/d</td><td class="n">—</td><td class="n">—</td><td>Estación en sitio</td></tr>
<tr><td>Temperatura ambiente</td><td class="n">{M['tmed']:.1f} °C</td><td class="n">{M['tmax']:.1f}</td><td class="n">{M['tmin']:.1f}</td><td>Estación en sitio</td></tr>
<tr class="alt"><td>Temperatura de módulo</td><td class="n">—</td><td class="n">{M['tcmax']:.1f}</td><td class="n">—</td><td>Sensor de célula, 6 puntos</td></tr>
<tr><td>Horas de operación con generación</td><td class="n">{M['horas']} h</td><td class="n">—</td><td class="n">—</td><td>SCADA</td></tr></table>
<div class="box"><h4>Contexto estacional de la generación</h4>
<p style="margin-bottom:0;">La generación de julio ({gen:,} MWh certificados) representa aproximadamente un <b>{gen/ (sum(mens)*1000/1000) *100/1:.0f}‰</b> del total anual modelado para esta central. Evaluar el activo contra el promedio anual, y no contra la expectativa del mes, produciría una conclusión errónea sobre su estado.</p></div>""",
f"{REF} · Muestra ilustrativa","05"))


_dr=""
for i,r in DD.iterrows():
    alt=' class="alt"' if i%2 else ''
    ch='c-ok' if r.cf>=9 else ('c-warn' if r.cf>=6 else 'c-hold')
    _dr+=('<tr%s><td class="n">%02d</td><td class="n">%s</td><td class="n">%s</td><td class="n">%.2f</td>'
          '<td class="n">%.2f</td><td class="n">%,d</td><td class="n">%.1f</td><td class="n">%.1f</td>'
          '<td class="n">%.1f</td><td><span class="chip %s">%s</span></td></tr>'
          ).replace("%,d","%s") % (alt,r.dia,r.ini,r.fin,r.horas,r.poa,format(int(r.mwh),","),r.cf,r.cfop,r.pk,ch,
                                   "Nominal" if r.cf>=9 else ("Bajo recurso" if r.cf>=6 else "Recurso mínimo"))
PAG_DIARIA = page(f"""<div class="sec-num">04 · Informe diario del período</div>
<div class="eyebrow">Detalle día a día</div><h2 class="t">Operación diaria: horario, generación y factor de planta</h2>
<p class="small">Horas de inicio y término determinadas por el primer y último registro de 15 minutos con potencia sobre el 0,5% de la potencia nominal ({0.005*120*1000:.0f} kW). <b>FP día</b> se calcula sobre las 24 horas; <b>FP oper.</b> solo sobre las horas efectivas de operación.</p>
<table style="font-size:8.6px;"><tr><th>Día</th><th style="text-align:right">Inicio</th><th style="text-align:right">Término</th><th style="text-align:right">Horas op.</th><th style="text-align:right">POA kWh/m²</th><th style="text-align:right">Generación MWh</th><th style="text-align:right">FP día %</th><th style="text-align:right">FP oper. %</th><th style="text-align:right">P máx MW</th><th>Estado</th></tr>
{_dr}
<tr style="border-top:1.4px solid var(--navy);font-weight:600;"><td>Mes</td><td class="n">{M['ini_min']}–{M['ini_max']}</td><td class="n">{M['fin_min']}–{M['fin_max']}</td><td class="n">{M['horas_tot']:.1f}</td><td class="n">{M['poa_tot']:.1f}</td><td class="n">{GEN_TOT:,}</td><td class="n">{M['cf_med']:.1f}</td><td class="n">{M['cf_op']:.1f}</td><td class="n">{M['pk_max']:.1f}</td><td></td></tr></table>
<div class="kpis">
{kpi("Horas de operación","%.2f h"%M['horas_med'],"promedio diario")}
{kpi("FP diario medio","%.1f%%"%M['cf_med'],"sobre 24 horas")}
{kpi("FP en operación","%.1f%%"%M['cf_op'],"solo horas con sol")}
{kpi("Rango de FP diario","%.1f – %.1f%%"%(M['cf_min'],M['cf_max']),"día %d al día %d"%(M['dia_min'],M['dia_max']))}</div>
<div class="box teal"><h4>El día se alarga durante el mes — y eso se mide</h4>
<p style="margin-bottom:0;">La operación comienza a las <b>{M['ini_max']}</b> los primeros días del mes y a las <b>{M['ini_min']}</b> al cierre; el término se desplaza de <b>{M['fin_min']}</b> a <b>{M['fin_max']}</b>. Son <b>{(M['horas_med']):.2f} horas</b> de operación media diaria, creciendo a lo largo del período por el alejamiento del solsticio de invierno. Este desplazamiento es geometría solar, no comportamiento del activo: una caída del horario de operación que <b>no</b> siga esta curva es una señal de falla, y es detectable exactamente por eso.</p></div>
<h3 class="t">Factor de planta diario</h3>
{bars_svg([("%d"%r.dia) if r.dia%3==1 else "" for _,r in DD.iterrows()],[float(r.cf) for _,r in DD.iterrows()],float(M['cf_med']),thr_label="media del mes %.1f%%"%M['cf_med'])}
<p class="small">Factor de planta diario sobre 24 horas. La dispersión entre {M['cf_min']:.1f}% y {M['cf_max']:.1f}% corresponde íntegramente a nubosidad: la disponibilidad técnica se mantuvo sobre 96% todos los días del período. Es la diferencia entre un activo que no puede generar y un activo al que no le llega recurso.</p>""",
f"{REF} · Muestra ilustrativa","05")

P.append(PAG_DIARIA)
P.append(page(f"""<div class="sec-num">05 · Hallazgos y excepciones</div>
<div class="eyebrow">Excepciones del período</div><h2 class="t">Hallazgos, en orden de materialidad</h2>
<div class="finding hold"><div class="fh"><b>H-01 — Cobertura bajo umbral, INV-11</b><span class="chip c-hold">Retenido</span></div>
<p>Pérdida de comunicación entre el datalogger del bloque 11 y el historiador de planta entre el 9 y el 24 de julio (15,1 días), reduciendo la cobertura a 51,2%. Disponibilidad y PR de INV-11 <b>se retienen</b> en lugar de estimarse, y su energía no se incorpora al total certificado.</p>
<p class="small"><b>Recomendación:</b> reemplazo del módulo de comunicaciones del datalogger 11. Clasificada como <b>correctiva</b>. Se recertificará el período una vez restablecida y validada la cobertura.</p></div>
<div class="finding warn"><div class="fh"><b>H-02 — Ensuciamiento sobre supuesto de diseño</b><span class="chip c-warn">Alerta</span></div>
<p>Pérdida por ensuciamiento estimada 1,1 puntos sobre el supuesto del estudio, sostenida durante las últimas tres semanas y consistente con el período sin precipitación registrado en la zona central.</p>
<p class="small"><b>Recomendación:</b> adelantar el ciclo de lavado. Clasificada como <b>preventiva</b>. Su impacto en julio es acotado por el bajo recurso, pero se materializa al entrar en primavera si no se corrige.</p></div>
<div class="finding warn"><div class="fh"><b>H-03 — Desbalance de corriente de strings, INV-06</b><span class="chip c-warn">Alerta</span></div>
<p>Desbalance detectado en 9 ocasiones en una ventana de 96 horas. INV-06 registra la menor energía y la menor disponibilidad del parque (96,2%), con un patrón compatible con ensuciamiento localizado antes que con falla de equipo.</p>
<p class="small"><b>Recomendación:</b> inspección visual de las filas asociadas durante el ciclo de lavado de H-02. Clasificada como <b>preventiva</b>.</p></div>
<div class="finding ok"><div class="fh"><b>H-04 — Vertimiento por instrucción del Coordinador</b><span class="chip c-ok">Sin impacto en evaluación</span></div>
<p>Cuatro eventos de limitación de inyección por instrucción del Coordinador, documentados con marca de tiempo y referencia de instrucción.</p>
<p class="small"><b>Acción:</b> ninguna requerida al titular. Se documenta separadamente para no imputar al activo una limitación de origen sistémico.</p></div>
<div class="box"><h4>Resumen de derivación</h4>
<table style="margin:6px 0 0;"><tr><th>Hallazgo</th><th>Clasificación</th><th>Derivado a</th><th>Estado</th></tr>
<tr><td>H-01</td><td>Correctiva</td><td>Comunicaciones / TI de planta</td><td><span class="chip c-hold">Abierto</span></td></tr>
<tr class="alt"><td>H-02</td><td>Preventiva</td><td>Mantenimiento — lavado</td><td><span class="chip c-warn">Abierto</span></td></tr>
<tr><td>H-03</td><td>Preventiva</td><td>Mantenimiento — inspección</td><td><span class="chip c-warn">Abierto</span></td></tr>
<tr class="alt"><td>H-04</td><td>Sistémico</td><td>—</td><td><span class="chip c-ok">Cerrado</span></td></tr></table>
<p class="small" style="margin:8px 0 0;">La clasificación preventiva/correctiva y la derivación al equipo competente son automáticas. El despacho de personal a terreno lo confirma siempre una persona.</p></div>
<p class="small" style="margin-top:16px;border-top:0.8px solid var(--border);padding-top:11px;">
<b>Sobre los datos.</b> La instalación, el titular, las cifras de desempeño y los hallazgos son ilustrativos. El recurso solar — irradiancia, perfil horario, temperatura y estacionalidad — se calcula a partir de la posición geográfica real de Santiago mediante modelos NREL SPA, Ineichen–Perez, Erbs, Hay–Davies y Faiman, y se valida contra el rango documentado por el Explorador Solar del Ministerio de Energía.<br><br>
jay@quorelia.org · quorelia.org · © 2026 Quorelia</p>""",
f"{REF} · Muestra ilustrativa","06"))
open("Informe-Muestra-Solar-PV.html","w",encoding="utf-8").write(doc(f"Quorelia — {NOM} — Informe PV (Muestra)","".join(P)))
print("PV Santiago escrito, paginas:",len(P))
