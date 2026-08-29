# -*- coding: utf-8 -*-
"""Modelo de precios Quorelia — cuenta CATL vía Cavex. Todo se calcula, nada se afirma."""
FX      = 915          # CLP/USD, rango 909-928 agosto 2026
IMM     = 553_553      # ingreso minimo mensual Chile, desde mayo 2026
JORNADA = 42           # horas/semana desde 26 abril 2026

def usd(clp): return clp / FX
def m(x): return f"{x:,.0f}".replace(",", ".")

print("="*66); print("1 · DONDE ESTA EL PRECIO ACTUAL"); print("="*66)
actual_mes = 300_000; mw = 1000
print(f"Precio actual           {m(actual_mes)} CLP/mes  = USD {usd(actual_mes):,.0f}/mes")
print(f"Anual                   {m(actual_mes*12)} CLP    = USD {usd(actual_mes*12):,.0f}/año")
print(f"Por MW                  {m(actual_mes/mw)} CLP/MW/mes = USD {usd(actual_mes*12/mw):,.2f}/MW/año")
print(f"Como % del IMM          {actual_mes/IMM*100:.0f}% de UN sueldo minimo")
piso_propio = 20_000
print(f"\nSu propio objetivo      USD {piso_propio:,}-100.000 /sitio/año")
print(f"Precio actual vs piso   {usd(actual_mes*12)/piso_propio*100:.0f}% del piso propio  ->  {piso_propio/usd(actual_mes*12):.1f}x por debajo")
for nombre, piso in [("AVEVA PI",25_000),("AlsoEnergy",30_000),("Power Factors",50_000),("Siemens/Hitachi/GE",100_000)]:
    print(f"  vs {nombre:<20} piso USD {piso:>7,}/año  ->  Quorelia = {usd(actual_mes*12)/piso*100:5.1f}%")

print("\n" + "="*66); print("2 · LO QUE PROPONES COBRAR"); print("="*66)
for p in (500_000, 1_000_000):
    print(f"{m(p)} CLP/sitio/mes = USD {usd(p*12):,.0f}/sitio/año  ->  {usd(p*12)/piso_propio*100:.0f}% de tu propio piso de USD 20.000")

print("\n" + "="*66); print("3 · DOTACION 24/7 (por que el punto 3 y 4 son otro negocio)"); print("="*66)
cob = 168/JORNADA
fte = cob*1.15
print(f"Cobertura pura 24/7     168 h/sem / {JORNADA} h = {cob:.2f} FTE por puesto")
print(f"+15% vacaciones, licencias, capacitacion  ->  {fte:.2f} FTE por puesto")

print("\n" + "="*66); print("4 · ESCENARIO A — SOLO CAPA DE DATOS (puntos 1, 2*, 5)"); print("="*66)
A = {"Guardia tecnica 24/7 (4 ing. rotativos: bono disponibilidad + horas efectivas)":3_400_000,
     "Analista de operaciones (1 FTE cargado)":2_200_000,
     "Jefatura tecnica / QA (0,5 FTE)":1_500_000,
     "Infraestructura (hosting, ingesta, almacenamiento, redundancia)":1_200_000,
     "Licencias y herramientas (alerting, ticketing, telefonia)":600_000,
     "Seguro de responsabilidad civil profesional (E&O)":800_000}
sub_a = sum(A.values()); oh_a = round(sub_a*0.20)
for k,v in A.items(): print(f"  {k:<62} {m(v):>12}")
print(f"  {'Overhead administrativo y comercial (20%)':<62} {m(oh_a):>12}")
costo_a = sub_a + oh_a; marg_a = 200_000
print(f"  {'COSTO FIJO MENSUAL':<62} {m(costo_a):>12}  = USD {usd(costo_a):,.0f}")
print(f"  {'Costo marginal por sitio adicional':<62} {m(marg_a):>12}")

print("\n" + "="*66); print("5 · ESCENARIO B — CENTRO 24/7 CON DOTACION (los 5 puntos)"); print("="*66)
op_n = round(2*fte); op_c = 1_600_000; sr_n = 3; sr_c = 2_600_000
B = {f"{op_n} operadores de turno (2 puestos concurrentes x {fte:.1f} FTE), cargados":op_n*op_c,
     f"{sr_n} ingenieros senior / jefes de turno":sr_n*sr_c,
     "Telefonia y atencion multilingue (ES/PT/EN/ZH)":1_500_000,
     "Infraestructura y licencias":2_100_000,
     "Seguro RC ampliado (juicio operacional sobre alarmas BMS)":1_800_000}
sub_b = sum(B.values()); oh_b = round(sub_b*0.20)
for k,v in B.items(): print(f"  {k:<62} {m(v):>12}")
print(f"  {'Overhead (20%)':<62} {m(oh_b):>12}")
costo_b = sub_b + oh_b
print(f"  {'COSTO FIJO MENSUAL':<62} {m(costo_b):>12}  = USD {usd(costo_b):,.0f}")
print(f"  {'Anual':<62} {m(costo_b*12):>12}  = USD {usd(costo_b*12):,.0f}")

print("\n" + "="*66); print("6 · PUNTO DE EQUILIBRIO A MARGEN CERO"); print("="*66)
import math
for etq, costo, mc in [("A (capa de datos)",costo_a,marg_a), ("B (centro dotado)",costo_b,300_000)]:
    for p in (500_000, 1_000_000, 2_000_000):
        n = math.ceil(costo/(p-mc))
        print(f"  Escenario {etq:<20} a {m(p):>9} CLP/sitio/mes  ->  {n:>3} sitios solo para cubrir costo")
    print()
