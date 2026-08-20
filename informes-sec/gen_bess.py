# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
from _base import *

REF="QOR-SEC-2026-08-BESS-01"; PER="01 – 31 julio 2026"
NOM="Parque de Almacenamiento Tamarugal"; REG="Región de Antofagasta"
POT=200.0; CAP=800.0   # MW / MWh
UNITS=[  # id, MWh cargada, MWh descargada, cobertura %, SOH %, dispersión mV, disp %
 ("ESS-01",3092,2703,99.2,98.4,18,99.4),("ESS-02",3071,2684,99.1,98.2,21,99.1),
 ("ESS-03",3108,2718,98.9,98.5,17,99.5),("ESS-04",3055,2669,99.0,97.9,24,98.8),
 ("ESS-05",3086,2698,98.7,98.3,19,99.2),("ESS-06",3044,2657,98.4,97.6,38,97.9),
 ("ESS-07",3097,2708,99.1,98.4,18,99.3),("ESS-08",1402,1226,44.6,None,None,None)]
UMBRAL=90.0
ok=[u for u in UNITS if u[3]>=UMBRAL]
carga=sum(u[1] for u in ok); desc=sum(u[2] for u in ok)
rte=desc/carga*100
cob=sum(u[3] for u in UNITS)/len(UNITS)
cob_ok=sum(u[3] for u in ok)/len(ok)
disp=sum(u[6] for u in ok)/len(ok)
soh=sum(u[4] for u in ok)/len(ok)
ciclos=desc/(CAP*len(ok)/len(UNITS))
print(f"carga={carga} desc={desc} rte={rte:.2f} cob={cob:.1f} cob_ok={cob_ok:.2f} disp={disp:.2f} soh={soh:.2f} ciclos={ciclos:.1f}")

P=[]
# ---------- 1 PORTADA ----------
P.append(page(f"""<div class="page-in" style="min-height:9.6in;display:flex;flex-direction:column;">
<div style="font-family:var(--mono);font-size:16px;letter-spacing:.28em;font-weight:600;">QUORELIA</div>
<div style="font-family:var(--mono);font-size:8px;letter-spacing:.2em;color:var(--teal);margin-top:6px;">INTELIGENCIA EN ENERGÍA RENOVABLE</div>
<div style="margin-top:26px;"><span class="wm">Informe de muestra · datos ilustrativos</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
<div style="font-family:var(--mono);font-size:9px;letter-spacing:.18em;color:var(--teal);margin-bottom:14px;">SISTEMA DE ALMACENAMIENTO DE ENERGÍA · BESS</div>
<h1 style="font-size:34px;line-height:1.12;font-weight:500;letter-spacing:-.03em;max-width:6.2in;">Informe de Verificación Independiente y Desempeño Operacional</h1>
<p style="color:var(--ink-2);font-size:11px;max-width:5.4in;margin-top:14px;">Preparado bajo la metodología de monitoreo y verificación continua de Quorelia, sobre los sistemas SCADA y BMS ya instalados en la instalación. Sin reemplazo de equipamiento.</p>
<table class="kv" style="margin-top:26px;max-width:5.6in;">
<tr><td style="color:var(--grey);">Instalación</td><td style="color:var(--ink);">{NOM}</td></tr>
<tr><td style="color:var(--grey);">Ubicación</td><td style="color:var(--ink);">{REG}, Chile</td></tr>
<tr><td style="color:var(--grey);">Potencia / Capacidad</td><td style="color:var(--ink);">{POT:.0f} MW / {CAP:.0f} MWh</td></tr>
<tr><td style="color:var(--grey);">Período informado</td><td style="color:var(--ink);">{PER}</td></tr>
<tr><td style="color:var(--grey);">Referencia</td><td style="color:var(--ink);font-family:var(--mono);">{REF}</td></tr></table></div>
<p class="small" style="color:var(--grey);border-top:1px solid var(--line);padding-top:11px;">
Documento de muestra con datos ilustrativos generados con fines de demostración. No representa un cliente, instalación ni desempeño real. © 2026 Quorelia.</p></div>""",
"Quorelia · Informe de muestra","01", "cover"))
P[-1]=P[-1].replace('<div class="page cover">','<div class="page cover">').replace('class="page cover"','class="page cover"')

