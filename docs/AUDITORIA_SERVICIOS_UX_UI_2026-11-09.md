# McBride & Sons Plumbing — Auditoría UX/UI de Servicios (actualizada)
**Fecha:** 9 de noviembre de 2026  
**Base auditada:** rama main, commit c43cac26b30057945388883100131d2ba27650ba, último cambio de funcionalidad 4-nov-2026.  
**Alcance:** Services overview y seis servicios. Revisión de código en GitHub, imágenes enlazadas, CSS, JS, JSON editorial, generador y registro maestro. Se contrastaron los servicios y contacto con https://mcbrideandsonsplumbing.com/ y https://mcbrideandsonsplumbing.com/contact-us. Esta auditoría NO incluye captura ni prueba visual del sitio publicado en navegador.

## Hallazgo central
La auditoría antigua ya no describe el proyecto: el 4 de noviembre se integraron los originales **Guided Service Atlas (3 capítulos)**, **Open Process Cards C03 (3 detalles)** y **Visual Feature Mosaic C02 (relacionados + retrato familiar)**. La página índice conserva además su galería 3×2. No reconstruir ninguna de estas partes ni proponerlas como inexistentes.

**Defecto principal demostrable:** en las 6 fichas el capítulo 1 y el 2 del Atlas muestran el mismo archivo fotográfico del servicio, con distinto punto focal; el capítulo 3 de todas reutiliza exactamente el mismo WebP de consulta. La fotografía principal se repite además en el hero y el CTA. Esto da apariencia de plantilla aunque ya existan imágenes en el contenido.

## Hechos confirmados / límites
- Servicios públicos: Drain Cleaning, Leak Repair, Hydro-Jetting, Water Heaters, Drain & Sewer Repair, Bathroom Remodeling; fuente: sitio original McBride.
- Teléfono público (817) 901-3328; sitio original declara 24/7, pero no garantiza tiempo de llegada. La fuente pública también presenta legado de marca desde 1953.
- El original muestra licencia M-39313; **su estado de vigencia/COI se debe comprobar en la TSBPE** antes de usarla como garantía: https://tsbpe.texas.gov/consumer-information/.
- Los materiales ilustrativos (incluso con uniforme/logo simulado) **no** demuestran trabajos ni empleados reales. El retrato familiar suministrado sí es material de empresa.
- No ampliar Water Heaters a calentadores de un tipo específico, ni Bathroom Remodeling a reforma integral, ni Hydro-Jetting a inspecciones/métodos no confirmados. No inventar precios, garantía, testimonios o citas.

## Estado técnico comprobado
| Componente | Verificación de código | Estado |
| --- | --- | --- |
| Hero / CTA Request Service | Componente y script presentes | IMPLEMENTADO; correo no probado |
| Atlas (tres capítulos, imágenes sticky y móvil) | CSS+JS original Atrezzo y marcado presente | IMPLEMENTADO |
| Open Process Cards | 3 detalles por página | IMPLEMENTADO |
| Mosaico de relacionados | 3 fotos/links en seis servicios | IMPLEMENTADO |
| Customer Feedback / logos / CTA | Presente en fichas | IMPLEMENTADO |
| SEO, favicon, OG y footer compartido | Commit 612e366 del 4-nov | IMPLEMENTADO |
| Deploy anterior | GitHub Actions run 41911804593 | SUCCESS |
| QA responsive anterior | 35 verificaciones iniciales 375/390/768/1024/1440 y pruebas de componente documentadas 4-nov | ANTERIORMENTE PROBADO; validación nueva por hacer |

## Prioridades UX/UI
**P1 · Diversidad fotográfica.** Generar/seleccionar al menos **una fotografía contextual nueva por servicio** (6 imágenes prioritarias), sin repetir la del hero y el CTA. La escena de consulta compartida debe revisarse después. Seleccionar cada plano por función narrativa y plausibilidad técnica. Imágenes con licencia o ilustrativas, nunca «obra realizada» de McBride.

**P1 · Ritmo distinto por servicio.** Mantener componentes originales y variar foco, iluminación, distribución interna y tempo de cada historia. No crear seis versiones de la misma escena; no añadir más bloques de texto o tarjetas genéricas. Si una escena no explica nada, no añadirla.

**P2 · Legibilidad.** Se constató texto principal de 13–14 px y acciones de 10–12 px en el componente central. En este commit se ajusta exclusivamente la hoja de adaptación para elevar cuerpo a 15–16 px, expandido a 14 px y enlaces a 13–14 px; sin cambiar contenidos ni reescribir la librería. Revalidar diseño renderizado y alturas tras el cambio.

