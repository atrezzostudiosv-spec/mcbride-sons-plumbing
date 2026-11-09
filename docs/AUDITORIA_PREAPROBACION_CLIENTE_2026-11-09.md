# McBride & Sons Plumbing — Auditoría de preaprobación del cliente
**Fecha:** 9 de noviembre de 2026  
**Versión auditada:** `f99a378e52e1feadc3a782f6783c5357132ea549`, GitHub Pages workflow `42595236133` completado correctamente.  
**Website:** https://atrezzostudiosv-spec.github.io/mcbride-sons-plumbing/  
**Alcance:** Home, About, Contact, Services y seis fichas de servicios (10 páginas), componentes globales, repositorio, metadatos y fuentes de negocio.  
**Tipo de prueba:** inspección estática de código y árbol Git, más contraste público de plataformas de reseñas. NO es un test visual en navegador de la versión final ni prueba de envíos reales.

## Veredicto
**PREPARADO ESTRUCTURALMENTE PARA REVISIÓN DE DISEÑO, NO PARA ENTREGA FINAL/PRODUCCIÓN.** Se debe hacer una ronda breve de QA visual sobre el commit vigente antes de remitir el enlace como «propuesta terminada». El link es una demo pública no indexable, marcada claramente como diseño no oficial de Atrezzo.

## 1 — Header, barra superior y callbar
- **Verificado por comparación exacta de HTML:** las 10 páginas incluyen una copia idéntica del componente `templates/site-announcement.html` (franja verde) y del `templates/mobile-callbar.html` (barra blanca y botón verde oscuro), sin variantes anteriores duplicadas. Cada página incluye `assets/css/site-chrome.css?v=20261109-home-chrome-v1`.
- **Verificado por lectura CSS:** hasta 640 px, franja centrada sin teléfono y callbar inferior fija con safe-area; desde 641 px, franja a dos extremos y callbar oculta. A 375 px, menú compacto; a 768 px, menú hamburguesa y botón de llamada del header; a 1024/1440 px menú de escritorio. Estos son resultados de reglas de CSS, no capturas verificadas.
- **Logo, tipografía y cromática:** `assets/css/home-art-direction.css` y `assets/css/site-nav.css` definen el mismo logo de 164×59, 145×53 (<=900 px), 126×48 (<=640 px), fondo carbón y acento verde. Menú, enlaces y CTA muestran las mismas etiquetas en las diez páginas; `aria-current` identifica la página correspondiente.
- **Inconsistencia real:** Home integra un *smart sticky header* que se oculta al bajar y reaparece al subir en escritorio >=1024px (salvo movimiento reducido), mediante `assets/css/home-art-direction.css` y `assets/js/main.js`. Las páginas internas utilizan header sticky sin esa transformación: mismo aspecto inicial, **diferente comportamiento al hacer scroll**. Decidir si unificar el comportamiento antes de presentar el preview, sin comprometer la accesibilidad/escenas cinematográficas.
- **Verificación visual pendiente:** menú abierto, foco, scroll descendente/ascendente y recortes a 375/390/640/768/900/1024/1440 px, iOS Safari y Android.

## 2 — Footer
- **Aprobado a nivel de fuente:** el bloque `<footer>` de las 10 páginas es idéntico al fichero `templates/footer.html` con sus rutas relativas por nivel. Mismo logo, descripción, links a Home/About/Services/Contact, 6 servicios, teléfono (817) 901-3328, email, copy de servicio y aviso explícito de demo.
- Hoja común: `assets/css/shared-footer.css`. Reglas de escritorio con columnas, tablet con 2 y móvil con 2 columnas.
- **No hay enlaces a política de privacidad/términos** en el footer y no hay páginas legales en el árbol auditado: elaborar y aprobar avisos aplicables antes de producción, sin inventarlos.
- **Pendiente:** comprobar legibilidad y espacio de las dos columnas de footer a 375 px y enlaces/foco/espaciado a 768/1024/1440. No modificar el diseño aprobado sin fallo reproducible.

## 3 — Rutas, navegación, contenido
- **759 recursos/referencias relativas e internas inspeccionadas** en HTML de 10 páginas; **0 rutas internas faltantes, 0 anclas locales rotas, 0 links vacíos '#', 0 imágenes sin atributo alt detectados** en la inspección de fuente. URLs externas y sus tiempos de respuesta no fueron exhaustivamente probados.
- Cada página posee un H1 y conjunto exclusivo de title/meta description/canonical/OG según `scripts/validate-site.py` y lectura independiente del código. Demostración sigue `noindex, nofollow`; canonical y sitemap apuntan a GitHub Pages, no al dominio definitivo.
- Diez páginas operativas en fuente, seis servicios documentados y página general. Hero de Home, secuencias de fotografía/scroll, testimonios/valoración y CTA final, About familiar, Contact, Atlas de 3 capítulos, disclosures y mosaico de relacionados ya implementados; no reconstruir lo aprobado.
- Se mantienen fotografías de stock/ilustrativas con disclaimer. Atlas de seis servicios repite el WebP del servicio en capítulos 1/2 y una escena de consulta común en capítulo 3; **oportunidad visual conocida, no bloqueante para mostrar concepto**, pero pendiente de dirección de arte si se busca aprobación final de experiencia.
- Navegación desplegable, scroll y popups con JS de código presente; no se ha reproducido aquí el comportamiento sobre el sitio desplegado.

