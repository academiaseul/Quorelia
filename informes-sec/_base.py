# -*- coding: utf-8 -*-
"""Shared design system + helpers for Quorelia regulatory sample reports (ES)."""

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');
*{box-sizing:border-box;margin:0;padding:0;}
:root{
  --ink:#101418; --ink-2:#3d474f; --grey:#8a949c; --line:#e2e5e8;
  --paper:#fff; --paper-2:#f2f3f4; --paper-3:#e9eaec;
  --navy:#0b1c2c; --teal:#149487; --teal-lt:#1fb6a8; --amber:#b45309; --red:#b91c1c;
  --sans:'Inter',-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
  --mono:'IBM Plex Mono','SF Mono',Consolas,monospace;
}
body{font-family:var(--sans);color:var(--ink);background:#8a929a;line-height:1.5;-webkit-font-smoothing:antialiased;}
.page{width:8.5in;min-height:11in;margin:0 auto 18px;background:var(--paper);padding:0.72in 0.78in 0.62in;
  position:relative;page-break-after:always;box-shadow:0 2px 18px rgba(0,0,0,.25);}
@media print{ body{background:#fff;} .page{box-shadow:none;margin:0;} }

/* Tipografía Palantir: peso ligero, tracking negativo */
h1,h2,h3,h4{font-weight:400;letter-spacing:-0.032em;line-height:1.08;}
h2.t{font-size:23px;margin-bottom:6px;}
h3.t{font-size:14px;font-weight:600;letter-spacing:-0.012em;margin:20px 0 8px;}
p{font-size:10.2px;line-height:1.62;color:var(--ink-2);margin-bottom:8px;}
.small{font-size:8.6px;color:var(--grey);line-height:1.55;}

/* Etiqueta monoespaciada en versales */
.eyebrow{font-family:var(--mono);font-size:8.5px;font-weight:500;letter-spacing:.16em;
  text-transform:uppercase;color:var(--grey);margin-bottom:9px;}
.sec-num{font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--grey);border-bottom:1px solid var(--ink);padding-bottom:7px;margin-bottom:18px;}
.foot{position:absolute;bottom:0.42in;left:0.78in;right:0.78in;display:flex;justify-content:space-between;
  font-family:var(--mono);font-size:7.6px;letter-spacing:.12em;text-transform:uppercase;color:var(--grey);
  border-top:1px solid var(--line);padding-top:7px;}

/* Tablas: regla superior gruesa, filas con hairline */
table{width:100%;border-collapse:collapse;margin:10px 0;}
th{font-family:var(--mono);font-size:7.6px;font-weight:500;letter-spacing:.13em;text-transform:uppercase;
  color:var(--grey);text-align:left;padding:8px 8px 8px 0;border-bottom:1.4px solid var(--ink);white-space:nowrap;}
td{font-size:9.4px;padding:7px 8px 7px 0;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2);}
td.n{font-family:var(--mono);text-align:right;font-size:8.8px;padding-right:0;color:var(--ink);}
td b{color:var(--ink);font-weight:600;}
tr.alt td{background:transparent;}

.kv{width:100%;border-collapse:collapse;}
.kv td{font-size:9.6px;padding:7px 0;border-bottom:1px solid var(--line);}
.kv td:first-child{width:34%;color:var(--grey);font-family:var(--mono);font-size:8px;
  letter-spacing:.11em;text-transform:uppercase;padding-right:12px;}

/* Chips sin relleno: sólo texto en mono, estilo Palantir */
.chip{display:inline-block;font-family:var(--mono);font-size:7.4px;font-weight:500;letter-spacing:.11em;
  text-transform:uppercase;white-space:nowrap;padding:2px 0;}
.c-ok{color:var(--teal);}
.c-warn{color:var(--amber);}
.c-hold{color:var(--red);}
.c-info{color:var(--grey);}

/* Cifras: peso ligero y grandes, con regla superior */
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin:14px 0 6px;border-top:1.4px solid var(--ink);}
.kpi{padding:14px 14px 14px 0;border-right:1px solid var(--line);}
.kpi:last-child{border-right:0;}
.kpi .l{font-family:var(--mono);font-size:7.4px;letter-spacing:.13em;text-transform:uppercase;color:var(--grey);margin-bottom:8px;}
.kpi .v{font-size:24px;font-weight:400;letter-spacing:-.04em;line-height:1;}
.kpi .s{font-size:7.8px;color:var(--grey);margin-top:5px;}

/* Avisos: filete lateral, sin fondo saturado */
.box{border-left:2px solid var(--ink);padding:13px 0 13px 15px;margin:12px 0;}
.box.teal{border-left-color:var(--teal);}
.box.amber{border-left-color:var(--amber);}
.box h4{font-size:11px;font-weight:600;margin-bottom:6px;letter-spacing:-.01em;}
.box p{font-size:9.8px;}

/* Hallazgos */
.finding{border-top:1px solid var(--line);padding:13px 0;margin:0;}
.finding.hold{border-top-color:var(--red);}
.finding.warn{border-top-color:var(--amber);}
.finding.ok{border-top-color:var(--teal);}
.finding .fh{display:flex;justify-content:space-between;align-items:baseline;gap:10px;margin-bottom:5px;}
.finding .fh b{font-size:10.6px;font-weight:600;color:var(--ink);}