**P2 · CTA y duplicidad.** Tres enlaces telefónicos casi iguales en cada capítulo son útiles pero repetitivos. Evaluar un único CTA editorial de final de secuencia manteniendo siempre el acceso a llamada y popup. No eliminar links aún.

**P2 · Contenido.** La información está limitada a lo confirmado y a educación general. Priorizar señales y preparación para llamar, no listas de supuestos servicios, diagnósticos, maquinaria o procedimientos.

## Dirección artística específica (PROYECTADA, NO IMPLEMENTADA)
**Sistema de identidad:** humano/legado + técnico/resolutivo, no lujo genérico; Manrope, verde, carbón y marfil existentes. Hero con acceso inmediato; Atlas M2 controlado; formularios M0; móvil en scroll vertical normal y reduced motion.

| Servicio | Enfoque emocional | Fotografía nueva prioritaria, ilustrativa | Tratamiento editorial |
| --- | --- | --- | --- |
| Drain Cleaning | Obstrucción cotidiana | Desagüe / tubería bajo fregadero con conexiones reales | Directo, limpio, corto; señales que se repiten |
| Leak Repair | Detección y contención | Humedad localizada, conexión con goteo técnicamente plausible | Dos escalas visuales: contexto y detalle |
| Hydro-Jetting | Trabajo técnico | Equipo y manguera de hidro-jetting con unión realista | Detalle técnico, ritmo sobrio |
| Water Heaters | Agua caliente y seguridad | Calentador y conexiones plausibles, sin modelo inventado | Luminoso, informativo, pausado |
| Drain & Sewer Repair | Alcance de la línea | Registro/tubería exterior coherente con drenaje | Robusto, imagen panorámica controlada |
| Bathroom Remodeling Plumbing | Planificación de instalaciones | Accesorios y fontanería de baño, realismo arquitectónico | Editorial luminoso, explicar toma y distribución |

## Partitura de aceptación para la ficha piloto: Drain Cleaning
| Sección | Contenido acreditado | Presentación | Movimiento | Móvil | CTA |
| --- | --- | --- | --- | --- | --- |
| Hero | Título/servicio y teléfono originales | Fondo ilustrativo original | M0–M1 | Encaje del sujeto, copy legible | Call / Request Service |
| Atlas 01 | Addressing Drain Blockages | Imagen actual del servicio | M2 original | Foto arriba, copy abajo | Teléfono disponible |
| Atlas 02 | Look beyond one slow fixture | **Nueva imagen contextual**; copy existente | Foto que cambia con scroll nativo | Bloque vertical; sin escena sticky | Enlace existente |
| Atlas 03 | When a blockage needs attention | Revisar si consulta existente explica el texto | M1–M2, sin retener scroll | Foto y texto legibles | Enlace existente |
| Before You Call | Preguntas, precauciones educativas | Disclosures nativos | M0 | Orden natural | Call |
| Related | Servicios relacionados / retrato familiar real | Mosaico C02 original | M1 | Apilado legible | Links originales |
| Feedback + trust | Reseñas y gráficos originales | Componentes aprobados | Carrusel aprobado | Continuo con pausa explícita | Google Maps ya existente |
| Cierre | CTA fotográfico aprobado | Full bleed | M0–M1 | Foto/contraste correctos | Call / Contact |

## Validación obligatoria de fase
- Revisar 375 / 390 / 768 / 1024 / 1440 y pantallas bajas, scroll hacia atrás, salto de ancla, tabulación, Escape del modal y reduced motion.
- Evitar desbordamiento horizontal, recorte de sujeto, texto oculto, retardos de lectura y bloqueo de scroll.
- No marcar probado el sitio público por haber revisado solo GitHub o una captura aislada.
- Respetar el builder: cambiar datos en content/service-content.json y regenerar con scripts/build-service-content.py; no editar solo HTML si se modifica el Atlas.

## Estado / siguiente acción
- AUDITORÍA: REALIZADA y registrada. Ajustes tipográficos: CÓDIGO ACTUALIZADO; **EN VALIDACIÓN visual**.
- Distinción fotográfica y nuevo ritmo: PLANIFICADOS, no implementados ni aprobados.
- Siguiente acción única: **revisar Drain Cleaning como piloto visual**, decidir su nueva escena contextual y después corregir las otras cinco fichas sin rehacer componentes cerrados.
