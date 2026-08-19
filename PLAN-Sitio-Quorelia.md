# quorelia.org — Plan de transformación

Respuesta al brief de rediseño, en mi rol de CEO / CPO / Director Creativo. Empieza con lo que recomiendo **no** hacer, porque ahí está la decisión que más importa.

---

## 0. Contexto que cambia la prioridad

La reunión es el **viernes 21 de agosto** con **Jack Nahmías S., Jefe de la Unidad de Generación y Transmisión de Electricidad de la SEC**.

Esto resuelve una ambigüedad que había quedado abierta: no es el Ministerio de Energía, es la **SEC** — el organismo fiscalizador. Cambia el discurso por completo. El Ministerio define política; la SEC verifica cumplimiento. A Nahmías no le interesa la transición energética en abstracto: le interesa **si una cifra informada por un titular es verificable o no**.

Eso es, literalmente, el producto.

---

## 1. Recomendación central: no rehacer el sitio antes del viernes

El brief pide once páginas nuevas, una experiencia Three.js, un asistente de IA interactivo y una calculadora de ROI. Es la hoja de ruta correcta para los próximos tres meses. **No es lo que conviene hacer en tres días.**

Tres razones concretas:

**Riesgo técnico en la sala.** Una escena Three.js pesada es exactamente lo que falla en una reunión de gobierno: red corporativa restringida, notebook institucional, WebGL deshabilitado por política, proyector a 1024×768. Si el sitio no carga o se traba, el daño a la credibilidad es mayor que el beneficio de haberlo intentado.

**Riesgo de credibilidad.** El brief pide posicionar predicción, vida útil remanente y probabilidad de falla. Frente a un fiscalizador técnico, cada una de esas afirmaciones invita a la pregunta *"muéstremelo"*. Si la respuesta es una demo simulada, se pierde en un minuto todo lo ganado con el análisis de Infotécnica.

**Costo de oportunidad.** El activo más fuerte que existe hoy no es una animación: son los **cuatro hallazgos reales sobre el registro nacional**. Ese material no lo tiene nadie más y responde exactamente a lo que la SEC declaró como prioridad.

### Qué construí ahora

`gobierno.html` — la página `/government` del brief, en español, apuntada a esta reunión. Ya está enlazada en el menú (EN: "Government" / ES: "Gobierno").

### Qué haría después, en este orden

| Prioridad | Página / capacidad | Cuándo | Por qué |
|---|---|---|---|
| **1** | `/gobierno` | **Listo** | Activo de la reunión del viernes |
| **2** | Home — bloque Ver/Entender/Anticipar/Actuar/Optimizar | Semana 1 | Estructura el discurso completo, bajo costo |
| **3** | `/plataforma` + Control Center | Semana 2–3 | Ya existe el dashboard embebido; falta la página que lo enmarca |
| **4** | `/seguridad` | Semana 3 | Lo pide todo comprador institucional; es copy, no ingeniería |
| **5** | Visualización interactiva del ecosistema | Mes 2 | Ver §3 sobre cómo abordarla |
| **6** | Asistente IA, calculadora ROI, salud de activos | Mes 2–3 | Alto costo, y varias requieren capacidad de producto que aún no existe |

---

## 2. Posicionamiento: cuál de los dos mensajes

El brief propone dos y pide elegir.

**A — «DATA → INTELLIGENCE → PREDICTION → ACTION»**
**B — «See more. Understand faster. Predict earlier. Act smarter.»**

**Recomiendo B como firma de marca y A como arquitectura interna**, con una corrección importante:

> **"Predict earlier" hay que sostenerlo o cambiarlo.**

Hoy Quorelia detecta *desviaciones sostenidas respecto del comportamiento esperado*. Eso es anticipación real y defendible. No es predicción estadística de falla ni vida útil remanente, que exige series históricas largas y validación activo por activo.

Frente a un ingeniero, la diferencia entre esas dos afirmaciones es la diferencia entre credibilidad y humo. En la página de gobierno lo dejé declarado de forma explícita, y esa honestidad **suma** en ese público en vez de restar.

Alternativa si se prefiere no matizar: **"See more. Understand faster. Act earlier."** — sostiene el mismo ritmo de cuatro tiempos sin prometer predicción.

---

## 3. Sobre Three.js: sí, pero no como lo pide el brief

El brief pide un ecosistema energético 3D interactivo. Mi recomendación es **invertir el orden de magnitud**:

**No hacer:** una escena WebGL completa con planta solar, turbinas, baterías y red, navegable en 3D. Es cara de construir, difícil de mantener, pesada en móvil y — el problema real — *se parece a un videojuego*, que es exactamente lo que el propio brief pide evitar.

