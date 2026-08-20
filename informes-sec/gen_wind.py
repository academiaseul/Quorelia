# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
from _base import *
REF="QOR-SEC-2026-08-EOL-01"; PER="01 – 31 julio 2026"; H=744
NOM="Parque Eólico Sierra Guanaco"; REG="Región del Biobío"
POT=108.0; NT=24; UMBRAL=90.0
# id, cobertura, disponibilidad, MWh, desv curva potencia %
WTG=[(f"WTG-{i:02d}",c,d,e,dv) for i,(c,d,e,dv) in enumerate([
 (99.2,97.8,1312,-0.4),(99.1,98.1,1325,-0.2),(98.9,97.4,1301,-0.6),(99.1,98.3,1331,+0.1),
 (98.7,96.9,1288,-0.9),(99.0,97.7,1309,-0.5),(99.1,98.0,1318,-0.3),(98.5,96.2,1272,-1.4),
 (99.1,98.2,1327,-0.2),(98.8,97.1,1294,-0.8),(99.1,97.9,1315,-0.4),(99.0,98.4,1334,+0.2),
 (99.1,97.6,1306,-0.5),(98.6,96.7,1283,-1.1),(99.1,98.1,1322,-0.3),(98.9,97.3,1298,-0.7),
 (99.1,98.5,1338,+0.3),(98.4,95.8,1264,-1.8),(99.0,97.8,1311,-0.4),(99.1,98.2,1329,-0.2),
 (62.4,None,None,None),(99.1,97.5,1304,-0.6),(98.8,97.0,1291,-0.9),(99.1,98.3,1330,+0.1)],1)]
ok=[w for w in WTG if w[1]>=UMBRAL]
gen=sum(w[3] for w in ok); cob=sum(w[1] for w in ok)/len(ok)
disp=sum(w[2] for w in ok)/len(ok)
cf=gen/(POT*len(ok)/NT*H)*100; heq=gen/(POT*len(ok)/NT)
vel=[7.2,8.1,9.4,8.8,6.9,7.5,10.2,11.1,9.6,8.2,7.1,6.4,7.8,9.9,10.8,9.2,8.4,7.6,6.8,8.9,10.4,9.7,8.3,7.2,6.6,8.0,9.5,10.1,8.7,7.9,8.6]
print(f"gen={gen} cob={cob:.2f} disp={disp:.2f} cf={cf:.2f} heq={heq:.0f} vmed={sum(vel)/len(vel):.2f}")
P=[]
P.append(page(f"""<div class="page-in" style="min-height:9.6in;display:flex;flex-direction:column;">
<div style="font-family:var(--mono);font-size:16px;letter-spacing:.28em;font-weight:600;">QUORELIA</div>
<div style="font-family:var(--mono);font-size:8px;letter-spacing:.2em;color:var(--teal);margin-top:6px;">INTELIGENCIA EN ENERGÍA RENOVABLE</div>
<div style="margin-top:26px;"><span class="wm">Informe de muestra · datos ilustrativos</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
<div style="font-family:var(--mono);font-size:9px;letter-spacing:.18em;color:var(--teal);margin-bottom:14px;">PARQUE EÓLICO · WIND</div>
<h1 style="font-size:34px;line-height:1.12;font-weight:500;letter-spacing:-.03em;max-width:6.2in;">Informe de Verificación Independiente y Desempeño Operacional</h1>
<p style="color:var(--ink-2);font-size:11px;max-width:5.4in;margin-top:14px;">Preparado bajo la metodología de monitoreo y verificación continua de Quorelia, sobre los sistemas SCADA y de medición ya instalados en el parque.</p>
<table class="kv" style="margin-top:26px;max-width:5.6in;">
<tr><td style="color:var(--grey);">Instalación</td><td style="color:var(--ink);">{NOM}</td></tr>
<tr><td style="color:var(--grey);">Ubicación</td><td style="color:var(--ink);">{REG}, Chile</td></tr>
<tr><td style="color:var(--grey);">Capacidad</td><td style="color:var(--ink);">{POT:.0f} MW · {NT} aerogeneradores de 4,5 MW</td></tr>
<tr><td style="color:var(--grey);">Período informado</td><td style="color:var(--ink);">{PER}</td></tr>
<tr><td style="color:var(--grey);">Referencia</td><td style="color:var(--ink);font-family:var(--mono);">{REF}</td></tr></table></div>
<p class="small" style="color:var(--grey);border-top:1px solid var(--line);padding-top:11px;">Documento de muestra con datos ilustrativos. No representa un cliente, instalación ni desempeño real. © 2026 Quorelia.</p></div>""",
"Quorelia · Informe de muestra","01","cover"))

