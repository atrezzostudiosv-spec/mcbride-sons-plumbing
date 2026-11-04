# McBride — integración de componentes originales de Atrezzo

## Realizado

Fuente local: `ATREZZO COMPONENTES 2026`, seleccionada por el usuario. Se leyeron las guías, contratos HTML/CSS/JS y ejemplos antes de integrar.

- **Guided Service Atlas**, de SERVICE SHOWCASE 01: tres capítulos con fotografía sticky y sincronización por scroll nativo. Los botones permiten saltar entre capítulos. En móvil, cada capítulo muestra su propia fotografía.
- **Open Process Cards / C03**, de CARDS 01: tres tarjetas `details/summary` con observaciones útiles antes de llamar; el resumen y la precaución importante permanecen visibles.
- **Visual Feature Mosaic / C02**, de CARDS 01: mosaico 1+2 de los dos servicios relacionados y la historia familiar. Solo se añade en las seis fichas; Services conserva su galería existente.

Los dos primeros se integran en las seis fichas y en el bloque informativo de Services. Cada ficha también utiliza su escena de servicio local en la portada.

## Archivos y mantenimiento

- `assets/atrezzo/service-showcase.css`, `service-showcase.js` y `cards-01.css`: copias originales sin cambios. Huellas y rutas de origen en `ATREZZO-COMPONENT-SOURCES.json`.
- `assets/css/service-content-atrezzo.css`: adaptación de Manrope, verde, carbón, marfil, espaciado, altura de lectura, encuadres y contraste. Incluye fallback con imágenes por artículo si el JS del componente no está disponible.
- `content/service-content.json`: contenido anterior recuperado, preguntas, precauciones y servicios relacionados.
- `scripts/build-service-content.py`: genera los siete bloques a partir del contenido y conserva los contratos de la biblioteca. No añade dependencias ni otro motor de scroll.

Después de editar el contenido:

```sh
python3 scripts/build-service-content.py
python3 scripts/validate-site.py
node --check assets/atrezzo/service-showcase.js
```

La tipografía y los tamaños del showroom no se trasladaron al branding de McBride. Se preservan las interacciones del Atlas y los disclosures nativos. Se redujo la altura de los capítulos para evitar alargar artificialmente la lectura.

## Recursos y contenido

Se reutilizan las ilustraciones WebP de servicios que ya estaban en el proyecto, con un encuadre de contexto y otro de detalle, y una escena de conversación previamente integrada. La imagen familiar procede del retrato auténtico suministrado. No se copiaron las imágenes arquitectónicas de prueba de la biblioteca.

Los avisos distinguen las escenas ilustrativas del personal y proyectos reales. No se añaden servicios, precios, tiempos de respuesta, resultados ni certificaciones. Se conservan las descripciones principales y las precauciones anteriores. El contenido añadido a los desplegables es orientación general para explicar una consulta.

Home, About y Contact no cambian en esta integración. Los formularios, las reseñas y logotipos, los metadatos SEO y el footer común se conservan en las páginas intervenidas.

## Verificado

- Siete páginas × 375, 390, 768, 1024 y 1440 px: 35 comprobaciones iniciales sin desbordamiento horizontal; tres capítulos, tres disclosures, un H1, un formulario y un footer por página.
- Atlas: selección por botones, capítulo/fotografía sincronizados y retorno por scroll nativo.
- C03: apertura con teclado y clic.
- Fixture aislado sin ninguna etiqueta script: fotografías integradas visibles, escenario sticky oculto, disclosure operativo y sin desbordamiento. Esto verifica los componentes nuevos, no todo el layout heredado que depende de Tailwind en tiempo de ejecución.
- Validación global de 739 referencias relativas, metadatos y footer.
- Sin errores de consola en el recorrido de muestra.

## No verificado / pendiente

- Las reglas de movimiento reducido están presentes y se revisaron en código; no se cambió la preferencia del sistema para una prueba visual.
- Safari e iOS/Android físicos no probados.
- Entrega real de formularios fuera del alcance de este cambio.
- Aprobación visual del usuario sobre la versión publicada.

Siguiente acción: revisar una ficha publicada en escritorio y móvil y, si hay correcciones concretas de encuadre o ritmo, aplicarlas al estilo compartido.