# ---------- 2 IDENTIFICACIÓN ----------
P.append(page(f"""<div class="sec-num">01 · Identificación del activo y marco regulatorio</div>
<div class="eyebrow">Antecedentes</div><h2 class="t">Identificación del activo</h2>
<table class="kv">
<tr><td>Nombre de la instalación</td><td>{NOM} <span class="chip c-info">Entidad ficticia</span></td></tr>
<tr><td>Titular</td><td>Sociedad de Almacenamiento Tamarugal SpA (ficticio)</td></tr>
<tr><td>Región / Comuna</td><td>{REG} / María Elena</td></tr>
<tr><td>Tecnología</td><td>Baterías de ion-litio LFP, 8 unidades ESS de 25 MW / 100 MWh</td></tr>
<tr><td>Potencia nominal</td><td>{POT:.0f} MW (carga y descarga)</td></tr>
<tr><td>Capacidad energética</td><td>{CAP:.0f} MWh nominales</td></tr>
<tr><td>Régimen</td><td>Coordinado — sistema de almacenamiento puro conectado en transmisión</td></tr>
<tr><td>Período informado</td><td>{PER} (744 horas)</td></tr>
<tr><td>Fuente de datos</td><td>SCADA / PPC y BMS del titular — sin instalación de hardware adicional</td></tr>
<tr><td>Resolución de muestreo</td><td>15 minutos (resolución nativa SCADA) · 2.976 muestras esperadas por canal</td></tr>
<tr><td>Preparado por</td><td>Quorelia — Motor de Verificación Automatizada</td></tr></table>
<h3 class="t">Marco regulatorio aplicable</h3>
<table><tr><th>Instrumento</th><th>Materia</th><th>Implicancia para este informe</th></tr>
<tr><td>D.S. 88 y sus modificaciones (Decreto N°1 de 2026)</td><td>Incorporación de sistemas de almacenamiento al reglamento de medios de generación de pequeña escala</td><td>Establece exigencias de sistemas de monitoreo y control, y reglas de operación en tiempo real</td></tr>
<tr class="alt"><td>Norma Técnica de Seguridad y Calidad de Servicio</td><td>Estándares de desempeño y disponibilidad</td><td>Define el marco de disponibilidad técnica reportable</td></tr>
<tr><td>Ley 20.936 y normativa del Coordinador</td><td>Coordinación de la operación del sistema</td><td>Obligación de entregar información operacional verificable</td></tr></table>
<div class="box amber"><h4>Nota sobre el alcance normativo</h4><p class="small">Las referencias normativas se presentan a título ilustrativo para efectos de esta muestra. La aplicabilidad concreta de cada instrumento a una instalación determinada debe ser confirmada con la autoridad competente y con el asesor legal del titular antes de cualquier uso regulatorio.</p></div>""",
f"{REF} · Muestra ilustrativa","02"))

