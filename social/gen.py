# -*- coding: utf-8 -*-
"""Compone las imágenes promocionales de las demos.
   Usa las cifras reales de la flota demo (Cerro Aurora) para que la
   imagen no prometa nada que el producto no muestre."""

ESTILO = """
  :root{
    --navy:#081522; --navy-2:#0e2233; --panel:#12293c;
    --line:rgba(255,255,255,.13); --line-2:rgba(255,255,255,.07);
    --txt:#f2f5f7; --dim:#8fa3b0; --dim-2:#5b6d7a;
    --teal:#1fb6a8; --amber:#d97706; --red:#e05252;
    --sans:'Inter',-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
    --mono:'IBM Plex Mono','SF Mono',Consolas,monospace;
  }
  *{box-sizing:border-box;margin:0;padding:0;}
  body{font-family:var(--sans);background:var(--navy);color:var(--txt);
    -webkit-font-smoothing:antialiased;}
  .card{position:relative;overflow:hidden;background:
      radial-gradient(120% 90% at 82% 12%, rgba(31,182,168,.10), transparent 58%),
      linear-gradient(160deg,#081522,#0c1e2e 58%,#081522);
    display:flex;flex-direction:column;}
  @media print{ .card{box-shadow:none;} }

  .marca{display:flex;align-items:center;gap:12px;}
  .kick{font-family:var(--mono);letter-spacing:.17em;text-transform:uppercase;color:var(--teal);}
  h1{font-weight:300;letter-spacing:-.024em;line-height:1.08;color:#fff;}
  .sub{color:var(--dim);line-height:1.5;}

  /* ── maqueta de tablero ── */
  .ui{background:var(--navy-2);border:1px solid var(--line);overflow:hidden;
    box-shadow:0 22px 60px rgba(0,0,0,.45);}
  .ui-top{display:flex;align-items:center;justify-content:space-between;
    padding:9px 14px;background:rgba(0,0,0,.28);border-bottom:1px solid var(--line);}
  .ui-t{font-family:var(--mono);font-size:9px;letter-spacing:.13em;text-transform:uppercase;color:var(--dim);}
  .dot{width:6px;height:6px;border-radius:50%;background:var(--teal);display:inline-block;margin-right:6px;}
  .kpis{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--line-2);}
  .kpi{padding:11px 13px;border-right:1px solid var(--line-2);}
  .kpi:last-child{border-right:0;}
  .kpi .k{font-family:var(--mono);font-size:7.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim-2);}
  .kpi .v{font-size:19px;font-weight:400;letter-spacing:-.035em;margin-top:4px;color:#fff;}
  .kpi .v.t{color:var(--teal);}
  .body{display:grid;grid-template-columns:1.55fr 1fr;}
  .chart{padding:13px 14px;border-right:1px solid var(--line-2);}
  .lg{font-family:var(--mono);font-size:7.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--dim-2);margin-bottom:9px;}
  .side{padding:13px 14px;display:flex;flex-direction:column;gap:9px;}
  .al{border-left:2px solid var(--amber);padding:7px 0 7px 9px;}
  .al.hold{border-left-color:var(--dim-2);}
  .al .h{font-family:var(--mono);font-size:7px;letter-spacing:.13em;text-transform:uppercase;color:var(--amber);}
  .al.hold .h{color:var(--dim-2);}
  .al .b{font-size:9.5px;color:#dbe6ec;line-height:1.4;margin-top:3px;}
  .al .b b{color:#fff;font-weight:600;}

  /* ── documento ── */
  .doc{background:#fff;color:#101418;overflow:hidden;
    box-shadow:0 22px 60px rgba(0,0,0,.45);}
  .doc-h{padding:11px 14px 9px;border-bottom:1.4px solid #101418;}
  .doc-k{font-family:var(--mono);font-size:7px;letter-spacing:.16em;text-transform:uppercase;color:#149487;}
  .doc-t{font-size:13px;font-weight:400;letter-spacing:-.02em;margin-top:4px;}
  .doc-r{display:flex;justify-content:space-between;padding:7px 14px;
    border-bottom:1px solid #e2e5e8;font-size:9px;color:#3d474f;}
  .doc-r b{color:#101418;font-weight:600;}

  .pie{display:flex;align-items:center;justify-content:space-between;gap:20px;}
  .cta{font-family:var(--mono);letter-spacing:.1em;color:var(--teal);}
  .free{display:inline-block;border:1px solid var(--teal);color:var(--teal);
    font-family:var(--mono);letter-spacing:.13em;text-transform:uppercase;}
"""

