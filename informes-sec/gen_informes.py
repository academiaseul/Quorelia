# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
import pandas as pd, numpy as np
from _base import *
import datos as D
DIA=23
CFG={
 'solar': dict(nom="Planta Solar Cerro Tinaja",reg="Región Metropolitana",com="Til Til",ref="FV",
   n=12,uni="INV",cap="120 MWac / 156 MWp",tipo="CENTRAL FOTOVOLTAICA",
   tec="Fotovoltaica · seguidor de un eje con backtracking"),
 'eolico': dict(nom="Parque Eólico Sierra Guanaco",reg="Región del Biobío",com="Los Ángeles",ref="EOL",
   n=24,uni="WTG",cap="108 MW",tipo="PARQUE EÓLICO",
   tec="Eólica · 24 aerogeneradores de 4,5 MW, buje 115 m"),
 'bess': dict(nom="Parque de Almacenamiento Tamarugal",reg="Región de Antofagasta",com="María Elena",ref="BESS",
   n=8,uni="ESS",cap="200 MW / 800 MWh",tipo="SISTEMA DE ALMACENAMIENTO",
   tec="Almacenamiento · ion-litio LFP, 8 unidades de 25 MW"),
}
def kv(*p): return "".join(f'<tr><td style="color:var(--grey);">{a}</td><td style="color:var(--ink);">{b}</td></tr>' for a,b in p)
def portada(c,titulo,sub,kvs,marca):
    return page(f"""<div class="page-in" style="min-height:9.6in;display:flex;flex-direction:column;">
<div style="font-family:var(--mono);font-size:16px;letter-spacing:.28em;font-weight:600;">QUORELIA</div>
<div style="font-family:var(--mono);font-size:8px;letter-spacing:.2em;color:var(--teal);margin-top:6px;">INTELIGENCIA EN ENERGÍA RENOVABLE</div>
<div style="margin-top:26px;"><span class="wm">{marca}</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
<div style="font-family:var(--mono);font-size:9px;letter-spacing:.18em;color:var(--teal);margin-bottom:14px;">{c['tipo']}</div>
<h1 style="font-size:33px;line-height:1.13;font-weight:500;letter-spacing:-.03em;max-width:6.2in;">{titulo}</h1>
<p style="color:var(--ink-2);font-size:11px;max-width:5.4in;margin-top:14px;">{sub}</p>
<table class="kv" style="margin-top:24px;max-width:5.6in;">{kvs}</table></div>
<p class="small" style="color:var(--grey);border-top:1px solid var(--line);padding-top:11px;">
Documento de muestra. La instalación, el titular y los hallazgos son ilustrativos. © 2026 Quorelia.</p></div>""",
"Quorelia · Informe de muestra","01","cover")
PIE='<p class="small" style="margin-top:14px;border-top:0.8px solid var(--border);padding-top:10px;">jay@quorelia.org · quorelia.org · © 2026 Quorelia — informe de muestra</p>'
def cobertura(c):
    tot=c['n']*96
    return f"""<h3 class="t">Cobertura de datos del día</h3>
<table><tr><th>Indicador</th><th style="text-align:right">Valor</th><th>Evaluación</th></tr>
<tr><td>Muestras esperadas ({c['n']} unidades × 96)</td><td class="n">{tot:,}</td><td>—</td></tr>
<tr class="alt"><td>Muestras recibidas y validadas</td><td class="n">{int(tot*0.981):,}</td><td><span class="chip c-ok">98,1%</span></td></tr>
<tr><td>Canales sin respuesta</td><td class="n">{tot-int(tot*0.981):,}</td><td><span class="chip c-warn">No observado</span></td></tr>
<tr class="alt"><td>Umbral para publicar cifras</td><td class="n">90,0%</td><td><span class="chip c-ok">Superado</span></td></tr></table>"""