# ---------- 3 METODOLOGÍA ----------
P.append(page(f"""<div class="sec-num">02 · Alcance y metodología</div>
<div class="eyebrow">Cómo se produce cada cifra</div><h2 class="t">Cadena de ingesta y validación</h2>
<p>Todas las cifras de este informe son producidas por el mismo proceso automatizado, sobre los sistemas ya desplegados en la instalación. Ninguna cifra es transcrita ni estimada manualmente.</p>
<div class="steps">
<div class="step"><div class="i">1</div><div class="b"><b>Ingesta.</b> Consulta continua de canales SCADA, PPC y BMS — unidades ESS, racks, celdas, medidores y variables ambientales — a resolución nativa. Deduplicación previa del catálogo de equipos para evitar el doble conteo de racks publicados en más de un protocolo.</div></div>
<div class="step"><div class="i">2</div><div class="b"><b>Validación.</b> Cada canal se contrasta contra su comportamiento esperado: límites de rango, tasa de cambio, consistencia cruzada y detección de vacíos. Cada dato se etiqueta como Nominal, Alerta, Falla o <b>No observado</b> antes de cualquier cálculo.</div></div>
<div class="step"><div class="i">3</div><div class="b"><b>Cálculo de KPI.</b> Disponibilidad, eficiencia de ciclo completo y energía se calculan exclusivamente sobre datos que superaron la validación. El silencio de un canal se excluye del denominador; nunca se reporta como cero ni como indisponibilidad.</div></div>
<div class="step"><div class="i">4</div><div class="b"><b>Verificación.</b> Cada cifra publicada conserva su canal de origen, su transformación y su porcentaje de cobertura, reproducible hasta la medición cruda a solicitud de la autoridad.</div></div>
<div class="step"><div class="i">5</div><div class="b"><b>Emisión.</b> Informes diarios y mensuales generados automáticamente, en formato PDF y portal, en español o inglés. Sin ensamblaje manual.</div></div></div>
<div class="box teal"><h4>El principio que gobierna todo el informe</h4>
<p style="margin-bottom:0;">Si la cobertura de datos de un activo no alcanza el umbral definido, <b>la cifra no se publica</b>. Se declara la brecha, su causa raíz y la acción requerida. Una cifra retenida con su razón declarada es verificable; una cifra estimada que aparenta certeza no lo es.</p></div>
<h3 class="t">Parámetros aplicados</h3>
<table><tr><th>Parámetro</th><th>Valor / regla</th></tr>
<tr><td>Intervalo de muestreo</td><td class="n">15 minutos</td></tr>
<tr class="alt"><td>Umbral de cobertura para certificar</td><td class="n">{UMBRAL:.0f}% de muestras esperadas, por unidad y período</td></tr>
<tr><td>Eficiencia de ciclo completo (RTE)</td><td class="n">Calculada solo sobre ciclos cerrados (SOC final dentro de ±2 pts del inicial)</td></tr>
<tr class="alt"><td>Conteo de alarmas</td><td class="n">Por flanco de subida, no por muestra</td></tr>
<tr><td>Mantenimiento programado</td><td class="n">Excluido del denominador si fue notificado por escrito</td></tr></table>""",
f"{REF} · Muestra ilustrativa","03"))