P.append(page(f"""<div class="sec-num">01 · Identificación y opinión</div>
<div class="eyebrow">Antecedentes</div><h2 class="t">Identificación del activo</h2>
<table class="kv">
<tr><td>Nombre del parque</td><td>{NOM} <span class="chip c-info">Entidad ficticia</span></td></tr>
<tr><td>Titular</td><td>Eólica Sierra Guanaco SpA (ficticio)</td></tr>
<tr><td>Región / Comuna</td><td>{REG} / Los Ángeles</td></tr>
<tr><td>Tecnología</td><td>{NT} aerogeneradores de eje horizontal, 4,5 MW, altura de buje 115 m</td></tr>
<tr><td>Capacidad instalada</td><td>{POT:.0f} MW</td></tr>
<tr><td>Régimen</td><td>Coordinado — conectado en transmisión zonal</td></tr>
<tr><td>Período informado</td><td>{PER} ({H} horas)</td></tr>
<tr><td>Medición de recurso</td><td>2 torres meteorológicas + anemometría de góndola en cada unidad</td></tr></table>
<div class="eyebrow" style="margin-top:18px;">Conclusión</div><h2 class="t">Opinión sobre el desempeño informado</h2>
<div class="kpis">
{kpi("Disponibilidad certificada",f"{disp:.2f}%",f"{len(ok)} de {NT} unidades","#149487")}
{kpi("Factor de planta",f"{cf:.1f}%","del período")}
{kpi("Horas equivalentes",f"{heq:.0f} h","sobre capacidad certificada")}
{kpi("Cobertura de datos",f"{cob:.1f}%","unidades certificadas")}</div>
<h3 class="t">Opinión</h3>
<p>La disponibilidad técnica del período se certifica en <b>{disp:.2f}%</b>, sustentada en cobertura observada de <b>{cob:.1f}%</b> sobre las {len(ok)} unidades certificadas. La generación certificada asciende a <b>{gen:,} MWh</b>, equivalente a un factor de planta de <b>{cf:.1f}%</b> y <b>{heq:.0f} horas equivalentes</b> de operación a plena carga.</p>
<p>La unidad <b>WTG-21 se retiene</b> por cobertura de datos de 62,4%, inferior al umbral de {UMBRAL:.0f}%. Véase Sección 04, Hallazgo H-01. No se publica cifra de disponibilidad ni de generación imputable a dicha unidad.</p>
<div class="box teal"><h4>Por qué la disponibilidad eólica no se mide como en solar</h4>
<p style="margin-bottom:0;">Un aerogenerador detenido por ausencia de viento no está indisponible: está correctamente fuera de servicio. La disponibilidad técnica informada excluye del denominador las horas bajo velocidad de arranque y sobre velocidad de corte, de modo que la cifra refleje el estado del equipo y no el del recurso. Confundir ambos conceptos es el error más frecuente en la fiscalización de activos eólicos.</p></div>""",
f"{REF} · Muestra ilustrativa","02"))

rows=""
for i,(uid,cv,dp,e,dv) in enumerate(WTG):
    alt=' class="alt"' if i%2 else ''
    if cv>=UMBRAL:
        ch='c-ok' if dv>-1.0 else 'c-warn'
        rows+=f'<tr{alt}><td>{uid}</td><td class="n">{cv:.1f}</td><td class="n">{dp:.1f}</td><td class="n">{e:,}</td><td class="n">{dv:+.1f}</td><td><span class="chip {ch}">Aprobado</span></td></tr>'
    else:
        rows+=f'<tr{alt}><td>{uid}</td><td class="n">{cv:.1f}</td><td class="n">—</td><td class="n">—</td><td class="n">—</td><td><span class="chip c-hold">Retenido</span></td></tr>'