/* Portada clara */
.cover{background:var(--paper);}
.cover .page-in{min-height:9.4in;display:flex;flex-direction:column;}
.wm{display:inline-block;font-family:var(--mono);font-size:7.4px;letter-spacing:.15em;text-transform:uppercase;
  color:var(--amber);border:1px solid rgba(180,83,9,.4);padding:3px 9px;}

/* Pasos numerados */
.steps{counter-reset:s;}
.step{display:grid;grid-template-columns:26px 1fr;gap:12px;padding:11px 0;border-top:1px solid var(--line);}
.step .i{font-family:var(--mono);font-size:9px;color:var(--grey);letter-spacing:.06em;}
.step .b{font-size:9.6px;line-height:1.6;color:var(--ink-2);}
.step .b b{color:var(--ink);font-size:10px;font-weight:600;}
"""

def page(inner, foot_l, foot_r, cls=""):
    return f'<div class="page {cls}">{inner}<div class="foot"><span>{foot_l}</span><span>{foot_r}</span></div></div>'

def kpi(label, value, sub="", color=None):
    c = f' style="color:{color}"' if color else ""
    return f'<div class="kpi"><div class="l">{label}</div><div class="v"{c}>{value}</div><div class="s">{sub}</div></div>'

def bars_svg(labels, values, threshold=None, w=680, h=190, unit="%", thr_label=""):
    """Simple vertical bar chart as inline SVG."""
    n=len(values); pad_l=30; pad_b=34; pad_t=10
    iw=w-pad_l-10; ih=h-pad_b-pad_t
    vmax=max(max(values), threshold or 0)*1.12
    bw=iw/n*0.62; gap=iw/n
    s=[f'<svg viewBox="0 0 {w} {h}" style="width:100%;height:auto;font-family:var(--mono)">']
    for gy in (0,.25,.5,.75,1):
        y=pad_t+ih-ih*gy
        s.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{w-10}" y2="{y:.1f}" stroke="#e3e9ec" stroke-width="0.8"/>')
        s.append(f'<text x="{pad_l-5}" y="{y+2.5:.1f}" font-size="7" fill="#8fa0ab" text-anchor="end">{gy*vmax:.0f}</text>')
    for i,(lb,v) in enumerate(zip(labels,values)):
        bh=ih*(v/vmax); x=pad_l+gap*i+(gap-bw)/2; y=pad_t+ih-bh
        col="#1fb6a8" if (threshold is None or v>=threshold) else "#ef4444"
        s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{col}" rx="1.5"/>')
        s.append(f'<text x="{x+bw/2:.1f}" y="{pad_t+ih+10:.1f}" font-size="6.4" fill="#5c7080" text-anchor="middle">{lb}</text>')
        s.append(f'<text x="{x+bw/2:.1f}" y="{y-3:.1f}" font-size="6.4" fill="#33454f" text-anchor="middle">{v:g}</text>')
    if threshold is not None:
        ty=pad_t+ih-ih*(threshold/vmax)
        s.append(f'<line x1="{pad_l}" y1="{ty:.1f}" x2="{w-10}" y2="{ty:.1f}" stroke="#f5a623" stroke-width="1.1" stroke-dasharray="5 3"/>')
        s.append(f'<text x="{w-12}" y="{ty-4:.1f}" font-size="6.8" fill="#b45309" text-anchor="end">{thr_label}</text>')
    s.append('</svg>')
    return "".join(s)

def line_svg(values, w=680, h=150, color="#1fb6a8", fill=True, labels=None, ylab=""):
    n=len(values); pad_l=32; pad_b=22; pad_t=8
    iw=w-pad_l-10; ih=h-pad_b-pad_t
    vmin=min(values)*0.96; vmax=max(values)*1.04
    rng=(vmax-vmin) or 1
    pts=[(pad_l+iw*i/(n-1), pad_t+ih-ih*((v-vmin)/rng)) for i,v in enumerate(values)]
    d=" ".join(f"{'M' if i==0 else 'L'}{x:.1f},{y:.1f}" for i,(x,y) in enumerate(pts))
    s=[f'<svg viewBox="0 0 {w} {h}" style="width:100%;height:auto;font-family:var(--mono)">']
    for gy in (0,.5,1):
        y=pad_t+ih-ih*gy
        s.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{w-10}" y2="{y:.1f}" stroke="#e3e9ec" stroke-width="0.8"/>')
        s.append(f'<text x="{pad_l-5}" y="{y+2.5:.1f}" font-size="7" fill="#8fa0ab" text-anchor="end">{vmin+rng*gy:.0f}</text>')
    if fill:
        s.append(f'<path d="{d} L{pts[-1][0]:.1f},{pad_t+ih} L{pad_l},{pad_t+ih} Z" fill="{color}" opacity="0.10"/>')
    s.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.6"/>')
    if labels:
        step=max(1,n//len(labels))
        for i,lb in enumerate(labels):
            x=pad_l+iw*(i*step)/(n-1) if n>1 else pad_l
            s.append(f'<text x="{x:.1f}" y="{h-7}" font-size="6.4" fill="#5c7080" text-anchor="middle">{lb}</text>')
    if ylab:
        s.append(f'<text x="{pad_l}" y="{pad_t-1}" font-size="6.6" fill="#8fa0ab">{ylab}</text>')
    s.append('</svg>')
    return "".join(s)

def doc(title, body):
    return (f'<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            f'<title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>')