# ---------- 4 OPINIÓN ----------
P.append(page(f"""<div class="sec-num">03 · Opinión de verificación independiente</div>
<div class="eyebrow">Conclusión</div><h2 class="t">Opinión sobre el desempeño informado</h2>
<div class="kpis">
{kpi("Disponibilidad certificada",f"{disp:.2f}%","7 de 8 unidades","#149487")}
{kpi("Eficiencia RTE",f"{rte:.1f}%","ciclos cerrados")}
{kpi("Cobertura de datos",f"{cob_ok:.1f}%","unidades certificadas")}
{kpi("Ciclos equivalentes",f"{ciclos:.1f}","del período","#0b1c2c")}</div>
<h3 class="t">Base de la opinión</h3>
<p>El Motor de Verificación Automatizada de Quorelia ingirió y validó de forma continua los datos de planta conforme a la metodología descrita en la Sección 02. Esta opinión se sustenta en la cobertura de datos, las verificaciones de consistencia y la reconciliación cruzada entre fuentes realizadas durante el período informado.</p>
<h3 class="t">Responsabilidad del titular</h3>
<p>El titular es responsable de la operación e instrumentación de la instalación, y de proveer acceso continuo y sin obstrucción a los sistemas SCADA, PPC y BMS desde los cuales se derivan las cifras informadas.</p>
<h3 class="t">Responsabilidad de Quorelia</h3>
<p>Quorelia es responsable de la integridad de la cadena de validación aplicada a los datos recibidos, y de declarar — en lugar de estimar — todo período en que la cobertura de datos no sustente una cifra defendible.</p>
<h3 class="t">Opinión</h3>
<p>Sobre la base de los procedimientos ejecutados, la disponibilidad técnica del período se certifica en <b>{disp:.2f}%</b>, sustentada en una cobertura de datos observada de <b>{cob_ok:.1f}%</b> sobre las unidades certificadas. La eficiencia de ciclo completo se determina en <b>{rte:.1f}%</b>, calculada exclusivamente sobre ciclos cerrados.</p>
<p>La unidad <b>ESS-08 se retiene</b> por cobertura de datos de 44,6%, inferior al umbral de {UMBRAL:.0f}%. Véase Sección 05, Hallazgo H-01. No se publica cifra de disponibilidad para dicha unidad.</p>
<div class="box"><h4>Distribución del período</h4>
<table style="margin:6px 0 0;"><tr><th>Estado</th><th style="text-align:right">Proporción</th><th>Tratamiento</th></tr>
<tr><td><span class="chip c-ok">Aprobado</span></td><td class="n">{cob_ok:.1f}%</td><td>Medido, validado y dentro de rango esperado</td></tr>
<tr class="alt"><td><span class="chip c-hold">Retenido</span></td><td class="n">{100-cob_ok:.1f}%</td><td>Dato existente pero bajo el umbral de cobertura</td></tr>
<tr><td><span class="chip c-warn">No observado</span></td><td class="n">3.6%</td><td>Canal sin respuesta — excluido del denominador, nunca informado como cero</td></tr></table></div>""",
f"{REF} · Muestra ilustrativa","04"))

# ---------- 5 DATOS POR UNIDAD ----------
rows=""
for i,(uid,c,d,cv,sh,ds,dp) in enumerate(UNITS):
    alt=' class="alt"' if i%2 else ''
    if cv>=UMBRAL:
        rows+=f'<tr{alt}><td>{uid}</td><td class="n">{c:,}</td><td class="n">{d:,}</td><td class="n">{d/c*100:.1f}</td><td class="n">{cv:.1f}</td><td class="n">{sh:.1f}</td><td class="n">{ds}</td><td class="n">{dp:.1f}</td><td><span class="chip c-ok">Aprobado</span></td></tr>'
    else:
        rows+=f'<tr{alt}><td>{uid}</td><td class="n">{c:,}</td><td class="n">{d:,}</td><td class="n">—</td><td class="n">{cv:.1f}</td><td class="n">—</td><td class="n">—</td><td class="n">—</td><td><span class="chip c-hold">Retenido</span></td></tr>'
P.append(page(f"""<div class="sec-num">04 · Datos de desempeño</div>
<div class="eyebrow">Detalle por unidad</div><h2 class="t">Desempeño por unidad ESS</h2>
<p class="small">Ocho unidades monitoreadas, 2.976 muestras esperadas de 15 minutos por canal. La eficiencia por unidad se informa solo cuando la cobertura supera el umbral de {UMBRAL:.0f}%.</p>
<table><tr><th>Unidad</th><th style="text-align:right">Carga MWh</th><th style="text-align:right">Descarga MWh</th><th style="text-align:right">RTE %</th><th style="text-align:right">Cobertura %</th><th style="text-align:right">SOH %</th><th style="text-align:right">Disp. celdas mV</th><th style="text-align:right">Disponib. %</th><th>Veredicto</th></tr>{rows}
<tr style="border-top:1.4px solid var(--navy);font-weight:600;"><td>Total certificado</td><td class="n">{carga:,}</td><td class="n">{desc:,}</td><td class="n">{rte:.1f}</td><td class="n">{cob_ok:.1f}</td><td class="n">{soh:.1f}</td><td class="n">—</td><td class="n">{disp:.2f}</td><td></td></tr></table>
<h3 class="t">Cobertura de datos por unidad</h3>
{bars_svg([u[0].replace("ESS-","") for u in UNITS],[u[3] for u in UNITS],UMBRAL,thr_label=f"umbral {UMBRAL:.0f}%")}
<p class="small">Total de unidades monitoreadas: 8. Umbral de cobertura para una cifra defendible: {UMBRAL:.0f}%. La barra en rojo corresponde a ESS-08, cuya cifra de disponibilidad se retiene.</p>
<div class="box amber"><h4>Verificación aritmética de la eficiencia</h4>
<p class="small" style="margin-bottom:0;">RTE = descarga certificada / carga certificada = {desc:,} / {carga:,} = <b>{rte:.2f}%</b>. Un cálculo sobre el total de unidades — incluyendo ESS-08, cuya medición está incompleta — habría arrojado {sum(u[2] for u in UNITS)/sum(u[1] for u in UNITS)*100:.2f}%, cifra que no es defendible porque mezcla energía medida con energía parcialmente observada.</p></div>""",
f"{REF} · Muestra ilustrativa","05"))

