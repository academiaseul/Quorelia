# Quorelia — Plan de mejoras del sitio, por audiencia

Fecha: 20 de agosto de 2026. Orden dentro de cada bloque: primero lo que más mueve la aguja.
Marcar con `[x]` al completar.

---

## 1 · Clientes potenciales (dueños de activos que podrían comprar)

- [ ] **Caso de negocio en una cifra.** La página vende verificabilidad pero nunca dice cuánto cuesta el problema. Un módulo "una cifra mal informada cuesta X" — disputa contractual, multa, o penalización de disponibilidad — convierte la trazabilidad en dinero. Sin este puente, sólo compra quien ya entendía.
- [ ] **Página de precios o al menos de modelo comercial.** ¿Por MW? ¿Por planta? ¿Suscripción? El silencio total sobre precio filtra a los serios. Basta un "desde" o un "cómo cotizamos".
- [ ] **Un caso de cliente real** (aunque sea anónimo: "un portafolio de 40 MW en la RM"). Todo el sitio es muestra ilustrativa; el primer logo o testimonio real cambia la categoría del sitio entero.
- [ ] **Onboarding visible:** los 3 pasos y días que separan "firmé" de "primer informe". El costo de cambio percibido es la objeción número uno en software industrial.
- [ ] Demo agendable con calendario (Calendly o similar) en vez de sólo formulario — reduce fricción de ida y vuelta.

## 2 · Equipos O&M (los usuarios diarios)

- [ ] **Página "Para operadores":** el sitio habla a dueños y reguladores; el técnico que recibirá las alertas no tiene página. Mostrar: cómo llega una alerta (correo/WhatsApp/plataforma), cómo se cierra un hallazgo, qué hace el sistema a las 3 AM.
- [ ] **Video de 90 segundos del Control Center en uso** — el recorrido real: alerta → diagnóstico → orden de trabajo. El demo interactivo existe pero nadie lo recorre solo.
- [ ] Especificaciones de integración: protocolos soportados (Modbus, OPC-UA, IEC-104, DNP3…), historiadores compatibles, requisitos de red. El ingeniero que evalúa necesita esta página para decir que sí.
- [ ] Mostrar el flujo de clasificación preventivo/correctivo con un ejemplo real de orden generada.

## 3 · Gobierno y reguladores

- [ ] **Resolver la fecha del teaser (21 vs 20 de agosto)** antes de la reunión — documento de registro público.
- [ ] Sección "Marco normativo": cómo se alinea Quorelia con la NTSyCS, el nuevo reglamento de coordinación y la Ley 21.505 de almacenamiento. Hoy la página cita cifras SEC pero no mapea normas.
- [ ] Versión PDF descargable de gobierno.html — los funcionarios circulan PDFs, no enlaces.
- [ ] Página de transparencia activa: registro de reuniones Ley de Lobby sostenidas. Señal de seriedad institucional que casi nadie del rubro da.
- [ ] Verificar estado del Decreto N°1/2026 en Contraloría antes de citarlo.

## 4 · Propietarios e inversionistas (stakeholders financieros)

- [ ] **Página "Para inversionistas y financistas":** el informe como instrumento de due diligence — disponibilidad certificable para covenants, RTE defendible para valorización de BESS, trazabilidad para vendor due diligence. Es la audiencia con mayor disposición a pagar y no tiene página.
- [ ] Conectar el teaser inversionista (ya existe en /teaser) desde el sitio — hoy es huérfano.
- [ ] Módulo "riesgo de dato" : qué pasa en un M&A cuando el comprador no puede reproducir las cifras del vendedor. Quorelia como seguro de verdad.
- [ ] Depreciación de activos y salud de celdas como argumento patrimonial (el módulo existe en el Control Center; el sitio no lo vende).

## 5 · Transversal (afecta a todas las audiencias)

- [ ] **Favicons faltantes** (favicon.ico, favicon-32.png referenciados en las 3 páginas, no existen en la carpeta).
- [ ] **Push a GitHub** — el sitio publicado sigue una versión atrás de todo el trabajo local.
- [ ] Excluir `demo-privado/` del despliegue (sigue accesible por URL directa en hosting estático).
- [ ] Restrict to Domain en Formspree → quorelia.org; confirmar correo de verificación de jay@quorelia.org.
- [ ] SEO: meta descriptions traducidas por idioma, hreflang para es/en/zh, sitemap.xml.
- [ ] Open Graph: la imagen social (quorelia-banner.jpg) es del diseño anterior; regenerar con el estilo actual.
- [ ] Accesibilidad: revisar contraste del teal sobre gris claro en etiquetas pequeñas; focus visible en el formulario.
- [ ] Analytics: definir eventos GA4 (envío de formulario, clic en informe, cambio de idioma) — hoy sólo mide páginas vistas.
- [ ] Unificar nombres de plantas ficticias entre Control Center (Cerro Aurora/Valle Luna/Salar Bravo) y los informes (Tamarugal/Cerro Tinaja/Sierra Guanaco).
- [ ] Página 404 con el estilo del sitio.

---

*Los tres primeros de cada bloque son los de mayor retorno. Si hay que elegir cinco en total: caso de negocio en una cifra, precios, página para inversionistas, video del Control Center, y el push a GitHub con favicons.*
