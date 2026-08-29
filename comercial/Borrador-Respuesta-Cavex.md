# Borrador de respuesta — para enviar a Cavex antes del 31 de agosto

Dos versiones. La primera es la que mandas tú a Cavex, en español. La segunda es el bloque en inglés que Cavex puede reenviar a CATL sin reescribirlo.

**Antes de enviar, revisa:** los precios son los recomendados en el análisis; ajústalos en el Excel si cambias supuestos. El número de sitios (12) es un supuesto mío — cámbialo o déjalo como está, ya que va explícitamente marcado como pendiente de confirmación.

---

## Versión 1 · Correo a Cavex (español)

**Asunto:** Estimación preliminar — centro de monitoreo Sudamérica CATL

Estimado [nombre],

Gracias por compartir el requerimiento de CATL. Lo revisamos en detalle y queremos responder antes del 31 con algo útil, así que va una estructura de precios con los supuestos explícitos, más las cuatro definiciones que necesitamos de su parte para cerrar un número firme.

**Lo primero, sobre el alcance.** Los cinco puntos del requerimiento no son de la misma naturaleza y conviene separarlos desde ahora:

Los puntos **1, 2 y 5** — monitoreo continuo de BMS/PCS/EMS, detección y registro de alarmas, y reportería diaria de operación — son exactamente lo que Quorelia hace. Los tomamos completos.

Los puntos **3 y 4** — distribución y gestión de órdenes de trabajo, y atención telefónica a clientes y personal en terreno — son coordinación de terreno y atención de llamadas. Requieren dotación presencial, conocimiento del contrato de O&M de cada sitio y capacidad de despacho de cuadrillas. Eso está del lado de Cavex, no del nuestro. Nosotros generamos el hallazgo con toda su trazabilidad y lo entregamos al sistema de órdenes de trabajo de ustedes; la gestión posterior la conducen ustedes.

Hay un matiz en el punto 2 que queremos dejar claro por escrito. El requerimiento habla de *"preliminary judgments"* sobre las alarmas. Quorelia detecta, clasifica según criterio preacordado, notifica dentro del SLA y deja registro auditable de cada evento. **La decisión operacional sobre un sistema de baterías de litio y su ejecución quedan en el operador.** No es una restricción comercial nuestra sino de responsabilidad: quien decide sobre una alarma de BMS debe ser quien tiene el control físico del activo. Nuestros términos de servicio lo establecen así y creemos que también protege a Cavex frente a CATL.

**Estructura de precios preliminar.** Sobre el alcance descrito (puntos 1, 2 y 5, disponibilidad 24/7):

| Bloque | Concepto | Precio (CLP, neto de IVA) |
|---|---|---|
| 1 | Plataforma, verificación y reportería — sitio hasta 200 MW | 950.000 /sitio/mes |
| 1 | Plataforma, verificación y reportería — sitio 200 a 500 MW | 1.450.000 /sitio/mes |
| 1 | Plataforma, verificación y reportería — sitio sobre 500 MW | 1.950.000 /sitio/mes |
| 2 | Servicio de monitoreo y guardia técnica 24/7 (cargo fijo de cuenta, hasta 20 sitios) | 14.500.000 /mes |
| 2 | Incremento por sitio a partir del 21º | 350.000 /sitio/mes |
| 3 | Implementación por sitio — integración estándar | 6.500.000 pago único |
| 3 | Implementación por sitio — integración compleja (BMS propietario o multi-vendor) | 13.000.000 pago único |

El bloque 2 va separado a propósito: el costo de sostener disponibilidad 24/7 es fijo y no depende de cuántos sitios haya en la cartera. Repartirlo dentro de la tarifa por sitio distorsionaría el precio en carteras chicas.

**Ejemplo, para dimensionar.** Una cartera de 12 sitios en el rango de 200 a 500 MW quedaría en 31.900.000 CLP mensuales netos, más la implementación inicial. Es un ejemplo sobre un supuesto nuestro de cómo se reparten los 6 GW — el número real depende del listado.

**El contrato vigente de 1 GW no cambia** con esta propuesta. Cubre un alcance distinto (verificación y reportería en horario hábil) y sigue como está hasta que esa instalación se incorpore al servicio 24/7, momento en el cual pasa a la tarifa del bloque 1 correspondiente a su banda de potencia.

**Lo que necesitamos para cerrar un número firme:**

1. **Listado de sitios** con potencia instalada, país y fecha estimada de incorporación. El precio por sitio depende de la banda de potencia y el cargo fijo depende del número total.
2. **SLA de respuesta exigido por CATL.** No es lo mismo notificar una alarma crítica en 15 minutos que en 2 horas; el dimensionamiento de la guardia cambia por completo.
3. **Arquitectura de datos.** El requerimiento menciona *"our designated monitoring platform/tool"*. Necesitamos saber si la operación corre sobre la plataforma de Quorelia con entrega de datos a CATL, o si se espera que operemos dentro de una herramienta de ellos. Son dos servicios distintos con costos distintos, y en el segundo caso perdemos la trazabilidad verificable que es la razón por la que ustedes nos contrataron.
4. **Reparto de responsabilidad** entre CATL, Cavex y Quorelia ante un evento en terreno, y el tope de responsabilidad que se contemplaría en nuestro contrato.