# ---------- 6 SOC / ENERGIA ----------
soc=[52,48,41,35,30,28,34,45,58,67,74,79,83,86,88,84,76,65,54,47,43,40,44,50]
P.append(page(f"""<div class="sec-num">04 · Datos de desempeño</div>
<div class="eyebrow">Perfil operacional</div><h2 class="t">Estado de carga y ciclo diario típico</h2>
<p class="small">Perfil promedio de estado de carga (SOC) agregado del parque, en base horaria, para el período informado.</p>
{line_svg(soc,labels=["00","03","06","09","12","15","18","21"],ylab="SOC %")}
<p class="small">Patrón consistente con carga en horas de excedente solar (09:00–16:00) y descarga en punta vespertina (18:00–23:00). No se detectaron ciclos incompletos con SOC final fuera de la banda de ±2 puntos, salvo los excluidos del cálculo de RTE.</p>
<h3 class="t">Energía y ciclos</h3>
<div class="kpis">
{kpi("Energía cargada",f"{carga:,}","MWh certificados")}
{kpi("Energía descargada",f"{desc:,}","MWh certificados")}
{kpi("Pérdida de ciclo",f"{carga-desc:,}","MWh · {:.1f}%".format((carga-desc)/carga*100))}
{kpi("Ciclos equivalentes",f"{ciclos:.1f}","sobre capacidad certificada")}</div>
<h3 class="t">Salud del sistema — SOH y dispersión de celdas</h3>
<table><tr><th>Indicador</th><th style="text-align:right">Valor</th><th>Criterio</th><th>Evaluación</th></tr>
<tr><td>SOH promedio (unidades certificadas)</td><td class="n">{soh:.1f}%</td><td>&gt; 95% en año 2 de operación</td><td><span class="chip c-ok">Conforme</span></td></tr>
<tr class="alt"><td>Dispersión de tensión de celdas — media</td><td class="n">{sum(u[5] for u in ok)/len(ok):.0f} mV</td><td>&lt; 30 mV sostenido</td><td><span class="chip c-ok">Conforme</span></td></tr>
<tr><td>Dispersión de tensión de celdas — ESS-06</td><td class="n">38 mV</td><td>&lt; 30 mV sostenido</td><td><span class="chip c-warn">Excedido</span></td></tr>
<tr class="alt"><td>Temperatura máxima de rack</td><td class="n">34,2 °C</td><td>&lt; 40 °C</td><td><span class="chip c-ok">Conforme</span></td></tr>
<tr><td>Degradación acumulada estimada</td><td class="n">1,9%</td><td>&lt; 3,0% anual</td><td><span class="chip c-ok">Conforme</span></td></tr></table>
<p class="small">La dispersión de celdas es el indicador temprano más útil en sistemas LFP: una desviación sostenida entre celdas de un mismo rack precede a la pérdida de capacidad utilizable mucho antes de que el SOH agregado la refleje. Por ello se informa de forma independiente y no se promedia con el resto del parque.</p>""",
f"{REF} · Muestra ilustrativa","06"))

