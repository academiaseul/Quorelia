# Tarjetas de presentación Quorelia

Cuatro archivos listos, dos por persona (español e inglés). Cada PDF tiene **2 páginas: página 1 = frente, página 2 = reverso**.

| Archivo | Persona | Idioma |
|---|---|---|
| `Quorelia-Tarjeta-Jay-ES.pdf` | Jae Hee Kim | Español |
| `Quorelia-Tarjeta-Jay-EN.pdf` | Jae Hee Kim | Inglés |
| `Quorelia-Tarjeta-Diego-ES.pdf` | Diego Ostertag | Español |
| `Quorelia-Tarjeta-Diego-EN.pdf` | Diego Ostertag | Inglés |

---

## ⚠️ Antes de mandar a imprenta — dos datos por confirmar

Abre `gen_tarjetas.py` y edita el bloque marcado `── EDITAR AQUÍ ──`:

1. **Teléfonos.** Ambas tarjetas dicen `+56 9 XXXX XXXX`. Es un marcador deliberado: no inventé números. Reemplázalos.
2. **El correo de Diego.** Puse `diego@quorelia.org` siguiendo el patrón de tu propia dirección, pero **no me consta que exista**. Confírmalo o corrígelo.

Después vuelve a generar con:

```
python3 gen_tarjetas.py
```

Si prefieres una tarjeta sin teléfono — algo cada vez más común — simplemente borra esa línea del bloque de datos y queda un diseño más limpio.

---

## Especificaciones de impresión

| Parámetro | Valor |
|---|---|
| Formato de corte | **90 × 55 mm** (estándar chileno y europeo) |
| Formato del archivo | **96 × 61 mm** — incluye 3 mm de sangrado por lado |
| Zona segura | 4 mm adicionales hacia adentro; ningún texto la cruza |
| Caras | Frente blanco / reverso azul marino (#0B1C2C) |
| Papel sugerido | 350 g couché mate, laminado mate |

**Nota sobre el reverso:** va con fondo azul de borde a borde, así que necesita impresión a sangre completa. Confirma con la imprenta que el archivo trae el sangrado incluido — ya lo trae, no hay que agregarlo.

**Si tu imprenta pide CMYK:** estos PDF están en RGB. Cualquier imprenta lo convierte, pero el teal (#1FB6A8) es un color vivo que en CMYK pierde algo de saturación. Si te importa que quede exacto, pide una prueba de color antes del tiraje, o considera imprimir el teal como tinta directa Pantone (la más cercana es **Pantone 3272 C**, verifícala contra una guía física).

---

## Sobre el diseño

Sigue la estructura de la tarjeta de referencia que enviaste:

- **Frente** — nombre grande a la izquierda, cargo debajo, filete de color, nombre de la empresa en negrita, descriptor del giro, y bloque de contacto con etiquetas de color en columna. El gráfico de marca sangra por el borde derecho, ocupando el tercio derecho de la tarjeta, igual que la hélice en la tarjeta original.
- **Reverso** — símbolo y marca denominativa centrados sobre fondo oscuro, con el descriptor y el lema. Abajo, la traza de observación: el mismo motivo de barras que usa el sitio, el teaser y los informes.

Esa traza es el detalle que amarra todo. Es el único elemento gráfico que aparece en cada pieza de Quorelia, y en una tarjeta funciona como firma discreta: quien ya vio el sitio o un informe la reconoce.

---

## Variantes que puedo generar si las quieres

- **Bilingüe en una sola tarjeta** — español al frente, inglés al reverso (ahorra tener dos juegos).
- **Pliego de imposición** — varias tarjetas por hoja A4 o carta con marcas de corte, si la imprenta lo pide así.
- **Versión con dirección física**, si deciden declarar oficina.
- **Reverso con código QR** al sitio o a tu LinkedIn.
