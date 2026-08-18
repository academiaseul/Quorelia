# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
from _base import *
REF="QOR-SEC-2026-08-FLOTA-01"; PER="julio 2026"
# Ilustrativo: cartera piloto
CART=[("Fotovoltaica",42,1840,96.8,3),("Eólica",18,1512,97.4,2),
      ("Almacenamiento BESS",11,880,95.1,4),("Mini hidro / PMGD",29,214,92.6,6)]
tot_n=sum(c[1] for c in CART); tot_mw=sum(c[2] for c in CART)
cob=sum(c[3]*c[1] for c in CART)/tot_n; flag=sum(c[4] for c in CART)
P=[]
P.append(page(f"""<div class="page-in" style="min-height:9.6in;display:flex;flex-direction:column;">
<div style="font-family:var(--mono);font-size:16px;letter-spacing:.28em;font-weight:800;">QUORELIA</div>
<div style="font-family:var(--mono);font-size:8px;letter-spacing:.2em;color:var(--teal);margin-top:5px;">INTELIGENCIA EN ENERGÍA RENOVABLE</div>
<div style="margin-top:26px;"><span class="wm">Documento de muestra · datos ilustrativos</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
<div style="font-family:var(--mono);font-size:9px;letter-spacing:.18em;color:var(--teal);margin-bottom:14px;">VISTA AGREGADA DE CARTERA · AUTORIDAD FISCALIZADORA</div>
<h1 style="font-size:32px;line-height:1.14;font-weight:500;letter-spacing:-.03em;max-width:6.3in;">Informe Consolidado de Verificación de Cartera de Generación</h1>
<p style="color:#9fb2bd;font-size:11px;max-width:5.5in;margin-top:14px;">Propuesta de formato estandarizado para la revisión documental de desempeño de centrales de generación, con trazabilidad reproducible de cada cifra informada.</p>
<table class="kv" style="margin-top:26px;max-width:5.6in;">
<tr><td style="color:#8fa0ab;">Destinatario</td><td style="color:#fff;">Subsecretaría de Energía · Documento de trabajo</td></tr>
<tr><td style="color:#8fa0ab;">Alcance de la muestra</td><td style="color:#fff;">{tot_n} centrales · {tot_mw:,} MW</td></tr>
<tr><td style="color:#8fa0ab;">Período</td><td style="color:#fff;">{PER}</td></tr>
<tr><td style="color:#8fa0ab;">Referencia</td><td style="color:#fff;font-family:var(--mono);">{REF}</td></tr></table></div>
<p class="small" style="color:#7f93a0;border-top:0.8px solid rgba(255,255,255,.15);padding-top:11px;">
Documento de trabajo con datos ilustrativos preparado para efectos de discusión metodológica. No constituye una fiscalización, ni contiene información de centrales reales. © 2026 Quorelia.</p></div>""",
"Quorelia · Documento de muestra","01","cover"))