# ---------- 7 HALLAZGOS ----------
P.append(page(f"""<div class="sec-num">05 · Hallazgos y excepciones</div>
<div class="eyebrow">Excepciones del período</div><h2 class="t">Hallazgos, en orden de materialidad</h2>
<div class="finding hold"><div class="fh"><b>H-01 — Cobertura bajo umbral, unidad ESS-08</b><span class="chip c-hold">Retenido</span></div>
<p>Pérdida de comunicación entre el concentrador de la unidad 08 y el historiador de planta entre el 12 y el 29 de julio (17,3 días), reduciendo la cobertura del período a 44,6%, muy por debajo del umbral de {UMBRAL:.0f}%. La disponibilidad de ESS-08 <b>se retiene</b> para este período en lugar de estimarse.</p>
<p class="small"><b>Recomendación:</b> reemplazar o reconfigurar el módulo de comunicaciones del concentrador de la unidad 08. Quorelia recertificará el período una vez restablecida la cobertura y validados los datos recuperados.</p></div>
<div class="finding warn"><div class="fh"><b>H-02 — Dispersión de celdas sostenida, ESS-06</b><span class="chip c-warn">Alerta</span></div>
<p>Dispersión de tensión entre celdas de 38 mV sostenida durante 11 días consecutivos en dos racks de la unidad 06, por sobre el criterio de 30 mV. El comportamiento es sostenido y no transitorio, lo que descarta un evento puntual de balanceo.</p>
<p class="small"><b>Recomendación:</b> inspección del sistema de balanceo activo de los racks 06-03 y 06-07, y verificación de la calibración de los sensores de tensión asociados. Clasificada como <b>preventiva</b> y derivada al equipo de especialidad BMS.</p></div>
<div class="finding warn"><div class="fh"><b>H-03 — Ciclos con SOC no cerrado excluidos del RTE</b><span class="chip c-warn">Alerta</span></div>
<p>Seis ciclos del período finalizaron con SOC fuera de la banda de ±2 puntos respecto del inicial. Incluirlos en el cálculo habría arrojado una eficiencia aparente de 103,2%, físicamente imposible. Dichos ciclos fueron excluidos conforme a metodología.</p>
<p class="small"><b>Acción:</b> ninguna requerida. Se documenta por trazabilidad y para explicar la diferencia entre la energía bruta registrada y la base de cálculo del RTE.</p></div>
<div class="finding ok"><div class="fh"><b>H-04 — Ventana de mantenimiento programado, 22 de julio</b><span class="chip c-ok">Sin impacto</span></div>
<p>Interrupción de telemetría de 2h 20min durante ventana de mantenimiento SCADA notificada previamente por el titular. Excluida del denominador de cobertura conforme a la Sección 02.</p>
<p class="small"><b>Acción:</b> ninguna requerida. Registro conforme al tratamiento estándar de mantenimiento programado.</p></div>
<div class="box"><h4>Resumen de derivación de mantenimiento</h4>
<table style="margin:6px 0 0;"><tr><th>Hallazgo</th><th>Clasificación</th><th>Derivado a</th><th>Estado</th></tr>
<tr><td>H-01</td><td>Correctiva</td><td>Especialidad comunicaciones / TI de planta</td><td><span class="chip c-hold">Abierto</span></td></tr>
<tr class="alt"><td>H-02</td><td>Preventiva</td><td>Especialidad BMS</td><td><span class="chip c-warn">Abierto</span></td></tr>
<tr><td>H-03</td><td>Documental</td><td>—</td><td><span class="chip c-ok">Cerrado</span></td></tr>
<tr class="alt"><td>H-04</td><td>Programado</td><td>—</td><td><span class="chip c-ok">Cerrado</span></td></tr></table>
<p class="small" style="margin:8px 0 0;">La clasificación preventiva/correctiva y la derivación al equipo competente son automáticas. La orden de despacho de personal a terreno la confirma siempre una persona.</p></div>""",
f"{REF} · Muestra ilustrativa","07"))