def barras(w, h, vals, color="#1fb6a8"):
    """Curva de generación en barras — perfil solar real de la demo."""
    n=len(vals); mx=max(vals); gap=w*0.018; bw=(w-gap*(n-1))/n
    out=[f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    for i in range(4):
        y=h*i/4
        out.append(f'<line x1="0" y1="{y:.1f}" x2="{w}" y2="{y:.1f}" stroke="rgba(255,255,255,.05)" stroke-width="1"/>')
    for i,v in enumerate(vals):
        bh=(v/mx)*h*0.92; x=i*(bw+gap); y=h-bh
        op=0.35 if v/mx<0.18 else 1
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{color}" opacity="{op}"/>')
    out.append('</svg>')
    return ''.join(out)

# perfil diario real del informe FV de muestra (MW por hora)
PERFIL=[0,0,0.4,9.4,35.3,48.4,53.9,56,55.9,53.7,47.7,33.1,7.3,0.5,0,0]

def tablero(ancho_grafico=250, alto_grafico=76):
    return f"""
    <div class="ui">
      <div class="ui-top">
        <span class="ui-t"><span class="dot"></span>Quorelia Control Center · BESS Cerro Aurora</span>
        <span class="ui-t">126 MW / 780 MWh</span>
      </div>
      <div class="kpis">
        <div class="kpi"><div class="k">Disponibilidad</div><div class="v t">98,4%</div></div>
        <div class="kpi"><div class="k">Cobertura de datos</div><div class="v">99,1%</div></div>
        <div class="kpi"><div class="k">Eficiencia de ciclo</div><div class="v">86,3%</div></div>
        <div class="kpi"><div class="k">Hallazgos abiertos</div><div class="v">3</div></div>
      </div>
      <div class="body">
        <div class="chart">
          <div class="lg">Potencia entregada · 15 min</div>
          {barras(ancho_grafico, alto_grafico, PERFIL)}
        </div>
        <div class="side">
          <div class="al">
            <div class="h">Riesgo emergente</div>
            <div class="b">ESS-08 · dispersión de celdas <b>131 → 470 mV</b> (umbral 500)</div>
          </div>
          <div class="al hold">
            <div class="h">Cifra retenida</div>
            <div class="b">RTE no publicada: <b>ciclo abierto</b>, SOC derivó +16,43 pp</div>
          </div>
        </div>
      </div>
    </div>"""

DOC = """
    <div class="doc">
      <div class="doc-h">
        <div class="doc-k">Informe diario de operación</div>
        <div class="doc-t">BESS Cerro Aurora · 23 jul 2026</div>
      </div>
      <div class="doc-r"><span>Energía descargada</span><b>401 MWh</b></div>
      <div class="doc-r"><span>Factor de planta</span><b>13,9%</b></div>
      <div class="doc-r"><span>Horas en operación</span><b>10,00 h</b></div>
      <div class="doc-r" style="border-bottom:0;"><span>Muestras validadas</span><b>1.130 / 1.152</b></div>
    </div>"""

# ══════════════ 1200 × 630 — tarjeta de enlace / X ══════════════
ANCHO = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{ESTILO}
@page{{size:1200px 630px;margin:0;}}
.card{{width:1200px;height:630px;padding:44px 48px;}}
.kick{{font-size:11px;}} h1{{font-size:40px;max-width:15ch;margin-top:14px;}}
.sub{{font-size:15px;max-width:44ch;margin-top:14px;}}
.free{{font-size:9.5px;padding:6px 12px;margin-top:20px;}}
.cta{{font-size:13px;}}
.split{{display:grid;grid-template-columns:1fr 1.12fr;gap:40px;align-items:center;flex:1;}}
.stack{{display:flex;flex-direction:column;gap:14px;}}
</style></head><body>
<div class="card">
  <div class="marca">
    <img src="quorelia-mark-white.png" style="height:27px;width:auto;">
    <img src="quorelia-wordmark-white.png" style="height:12px;width:auto;">
  </div>
  <div class="split">
    <div>
      <p class="kick">Demo gratuita · sobre sus propios datos</p>
      <h1>Su SCADA ya ve todo.<br>Nadie alcanza a leerlo.</h1>
      <p class="sub">Una capa de inteligencia sobre el sistema que usted ya tiene. Informes automáticos, Control Center a medida, cada cifra trazable hasta su medición.</p>
      <span class="free">Sin reemplazar nada · Sin compromiso</span>
    </div>
    <div class="stack">
      {tablero(268, 78)}
      {DOC}
    </div>
  </div>
  <div class="pie">
    <span class="cta">jay@quorelia.org · quorelia.org</span>
    <span class="kick" style="color:#5b6d7a;font-size:9px;">Datos ilustrativos · flota demo</span>
  </div>
</div></body></html>"""

# ══════════════ 1080 × 1080 — feed LinkedIn ══════════════
CUAD = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{ESTILO}
@page{{size:1080px 1080px;margin:0;}}
.card{{width:1080px;height:1080px;padding:56px 58px;}}
.kick{{font-size:12.5px;}} h1{{font-size:52px;max-width:16ch;margin-top:16px;}}
.sub{{font-size:17px;max-width:52ch;margin-top:16px;}}
.free{{font-size:11px;padding:8px 15px;margin-top:24px;}}
.cta{{font-size:15px;}}
.stack{{display:flex;flex-direction:column;gap:18px;margin:34px 0;flex:1;justify-content:center;}}
</style></head><body>
<div class="card">
  <div class="marca">
    <img src="quorelia-mark-white.png" style="height:34px;width:auto;">
    <img src="quorelia-wordmark-white.png" style="height:15px;width:auto;">
  </div>
  <p class="kick" style="margin-top:34px;">Demo gratuita · sobre sus propios datos</p>
  <h1>Su SCADA ya ve todo.<br>Nadie alcanza a leerlo.</h1>
  <p class="sub">Una capa de inteligencia sobre el sistema que usted ya tiene. Informes automáticos, Control Center a medida, y cada cifra trazable hasta la medición que la produjo.</p>
  <div class="stack">
    {tablero(560, 118)}
    {DOC}
  </div>
  <div class="pie">
    <span class="cta">jay@quorelia.org · quorelia.org</span>
    <span class="kick" style="color:#5b6d7a;font-size:10px;">Datos ilustrativos</span>
  </div>
</div></body></html>"""

open('promo-ancho.html','w',encoding='utf-8').write(ANCHO)
open('promo-cuadrado.html','w',encoding='utf-8').write(CUAD)
print('html generado')