P.append(page(f"""<div class="sec-num">01 · Planteamiento</div>
<div class="eyebrow">El problema que aborda este formato</div><h2 class="t">La revisión documental es el cuello de botella, no la fiscalización en terreno</h2>
<p>Durante 2025, la Superintendencia de Electricidad y Combustibles realizó <b>10.769 fiscalizaciones</b> en el sector eléctrico y de combustibles. En el segmento de generación distribuida, se ejecutaron <b>2.341 fiscalizaciones</b>, de las cuales <b>2.100 fueron revisiones documentales</b> y 241 revisiones en terreno.</p>
<p>Es decir: cerca del <b>90% del esfuerzo de fiscalización en ese segmento consiste en leer documentos</b>. Cada uno de esos documentos llega en un formato distinto, definido por el titular, sin una cadena de trazabilidad que permita reproducir la cifra informada hasta la medición que la sustenta.</p>
<div class="kpis">
{kpi("Fiscalizaciones 2025","10.769","total sector eléctrico y combustibles")}
{kpi("Generación distribuida","2.341","fiscalizaciones del segmento")}
{kpi("Revisión documental","2.100","90% del esfuerzo del segmento","#b45309")}
{kpi("Revisión en terreno","241","10% del esfuerzo del segmento")}</div>
<p class="small">Fuente: Cuenta Pública Participativa 2026 de la SEC, correspondiente a la gestión 2025.</p>
<h3 class="t">Tres consecuencias de la heterogeneidad de formatos</h3>
<div class="steps">
<div class="step"><div class="i">1</div><div class="b"><b>No se puede comparar.</b> Dos centrales equivalentes informan disponibilidad con definiciones distintas de denominador. La cifra parece comparable y no lo es.</div></div>
<div class="step"><div class="i">2</div><div class="b"><b>No se puede verificar.</b> Un informe en PDF sin cadena de trazabilidad no permite establecer si la cifra proviene de una medición, de una estimación o de una interpolación sobre datos faltantes.</div></div>
<div class="step"><div class="i">3</div><div class="b"><b>No se puede priorizar.</b> Sin una señal de calidad de dato homogénea, el criterio para decidir qué instalación amerita visita en terreno queda sujeto a denuncia o a rotación, no a riesgo.</div></div></div>
<div class="box teal"><h4>Alineación con la estrategia declarada de la SEC</h4>
<p style="margin-bottom:0;">La SEC ha declarado públicamente su avance hacia un modelo de fiscalización <b>proactivo y basado en análisis de datos y gestión de riesgo</b>, incorporando inteligencia artificial a sus procesos. El formato que se propone en este documento no plantea una función nueva: plantea el insumo estandarizado y verificable que ese modelo requiere para operar sobre la cartera completa.</p></div>""",
f"{REF} · Documento ilustrativo","02"))

rows=""
for i,(t,n,mw,cv,fl) in enumerate(CART):
    alt=' class="alt"' if i%2 else ''
    ch='c-ok' if cv>=95 else 'c-warn'
    rows+=f'<tr{alt}><td>{t}</td><td class="n">{n}</td><td class="n">{mw:,}</td><td class="n">{cv:.1f}</td><td class="n">{fl}</td><td><span class="chip {ch}">{"Conforme" if cv>=95 else "Observado"}</span></td></tr>'
P.append(page(f"""<div class="sec-num">02 · Vista consolidada de cartera</div>
<div class="eyebrow">Ejemplo de salida agregada</div><h2 class="t">Qué vería la autoridad en una sola pantalla</h2>
<p class="small">Cartera ilustrativa de {tot_n} centrales. La misma estructura escala sin cambios a la cartera nacional; el volumen de centrales no altera el formato del informe, solo el tamaño de la tabla.</p>
<div class="kpis">
{kpi("Centrales monitoreadas",f"{tot_n}","cartera de la muestra")}
{kpi("Capacidad agregada",f"{tot_mw:,}","MW")}
{kpi("Cobertura media de datos",f"{cob:.1f}%","ponderada por central")}
{kpi("Centrales observadas",f"{flag}","requieren atención","#b45309")}</div>
<table><tr><th>Tecnología</th><th style="text-align:right">Centrales</th><th style="text-align:right">MW</th><th style="text-align:right">Cobertura media %</th><th style="text-align:right">Observadas</th><th>Estado</th></tr>{rows}
<tr style="border-top:1.4px solid var(--navy);font-weight:600;"><td>Total cartera</td><td class="n">{tot_n}</td><td class="n">{tot_mw:,}</td><td class="n">{cob:.1f}</td><td class="n">{flag}</td><td></td></tr></table>
<h3 class="t">Cobertura media de datos por tecnología</h3>
{bars_svg([c[0].split()[0][:9] for c in CART],[c[3] for c in CART],90.0,thr_label="umbral 90%")}
<h3 class="t">Priorización por riesgo, no por rotación</h3>
<table><tr><th>Nivel</th><th style="text-align:right">Centrales</th><th>Criterio objetivo</th><th>Acción sugerida</th></tr>
<tr><td><span class="chip c-hold">Prioridad 1</span></td><td class="n">5</td><td>Cobertura bajo 90% sostenida más de 15 días</td><td>Requerimiento de información / visita</td></tr>
<tr class="alt"><td><span class="chip c-warn">Prioridad 2</span></td><td class="n">10</td><td>Hallazgo abierto sin cierre en dos períodos consecutivos</td><td>Seguimiento documental dirigido</td></tr>
<tr><td><span class="chip c-info">Prioridad 3</span></td><td class="n">23</td><td>Desviación de desempeño sin explicación de recurso</td><td>Monitoreo, sin acción inmediata</td></tr>
<tr class="alt"><td><span class="chip c-ok">Sin observaciones</span></td><td class="n">62</td><td>Cobertura y trazabilidad conformes</td><td>Ninguna</td></tr></table>
<p class="small">El valor para la autoridad no es el informe individual, sino el ordenamiento: de {tot_n} centrales, 5 concentran el riesgo verificable. La revisión documental de las 62 conformes puede automatizarse íntegramente, liberando capacidad fiscalizadora hacia donde existe evidencia objetiva de problema.</p>""",
f"{REF} · Documento ilustrativo","03"))