# ================= DIARIO =================
def diario_solar_eol(tec):
    c=CFG[tec]; d=getattr(D,tec)(); r=D.diario(d); r=r[r.dia==DIA].iloc[0]
    pot=d['pot']; hh=pot[pot.index.day==DIA].resample('h').mean()
    horas=[f"{h:02d}" for h in hh.index.hour]; REF=f"QOR-{c['ref']}-D-20260723"
    sol = tec=='solar'
    if sol:
        extra=kpi("Irradiancia POA",f"{r.poa:.2f}","kWh/m² del día")
        fx=f'<tr class="alt"><td>Irradiancia POA acumulada</td><td class="n">{r.poa:.2f} kWh/m²</td><td>Estación en sitio</td></tr>'
        ev=(f'<tr><td class="n">{r.ini}</td><td>Inicio de generación</td><td><span class="chip c-info">Operacional</span></td><td>Ninguna</td></tr>'
            f'<tr class="alt"><td class="n">10:20</td><td>Desbalance de corriente de strings, INV-06</td><td><span class="chip c-warn">Preventiva</span></td><td>Inspección en próximo lavado</td></tr>'
            f'<tr><td class="n">13:15</td><td>Potencia máxima del día: {r.pk:.1f} MW</td><td><span class="chip c-ok">Nominal</span></td><td>Ninguna</td></tr>'
            f'<tr class="alt"><td class="n">{r.fin}</td><td>Término de generación</td><td><span class="chip c-info">Operacional</span></td><td>Ninguna</td></tr>')
    else:
        extra=kpi("Velocidad media",f"{r.vel:.2f}","m/s a altura de buje")
        fx=(f'<tr class="alt"><td>Velocidad media de viento</td><td class="n">{r.vel:.2f} m/s</td><td>Torre meteorológica + góndola</td></tr>'
            f'<tr><td>Horas bajo velocidad de arranque</td><td class="n">{r.bajo:.2f} h</td><td>Excluidas del denominador</td></tr>'
            f'<tr class="alt"><td>Horas sobre velocidad de corte</td><td class="n">{r.sobre:.2f} h</td><td>Excluidas del denominador</td></tr>')
        ev=(f'<tr><td class="n">03:40</td><td>Detención por sistema de pitch, WTG-18 · reinicio automático</td><td><span class="chip c-warn">Preventiva</span></td><td>Revisión hidráulica programada</td></tr>'
            f'<tr class="alt"><td class="n">09:05</td><td>Velocidad bajo arranque · {r.bajo:.2f} h acumuladas</td><td><span class="chip c-info">Recurso</span></td><td>Excluido del denominador</td></tr>'
            f'<tr><td class="n">17:50</td><td>Potencia máxima del día: {r.pk:.1f} MW</td><td><span class="chip c-ok">Nominal</span></td><td>Ninguna</td></tr>'
            f'<tr class="alt"><td class="n">21:30</td><td>Desviación de curva de potencia, WTG-18 · −1,8%</td><td><span class="chip c-warn">Preventiva</span></td><td>Verificar calibración de anemometría</td></tr>')
    P=[portada(c,"Informe Diario de Operación",
        "Generado automáticamente al cierre del día operacional, sin ensamblaje manual. Emitido a las 00:15 del día siguiente.",
        kv(("Instalación",c['nom']),("Ubicación",f"{c['com']}, {c['reg']}"),("Capacidad",c['cap']),
           ("Fecha de operación","23 de julio de 2026"),("Referencia",REF)),"Informe diario · muestra")]
    P.append(page(f"""<div class="sec-num">01 · Resumen del día · 23 julio 2026</div>
<div class="eyebrow">Cierre operacional</div><h2 class="t">Qué hizo el activo hoy</h2>
<div class="kpis">{kpi("Generación",f"{r.mwh:,.0f}","MWh del día","#149487")}
{kpi("Factor de planta",f"{r.fp:.1f}%","sobre 24 horas")}
{kpi("FP en operación",f"{r.fpop:.1f}%","solo horas activas")}{extra}</div>
<h3 class="t">Horario de operación</h3>
<table><tr><th>Indicador</th><th style="text-align:right">Valor</th><th>Definición aplicada</th></tr>
<tr><td>Inicio de operación</td><td class="n">{r.ini}</td><td>Primer registro de 15 min sobre 0,5% de la potencia nominal</td></tr>
<tr class="alt"><td>Término de operación</td><td class="n">{r.fin}</td><td>Último registro sobre el mismo umbral</td></tr>
<tr><td>Horas en operación</td><td class="n">{r.horas:.2f} h</td><td>Suma de intervalos sobre umbral</td></tr>
<tr class="alt"><td>Potencia máxima</td><td class="n">{r.pk:.1f} MW</td><td>Máximo instantáneo de 15 min</td></tr>
<tr><td>Factor de planta (24 h)</td><td class="n">{r.fp:.1f}%</td><td>Energía / (P nominal × 24 h)</td></tr>
<tr class="alt"><td>Factor de planta (operación)</td><td class="n">{r.fpop:.1f}%</td><td>Energía / (P nominal × horas en operación)</td></tr></table>
<h3 class="t">Condiciones del recurso</h3>
<table><tr><th>Variable</th><th style="text-align:right">Valor</th><th>Fuente</th></tr>
<tr><td>Temperatura ambiente media</td><td class="n">{d['tamb'][d['tamb'].index.day==DIA].mean():.1f} °C</td><td>Estación en sitio</td></tr>{fx}</table>
<div class="box teal"><h4>Dos factores de planta, dos preguntas distintas</h4>
<p style="margin-bottom:0;">El factor sobre 24 horas ({r.fp:.1f}%) responde cuánto produjo el activo respecto de su máximo teórico diario. El factor sobre horas de operación ({r.fpop:.1f}%) responde qué tan bien trabajó mientras tuvo recurso disponible. Publicar uno sin declarar cuál se está usando es la fuente más común de comparaciones inválidas entre centrales.</p></div>""",
f"{REF} · Muestra","02"))
    P.append(page(f"""<div class="sec-num">02 · Perfil intradiario y eventos</div>
<div class="eyebrow">Curva de generación</div><h2 class="t">Potencia entregada, hora a hora</h2>
<p class="small">Potencia media horaria en MW, calculada sobre registros de 15 minutos. Operación entre las {r.ini} y las {r.fin}.</p>
{bars_svg(horas,[round(float(v),1) for v in hh.values],None)}
<h3 class="t">Registro de eventos del día</h3>
<table><tr><th>Hora</th><th>Evento</th><th>Clasificación</th><th>Acción</th></tr>{ev}
<tr><td class="n">00:15</td><td>Emisión automática del presente informe</td><td><span class="chip c-info">Sistema</span></td><td>—</td></tr></table>
{cobertura(c)}
<div class="box"><h4>Qué debe hacer el equipo mañana</h4>
<p style="margin-bottom:0;"><b>Una acción preventiva abierta.</b> No afecta la disponibilidad certificada del día ni requiere detención. La clasificación y la derivación al equipo competente son automáticas; la orden de despacho de personal a terreno la confirma siempre el jefe de turno.</p></div>{PIE}""",
f"{REF} · Muestra","03"))
    open(f"Informe-Diario-{c['ref']}.html","w",encoding="utf-8").write(doc(f"Quorelia — {c['nom']} — Informe Diario","".join(P)))
    return len(P)

