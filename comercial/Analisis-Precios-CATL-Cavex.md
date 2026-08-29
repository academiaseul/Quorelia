# Análisis de precios — cuenta CATL vía Cavex

**Para:** Jae Hee Kim, Quorelia SpA
**Fecha:** 28 de agosto de 2026
**Plazo de respuesta:** lunes 31 de agosto
**Tipo de cambio usado:** 915 CLP/USD (rango observado en agosto 2026: 909–928)

---

## Resumen en cinco líneas

1. Cobras **300.000 CLP/mes por 1 GW**. Eso es **USD 3.934 al año**: el **20%** del piso de tu propia tabla de referencia y el **4%** del piso de Siemens, Hitachi o GE.
2. Los dos números que estabas pensando (500.000 y 1.000.000 CLP/sitio/mes) **también quedan bajo tu propio piso**: son el 33% y el 66% de los USD 20.000/sitio/año que tú mismo fijaste como objetivo.
3. Peor: a 12 sitios, **ambos pierden plata**. El techo de tu rango deja un resultado de **−2.040.000 CLP al mes**.
4. El correo no pide ampliar tu servicio. Pide **montar un centro de operaciones 24/7 con dotación**, sobre la plataforma de CATL. Eso no es software, es dotación de personal: costo laboral que no escala y margen de BPO.
5. La salida buena existe y es limpia: **quédate con los puntos 1, 2 y 5, y deja el 3 y el 4 a Cavex.** Cuestan casi lo mismo que ya haces, y son exactamente donde eres irreemplazable.

---

## 01 · Dónde está el precio actual

| Métrica | Valor |
|---|---|
| Tarifa mensual | 300.000 CLP = **USD 328** |
| Ingreso anual del contrato | 3.600.000 CLP = **USD 3.934** |
| Precio por MW | 300 CLP/MW/mes = **USD 3,93/MW/año** |
| Como fracción de un sueldo mínimo chileno | **0,54 ×** |

Esa última fila merece un segundo. El ingreso mensual completo de esta cuenta es **poco más de la mitad de un solo ingreso mínimo** (553.553 CLP desde mayo de 2026). No alcanza para pagar a una persona a jornada parcial.

Contra la tabla de referencia que ya tenías armada:

| Proveedor | Piso indicativo | Quorelia hoy | El piso es… |
|---|---|---|---|
| **Quorelia · objetivo propio** | USD 20.000/año | 19,7% | **5,1× más caro** |
| AVEVA PI System | USD 25.000/año | 15,7% | 6,4× más caro |
| AlsoEnergy | USD 30.000/año | 13,1% | 7,6× más caro |
| Power Factors / Unity | USD 50.000/año | 7,9% | 12,7× más caro |
| ABB | USD 75.000/año | 5,2% | 19,1× más caro |
| Siemens · Hitachi · GE Vernova | USD 100.000/año | 3,9% | **25,4× más caro** |

Esto no es "muy por debajo del precio de mercado", que es como lo vienes contando. Es un precio que **no comunica bajo costo, comunica bajo valor**. Y ya está fijado como ancla para la negociación de los 6 GW.

---

## 02 · Lo que estabas pensando cobrar

| Tarifa propuesta | USD/sitio/año | % de tu propio piso de USD 20.000 |
|---|---|---|
| 500.000 CLP/sitio/mes | USD 6.557 | **33%** |
| 1.000.000 CLP/sitio/mes | USD 13.115 | **66%** |

Estás a punto de subir el precio **y seguir por debajo del piso que tú mismo definiste.** Es el peor de los dos mundos: gastas el capital político de un alza sin llegar a un número sostenible.

---

## 03 · El correo no pide más servicio. Pide otro negocio.

Los cinco puntos de CATL no son homogéneos. Tres de ellos son software; dos son trabajo humano. Mezclarlos en una sola tarifa por sitio es el error que hay que evitar.

| Punto | Naturaleza | Quién | Por qué |
|---|---|---|---|
| **1 · Monitoreo 24/7 de BMS, PCS, EMS** | Software | **Quorelia** | Es literalmente el producto. Costo marginal casi nulo. |
| **2 · Alarmas: detectar, clasificar, notificar, registrar** | Software | **Quorelia** | La detección trazable es tu diferenciador. |
| **2b · "Preliminary judgments" sobre la alarma** | Decisión operacional | **Cavex** | Ver sección 05. |
| **3 · Órdenes de trabajo 24/7** | Coordinación de terreno | **Cavex** | Tú generas el hallazgo; despachar cuadrillas es de ellos. |
| **4 · Atención de llamadas 24/7** | Call center | **Cavex** | Es un call center multilingüe. Margen bajo, cero diferenciación. |
| **5 · Registro e informe diario** | Software | **Quorelia** | Ya lo entregas. Es el corazón del servicio. |

### Por qué importa tanto: la aritmética de turnos

Desde el 26 de abril de 2026 la jornada legal en Chile es de **42 horas semanales** (Ley 21.561). Cubrir un solo puesto 24/7/365 exige:

```
168 horas por semana ÷ 42 horas de jornada        = 4,00 FTE
+ 15% por vacaciones, licencias y capacitación    = 4,60 FTE por puesto
```

Con dos puestos concurrentes (no puedes atender alarmas, llamadas y órdenes de trabajo con una sola persona) más tres seniors de turno, son **12 personas en nómina**.

| | **Escenario A**<br>capa de datos (1, 2, 5) | **Escenario B**<br>centro dotado (los 5) |
|---|---|---|
| Costo fijo mensual | **11.640.000 CLP** | **33.120.000 CLP** |
| Costo fijo anual | USD 152.656 | **USD 434.361** |
| Personas dedicadas | 5,5 | 12 |
| Sitios para equilibrio a 1.000.000 CLP/sitio | **15** | **48** |
| Sitios para equilibrio a 500.000 CLP/sitio | 39 | **166** |

**CATL tiene ~6 GW en LatAm, no 166 sitios.** El escenario B no llega a equilibrio con esta cuenta a los precios que estabas considerando. Ni cerca.

---

## 04 · Tarifa recomendada — tres bloques

La clave es **separar lo que escala de lo que no escala**. Una sola tarifa por sitio te mata en carteras chicas y te deja plata en la mesa en carteras grandes.

### Bloque 1 · Plataforma, verificación y reportería — recurrente por sitio

| Banda de potencia | CLP/sitio/mes | USD/sitio/año |
|---|---|---|
| Hasta 200 MW | 950.000 | USD 12.459 |
| 200 – 500 MW | 1.450.000 | USD 19.016 |
| Más de 500 MW | 1.950.000 | USD 25.574 |

### Bloque 2 · Servicio de monitoreo y guardia 24/7 — cargo fijo de cuenta

| Concepto | CLP/mes |
|---|---|
| Cargo fijo (hasta 20 sitios) | **14.500.000** |
| Incremento por sitio a partir del 21º | 350.000 |

Este bloque es el que paga la guardia. Va aparte precisamente porque **el costo del 24/7 no depende de cuántos sitios haya**, y si lo escondes dentro de la tarifa por sitio, una cartera de 6 sitios te deja en pérdida.

### Bloque 3 · Implementación — pago único por sitio

| Tipo de integración | CLP | USD |
|---|---|---|
| Estándar — SCADA/EMS conocido | 6.500.000 | USD 7.104 |
| Compleja — BMS propietario o multi-vendor | 13.000.000 | USD 14.208 |

### Cómo queda según el tamaño de la cartera

| Sitios | Recurrente CLP/mes | USD/año | USD/sitio/año | Margen bruto |
|---|---|---|---|---|
| 1 | 16.450.000 | 215.738 | 215.738 | 28% |
| 6 | 23.200.000 | 304.262 | 50.710 | 45% |
| **12** | **31.900.000** | **418.361** | **34.863** | **56%** |
| 20 | 43.500.000 | 570.492 | 28.525 | 64% |
| 30 | 46.500.000 | 609.836 | 20.328 | 62% |
| 40 | 59.500.000 | 780.328 | 19.508 | 67% |

A 12 sitios el precio por sitio queda en **USD 34.863/año** — dentro de tu propia banda objetivo de USD 20.000–100.000 y todavía por debajo de Power Factors. Sigues siendo la opción barata, pero a un precio que sostiene la empresa.

### El contraste que importa

Cartera de 12 sitios, costo mensual de servirlos: **14.040.000 CLP**.

| Opción | Ingreso/mes | Resultado/mes | |
|---|---|---|---|
| Tu rango bajo — 500.000 CLP/sitio | 6.000.000 | **−8.040.000** | pérdida |
| Tu rango alto — 1.000.000 CLP/sitio | 12.000.000 | **−2.040.000** | pérdida |
| **Tarifa recomendada** | **31.900.000** | **+17.860.000** | margen 56% |

---

## 05 · Cómo presentar el cambio de precio

**No lo presentes como un alza.** Si dices "subimos de 300.000 a X", la conversación es sobre por qué te encareciste y pierdes.

Preséntalo como **un servicio distinto con su propia tarifa**:

> El contrato vigente cubre reportería y verificación en horario hábil sobre una instalación. Lo que se describe en el correo del 2X de agosto — monitoreo continuo, gestión de alarmas y reportería diaria sobre una cartera regional — es un servicio de naturaleza distinta, con disponibilidad 24/7 y dotación asociada. A continuación su estructura de precios.

El contrato de 1 GW sigue como está hasta que la planta entre al alcance nuevo. Así el número viejo no funciona como ancla del número nuevo.

---

## 06 · Los riesgos que hay que atender antes de cotizar

### 6.1 · No tienes relación directa con CATL

El contrato lo tiene Cavex. **Los 6 GW son pipeline de Cavex, no tuyo.** Si entregas el diseño operativo completo de un centro 24/7, le estás entregando a Cavex el plano de algo que puede construir en casa o licitar a un tercero una vez que el modelo esté probado.

