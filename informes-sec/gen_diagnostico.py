# -*- coding: utf-8 -*-
import sys, re; sys.path.insert(0,'.')
import pandas as pd, numpy as np
from _base import *
U="/sessions/nifty-magical-gates/mnt/uploads/"
F1=U+"reporte_unidades-generadoras.xlsx"; F2=U+"reporte_unidades-generadoras-pmgd.xlsx"
ID=['ID','Nombre','Número Unidad','Nombre Propietario','Nombre Central','Tipo Tecnología','Nemotecnico','Descripcion']
NUL=re.compile(r'^\s*(no aplica|n/?a|s/?i|sin informaci[oó]n|-{1,3}|\.)\s*$',re.I)
def sheet(f,sh):
    d=pd.read_excel(f,sheet_name=sh,header=6).dropna(how='all')
    d.columns=[str(c).strip() for c in d.columns]
    return d[d['ID'].notna()] if 'ID' in d.columns else None
def clean(df): return df.applymap(lambda v: np.nan if (pd.isna(v) or NUL.match(str(v))) else v)
a=sheet(F1,'1.- Antecedentes Generales'); p=sheet(F2,'1.- Antecedentes Generales')
NU,NP=len(a),len(p); CU,CP=a['Nombre Central'].nunique(),p['Nombre Central'].nunique()
OU,OP=a['Nombre Propietario'].nunique(),p['Nombre Propietario'].nunique()
gu=a.groupby('Nombre Propietario')['Nombre Central'].nunique(); gp=p.groupby('Nombre Propietario')['Nombre Central'].nunique()
solo_u,solo_p=(gu==1).sum(),(gp==1).sum()
cen_solo_u,cen_solo_p=int(gu[gu==1].sum()),int(gp[gp==1].sum())
tec=(pd.concat([a.groupby('Tipo Tecnología')['Nombre Central'].nunique().rename('Coordinadas'),
                p.groupby('Tipo Tecnología')['Nombre Central'].nunique().rename('PMGD')],axis=1).fillna(0).astype(int))
tec['Total']=tec.sum(axis=1); tec=tec.sort_values('Total',ascending=False)
FICHAS=[("COORD","7.- Planta de Generacion Solar",F1,"Planta fotovoltaica"),
        ("COORD","6.- Turbinas Eolicas",F1,"Turbinas eólicas"),
        ("COORD","3.- Turbinas Hidraulicas",F1,"Turbinas hidráulicas"),
        ("COORD","4.- Turbina a Gas",F1,"Turbina a gas"),
        ("COORD","5.- Turbinas a Vapor",F1,"Turbinas a vapor"),
        ("COORD","8.- Motor de Combustion Interna",F1,"Motor combustión interna"),
        ("COORD","2.- Generadores",F1,"Generadores"),
        ("PMGD","9.- Sistema de Almacenamiento d",F2,"Almacenamiento (SAE)")]
comp=[]
for tag,sh,f,lab in FICHAS:
    d=sheet(f,sh); t=[c for c in d.columns if c not in ID and not c.startswith('Unnamed')]
    s=clean(d[t]); ap=s.notna().any(axis=1); n=int(ap.sum())
    c=(s[ap].notna().sum().sum()/s[ap].size*100) if n else 0.0
    comp.append((lab,tag,n,len(t),c))