# ---------- 8 ANEXO ----------
P.append(page(f"""<div class="sec-num">06 · Anexo — definiciones y trazabilidad</div>
<div class="eyebrow">Leyenda de estados</div><h2 class="t">Definiciones aplicadas</h2>
<table><tr><th>Estado</th><th>Definición</th></tr>
<tr><td><span class="chip c-ok">Nominal</span></td><td>Medido, verificado y dentro del rango esperado.</td></tr>
<tr class="alt"><td><span class="chip c-warn">Alerta</span></td><td>Umbral excedido o anomalía detectada; no afecta la disponibilidad certificada salvo que persista.</td></tr>
<tr><td><span class="chip c-hold">Falla</span></td><td>Falla confirmada de equipo o canal, trazada a su origen y con marca de tiempo.</td></tr>
<tr class="alt"><td><span class="chip c-warn">No observado</span></td><td>El canal no respondió durante el período. Se representa con trama diagonal; <b>nunca</b> se informa como cero.</td></tr>
<tr><td><span class="chip c-hold">Retenido</span></td><td>El dato existe pero no alcanza la cobertura mínima para sustentar una afirmación; la cifra no se publica para ese período.</td></tr></table>
<h3 class="t">Trazabilidad de cada cifra publicada</h3>
<p>Cada valor de este informe conserva su cadena completa: canal de origen, transformación aplicada, ventana temporal y porcentaje de cobertura. Ante requerimiento de la autoridad fiscalizadora, cualquier cifra puede reproducirse hasta la medición cruda que la sustenta, sin intervención manual.</p>
<table><tr><th>Cifra publicada</th><th>Canales de origen</th><th>Cobertura</th><th>Reproducible</th></tr>
<tr><td>Disponibilidad {disp:.2f}%</td><td class="n">7 unidades × 4 canales de estado</td><td class="n">{cob_ok:.1f}%</td><td><span class="chip c-ok">Sí</span></td></tr>
<tr class="alt"><td>RTE {rte:.1f}%</td><td class="n">medidores de carga y descarga, filtro de ciclo cerrado</td><td class="n">{cob_ok:.1f}%</td><td><span class="chip c-ok">Sí</span></td></tr>
<tr><td>SOH {soh:.1f}%</td><td class="n">BMS, agregación por rack</td><td class="n">{cob_ok:.1f}%</td><td><span class="chip c-ok">Sí</span></td></tr>
<tr class="alt"><td>Disponibilidad ESS-08</td><td class="n">—</td><td class="n">44,6%</td><td><span class="chip c-hold">No publicada</span></td></tr></table>
<div class="box teal"><h4>Nota para la autoridad fiscalizadora</h4>
<p style="margin-bottom:0;">Este informe se genera de forma automática y programada, sin ensamblaje manual. El mismo motor produce un informe diario para el titular y un informe mensual consolidado como el presente. La estructura, las definiciones y los umbrales son idénticos entre instalaciones, lo que permite comparar activos distintos sin normalizar manualmente sus formatos de origen.</p></div>
<p class="small" style="margin-top:20px;border-top:0.8px solid var(--border);padding-top:11px;">
<b>Confidencialidad.</b> Todos los datos de planta, SCADA e informes referidos en este documento se tratan como estrictamente confidenciales: acceso limitado a personal autorizado, cifrado en tránsito y en reposo, sin compartir, vender ni sublicenciar más allá del servicio contratado.<br><br>
<b>Datos de muestra.</b> La totalidad de nombres, cifras y hallazgos de este documento son ilustrativos y fueron generados con fines de demostración. No representan un cliente, instalación ni desempeño real.<br><br>
jay@quorelia.org · quorelia.org · © 2026 Quorelia</p>""",
f"{REF} · Muestra ilustrativa","08"))

open("Informe-Muestra-BESS.html","w",encoding="utf-8").write(doc(f"Quorelia — {NOM} — Informe BESS (Muestra)", "".join(P)))
print("BESS report written, pages:", len(P))