def diario_bess():
    c=CFG['bess']; d=D.bess(); r=D.diario(d); r=r[r.dia==DIA].iloc[0]
    pot=d['pot']; hh=pot[pot.index.day==DIA].resample('h').mean()
    soc=d['soc'][d['soc'].index.day==DIA].resample('h').mean()
    horas=[f"{h:02d}" for h in hh.index.hour]; REF=f"QOR-{c['ref']}-D-20260723"
    cerr='<span class="chip c-ok">Cerrado</span>' if r.cerrado else '<span class="chip c-hold">No cerrado</span>'
    rte=f"{r.rte:.1f}%" if r.cerrado else "Retenido"
    P=[portada(c,"Informe Diario de Operación",
        "Generado automáticamente al cierre del día operacional, sin ensamblaje manual. Emitido a las 00:15 del día siguiente.",
        kv(("Instalación",c['nom']),("Ubicación",f"{c['com']}, {c['reg']}"),("Capacidad",c['cap']),
           ("Fecha de operación","23 de julio de 2026"),("Referencia",REF)),"Informe diario · muestra")]
    P.append(page(f"""<div class="sec-num">01 · Resumen del día · 23 julio 2026</div>
<div class="eyebrow">Cierre operacional</div><h2 class="t">Qué hizo el activo hoy</h2>
<div class="kpis">{kpi("Energía descargada",f"{r.desc:,.0f}","MWh","#149487")}
{kpi("Energía cargada",f"{r.carga:,.0f}","MWh")}
{kpi("Eficiencia RTE",rte,"ciclo "+("cerrado" if r.cerrado else "NO cerrado"),None if r.cerrado else "#b91c1c")}
{kpi("Ciclos equivalentes",f"{r.ciclos:.2f}","del día")}</div>
<h3 class="t">Ventanas de operación</h3>
<table><tr><th>Ventana</th><th style="text-align:right">Inicio</th><th style="text-align:right">Término</th><th style="text-align:right">Energía MWh</th></tr>
<tr><td>Carga</td><td class="n">{r.ini_c}</td><td class="n">{r.fin_c}</td><td class="n">{r.carga:,.0f}</td></tr>
<tr class="alt"><td>Descarga</td><td class="n">{r.ini_d}</td><td class="n">{r.fin_d}</td><td class="n">{r.desc:,.0f}</td></tr>
<tr style="border-top:1.2px solid var(--navy);font-weight:600;"><td>Total en operación · {r.horas:.2f} h</td><td class="n">{r.ini_c}</td><td class="n">{r.fin_d}</td><td class="n">{r.carga+r.desc:,.0f}</td></tr></table>
<h3 class="t">Estado de carga y potencia</h3>
<table><tr><th>Indicador</th><th style="text-align:right">Valor</th><th>Criterio</th><th>Evaluación</th></tr>
<tr><td>SOC inicial · SOC final</td><td class="n">{r.soc_i:.1f}% · {r.soc_f:.1f}%</td><td>Δ ≤ 2,0 pts para ciclo cerrado</td><td>{cerr}</td></tr>
<tr class="alt"><td>SOC mínimo del día</td><td class="n">{r.soc_min:.1f}%</td><td>≥ 8%</td><td><span class="chip c-ok">Conforme</span></td></tr>
<tr><td>SOC máximo del día</td><td class="n">{r.soc_max:.1f}%</td><td>≤ 95%</td><td><span class="chip c-ok">Conforme</span></td></tr>
<tr class="alt"><td>Potencia máxima</td><td class="n">{r.pk:.1f} MW</td><td>≤ 200 MW</td><td><span class="chip c-ok">Conforme</span></td></tr>
<tr><td>Factor de planta (descarga, 24 h)</td><td class="n">{r.fp:.1f}%</td><td>—</td><td><span class="chip c-info">Informativo</span></td></tr></table>
<div class="box teal"><h4>Regla aplicada a la eficiencia</h4>
<p style="margin-bottom:0;">El RTE solo se publica cuando el ciclo cierra: el SOC final debe volver a ±2 puntos del inicial. Calcularlo sobre un ciclo abierto mide energía almacenada el día anterior y produce valores sobre 100%, físicamente imposibles. Cuando el ciclo no cierra, la cifra se retiene y se declara la razón.</p></div>""",
f"{REF} · Muestra","02"))
    P.append(page(f"""<div class="sec-num">02 · Perfil intradiario y eventos</div>
<div class="eyebrow">Curva de potencia</div><h2 class="t">Potencia y estado de carga, hora a hora</h2>
<p class="small">Potencia neta en MW. Valores negativos corresponden a carga; positivos, a descarga.</p>
{bars_svg(horas,[round(float(v),1) for v in hh.values],None)}
<h3 class="t">Estado de carga durante el día</h3>
{line_svg([float(v) for v in soc.values],labels=["00","06","12","18","23"],ylab="SOC %")}
<h3 class="t">Registro de eventos del día</h3>
<table><tr><th>Hora</th><th>Evento</th><th>Clasificación</th><th>Acción</th></tr>
<tr><td class="n">{r.ini_c}</td><td>Inicio de ventana de carga</td><td><span class="chip c-info">Operacional</span></td><td>Ninguna</td></tr>
<tr class="alt"><td class="n">11:45</td><td>Dispersión de celdas 34 mV, rack ESS-06-03</td><td><span class="chip c-warn">Preventiva</span></td><td>Derivado a especialidad BMS</td></tr>
<tr><td class="n">{r.ini_d}</td><td>Inicio de ventana de descarga</td><td><span class="chip c-info">Operacional</span></td><td>Ninguna</td></tr>
<tr class="alt"><td class="n">{r.fin_d}</td><td>Cierre de descarga · SOC {r.soc_f:.1f}%</td><td><span class="chip c-ok">Nominal</span></td><td>Ninguna</td></tr>
<tr><td class="n">00:15</td><td>Emisión automática del presente informe</td><td><span class="chip c-info">Sistema</span></td><td>—</td></tr></table>
{cobertura(c)}
<div class="box"><h4>Qué debe hacer el equipo mañana</h4>
<p style="margin-bottom:0;"><b>Una acción preventiva abierta:</b> inspección del sistema de balanceo del rack ESS-06-03. No afecta la disponibilidad certificada del día ni requiere detención. La orden de despacho la confirma el jefe de turno.</p></div>{PIE}""",
f"{REF} · Muestra","03"))
    open("Informe-Diario-BESS.html","w",encoding="utf-8").write(doc(f"Quorelia — {c['nom']} — Informe Diario","".join(P)))
    return len(P)

if __name__=="__main__":
    print("diario solar :",diario_solar_eol('solar'),"páginas")
    print("diario eólico:",diario_solar_eol('eolico'),"páginas")
    print("diario BESS  :",diario_bess(),"páginas")
