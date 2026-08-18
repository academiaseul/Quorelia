# Brief — Reunión Subsecretaría de Energía · viernes 21 de agosto de 2026

Documento interno de preparación. No entregar.

---

## 1. Tres correcciones antes de entrar a la sala

**(a) El cargo.** La SEC es encabezada por un **Superintendente**, no por un Subsecretario. El *Subsecretario de Energía* es **Hugo Briones**, del Ministerio de Energía (gobierno Kast, asumió en febrero de 2026), bajo la ministra Ximena Rincón. Confirma con quién es la reunión: son instituciones distintas con atribuciones distintas — el Ministerio define política, la SEC fiscaliza. El pitch cambia según cuál sea.

**(b) Briones es ingeniero, no político.** Ingeniero civil electricista de la Universidad de Chile, MBA, con trayectoria en proyectos de generación y transmisión — térmica, hidráulica y eólica. **Entiende P50, factor de planta, curva de potencia y disponibilidad técnica.** No simplifiques. La distinción recurso-vs-activo y el tratamiento del silencio de canal le van a resultar inmediatamente reconocibles como problemas reales. Ese es tu terreno más fuerte.

**(c) El número de centrales — corrección: tenías razón.** Te advertí antes que la cifra pública era de ~1.100 centrales. **Retiro esa observación.** Analizado el registro completo de Infotécnica que descargaste (extracción del 16-08-2026), el parque es:

| | Unidades generadoras | Centrales únicas | Propietarios |
|---|---:|---:|---:|
| Coordinadas | 1.641 | 1.198 | 905 |
| PMGD | 977 | 831 | 709 |
| **Total** | **2.618** | **2.029** | **1.614** |

Tu cifra de 1.800 estaba mucho más cerca que la mía. **Usa 2.029 centrales** y respáldala con la fuente: es el dato oficial del Coordinador y es verificable en el momento. La diferencia con las cifras de prensa es que aquéllas suelen contar solo centrales coordinadas en operación, sin PMGD.

---

## 2. El dato que debe estructurar toda la reunión

De la Cuenta Pública 2026 de la SEC (gestión 2025):

> **10.769 fiscalizaciones** en el sector eléctrico y de combustibles.
> En generación distribuida: **2.341 fiscalizaciones — 2.100 documentales y 241 en terreno.**

**El 90% del esfuerzo de fiscalización en ese segmento es leer documentos.**

Ese es el número con el que abres. No hables de Quorelia hasta haberlo dicho. Es su propia cifra, es verificable, y define el problema en los términos de ellos, no en los tuyos.

---

## 2-bis. Los cuatro hallazgos sobre datos oficiales — tu activo más fuerte

Analicé el registro completo de Infotécnica. Estos cuatro hallazgos son **reales, reproducibles y nadie más los ha puesto sobre la mesa.** Están desarrollados en `Informe-Diagnostico-Parque-Nacional.html`.

**(1) El parque está extremadamente fragmentado.** De 1.614 titulares, el **91,7% opera una sola central**. Entre los PMGD, el 93,4%. Solo 37 titulares en todo el país operan 4 o más centrales.

> *La consecuencia, y es el argumento más potente que tienes:* exigirle un formato de reporte más estricto a un parque monoactivo no produce mejor información — produce incumplimiento, o planillas llenadas a mano con la misma calidad que se quería corregir. **La única vía escalable es que el informe se genere solo, desde los datos que la central ya produce.** Eso es exactamente lo que vendes.

**(2) La tecnología dominante es la peor documentada.** La fotovoltaica concentra **1.375 de las 2.029 centrales (67,8%)**, y su ficha técnica en el segmento coordinado tiene una completitud de **23,1%** — la más baja de todas las fichas del registro.

**(3) El registro de almacenamiento está vacío: 2 unidades de 977.** El resto declara «no aplica» en los 31 campos de la ficha. Y el Decreto N°1/2026 acaba de incorporar almacenamiento al régimen con exigencias de monitoreo. **El registro va a recibir cientos de instalaciones de una tecnología de la que hoy tiene dos ejemplares, y no existe formato consolidado de reporte para ella.**

**(4) Con solo 2 fichas de almacenamiento ya hay 3 errores estructurales.** Vocabulario no normalizado («LFP LiFePO4» vs. «Ion-Litio»), un rango de SOC declarado como **[0%–100%]** que es físicamente implausible — ningún BMS opera así —, y la palabra «En Pruebas» escrita dentro de un campo de fecha. Ninguno es detectable a ojo a escala de cartera; los tres se detectan automáticamente al momento de la carga.

