# -*- coding: utf-8 -*-
FX=915
def usd(c): return c/FX
def m(x): return f"{x:,.0f}".replace(",",".")
COSTO_FIJO_A=11_640_000; MARG=200_000

FIJO   = 14_500_000            # bloque 2: servicio 24/7 de la capa de datos, hasta 20 sitios
BANDA  = {"<=200 MW":950_000, "200-500 MW":1_450_000, ">500 MW":1_950_000}
EXTRA  = 350_000               # sitio 21 en adelante
IMPL   = {"estandar":6_500_000, "compleja":13_000_000}

print("="*74); print("TARIFA RECOMENDADA — TRES BLOQUES"); print("="*74)
print(f"Bloque 1 · Plataforma y verificacion, por sitio y por banda de potencia")
for k,v in BANDA.items(): print(f"    {k:<12} {m(v):>10} CLP/mes   = USD {usd(v*12):>7,.0f}/sitio/año")
print(f"\nBloque 2 · Servicio de monitoreo y guardia 24/7 (cargo fijo de cuenta)")
print(f"    hasta 20 sitios  {m(FIJO):>10} CLP/mes   = USD {usd(FIJO):>7,.0f}/mes")
print(f"    sitio 21+        {m(EXTRA):>10} CLP/sitio/mes")
print(f"\nBloque 3 · Implementacion, pago unico por sitio")
for k,v in IMPL.items(): print(f"    {k:<12} {m(v):>10} CLP        = USD {usd(v):>7,.0f}")

print("\n"+"="*74); print("COMO QUEDA SEGUN EL TAMAÑO DE LA CARTERA"); print("="*74)
print(f"{'Sitios':>7} {'Banda':<12} {'Recurrente/mes':>16} {'USD/año':>12} {'USD/sitio/año':>14} {'Costo':>13} {'Margen':>8}")
print("-"*74)
for n,banda in [(1,">500 MW"),(6,"200-500 MW"),(12,"200-500 MW"),(20,"200-500 MW"),(30,"<=200 MW"),(40,"<=200 MW")]:
    b1=n*BANDA[banda]; b2=FIJO+max(0,n-20)*EXTRA; rec=b1+b2
    costo=COSTO_FIJO_A+n*MARG; margen=(rec-costo)/rec*100
    print(f"{n:>7} {banda:<12} {m(rec):>16} {usd(rec*12):>12,.0f} {usd(rec*12/n):>14,.0f} {m(costo):>13} {margen:>7.0f}%")

print("\n"+"="*74); print("CONTRASTE CON LO QUE IBAS A COTIZAR (12 sitios de 200-500 MW)"); print("="*74)
n=12
rec_prop_lo=n*500_000; rec_prop_hi=n*1_000_000
rec_rec=n*BANDA["200-500 MW"]+FIJO
costo=COSTO_FIJO_A+n*MARG
for etq,r in [("Tu rango bajo  (500k/sitio)",rec_prop_lo),("Tu rango alto  (1M/sitio)",rec_prop_hi),("Tarifa recomendada",rec_rec)]:
    res=r-costo
    print(f"  {etq:<30} {m(r):>12} CLP/mes   resultado {m(res):>13} CLP/mes   {'PERDIDA' if res<0 else 'margen '+str(round(res/r*100))+'%'}")
print(f"\n  Costo mensual de servir 12 sitios (escenario A): {m(costo)} CLP")

print("\n"+"="*74); print("IMPLEMENTACION UNICA, CARTERA DE 12 SITIOS"); print("="*74)
prom=(IMPL['estandar']+IMPL['compleja'])/2
print(f"  12 sitios x {m(prom)} CLP promedio = {m(12*prom)} CLP  = USD {usd(12*prom):,.0f}")