sae=sheet(F2,'9.- Sistema de Almacenamiento d')
ts=[c for c in sae.columns if c not in ID]; sr=clean(sae[ts]).notna().any(axis=1)
N_SAE=int(sr.sum())
print(f"unid={NU}+{NP}={NU+NP} centrales={CU}+{CP}={CU+CP} prop={OU}+{OP}={OU+OP} SAE={N_SAE}")
solar_c=[c for c in comp if c[0].startswith("Planta fotov")][0][4]
FECHA="16 de agosto de 2026"
P=[]
P.append(page(f"""<div class="page-in" style="min-height:9.6in;display:flex;flex-direction:column;">
<div style="font-family:var(--mono);font-size:16px;letter-spacing:.28em;font-weight:600;">QUORELIA</div>
<div style="font-family:var(--mono);font-size:8px;letter-spacing:.2em;color:var(--teal);margin-top:6px;">INTELIGENCIA EN ENERGÍA RENOVABLE</div>
<div style="margin-top:26px;"><span class="wm" style="color:var(--teal);border-color:rgba(31,182,168,.5);">Datos oficiales · Infotécnica del Coordinador</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
<div style="font-family:var(--mono);font-size:9px;letter-spacing:.18em;color:var(--teal);margin-bottom:14px;">DIAGNÓSTICO DEL REGISTRO TÉCNICO NACIONAL</div>
<h1 style="font-size:31px;line-height:1.14;font-weight:500;letter-spacing:-.03em;max-width:6.3in;">Estado de completitud del registro de unidades generadoras del Sistema Eléctrico Nacional</h1>
<p style="color:var(--ink-2);font-size:11px;max-width:5.5in;margin-top:14px;">Análisis sobre la totalidad del registro público de Infotécnica: {NU+NP:,} unidades generadoras, {CU+CP:,} centrales, {OU+OP:,} propietarios. Sin datos simulados.</p>
<table class="kv" style="margin-top:26px;max-width:5.6in;">
<tr><td style="color:var(--grey);">Fuente</td><td style="color:var(--ink);">Infotécnica · Coordinador Eléctrico Nacional</td></tr>
<tr><td style="color:var(--grey);">Extracción</td><td style="color:var(--ink);">{FECHA}</td></tr>
<tr><td style="color:var(--grey);">Universo</td><td style="color:var(--ink);">{NU:,} unidades coordinadas + {NP} unidades PMGD</td></tr>
<tr><td style="color:var(--grey);">Referencia</td><td style="color:var(--ink);font-family:var(--mono);">QOR-DIAG-2026-08-01</td></tr></table></div>
<p class="small" style="color:var(--grey);border-top:1px solid var(--line);padding-top:11px;">
Documento de trabajo elaborado a partir de información pública. Las cifras de este informe son reproducibles ejecutando el análisis sobre los mismos archivos de origen. © 2026 Quorelia.</p></div>""",
"Quorelia · Diagnóstico sobre datos oficiales","01","cover"))

P.append(page(f"""<div class="sec-num">01 · Dimensión real del parque</div>
<div class="eyebrow">Punto de partida</div><h2 class="t">Cuántas instalaciones hay que fiscalizar</h2>
<div class="kpis">
{kpi("Unidades generadoras",f"{NU+NP:,}",f"{NU:,} coordinadas + {NP} PMGD","#149487")}
{kpi("Centrales únicas",f"{CU+CP:,}",f"{CU:,} coordinadas + {CP} PMGD")}
{kpi("Propietarios distintos",f"{OU+OP:,}","titulares registrados","#b45309")}
{kpi("Centrales por propietario",f"{(CU+CP)/(OU+OP):.2f}","promedio nacional")}</div>
<p>La distinción entre <b>unidad generadora</b> y <b>central</b> es la primera fuente de confusión al dimensionar el parque: una central puede contener múltiples unidades. El registro contiene {NU+NP:,} unidades agrupadas en {CU+CP:,} centrales.</p>
<h3 class="t">Distribución por tecnología — centrales</h3>
<table><tr><th>Tecnología</th><th style="text-align:right">Coordinadas</th><th style="text-align:right">PMGD</th><th style="text-align:right">Total</th><th style="text-align:right">% del parque</th></tr>
{"".join(f'<tr{" class=alt" if i%2 else ""}><td>{ix}</td><td class="n">{r.Coordinadas}</td><td class="n">{r.PMGD}</td><td class="n">{r.Total}</td><td class="n">{r.Total/(CU+CP)*100:.1f}</td></tr>' for i,(ix,r) in enumerate(tec.head(10).iterrows()))}
<tr style="border-top:1.4px solid var(--navy);font-weight:600;"><td>Total</td><td class="n">{CU:,}</td><td class="n">{CP}</td><td class="n">{CU+CP:,}</td><td class="n">100,0</td></tr></table>
<div class="box teal"><h4>La fotovoltaica define el problema</h4>
<p style="margin-bottom:0;">Con {tec.loc['Fotovoltaica','Total']:,} centrales, la fotovoltaica representa el <b>{tec.loc['Fotovoltaica','Total']/(CU+CP)*100:.1f}%</b> del parque nacional en número de instalaciones. Cualquier estrategia de fiscalización que no resuelva primero el caso fotovoltaico no resuelve el problema de escala.</p></div>""",
"Fuente: Infotécnica · Coordinador Eléctrico Nacional","02"))

