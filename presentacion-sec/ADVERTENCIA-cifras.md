# ⚠️ Dos cifras que hay que corregir antes de la reunión

**Léelo antes que la presentación.** La reunión es bajo **Ley 20.730 de Lobby**: el registro de audiencia es público, y lo que se afirma frente a la SEC queda documentado. Las dos observaciones siguientes son las que más riesgo tienen.

---

## 1. «2.291 MW en operación en Chile» — el número está mal atribuido

El brief dice: *"en Chile actualmente está con operación 2.291 MW, de lo cual 1 GW lo tenemos instalado nosotros"*.

Esa cifra **no es la capacidad del sistema eléctrico chileno**. Es, casi exactamente, la capacidad instalada de **almacenamiento con baterías**.

| Concepto | Cifra real | Fuente |
|---|---:|---|
| Capacidad instalada total del SEN | **38.709 MW** (mayo 2026) | Coordinador / CNE |
| Proyección a agosto 2026 | ~39.770 MW | Coordinador / CNE |
| **BESS en operación** | **2.283 MW** (marzo 2026) | Coordinador |
| Proyección BESS fin de 2026 | 5.081 MW · 18.643 MWh | Coordinador |

**Por qué importa tanto.** Decir *"1 GW de los 2.291 MW que operan en Chile"* frente al Jefe de la Unidad de Generación y Transmisión de la SEC afirma, en la práctica, que Quorelia cubre **el 44% del sistema eléctrico nacional**. Él sabe que el sistema tiene casi 39.000 MW. La frase no se lee como una exageración: se lee como que quien la dice no conoce la magnitud del parque que pretende ayudar a fiscalizar.

Y quedaría en el registro público de la audiencia.

### Formulación correcta

> «El almacenamiento con baterías pasó de una base marginal a **2.283 MW en operación en marzo de 2026**, y el Coordinador proyecta que se duplique a 5.081 MW hacia fin de año. La tecnología de Quorelia se está aplicando en el contexto de infraestructura BESS **del orden de 1 GW**.»

Eso es exacto, es verificable, y sigue siendo una cifra grande: del orden del 40% del parque de almacenamiento actual. **Es más impresionante bien dicho que mal dicho**, porque resiste la repregunta.

### Si te preguntan «¿1 GW de qué exactamente?»

Ten preparada la respuesta precisa: qué instalaciones, bajo qué figura contractual, y si la cifra corresponde a potencia (MW) o energía (MWh). Es la primera pregunta que hará un ingeniero eléctrico, y la vaguedad ahí cuesta más que cualquier número.

---

## 2. «BESS Cerro Aurora, Valle Luna y Salar Bravo» — no existen en tus archivos

El brief describe *"las 3 plantas activas que actualmente integran el sistema (BESS Cerro Aurora, Valle Luna y Salar Bravo, sumando 303 MW y 1.872 MWh)"*.

**Busqué esos tres nombres en todo el repositorio de Quorelia y no aparecen en ningún archivo.** No están en el tablero SCADA, ni en los informes de muestra, ni en el sitio. Las instalaciones ficticias que sí creamos se llaman *Parque de Almacenamiento Tamarugal*, *Planta Solar Cerro Tinaja* y *Parque Eólico Sierra Guanaco*, y están marcadas como ilustrativas en cada página.

Hay dos posibilidades y conviene aclararlas antes del viernes:

- **Son plantas reales de un cliente.** Entonces necesitas autorización escrita para nombrarlas ante la autoridad, y hay que verificar sus cifras contra la fuente.
- **Son nombres de demostración generados para una maqueta.** Entonces **no pueden presentarse como "3 plantas activas que actualmente integran el sistema"**. Eso sería describir una capacidad instalada que no existe, ante un fiscalizador, en una audiencia de registro público.

**Recomendación:** no incluir nombres de instalaciones en esta presentación. La versión que construí no menciona ninguna. El argumento se sostiene con el análisis de Infotécnica, que es real, verificable y —esto es lo importante— *nadie más lo ha hecho*.

---

## 3. Lo que sí puedes afirmar sin ninguna reserva

Todo esto está verificado y con fuente citada en la presentación:

- **2.029 centrales** de **1.614 titulares** en el registro nacional
- **91,7% de los titulares opera una sola central**; solo 37 operan cuatro o más
- **23,1% de completitud** en la ficha solar coordinada, la tecnología con 1.375 de las 2.029 centrales
- **2 de 977 unidades PMGD** declaran almacenamiento
- **Tres errores estructurales** en las dos únicas fichas de almacenamiento que existen
- **2.100 de 2.341 fiscalizaciones** de generación distribuida en 2025 fueron documentales *(Cuenta Pública 2026 de la SEC)*

Ese conjunto es más potente que cualquier cifra de cobertura propia, porque **habla del problema de ellos con los datos de ellos**.

---

## 4. Una nota sobre el marco «Velocidad Adaptativa»

El marco de siete etapas está bien construido y lo incorporé completo. Un solo ajuste de tono: frente a un regulador, las etapas 5 y 6 —*Transformación* e *Institucionalización*— pueden sonar a que un proveedor privado propone rediseñar procesos y gobernanza del Estado.

En la presentación las redacté como capacidades **del sistema de información**, no como intervención institucional. Si te preguntan por ellas, conviene enmarcarlas así: *«institucionalizar el formato»*, no *«institucionalizar el cambio en la SEC»*.

---

## Antes del viernes

- [ ] Corregir mentalmente 2.291 MW → **2.283 MW de BESS**, sistema total ~38.700 MW
- [ ] Definir con precisión qué respalda el «1 GW» y en qué unidades
- [ ] Decidir sobre los tres nombres de plantas: autorización, o no mencionarlos
- [ ] Confirmar la razón social «Quorelia SpA»
- [ ] Llevar los dos Excel de Infotécnica por si piden ver el origen del análisis

---

### Fuentes

- [Capacidad instalada SEN y proyección BESS 2026 — Coordinador Eléctrico Nacional](https://www.coordinador.cl/)
- [Potencia instalada de almacenamiento se duplicará en 2026 — Electromineria](https://electromineria.cl/potencia-instalada-almacenamiento-sistema-electrico-se-duplicara-2026/)
- [CNE proyecta casi 13.000 MWh nuevos de almacenamiento hacia fines de 2026 — Reporte Minero](https://www.reporteminero.cl/noticia/noticias/2026/05/cne-almacenamiento-bess-chile-2026)
- [Infotécnica — Coordinador Eléctrico Nacional](https://infotecnica.coordinador.cl/instalaciones/unidades-generadoras-pmgd) *(extracción 16-08-2026)*
- [Cuenta Pública 2026 de la SEC — Revista Electricidad](https://www.revistaei.cl/sec-realiza-cuenta-publica-participativa-2026-destacando-ejes-de-su-gestion/)
