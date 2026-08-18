# -*- coding: utf-8 -*-
"""Prepara una variante del teaser apta para WeasyPrint y genera el PDF."""
import re, sys, base64, pathlib
from weasyprint import HTML, CSS

def b64(p):
    return "data:image/jpeg;base64,"+base64.b64encode(pathlib.Path(p).read_bytes()).decode()

def preparar(src):
    s=pathlib.Path(src).read_text(encoding='utf-8')
    # 1) <div class="bg"><img src="X"></div>  ->  background-image en la propia slide
    imgs=re.findall(r'<div class="bg"><img src="([^"]+)"[^>]*></div>',s)
    for i,img in enumerate(imgs):
        s=s.replace(f'<div class="bg"><img src="{img}" alt=""></div>',
                    f'<div class="bg" style="background-image:url(\'{b64(img)}\');background-size:cover;background-position:center;"></div>',1)
    # 2) object-fit no existe en weasyprint; .bg ya no lleva <img>
    s=s.replace(".bg img{width:100%;height:100%;object-fit:cover;display:block;}","")
    # 3) sombras de pantalla fuera; una slide por página
    s=s.replace("box-shadow:0 3px 34px rgba(0,0,0,0.55);","")
    s=s.replace("margin:0 auto 20px;","margin:0;")
    s=s.replace("background:#2a3138;","background:#05090f;")
    # 5) el pie va posicionado en absoluto: reservar espacio para que no colisione
    s=s.replace("padding:0.62in 0.78in;","padding:0.55in 0.78in 0.92in;")
    s=s.replace("bottom:0.42in;left:0.78in;right:0.78in;","bottom:0.26in;left:0.78in;right:0.78in;")
    # 4) forzar tamaño de página exacto
    s=s.replace("@page{size:13.333in 7.5in;margin:0;}","@page{size:13.333in 7.5in;margin:0;}")
    # 6) la barra de tags es el último bloque: comprimirla para que libere el pie
    s=s.replace(".tagbar{display:flex;gap:0;margin-top:16px;border-top:1px solid var(--line);padding-top:13px;}",
                ".tagbar{display:flex;gap:0;margin-top:9px;border-top:1px solid var(--line);padding-top:9px;}")
    return s

def render(src,out):
    html=preparar(src)
    tmp=pathlib.Path("/tmp/_pdf_src.html"); tmp.write_text(html,encoding='utf-8')
    HTML(filename=str(tmp), base_url=str(pathlib.Path(src).parent)).write_pdf(out)
    print(f"{out}  <-  {src}")

if __name__=="__main__":
    render(sys.argv[1], sys.argv[2])
