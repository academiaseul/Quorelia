# Demo privada — no publicar

`control-center.html` vivía en la raíz del sitio y era accesible en
`quorelia.org/control-center.html`. Se movió aquí para sacarlo de la web:
ahora ningún enlace del sitio apunta a él.

En su lugar, los tres puntos de entrada que existían ahora abren un correo
a **jay@quorelia.org** con asunto y cuerpo prellenados, para agendar una
sesión guiada:

| Dónde | Qué dice ahora |
|---|---|
| `index.html` · Capacidades, botón negro | Solicitar una demo del Control Center |
| `index.html` · sección Control Center | Solicitar una demo del Control Center |
| `gobierno.html` · nota "Vista Regulatoria" | Solicitar una demostración del Control Center |

## Advertencia sobre hosting estático

El sitio se publica desde el repositorio `academiaseul/Quorelia` en GitHub.
En un host estático **todo archivo del repositorio es accesible por URL**,
aunque no esté enlazado desde ninguna página. Es decir: mover el archivo a
esta carpeta lo saca de la navegación, pero seguirá respondiendo en
`quorelia.org/demo-privado/control-center.html` si el despliegue publica la
raíz del repositorio completa.

Para que quede realmente fuera del sitio hay que hacer una de estas tres:

1. Excluir la carpeta `demo-privado/` en la configuración de despliegue.
2. Sacar el archivo del repositorio y guardarlo fuera de él.
3. Publicar sólo una lista explícita de archivos, no la raíz completa.

El archivo es autocontenido — no depende de `quorelia.css` ni de ningún otro
recurso — así que se puede abrir con doble clic desde cualquier carpeta,
incluida una llave USB, para mostrarlo en reunión sin conexión.