**Un punto comercial, con franqueza.** Si esto avanza hacia los 6 GW de la cartera regional, nos gustaría conversar sobre exclusividad de la capa de datos y una cláusula de no elusión. Estamos dispuestos a invertir en el dimensionamiento y en la ingeniería de integración, y esa inversión se justifica si hay continuidad. Es una conversación que preferimos tener ahora y no después.

Quedamos atentos. Si conviene, podemos hacer una llamada esta semana para cerrar los cuatro puntos.

Saludos cordiales,

Jae Hee Kim
Quorelia SpA
jay@quorelia.org

---

## Versión 2 · Bloque en inglés (para que Cavex reenvíe a CATL)

**Subject:** Preliminary budget estimate — South America monitoring center

Dear [name],

Thank you for the detailed requirement. Please find below a preliminary structure, together with the assumptions it rests on and the four points we need confirmed before we can issue a firm figure.

**On scope.** The five responsibilities described are not of the same nature, and we believe separating them serves the project:

Items **1, 2 and 5** — 24/7 real-time monitoring of BMS, PCS and EMS; alarm detection, classification, notification and record-keeping; and daily operation reporting — fall within our data and verification layer. We take these in full.

Items **3 and 4** — work order distribution and processing, and 24/7 call response with customers and on-site personnel — require field coordination, site-specific O&M contract knowledge and crew dispatch capability. These sit with the local O&M organization. Our platform generates each finding with full traceability and delivers it into the work order system; the subsequent management is conducted locally.

One clarification on item 2. The requirement refers to *"preliminary judgments"* on alarms. Our service detects, classifies against pre-agreed criteria, notifies within an agreed SLA, and leaves an auditable record of every event. **The operational decision on a lithium battery system, and its execution, remain with the operator.** This is not a commercial limitation but a liability one: the party deciding on a BMS alarm should be the party with physical control of the asset. We believe this also protects the project.

**Preliminary pricing structure** (scope: items 1, 2 and 5, with 24/7 availability). All figures in Chilean pesos, net of VAT.

| Block | Item | Price |
|---|---|---|
| 1 | Platform, verification and reporting — site up to 200 MW | 950,000 /site/month |
| 1 | Platform, verification and reporting — site 200 to 500 MW | 1,450,000 /site/month |
| 1 | Platform, verification and reporting — site above 500 MW | 1,950,000 /site/month |
| 2 | 24/7 monitoring service and technical standby (fixed account fee, up to 20 sites) | 14,500,000 /month |
| 2 | Increment per site from the 21st onward | 350,000 /site/month |
| 3 | Per-site implementation — standard integration | 6,500,000 one-time |
| 3 | Per-site implementation — complex integration (proprietary BMS or multi-vendor) | 13,000,000 one-time |

Block 2 is quoted separately by design: the cost of sustaining 24/7 availability is fixed and independent of portfolio size. Folding it into a per-site rate would distort pricing for smaller portfolios.

For scale: a portfolio of 12 sites in the 200–500 MW range would total 31,900,000 CLP per month, plus initial implementation. This assumes a particular split of the 6 GW and will be revised against the actual site list.

**To issue a firm quotation we need:**

1. **Site list** with installed capacity, country and estimated onboarding date.
2. **Required response SLA.** Notifying a critical alarm within 15 minutes versus 2 hours changes the standby model entirely.
3. **Data architecture.** The requirement refers to *"our designated monitoring platform/tool"*. We need to establish whether monitoring runs on the Quorelia platform with data delivery to CATL, or whether operation is expected inside a CATL-provided tool. These are materially different services with different costs, and the second removes the verifiable traceability that our reporting is built on.
4. **Allocation of responsibility** among the parties in the event of a field incident, and the liability cap contemplated in our agreement.

We are available for a call this week to close these points.

Kind regards,

---

## Notas para ti, no para enviar

- **El párrafo sobre la plataforma (punto 3) es el más importante de todo el correo.** Si CATL insiste en que operes dentro de su herramienta, tu diferenciador desaparece y pasas a ser dotación de personal reemplazable. Vale la pena que esa pregunta esté por escrito desde el primer intercambio.
- **El párrafo de exclusividad va solo en la versión a Cavex**, no en la que ellos reenvían. Es una conversación entre ustedes dos.
- **No mandes el modelo Excel a Cavex.** Muestra tus costos y tu margen. El memo y el modelo son para ti.
- Si Cavex presiona por un número único y cerrado antes del lunes, la respuesta honesta es que sin el listado de sitios y el SLA cualquier número firme sería inventado — y que prefieres darles uno que puedas sostener. Eso se lee como seriedad, no como evasiva.