P.append(page(f"""<div class="sec-num">02 · Datos de desempeño</div>
<div class="eyebrow">Detalle por aerogenerador</div><h2 class="t">Desempeño por unidad</h2>
<p class="small">Desviación de curva de potencia: diferencia entre la energía medida y la esperada según la curva garantizada del fabricante, corregida por densidad de aire del sitio.</p>
<table><tr><th>Unidad</th><th style="text-align:right">Cobertura %</th><th style="text-align:right">Disponib. %</th><th style="text-align:right">Energía MWh</th><th style="text-align:right">Desv. curva %</th><th>Veredicto</th></tr>{rows}
<tr style="border-top:1.4px solid var(--navy);font-weight:600;"><td>Total certificado</td><td class="n">{cob:.1f}</td><td class="n">{disp:.2f}</td><td class="n">{gen:,}</td><td class="n">{sum(w[4] for w in ok)/len(ok):+.1f}</td><td></td></tr></table>
<h3 class="t">Velocidad media diaria de viento</h3>
{line_svg(vel,labels=["01","07","14","21","28"],ylab="m/s a 115 m")}
<p class="small">Velocidad media del período: {sum(vel)/len(vel):.2f} m/s a altura de buje. Densidad de aire media corregida: 1,196 kg/m³. Horas bajo velocidad de arranque (3,0 m/s): 41 h, excluidas del denominador de disponibilidad técnica.</p>""",
f"{REF} · Muestra ilustrativa","03"))

P.append(page(f"""<div class="sec-num">03 · Recurso, curva de potencia y pérdidas</div>
<div class="eyebrow">Condiciones del período</div><h2 class="t">Variables de recurso</h2>
<table><tr><th>Variable</th><th style="text-align:right">Media</th><th style="text-align:right">Máx</th><th style="text-align:right">Mín</th><th>Fuente</th></tr>
<tr><td>Velocidad de viento (115 m)</td><td class="n">8,52 m/s</td><td class="n">11,1</td><td class="n">6,4</td><td>Torre meteorológica + góndola</td></tr>
<tr class="alt"><td>Dirección predominante</td><td class="n">SO (223°)</td><td class="n">—</td><td class="n">—</td><td>Veleta de góndola</td></tr>
<tr><td>Densidad de aire corregida</td><td class="n">1,196 kg/m³</td><td class="n">1,214</td><td class="n">1,178</td><td>Calculada — presión y temperatura</td></tr>
<tr class="alt"><td>Temperatura ambiente</td><td class="n">9,1 °C</td><td class="n">18,4</td><td class="n">-1,8</td><td>Torre meteorológica</td></tr>
<tr><td>Turbulencia (TI a 15 m/s)</td><td class="n">0,112</td><td class="n">0,168</td><td class="n">0,081</td><td>Calculada</td></tr>
<tr class="alt"><td>Horas bajo velocidad de arranque</td><td class="n">41 h</td><td class="n">—</td><td class="n">—</td><td>SCADA</td></tr>
<tr><td>Horas sobre velocidad de corte</td><td class="n">6 h</td><td class="n">—</td><td class="n">—</td><td>SCADA</td></tr>
<tr class="alt"><td>Horas de operación con generación</td><td class="n">631 h</td><td class="n">—</td><td class="n">—</td><td>SCADA</td></tr></table>
<h3 class="t">Descomposición de pérdidas de energía</h3>
<table><tr><th>Concepto</th><th style="text-align:right">Pérdida</th><th>Naturaleza</th><th>Evaluación</th></tr>
<tr><td>Indisponibilidad de equipos</td><td class="n">2,1%</td><td>Accionable</td><td><span class="chip c-ok">Conforme</span></td></tr>
<tr class="alt"><td>Desviación de curva de potencia</td><td class="n">0,5%</td><td>Accionable — calibración/pitch</td><td><span class="chip c-ok">Conforme</span></td></tr>
<tr><td>Efecto estela entre unidades</td><td class="n">6,4%</td><td>De diseño</td><td><span class="chip c-ok">Conforme</span></td></tr>
<tr class="alt"><td>Vertimiento por instrucción del Coordinador</td><td class="n">1,2%</td><td>Sistémico</td><td><span class="chip c-info">Documentado</span></td></tr>
<tr><td>Pérdidas eléctricas internas</td><td class="n">1,8%</td><td>De diseño</td><td><span class="chip c-ok">Conforme</span></td></tr>
<tr class="alt"><td>Restricción por ruido / fauna</td><td class="n">0,4%</td><td>Ambiental — compromiso RCA</td><td><span class="chip c-info">Documentado</span></td></tr></table>
<div class="box amber"><h4>Desviación de curva de potencia — WTG-18</h4>
<p style="margin-bottom:0;">La unidad WTG-18 presenta una desviación de -1,8% respecto de la curva garantizada, la mayor del parque y 1,3 puntos peor que la media. El patrón se concentra en el rango de 7 a 11 m/s, compatible con desalineación de yaw o desviación de calibración del anemómetro de góndola, más que con degradación de pala. Un error de calibración de 0,3 m/s en la anemometría produce una desviación aparente de esta magnitud sin que exista falla real de equipo — razón por la cual el hallazgo se clasifica como verificación de instrumentación y no como falla mecánica.</p></div>""",
f"{REF} · Muestra ilustrativa","04"))