> **El cierre natural para Briones:** *"El momento de definir el formato de reporte de almacenamiento es antes de que ingresen las trescientas instalaciones que el nuevo marco habilita, no después. Corregir un registro de dos unidades es trivial. Corregir uno de trescientas, con vocabularios ya consolidados, no lo es."*

**Salvedad que debes decir tú antes de que la digan ellos:** parte de los campos vacíos puede ser legítimamente no aplicable (características de seguimiento en una planta de estructura fija, por ejemplo). Preséntalo como medida de *información estructurada disponible para análisis automatizado*, no como incumplimiento de los titulares. Que el registro no permita distinguir «no aplica» de «no informado» es, en sí mismo, parte del hallazgo.

---

## 3. El posicionamiento correcto (y el error a evitar)

La SEC **ya declaró públicamente** que está incorporando inteligencia artificial y que avanza desde un modelo reactivo hacia uno **proactivo, basado en análisis de datos y gestión de riesgo**.

> **No llegues a proponerles IA.** Ya la tienen en su discurso oficial. Si entras vendiendo "IA para fiscalización", te ubicas como un proveedor más ofreciendo lo que ellos ya anunciaron.

El posicionamiento que funciona es el inverso:

> *"Ustedes ya declararon que van hacia fiscalización proactiva basada en riesgo. Ese modelo necesita un insumo que hoy no existe: informes con formato idéntico entre centrales y con trazabilidad reproducible hasta la medición. Sin eso, el análisis de riesgo se ejecuta sobre datos que no son comparables entre sí."*

Tú no vendes la capacidad analítica. Vendes **el insumo estandarizado que esa capacidad requiere para funcionar**.

---

## 4. Por qué empezar por almacenamiento (BESS)

El **Decreto N°1 de 2026** modificó el D.S. 88 e incorporó los sistemas de almacenamiento al reglamento de medios de generación de pequeña escala, que antes solo contemplaba generación. Entre las modificaciones hay **exigencias de sistemas de monitoreo y control** para la integración con el centro de control de la distribuidora, y reglas de operación en tiempo real.

Es decir: hay una obligación de monitoreo **nueva, de este año, sobre una tecnología que la autoridad aún no tiene experiencia fiscalizando en volumen**. Ese es el punto de entrada más natural que existe, y explica por qué el informe BESS es el primero de la carpeta.

Verifica el estado de tramitación del decreto antes de la reunión — hubo reingreso a Contraloría y conviene no afirmar vigencia si aún está en trámite.

---

## 5. Los cuatro documentos y para qué sirve cada uno

| Documento | Rol en la reunión |
|---|---|
| **Informe-Diagnostico-Parque-Nacional** | **El que abre la reunión.** Datos oficiales reales, no muestra. Es tu credencial técnica: llegas con un análisis del registro de ellos que ellos no tienen hecho. |
| **Informe-Muestra-Cartera-SEC** | La vista de la autoridad: priorización por riesgo y propuesta de piloto. |
| **Informe-Muestra-BESS** | La profundidad técnica. 8 páginas. Demuestra que el nivel de detalle existe de verdad. |
| **Informe-Muestra-Solar-PV** | La descomposición recurso-vs-activo. El argumento más fuerte para un ingeniero. |
| **Informe-Muestra-Eolico** | La estandarización. Otra tecnología, indicadores distintos, mismas reglas de validez. |

Todos en español, con marca de "muestra ilustrativa" en cada página y entidades declaradas como ficticias.

---

## 6. Los tres argumentos técnicos que van a convencer a un ingeniero

**(a) El silencio no es indisponibilidad.** Un canal que no responde no es un canal que reporta cero. Tratarlo como cero produce cifras falsamente catastróficas; tratarlo como disponible produce cifras indefendibles. La única respuesta correcta es excluirlo del denominador y declararlo. Briones va a reconocer esto de inmediato.

**(b) Recurso y activo son cosas distintas.** El informe PV descompone una desviación de −4,9% frente a P50 en sus componentes: −2,4% recurso, −0,9% ensuciamiento, −0,4% indisponibilidad, −0,3% vertimiento sistémico, −0,9% no asignado. **Sin esa separación, una central mal mantenida en un buen año meteorológico es indistinguible de una central bien operada.** Ese es, en una frase, por qué la generación total no sirve para fiscalizar.