P.append(page(f"""<div class="sec-num">03 · Estandarización entre tecnologías</div>
<div class="eyebrow">El mismo marco, tres tecnologías</div><h2 class="t">Comparabilidad sin normalización manual</h2>
<p>Cada tecnología tiene indicadores propios que no son intercambiables. Un Performance Ratio no significa nada en un parque eólico; una eficiencia de ciclo completo no existe en una central fotovoltaica. Lo que sí puede — y debe — ser idéntico entre tecnologías es <b>la definición de qué hace válida a una cifra</b>.</p>
<table><tr><th>Elemento</th><th>Fotovoltaica</th><th>Eólica</th><th>Almacenamiento BESS</th></tr>
<tr><td>Indicador principal de recurso</td><td>Irradiancia POA</td><td>Velocidad y densidad de aire</td><td>No aplica</td></tr>
<tr class="alt"><td>Indicador de eficiencia</td><td>Performance Ratio</td><td>Desviación de curva de potencia</td><td>Eficiencia de ciclo (RTE)</td></tr>
<tr><td>Indicador de utilización</td><td>Factor de planta</td><td>Horas equivalentes</td><td>Ciclos equivalentes</td></tr>
<tr class="alt"><td>Salud del activo</td><td>Degradación normalizada</td><td>Disponibilidad por unidad</td><td>SOH y dispersión de celdas</td></tr>
<tr style="background:rgba(31,182,168,.07);"><td><b>Umbral de cobertura</b></td><td colspan="3" style="text-align:center;"><b>90% de muestras esperadas — idéntico</b></td></tr>
<tr><td><b>Tratamiento del silencio</b></td><td colspan="3" style="text-align:center;"><b>No observado, excluido del denominador — nunca cero</b></td></tr>
<tr style="background:rgba(31,182,168,.07);"><td><b>Regla de publicación</b></td><td colspan="3" style="text-align:center;"><b>Bajo umbral, la cifra se retiene y se declara la causa</b></td></tr>
<tr><td><b>Trazabilidad exigida</b></td><td colspan="3" style="text-align:center;"><b>Canal de origen, transformación y cobertura por cifra</b></td></tr>
<tr style="background:rgba(31,182,168,.07);"><td><b>Separación recurso / activo</b></td><td colspan="3" style="text-align:center;"><b>Obligatoria — el vertimiento sistémico se documenta aparte</b></td></tr></table>
<div class="box teal"><h4>La consecuencia práctica</h4>
<p style="margin-bottom:0;">Con estas cinco reglas comunes, un fiscalizador puede leer un informe fotovoltaico y uno eólico sin cambiar de criterio, y puede confiar en que un 97% de disponibilidad significa lo mismo en ambos. Hoy no lo significa.</p></div>
<h3 class="t">Contraste con el estado actual</h3>
<table><tr><th>Dimensión</th><th>Práctica habitual</th><th>Formato propuesto</th></tr>
<tr><td>Formato de entrega</td><td>Definido por cada titular</td><td>Estructura idéntica entre activos y tecnologías</td></tr>
<tr class="alt"><td>Datos faltantes</td><td>Interpolados o informados como cero</td><td>Declarados como no observados y excluidos</td></tr>
<tr><td>Verificabilidad</td><td>No reproducible desde el documento</td><td>Cada cifra reproducible hasta la medición cruda</td></tr>
<tr class="alt"><td>Elaboración</td><td>Manual, con horas de ingeniería por informe</td><td>Automatizada y programada</td></tr>
<tr><td>Criterio de fiscalización</td><td>Denuncia o rotación</td><td>Riesgo objetivo y medible</td></tr></table>""",
f"{REF} · Documento ilustrativo","04"))