Pide, antes de entregar la cotización detallada:

- **Cláusula de no elusión y no captación** (non-circumvention / non-solicitation) por 24–36 meses.
- **Derecho de primera opción** sobre las plantas adicionales de la misma cartera.
- **Mención nominada** de Quorelia como proveedor de la capa de datos en el contrato Cavex–CATL, o al menos reconocimiento escrito.

### 6.2 · No sabes cuánto factura Cavex a CATL

Cotiza **sobre tu costo más margen**, nunca sobre lo que supones que CATL pagará. Si Cavex marca sobre tu número, ese margen es de ellos y es legítimo — pero no es razón para que tú operes bajo costo.

Vale la pena preguntar directamente cómo se estructura el margen de Cavex en esta línea. La respuesta, incluso si es evasiva, te dice mucho.

### 6.3 · Riesgo cambiario

Si Cavex factura a CATL en dólares y te paga a ti en pesos a tipo fijo, **el riesgo de tipo de cambio es tuyo** en un contrato plurianual. En agosto de 2026 el dólar se movió entre 909 y 928 en una sola semana.

Pide indexación: tarifa expresada en UF o en USD con conversión al observado del último día del mes.

### 6.4 · El punto 2 contradice tus propios Términos y Condiciones

Tu sección 03 dice, textualmente, que el servicio es *"estrictamente pasiva y de solo lectura"* y que Quorelia *"no opera, no controla, no despacha ni interviene"*.

El correo pide *"make preliminary judgments"* sobre alarmas de **BMS, PCS y EMS de sistemas de baterías de litio**. Si aceptas eso:

- Entras en la cadena causal de cualquier evento térmico. En BESS eso significa contenedores destruidos y, en el peor caso, personas.
- Tienes que reescribir tus Términos, que son uno de tus activos comerciales.
- Necesitas seguro de responsabilidad civil profesional real, no nominal.

**La redacción que te protege y aun así sirve a CATL:** Quorelia *detecta, clasifica según criterio preacordado, notifica dentro de un SLA y deja registro trazable*. La decisión operacional y su ejecución son de Cavex o del operador.

### 6.5 · Flow-down de responsabilidad

Lo que CATL le imponga a Cavex, Cavex intentará traspasártelo. Para una SpA chica eso es existencial. Innegociable:

- **Tope de responsabilidad = 12 meses de honorarios efectivamente pagados.**
- **Exclusión expresa de daños indirectos, lucro cesante y pérdida de producción.**
- Sin responsabilidad por decisiones operacionales tomadas por terceros a partir de la información entregada.

### 6.6 · La barrera idiomática y horaria

El punto 4 pide atender llamadas de clientes y personal en sitio en toda Sudamérica. Eso son al menos español y portugués, probablemente inglés con CATL, y mandarín con la casa matriz. Tres husos horarios. **Es un negocio de call center y no deberías estar en él.**

---

## 07 · Qué hacer antes del lunes

1. **No mandes un número suelto.** Manda una estructura con supuestos explícitos y las preguntas de alcance abiertas. Es la respuesta profesional y te deja espacio para negociar cuando lleguen los datos.
2. **Divide el alcance en el propio correo.** Que quede por escrito que los puntos 3 y 4 son de Cavex, antes de que nadie asuma otra cosa.
3. **Pide los datos que faltan:** listado de sitios con potencia y país, SLA de respuesta exigido, qué plataforma se usa, y cómo se reparte la responsabilidad.
4. **Levanta el tema de la exclusividad ahora**, no después de que el modelo esté probado.

---

## Fuentes

- Tipo de cambio USD/CLP agosto 2026: [Wise — historial CLP/USD](https://wise.com/us/currency-converter/usd-to-clp-rate/history)
- Jornada de 42 horas desde el 26 de abril de 2026: [Ley 21.561 — alerta legal NSS](https://www.nss.cl/alertas-legales/jornada-42-horas-abril-2026) · [Ministerio del Trabajo — 40 horas](https://www.mintrab.gob.cl/40horas/)
- Ingreso mínimo mensual 553.553 CLP desde mayo 2026: [Dirección del Trabajo](https://www.dt.gob.cl/portal/1628/w3-article-60141.html) · [Carey Abogados](https://www.carey.cl/reajuste-del-ingreso-minimo-mensual-a-contar-de-enero-2026)
- Referencias salariales sector eléctrico Chile 2026: [Computrabajo — ingeniero eléctrico](https://cl.computrabajo.com/salarios/ingeniero-electrico) · [ChileTrabajos — técnico eléctrico](https://www.chiletrabajos.cl/sueldos/tecnico/electrico)
- Tabla de precios de competidores: benchmark interno de Quorelia (documento aportado por el usuario)

*Los costos de dotación e infraestructura son estimaciones internas basadas en las referencias salariales citadas más cargas del empleador y turnos rotativos. Todos son editables en el modelo Excel adjunto.*