P.append(page(f"""<div class="sec-num">02 · Estructura de propiedad</div>
<div class="eyebrow">Quién opera estas centrales</div><h2 class="t">Un parque extremadamente fragmentado</h2>
<table><tr><th>Segmento</th><th style="text-align:right">Propietarios</th><th style="text-align:right">Con 1 sola central</th><th style="text-align:right">%</th><th style="text-align:right">Centrales que operan</th><th style="text-align:right">% del segmento</th></tr>
<tr><td>Coordinadas</td><td class="n">{OU}</td><td class="n">{solo_u}</td><td class="n">{solo_u/OU*100:.1f}</td><td class="n">{cen_solo_u}</td><td class="n">{cen_solo_u/CU*100:.1f}</td></tr>
<tr class="alt"><td>PMGD</td><td class="n">{OP}</td><td class="n">{solo_p}</td><td class="n">{solo_p/OP*100:.1f}</td><td class="n">{cen_solo_p}</td><td class="n">{cen_solo_p/CP*100:.1f}</td></tr>
<tr style="border-top:1.4px solid var(--navy);font-weight:600;"><td>Total</td><td class="n">{OU+OP}</td><td class="n">{solo_u+solo_p}</td><td class="n">{(solo_u+solo_p)/(OU+OP)*100:.1f}</td><td class="n">{cen_solo_u+cen_solo_p}</td><td class="n">{(cen_solo_u+cen_solo_p)/(CU+CP)*100:.1f}</td></tr></table>
<div class="kpis">
{kpi("Propietarios de 1 central",f"{(solo_u+solo_p)/(OU+OP)*100:.1f}%","del total de titulares","#b45309")}
{kpi("Centrales que operan",f"{(cen_solo_u+cen_solo_p)/(CU+CP)*100:.1f}%","del parque nacional")}
{kpi("Propietarios con 4+",f"{int((gu>=4).sum()+(gp>=4).sum())}","de {} titulares".format(OU+OP))}
{kpi("PMGD monoactivo",f"{solo_p/OP*100:.1f}%","de titulares PMGD","#b45309")}</div>
<h3 class="t">Por qué esto es determinante para el diseño de la fiscalización</h3>
<p>El <b>{(solo_u+solo_p)/(OU+OP)*100:.1f}%</b> de los titulares del país opera <b>una sola central</b>. Entre los PMGD la cifra sube a {solo_p/OP*100:.1f}%. Estos titulares, por definición, no cuentan con un área de monitoreo, ni con un equipo de ingeniería dedicado, ni con capacidad de producir informes normalizados de desempeño.</p>
<p>La consecuencia es directa: <b>exigir un formato de reporte más exigente no produce mejor información en este segmento</b> — produce incumplimiento, o produce planillas llenadas a mano con la misma calidad que se buscaba corregir. La única vía escalable es que el informe se genere automáticamente desde los datos que la central ya produce.</p>
<div class="box amber"><h4>Concentración inversa</h4>
<p style="margin-bottom:0;">Solo {int((gu>=4).sum()+(gp>=4).sum())} titulares de {OU+OP} operan 4 o más centrales. La capacidad de reporte profesional se concentra en ese grupo reducido; el resto del parque — que es la mayoría de las instalaciones — carece estructuralmente de ella.</p></div>""",
"Fuente: Infotécnica · Coordinador Eléctrico Nacional","03"))

def _chip(c):
    if c<40: return '<span class="chip c-hold">Crítico</span>'
    if c<65: return '<span class="chip c-warn">Bajo</span>'
    return '<span class="chip c-ok">Aceptable</span>'
rows="".join('<tr%s><td>%s</td><td>%s</td><td class="n">%s</td><td class="n">%d</td><td class="n">%.1f%%</td><td>%s</td></tr>'
    % (' class="alt"' if i%2 else '', l, t, format(n,","), k, c, _chip(c)) for i,(l,t,n,k,c) in enumerate(comp))
