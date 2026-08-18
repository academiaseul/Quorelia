# -*- coding: utf-8 -*-
"""Tarjetas de presentación Quorelia — 90×55 mm + 3 mm de sangrado (96×61 mm).
Estructura tomada de la tarjeta de referencia: nombre grande, cargo al costado,
empresa en negrita, dirección, contactos etiquetados en dos columnas,
gráfico de marca sangrando por el borde derecho. Reverso con logo centrado."""
import base64, pathlib
from weasyprint import HTML

def b64(p, mime="image/png"):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()

SIMBOLO = b64("quorelia-symbol-color.png")
LOGO_BLANCO = b64("quorelia-logo-full-white.png")

# ── EDITAR AQUÍ ────────────────────────────────────────────────────────────
PERSONAS = {
 "Jay": dict(
    nombre="Jae Hee Kim", nombre_corto="Jay Kim",
    cargo="Cofundador &amp; COO", cargo_en="Co-Founder &amp; COO",
    movil="+56 9 XXXX XXXX",              # ← completar
    email="jay@quorelia.org",
 ),
 "Diego": dict(
    nombre="Diego Ostertag", nombre_corto="Diego Ostertag",
    cargo="Cofundador &amp; CEO", cargo_en="Co-Founder &amp; CEO",
    movil="+56 9 XXXX XXXX",              # ← completar
    email="diego@quorelia.org",           # ← confirmar
 ),
}
EMPRESA   = "Quorelia SpA"
CIUDAD    = "Santiago · Chile"
WEB       = "quorelia.org"
# ───────────────────────────────────────────────────────────────────────────

CSS = """
@page{size:96mm 61mm;margin:0;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Inter','Segoe UI',Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;}
.card{width:96mm;height:61mm;position:relative;overflow:hidden;page-break-after:always;}
/* zona segura: 3 mm de sangrado + 4 mm de margen interior */
.safe{position:absolute;left:7mm;top:7mm;right:7mm;bottom:7mm;}

/* ───── FRENTE ───── */
.front{background:#ffffff;}
.sym{
  position:absolute;right:-9mm;top:50%;transform:translateY(-50%);
  width:39mm;height:auto;opacity:0.95;
}
.nombre{font-size:17pt;font-weight:300;letter-spacing:-0.03em;color:#0b1c2c;line-height:1;}
.cargo{font-size:7.6pt;font-weight:500;color:#5c7080;line-height:1.35;margin-top:2mm;}
.empresa{font-size:10pt;font-weight:700;color:#0b1c2c;letter-spacing:-0.015em;}
.giro{
  font-family:'SF Mono',Consolas,monospace;font-size:5.6pt;letter-spacing:0.14em;
  text-transform:uppercase;color:#1fb6a8;margin-top:1.1mm;
}
.rule{width:11mm;height:0.5mm;background:#1fb6a8;margin:3.2mm 0;}
.datos{font-size:7pt;line-height:1.66;color:#33454f;}
.datos .lab{
  display:inline-block;width:13mm;font-weight:700;color:#1fb6a8;
  font-size:6.4pt;letter-spacing:0.03em;
}
.ciudad{font-size:7pt;color:#5c7080;line-height:1.5;}

/* ───── REVERSO ───── */
.back{background:#0b1c2c;}
.back .center{
  position:absolute;inset:0;display:flex;flex-direction:column;
  align-items:center;justify-content:center;padding-bottom:9mm;
}
.logo{width:38mm;height:auto;display:block;}
.tag{
  font-family:'SF Mono',Consolas,monospace;font-size:5.4pt;letter-spacing:0.2em;
  text-transform:uppercase;color:#1fb6a8;margin-top:4mm;text-align:center;
}
.motto{font-size:7pt;font-weight:300;color:#8fa3b0;margin-top:2.6mm;text-align:center;font-style:italic;}
.trace{
  position:absolute;left:7mm;right:7mm;bottom:5.5mm;
  display:flex;align-items:flex-end;gap:0.5mm;height:2.8mm;
}
.trace i{flex:1;background:#149487;border-radius:0.2mm;display:block;}
.trace i.a{background:#1fb6a8;}
.trace i.g{background:#243642;}
"""

def barras(n=46):
    import random
    random.seed(7); out=[]
    for i in range(n):
        r=random.random()
        if r<0.05: out.append('<i class="g" style="height:100%"></i>')
        elif r<0.5: out.append(f'<i class="a" style="height:{random.randint(38,100)}%"></i>')
        else:       out.append(f'<i style="height:{random.randint(30,92)}%"></i>')
    return "".join(out)

def tarjeta(p, idioma="es"):
    cargo = p["cargo"] if idioma=="es" else p["cargo_en"]
    lab_mov = "Móvil" if idioma=="es" else "Mobile"
    lab_web = "Web"
    giro = "Inteligencia en energía renovable" if idioma=="es" else "Renewable energy intelligence"
    motto = ("Siempre vigilando. Al servicio de la energía del planeta."
             if idioma=="es" else
             "Ever watching. In service of the planet's energy.")
    front = f"""<div class="card front">
  <img class="sym" src="{SIMBOLO}" alt="">
  <div class="safe">
    <div class="nombre">{p['nombre']}</div>
    <div class="cargo">{cargo}</div>
    <div class="rule"></div>
    <div class="empresa">{EMPRESA}</div>
    <div class="giro">{giro}</div>
    <div style="position:absolute;left:0;bottom:0;">
      <div class="datos">
        <div><span class="lab">{lab_mov}</span>{p['movil']}</div>
        <div><span class="lab">E-mail</span>{p['email']}</div>
        <div><span class="lab">{lab_web}</span>{WEB}</div>
      </div>
      <div class="ciudad" style="margin-top:1.6mm;">{CIUDAD}</div>
    </div>
  </div>
</div>"""
    back = f"""<div class="card back">
  <div class="center">
    <img class="logo" src="{LOGO_BLANCO}" alt="Quorelia">
    <div class="tag">{giro}</div>
    <div class="motto">{motto}</div>
  </div>
  <div class="trace">{barras()}</div>
</div>"""
    return front + back

def generar(clave, idioma, salida):
    p = PERSONAS[clave]
    html = f"<!DOCTYPE html><html lang='{idioma}'><head><meta charset='UTF-8'><style>{CSS}</style></head><body>{tarjeta(p,idioma)}</body></html>"
    pathlib.Path("/tmp/_card.html").write_text(html, encoding="utf-8")
    HTML(filename="/tmp/_card.html", base_url=".").write_pdf(salida)
    print("→", salida)

if __name__ == "__main__":
    generar("Jay","es","Quorelia-Tarjeta-Jay-ES.pdf")
    generar("Jay","en","Quorelia-Tarjeta-Jay-EN.pdf")
    generar("Diego","es","Quorelia-Tarjeta-Diego-ES.pdf")
    generar("Diego","en","Quorelia-Tarjeta-Diego-EN.pdf")