**(c) La misma definición de validez entre tecnologías.** Un PR no significa nada en eólica y un RTE no existe en solar. Pero el umbral de cobertura, el tratamiento del dato faltante y la regla de publicación pueden y deben ser idénticos. Eso es lo que hace comparable una cartera heterogénea sin normalizar formatos a mano.

---

## 7. Lo que NO debes ofrecer

- **No ofrezcas certificar con efecto regulatorio.** No tienes esa atribución y ofrecerla te descalifica.
- **No proyectes ahorro de horas.** Es tentador decir "reducimos 2.100 revisiones documentales a X". No lo midas tú: **propón que lo mida el piloto, con el equipo revisor de ellos, cronómetro en mano.** Un proveedor que se niega a inventar su propio número de ahorro gana más credibilidad que uno que presenta una proyección optimista.
- **No pidas acceso a sistemas de la autoridad.** El piloto corre sobre datos de los titulares, voluntariamente. Cero fricción institucional.
- **No hables de precio en esta reunión** salvo que te lo pregunten directamente.

---

## 8. El cierre que debes buscar

No busques una decisión. Busca **un piloto acotado**: 10 a 15 centrales voluntarias, tres meses, informe estandarizado en paralelo al reporte habitual, sin reemplazar ningún proceso vigente. Cero riesgo institucional para ellos, y al final hay un contraste medible entre ambas series.

Si sales de la sala con interés en un piloto y un nombre de contacto técnico para coordinarlo, la reunión fue un éxito.

---

## 9. Pendientes antes del viernes

- [ ] Confirmar con quién exactamente es la reunión (Ministerio o SEC) y ajustar el discurso
- [ ] Verificar el estado de tramitación del Decreto N°1 de 2026 en Contraloría
- [x] ~~Reconciliar el número de centrales~~ — resuelto: **2.029 centrales**, fuente Infotécnica, verificable
- [ ] Llevar los dos Excel de Infotécnica en el notebook por si piden ver el origen del análisis
- [ ] Imprimir los cuatro informes a color, o llevarlos en PDF en tablet
- [ ] Definir quién de las centrales que ya conoces podría ofrecerse como voluntaria al piloto

---

## Fuentes

- [SEC realiza Cuenta Pública Participativa 2026 — Revista Electricidad](https://www.revistaei.cl/sec-realiza-cuenta-publica-participativa-2026-destacando-ejes-de-su-gestion/)
- [SEC presentó Cuenta Pública 2026 destacando uso de IA y 10.700 fiscalizaciones de terreno — Reporte Minero](https://www.reporteminero.cl/noticia/noticias/2026/07/sec-cuenta-publica-2026-rancagua-inteligencia-artificial-fiscalizaciones)
- [SEC despliega inteligencia artificial para anticipar riesgos y reforzar fiscalización — Reporte Minero](https://www.reporteminero.cl/noticia/noticias/2026/04/sec-inteligencia-artificial-fiscalizacion-energia-chile)
- [PMGD y almacenamiento: alcances del reingreso del DS 1/2026 — Cuatrecasas](https://www.cuatrecasas.com/es/latam/art/energia-infraestructura-pmgd-almacenamiento-alcances-reingreso-ds-1-2026)
- [Modificaciones al Reglamento D.S. 88 — Ministerio de Energía](https://energia.gob.cl/consultas-publicas/modificaciones-al-reglamento-ds-88-para-medios-de-generacion-de-pequena-escala)
- [Hugo Briones, Subsecretario de Energía — Ministerio de Energía](https://energia.gob.cl/autoridades/hugo-briones)
- [Ximena Rincón y Hugo Briones asumen como ministra y subsecretario de Energía](https://energia.gob.cl/noticias/nacional/ximena-rincon-y-hugo-briones-asumen-como-ministra-y-subsecretario-de-energia)
- [Reporte Anual de Desempeño del Sistema Eléctrico Nacional — Coordinador Eléctrico Nacional](https://www.coordinador.cl/wp-content/uploads/2025/04/CEN-Reporte-Art-72-15-ano-2024.pdf)
- [Infotécnica — Unidades Generadoras PMGD, Coordinador Eléctrico Nacional](https://infotecnica.coordinador.cl/instalaciones/unidades-generadoras-pmgd) *(fuente de los datos analizados, extracción 16-08-2026)*