P.append(page(f"""<div class="sec-num">04 · Hallazgos y excepciones</div>
<div class="eyebrow">Excepciones del período</div><h2 class="t">Hallazgos, en orden de materialidad</h2>
<div class="finding hold"><div class="fh"><b>H-01 — Cobertura bajo umbral, WTG-21</b><span class="chip c-hold">Retenido</span></div>
<p>Interrupción del enlace de fibra al aerogenerador 21 entre el 14 y el 25 de julio (11,6 días), reduciendo la cobertura del período a 62,4%. Disponibilidad y generación imputable a WTG-21 <b>se retienen</b> en lugar de estimarse. La energía de esta unidad tampoco se incluye en el total certificado del parque.</p>
<p class="small"><b>Recomendación:</b> revisión del enlace de fibra del ramal norte y del conversor de medio asociado. Clasificada como <b>correctiva</b>.</p></div>
<div class="finding warn"><div class="fh"><b>H-02 — Desviación de curva de potencia, WTG-18</b><span class="chip c-warn">Alerta</span></div>
<p>Desviación sostenida de -1,8% respecto de la curva garantizada, concentrada en el rango de 7 a 11 m/s. Patrón compatible con desalineación de yaw o desviación de calibración de anemometría de góndola.</p>
<p class="small"><b>Recomendación:</b> verificación de calibración del anemómetro de góndola y de la alineación de yaw antes de escalar a inspección mecánica. Clasificada como <b>preventiva</b>.</p></div>
<div class="finding warn"><div class="fh"><b>H-03 — Disponibilidad bajo media, WTG-08 y WTG-18</b><span class="chip c-warn">Alerta</span></div>
<p>Ambas unidades registran disponibilidad bajo 96,5%, contra una media de parque de {disp:.2f}%. Las detenciones se concentran en eventos de sistema de pitch, con reinicio automático exitoso en la mayoría de los casos.</p>
<p class="small"><b>Recomendación:</b> revisión del sistema hidráulico de pitch en la próxima ventana programada. Clasificada como <b>preventiva</b>.</p></div>
<div class="finding ok"><div class="fh"><b>H-04 — Vertimiento por instrucción del Coordinador</b><span class="chip c-ok">Sin impacto en evaluación</span></div>
<p>Once eventos de limitación de inyección por instrucción del Coordinador, totalizando 19h 15min y 371 MWh no inyectados, documentados con marca de tiempo y referencia de instrucción.</p>
<p class="small"><b>Acción:</b> ninguna requerida al titular. Se documenta separadamente para no imputar al activo una limitación de origen sistémico.</p></div>
<div class="box"><h4>Resumen de derivación</h4>
<table style="margin:6px 0 0;"><tr><th>Hallazgo</th><th>Clasificación</th><th>Derivado a</th><th>Estado</th></tr>
<tr><td>H-01</td><td>Correctiva</td><td>Comunicaciones / TI de planta</td><td><span class="chip c-hold">Abierto</span></td></tr>
<tr class="alt"><td>H-02</td><td>Preventiva</td><td>Especialidad control / instrumentación</td><td><span class="chip c-warn">Abierto</span></td></tr>
<tr><td>H-03</td><td>Preventiva</td><td>Mantenimiento mecánico</td><td><span class="chip c-warn">Abierto</span></td></tr>
<tr class="alt"><td>H-04</td><td>Sistémico</td><td>—</td><td><span class="chip c-ok">Cerrado</span></td></tr></table>
<p class="small" style="margin:8px 0 0;">La clasificación preventiva/correctiva y la derivación son automáticas. El despacho de personal a terreno lo confirma siempre una persona.</p></div>
<p class="small" style="margin-top:16px;border-top:0.8px solid var(--border);padding-top:11px;"><b>Datos de muestra.</b> Nombres, cifras y hallazgos ilustrativos, generados con fines de demostración. No representan un cliente, instalación ni desempeño real.<br>jay@quorelia.org · quorelia.org · © 2026 Quorelia</p>""",
f"{REF} · Muestra ilustrativa","05"))
open("Informe-Muestra-Eolico.html","w",encoding="utf-8").write(doc(f"Quorelia — {NOM} — Informe Eólico (Muestra)","".join(P)))
print("Wind written, pages:",len(P))