P.append(page(f"""<div class="sec-num">03 · Completitud del registro técnico</div>
<div class="eyebrow">El hallazgo central</div><h2 class="t">Cuánto del registro está efectivamente informado</h2>
<p class="small">Metodología: para cada ficha técnica se consideran únicamente las unidades que declararon al menos un campo real. Se tratan como <b>ausentes</b> los valores «no aplica», «S/I», «sin información» y guiones. Completitud = campos con dato real sobre campos totales de la ficha.</p>
<table><tr><th>Ficha técnica</th><th>Ámbito</th><th style="text-align:right">Unidades</th><th style="text-align:right">Campos</th><th style="text-align:right">Completitud</th><th>Evaluación</th></tr>{rows}</table>
<h3 class="t">Completitud por ficha</h3>
{bars_svg([c[0][:11] for c in comp],[round(c[4],1) for c in comp],65.0,thr_label="referencia 65%")}
<div class="box amber"><h4>La tecnología más numerosa es la peor documentada</h4>
<p>La ficha de <b>planta de generación solar</b> del segmento coordinado presenta una completitud de <b>{solar_c:.1f}%</b> — la más baja de todas las fichas analizadas. Es, simultáneamente, la tecnología con más centrales del país ({tec.loc['Fotovoltaica','Total']:,}).</p>
<p style="margin-bottom:0;">Dicho de otro modo: <b>el segmento sobre el que existe menos información técnica estructurada es el que concentra dos tercios de las instalaciones a fiscalizar.</b></p></div>
<h3 class="t">Salvedad metodológica</h3>
<p class="small">Parte de los campos vacíos puede corresponder a atributos legítimamente no aplicables a una instalación concreta — por ejemplo, características de seguimiento en una planta de estructura fija. Esta cifra <b>no debe leerse como incumplimiento</b> de los titulares, sino como una medida de cuánta información estructurada y comparable está efectivamente disponible hoy para un análisis automatizado de cartera. La distinción entre «no aplica» y «no informado» no es recuperable desde el registro, y esa ambigüedad es en sí misma un hallazgo.</p>""",
"Fuente: Infotécnica · Coordinador Eléctrico Nacional","04"))

P.append(page(f"""<div class="sec-num">04 · Almacenamiento</div>
<div class="eyebrow">El punto ciego</div><h2 class="t">El registro de almacenamiento está prácticamente vacío</h2>
<div class="kpis">
{kpi("Unidades PMGD",f"{NP}","en el registro")}
{kpi("Con SAE declarado",f"{N_SAE}","unidades","#b91c1c")}
{kpi("Proporción",f"{N_SAE/NP*100:.2f}%","del segmento PMGD","#b91c1c")}
{kpi("Campos de la ficha",f"{len(ts)}","definidos y sin poblar")}</div>
<p>La ficha de Sistema de Almacenamiento de Energía del segmento PMGD contempla <b>{len(ts)} campos técnicos</b>. De las <b>{NP} unidades</b> del registro, únicamente <b>{N_SAE}</b> tienen un sistema de almacenamiento efectivamente declarado. Las {NP-N_SAE} restantes consignan «no aplica» en la totalidad de los campos.</p>
<div class="box teal"><h4>Por qué esto importa ahora y no antes</h4>
<p style="margin-bottom:0;">El Decreto N°1 de 2026 modificó el D.S. 88 incorporando los sistemas de almacenamiento al reglamento de medios de generación de pequeña escala — que hasta entonces solo contemplaba generación — e introdujo exigencias de <b>sistemas de monitoreo y control</b> para la integración con el centro de control de la distribuidora. El registro nacional enfrentará el ingreso masivo de una tecnología de la cual hoy contiene <b>dos ejemplares</b>. No existe todavía un formato consolidado de reporte de desempeño para ella.</p></div>
<h3 class="t">Las dos únicas fichas pobladas — y lo que revelan</h3>
<table><tr><th>Campo</th><th>Unidad A</th><th>Unidad B</th><th>Observación</th></tr>
<tr><td>Tipo de batería</td><td>LFP (LiFePO4)</td><td>Ion-Litio</td><td>Granularidad distinta para la misma familia química</td></tr>
<tr class="alt"><td>Potencia nominal DC</td><td class="n">3.600</td><td class="n">2.937,6</td><td>Coherente</td></tr>
<tr><td>Energía nominal DC</td><td class="n">7.200</td><td class="n">11.750,4</td><td>Duración 2,0 h vs 4,0 h</td></tr>
<tr class="alt"><td>Rango operativo SOC</td><td class="n">[5% – 95%]</td><td class="n">[0% – 100%]</td><td><span class="chip c-warn">Implausible</span> ningún BMS opera de 0 a 100%</td></tr>
<tr><td>Fecha entrada en operación</td><td>«En Pruebas»</td><td>20-04-2026</td><td><span class="chip c-warn">Inconsistente</span> texto en campo de fecha</td></tr></table>
<p>Con una muestra de dos registros ya aparecen tres problemas estructurales: <b>vocabulario no normalizado</b> en el tipo de batería, un <b>valor físicamente implausible</b> en el rango de SOC, y un <b>tipo de dato inconsistente</b> en un campo de fecha. Ninguno de los tres es detectable por inspección visual a escala de cartera; los tres son detectables automáticamente en el momento de la carga.</p>
<div class="box"><h4>Lectura para el diseño normativo</h4>
<p style="margin-bottom:0;">El momento de definir el formato de reporte de almacenamiento es <b>antes</b> de que ingresen los cientos de instalaciones que el nuevo marco habilita, no después. Corregir un registro de dos unidades es trivial; corregir uno de trescientas, con vocabularios divergentes ya consolidados, no lo es.</p></div>""",
"Fuente: Infotécnica · Coordinador Eléctrico Nacional","05"))