P.append(page(f"""<div class="sec-num">04 · Propuesta de piloto</div>
<div class="eyebrow">Cómo se probaría esto sin comprometer nada</div><h2 class="t">Piloto acotado y verificable</h2>
<p>La propuesta no requiere modificación normativa, ni instalación de equipamiento, ni acceso a sistemas de la autoridad. Se ejecuta sobre datos que las centrales ya generan y que ya están obligadas a conservar.</p>
<div class="steps">
<div class="step"><div class="i">1</div><div class="b"><b>Selección de la muestra.</b> Un conjunto acotado de centrales voluntarias — idealmente 10 a 15, cubriendo fotovoltaica, eólica y almacenamiento — con al menos una instalación de cada régimen relevante.</div></div>
<div class="step"><div class="i">2</div><div class="b"><b>Generación en paralelo.</b> Durante tres meses, cada central continúa con su reporte habitual y, en paralelo, Quorelia emite el informe estandarizado desde el SCADA del titular. No se reemplaza ningún proceso vigente.</div></div>
<div class="step"><div class="i">3</div><div class="b"><b>Contraste.</b> Al cierre, se comparan ambas series: cuántas cifras coinciden, cuántas difieren, y en cuántos casos la diferencia se explica por tratamiento de datos faltantes. Ese contraste es el resultado del piloto.</div></div>
<div class="step"><div class="i">4</div><div class="b"><b>Evaluación de la autoridad.</b> La Subsecretaría evalúa si el formato estandarizado reduce efectivamente el tiempo de revisión documental y si mejora la calidad de la priorización de fiscalización en terreno.</div></div></div>
<h3 class="t">Qué se mediría, explícitamente</h3>
<table><tr><th>Métrica del piloto</th><th>Cómo se mide</th></tr>
<tr><td>Tiempo de revisión por informe</td><td>Cronometrado por el equipo revisor, formato actual vs. estandarizado</td></tr>
<tr class="alt"><td>Cifras no reproducibles detectadas</td><td>Conteo de valores del informe habitual que no pueden trazarse a una medición</td></tr>
<tr><td>Datos faltantes tratados como cero</td><td>Conteo de períodos con silencio de canal informados como generación nula</td></tr>
<tr class="alt"><td>Centrales correctamente priorizadas</td><td>Contraste entre la priorización por riesgo y los hallazgos efectivos en terreno</td></tr></table>
<div class="box amber"><h4>Sobre las cifras de este documento</h4>
<p style="margin-bottom:0;">Las cifras de cartera de este informe son <b>ilustrativas</b> y fueron construidas para mostrar la estructura de salida, no para representar el estado del parque nacional. Las cifras de fiscalización citadas en la Sección 01 provienen de la Cuenta Pública 2026 de la SEC. Cualquier estimación de ahorro de tiempo debe surgir del piloto y medirse con el equipo revisor de la autoridad, no proyectarse anticipadamente por el proveedor.</p></div>
<h3 class="t">Lo que este formato no hace</h3>
<p class="small">No reemplaza la fiscalización en terreno, no sustituye el juicio del fiscalizador, no accede a sistemas de la autoridad y no emite certificaciones con efecto regulatorio. Es un insumo documental estandarizado y trazable, cuya utilidad es liberar capacidad de revisión hacia donde existe evidencia objetiva de riesgo.</p>
<p class="small" style="margin-top:18px;border-top:0.8px solid var(--border);padding-top:11px;">
<b>Confidencialidad.</b> Todo dato de planta tratado bajo este formato se considera estrictamente confidencial, con acceso limitado a personal autorizado y cifrado en tránsito y reposo.<br><br>
<b>Datos de muestra.</b> Las centrales, cifras y hallazgos de cartera son ilustrativos. No representan instalaciones reales.<br><br>
jay@quorelia.org · quorelia.org · © 2026 Quorelia</p>""",
f"{REF} · Documento ilustrativo","05"))
open("Informe-Muestra-Cartera-SEC.html","w",encoding="utf-8").write(doc("Quorelia — Informe Consolidado de Cartera (Muestra)","".join(P)))
print("Fleet written, pages:",len(P), "| centrales:",tot_n,"| MW:",tot_mw,"| cob:",round(cob,1),"| flagged:",flag)