## 4 — Revisión de conversiones y confianza
- Los **9 formularios** (Home, Contact, Services índice y seis fichas) envían al endpoint de prueba `https://formsubmit.co/atrezzostudiosv@gmail.com`, no al correo de McBride. About no tiene formulario y enlaza al teléfono. La presencia de acción no prueba recepción. **Demo intencional**, bloquear el uso como canal comercial hasta que cliente apruebe destino y una prueba real de envío/recepción confirme funcionamiento.
- CTA telefónicos apuntan consistentemente a `tel:+18179013328`. El footer contiene `owner@mcbrideandsonsplumbing.com`.
- “5-Star Plumbing Experts” y logos ilustrados con cinco estrellas fueron suministrados desde el sitio original; **no equivalen a ratings actuales confirmados**. Página pública HomeAdvisor reporta **4.6/5 y 327 reseñas** al revisar (fuente: https://www.homeadvisor.com/rated.McBridePlumbing.132331234.html), mientras la gráfica muestra cinco estrellas. Facebook no tiene rating verificado. Mantener la advertencia editorial y exigir aprobación explícita de cliente/compliance antes de publicar esas imágenes como credenciales propias. El emblema TSBPE no implica patrocinio ni licencia verificada.
- El propio original declara disponibilidad de emergencias 24/7, pero la ficha externa HomeAdvisor incluye horarios convencionales: confirmar vigencia y alcance del 24/7 con el cliente antes de activar una web de negocio.

## 5 — Rendimiento, accesibilidad y dependencias
- Pages despliegue **success** del 9-nov-2026; certifica despliegue, no renderizado, Core Web Vitals ni funcionamiento de formularios.
- Ocho páginas internas aún cargan `cdn.tailwindcss.com` en tiempo de ejecución y algunas Font Awesome/CDN; conviene compilar y localizar los estilos para la salida a producción. Home presenta dependencias externas de fotos; carga de medios/CDN no medida.
- En JS hay soporte de navegación, modales, carrusel con pausa y `prefers-reduced-motion`; falta prueba de teclado real, foco, reader, contraste, WCAG 2.2 AA y iOS/Android. No afirmar aprobación técnica por inspección estática.
- La revisión anterior del 4-nov documentó 35–40 comprobaciones por viewport, **pero el último cambio del 9-nov unificó header y callbar con nuevo CSS**, por lo que la actualización requiere regresión visual específica.

## 6 — Decisión de entrega
### Sí se puede presentar al cliente como propuesta visual
- Estructura completa con 10 páginas navegables y 6 servicios reales.
- Marca familiar, contenido editorial, fotos ilustrativas identificadas, CTA y teléfono.
- Header, franja superior, callbar y footer compartidos en fuente.
- SEO/social preparado en demo, enlace HTTPS de GitHub Pages y disclaimer de no oficial.

### Antes de enviar para aprobación formal de diseño
1. Revisar visualmente el **build actual**, no capturas antiguas, a 375/768/1024/1440 px; abrir/usar menú, llamar, volver arriba/abajo, verificar que callbar no tape footer y scroll no bloquee lectura. Corregir solo fallos comprobados.
2. Decidir si el comportamiento del header desktop debe ser uniforme; no confundir equivalencia estética con interacción.
3. Remitir al cliente para aprobar visual, fotografías ilustrativas, copy comercial y claims/reseñas; **avisar que formularios son de pruebas**.

### Antes de producción (fase diferente)
- Confirmar email destino y prueba recibida, dominio/hosting, política legal aplicable, licencia y evidencias de reseñas/ratings, accesibilidad real, performance, CDN/media y retirar noindex solo tras autorización.

## Estado según Regla de continuidad
- **Estructura, componentes compartidos, footer y ruta de preview: IMPLEMENTADOS Y VERIFICADOS EN CÓDIGO.**
- **QA visual del build del 9-nov: EN VALIDACIÓN (NO COMPROBADO).**
- **Claims/fotografía/ratings: PENDIENTES DE APROBACIÓN DEL CLIENTE.**
- **Producción, emails, privacidad, rendimiento: BLOQUEADOS hasta autorización y pruebas.**
- **SIGUIENTE ACCIÓN ÚNICA:** revisión visual de regresión de 10 páginas a 375/768/1024/1440 px para decidir envío de demo, sin rehacer fases cerradas.