P.append(page(f"""<div class="sec-num">05 · Conclusiones y propuesta</div>
<div class="eyebrow">Síntesis</div><h2 class="t">Cuatro conclusiones del análisis</h2>
<div class="steps">
<div class="step"><div class="i">1</div><div class="b"><b>El parque es más grande y más fragmentado de lo que sugiere la cifra de capacidad.</b> {CU+CP:,} centrales en manos de {OU+OP:,} titulares distintos, de los cuales el {(solo_u+solo_p)/(OU+OP)*100:.1f}% opera una sola instalación.</div></div>
<div class="step"><div class="i">2</div><div class="b"><b>La capacidad de reporte no está distribuida.</b> Solo {int((gu>=4).sum()+(gp>=4).sum())} titulares operan 4 o más centrales. Exigir más formato a un parque monoactivo no produce mejor dato.</div></div>
<div class="step"><div class="i">3</div><div class="b"><b>La tecnología dominante es la menos documentada.</b> La fotovoltaica concentra el {tec.loc['Fotovoltaica','Total']/(CU+CP)*100:.1f}% de las centrales y su ficha técnica coordinada alcanza {solar_c:.1f}% de completitud.</div></div>
<div class="step"><div class="i">4</div><div class="b"><b>Almacenamiento es una hoja en blanco con plazo encima.</b> {N_SAE} de {NP} unidades PMGD, justo cuando el nuevo marco lo incorpora con exigencias de monitoreo.</div></div></div>
<h3 class="t">Propuesta: piloto acotado, medible y sin riesgo institucional</h3>
<table><tr><th>Elemento</th><th>Definición</th></tr>
<tr><td>Alcance</td><td>10 a 15 centrales voluntarias: fotovoltaica coordinada, PMGD fotovoltaico y al menos una con almacenamiento</td></tr>
<tr class="alt"><td>Duración</td><td>Tres meses, en paralelo al reporte habitual — no reemplaza ningún proceso vigente</td></tr>
<tr><td>Insumo</td><td>Datos SCADA que las centrales ya generan. Sin hardware nuevo, sin acceso a sistemas de la autoridad</td></tr>
<tr class="alt"><td>Producto</td><td>Informe estandarizado por central + vista consolidada de cartera, con trazabilidad por cifra</td></tr>
<tr><td>Métrica de éxito</td><td>Tiempo de revisión documental medido por el equipo revisor de la autoridad, formato actual vs. estandarizado</td></tr>
<tr class="alt"><td>Definición de fracaso</td><td>Si el tiempo de revisión no baja de forma medible, el piloto se declara sin éxito y termina</td></tr></table>
<div class="box teal"><h4>Lo que no se propone</h4>
<p style="margin-bottom:0;">No se propone sustituir la fiscalización en terreno, ni emitir certificaciones con efecto regulatorio, ni acceder a sistemas de la autoridad, ni modificar la normativa vigente. Se propone un insumo documental estandarizado y verificable, y que su utilidad la mida quien lo va a usar.</p></div>
<p class="small" style="margin-top:16px;border-top:0.8px solid var(--border);padding-top:11px;">
<b>Reproducibilidad.</b> Todas las cifras de este informe se obtienen del registro público de Infotécnica del Coordinador Eléctrico Nacional, extraído el {FECHA}. El análisis es reproducible ejecutando el mismo procedimiento sobre los archivos de origen. No se emplearon datos simulados ni estimados.<br><br>
jay@quorelia.org · quorelia.org · © 2026 Quorelia</p>""",
"Fuente: Infotécnica · Coordinador Eléctrico Nacional","06"))
open("Informe-Diagnostico-Parque-Nacional.html","w",encoding="utf-8").write(doc("Quorelia — Diagnóstico del Registro Técnico Nacional","".join(P)))
print("OK páginas:",len(P))
