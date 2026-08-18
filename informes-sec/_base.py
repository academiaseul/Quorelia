# -*- coding: utf-8 -*-
"""Shared design system + helpers for Quorelia regulatory sample reports (ES)."""

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
*{box-sizing:border-box;margin:0;padding:0;}
:root{
  --navy:#0b1c2c; --navy-2:#122a40; --teal:#1fb6a8; --teal-dark:#149487;
  --amber:#f5a623; --green:#22c55e; --red:#ef4444;
  --ink:#0b1c2c; --muted:#5c7080; --bg:#f7f9fa; --white:#fff; --border:#e3e9ec;
  --mono:'SF Mono',Consolas,'Courier New',monospace;
}
body{font-family:'Inter',sans-serif;color:var(--ink);background:#8a929a;line-height:1.55;}
.page{width:8.5in;min-height:11in;margin:0 auto 18px;background:#fff;padding:0.7in 0.75in 0.55in;
  position:relative;page-break-after:always;box-shadow:0 2px 18px rgba(0,0,0,.25);}
@media print{ body{background:#fff;} .page{box-shadow:none;margin:0;} }
h1,h2,h3,h4{letter-spacing:-0.02em;font-weight:600;}
.eyebrow{font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--teal-dark);margin-bottom:7px;}
.sec-num{font-family:var(--mono);font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);
  border-bottom:0.8px solid var(--border);padding-bottom:6px;margin-bottom:16px;}
h2.t{font-size:19px;margin-bottom:5px;} h3.t{font-size:13.5px;margin:16px 0 7px;}
p{font-size:10.2px;line-height:1.62;color:#33454f;margin-bottom:8px;}
.small{font-size:8.6px;color:var(--muted);line-height:1.55;}
.foot{position:absolute;bottom:0.4in;left:0.75in;right:0.75in;display:flex;justify-content:space-between;
  font-family:var(--mono);font-size:7.6px;letter-spacing:.07em;text-transform:uppercase;color:#8fa0ab;
  border-top:0.8px solid var(--border);padding-top:6px;}
table{width:100%;border-collapse:collapse;margin:9px 0;}
th{font-family:var(--mono);font-size:7.8px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
  text-align:left;padding:6px 7px;border-bottom:1.2px solid var(--navy);white-space:nowrap;}
td{font-size:9.4px;padding:5px 7px;border-bottom:0.8px solid var(--border);vertical-align:top;}
td.n{font-family:var(--mono);text-align:right;font-size:9px;}
tr.alt td{background:#f7f9fa;}
.kv{width:100%;border-collapse:collapse;}
.kv td{font-size:9.6px;padding:6px 0;border-bottom:0.8px solid var(--border);}
.kv td:first-child{width:34%;color:var(--muted);font-family:var(--mono);font-size:8.2px;
  letter-spacing:.07em;text-transform:uppercase;padding-right:12px;}
.chip{display:inline-block;font-family:var(--mono);font-size:7.6px;font-weight:600;letter-spacing:.08em;
  text-transform:uppercase;padding:2.5px 7px;border-radius:3px;white-space:nowrap;}
.c-ok{background:rgba(34,197,94,.14);color:#15803d;}
.c-warn{background:rgba(245,166,35,.16);color:#b45309;}
.c-hold{background:rgba(239,68,68,.12);color:#b91c1c;}
.c-info{background:rgba(31,182,168,.14);color:var(--teal-dark);}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin:12px 0 4px;
  border:0.8px solid var(--border);border-radius:6px;overflow:hidden;}
.kpi{padding:11px 13px;border-left:0.8px solid var(--border);}
.kpi:first-child{border-left:0;}
.kpi .l{font-family:var(--mono);font-size:7.4px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:5px;}
.kpi .v{font-size:20px;font-weight:600;letter-spacing:-0.03em;line-height:1;}
.kpi .s{font-size:8px;color:var(--muted);margin-top:4px;}
.box{border:0.8px solid var(--border);border-radius:6px;padding:13px 15px;margin:10px 0;background:#fbfcfd;}
.box.teal{border-color:rgba(31,182,168,.35);background:rgba(31,182,168,.05);}
.box.amber{border-color:rgba(245,166,35,.4);background:rgba(245,166,35,.05);}
.box h4{font-size:11px;margin-bottom:6px;}
.finding{border-left:2.5px solid var(--border);padding:9px 0 9px 13px;margin:10px 0;}
.finding.hold{border-left-color:var(--red);} .finding.warn{border-left-color:var(--amber);}
.finding.ok{border-left-color:var(--green);}
.finding .fh{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:5px;}
.finding .fh b{font-size:10.4px;}
.cover{background:var(--navy);color:#fff;}
.cover .page-in{min-height:9.6in;display:flex;flex-direction:column;}
.wm{display:inline-block;font-family:var(--mono);font-size:7.6px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--amber);border:0.8px solid rgba(245,166,35,.5);padding:3.5px 9px;border-radius:3px;}
.steps{counter-reset:s;}
.step{display:flex;gap:11px;margin-bottom:9px;}
.step .i{flex:none;width:19px;height:19px;border-radius:4px;background:var(--navy);color:var(--teal);
  font-family:var(--mono);font-size:9px;display:flex;align-items:center;justify-content:center;font-weight:700;}
.step .b{font-size:9.6px;line-height:1.6;color:#33454f;}
.step .b b{color:var(--ink);font-size:10px;}
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