**Hacer:** una **visualización de sistema en 2D con Canvas o SVG animado**: nodos de activos conectados, señal fluyendo entre ellos, estados que cambian, click para desplegar el detalle de cada activo. Peso: decenas de kilobytes en vez de megabytes. Funciona en cualquier dispositivo. Y comunica mejor la idea de *capa de inteligencia* que un render tridimensional, porque una capa es conceptualmente plana.

Si más adelante se quiere 3D, que sea **un solo elemento acotado** — por ejemplo el símbolo Q rotando con datos orbitando — con fallback a imagen estática, y nunca en la ruta crítica de carga.

---

## 4. Copy: hero de la home

El brief propone *"INTELLIGENCE FOR THE ENERGY INFRASTRUCTURE OF TOMORROW"*. Es correcto pero genérico: podría ser de cualquiera.

Tres alternativas más específicas, en orden de preferencia:

**1.** «Cada cifra que su planta reporta, defendible.» / *"Every number your plant reports, made defensible."*
→ Concreto, único, y es literalmente lo que hace el producto.

**2.** «Sus datos ya existen. La inteligencia, todavía no.» / *"Your data already exists. The intelligence doesn't yet."*
→ Tensión inmediata, formulada como problema del lector.

**3.** «Ver más. Entender antes. Actuar a tiempo.» / *"See more. Understand faster. Act earlier."*
→ La firma de marca como titular. Memorable, menos específico.

El hero actual usa el lema («Siempre vigilando. Al servicio de la energía del planeta»), que es emocionalmente fuerte pero no dice qué se vende. Sugiero **lema como pre-título pequeño y una de las tres frases como titular**.

---

## 5. Lo que la página de gobierno hace distinto

Cuatro decisiones deliberadas, cada una en contra del instinto comercial:

**Abre con las cifras de ellos, no con las nuestras.** 10.769 fiscalizaciones, 2.341 en generación distribuida, 2.100 documentales. Es su Cuenta Pública. Define el problema en sus términos antes de mencionar el producto.

**Declara los límites en una sección propia.** Hay un bloque completo titulado «Lo que Quorelia no hace»: no reemplaza fiscalización en terreno, no sustituye el juicio del fiscalizador, no accede a sistemas del Estado, no emite certificaciones con efecto regulatorio, no opera instalaciones. En venta institucional, enumerar límites genera más confianza que enumerar capacidades.

**Se niega explícitamente a proyectar ahorro.** Dice, textualmente, que sería fácil presentar una cifra optimista y que preferimos que la mida el equipo revisor de ellos con cronómetro. Un proveedor que no fabrica su propio número de ahorro es más creíble que uno que lo presenta.

**Incluye la definición de fracaso del piloto.** «Si el tiempo de revisión no disminuye de forma medible, el piloto se declara sin éxito y termina.» Nadie escribe eso en una propuesta comercial. Por eso funciona.

---

## 6. SEO — enfoque recomendado

Las palabras del brief son correctas pero compiten con presupuestos enormes. La ventaja real de Quorelia está en **la cola larga en español y específica de Chile**, donde casi no hay contenido:

- `disponibilidad contractual PMGD`
- `informe O&M automatizado Chile`
- `verificación datos SCADA planta solar`
- `monitoreo BESS normativa Chile`
- `trazabilidad cifras generación eléctrica`
- `DS 88 almacenamiento monitoreo`

**Táctica de mayor rendimiento:** publicar el análisis de Infotécnica como artículo público. Es contenido original, con datos verificables, sobre un registro que muchos consultan y nadie ha analizado. Genera enlaces entrantes de forma natural — que es lo que realmente mueve el posicionamiento.

---

## 7. Test creativo final del brief

| Pregunta | Página de gobierno |
|---|---|
| ¿Un funcionario confiaría en esto? | Sí — declara límites, cita fuentes, no exagera |
| ¿Un ingeniero lo respetaría? | Sí — la regla de retención y la distinción recurso/activo son argumentos técnicos reales |
| ¿Un inversionista entendería la oportunidad? | Parcialmente — falta la página de plataforma |
| ¿Un operador querría usarlo? | No es su página; corresponde a `/plataforma` |
| ¿Pediría una demo? | Sí — el CTA es una sesión técnica de 45 minutos, sin presentación comercial |
| ¿Recordaría Quorelia después? | El «2 de 977» y el «91,7% opera una sola central» son difíciles de olvidar |

---

## 8. Lo siguiente que necesito de ustedes

1. **Confirmar el mensaje de marca** — ¿«Predict earlier» se sostiene o se cambia por «Act earlier»?
2. **Decidir sobre el hero de la home** — ¿lema como titular, o una de las tres frases?
3. **Revisar la página de gobierno antes del viernes**, en especial la sección de gobernanza de datos: son principios de arquitectura y conviene que reflejen lo que efectivamente está implementado.
4. **Confirmar la razón social** — usé «Quorelia SpA»; corregir si no corresponde.
