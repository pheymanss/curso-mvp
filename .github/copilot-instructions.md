Este repositorio contiene todo el contenido de un curso para científicos de datos en el ámbito profesional. 

Audiencia objetivo: Profesionales con 2-5 años de experiencia en data science o ingeniería que buscan especialización senior.


Alinear contenido al perfil especificado en `programa.md`


# Instrucciones generales:

1. Estilo de redacción: 
- Personalmente no me gusta la palabra "empresarial". Mejor usar expresiones como "en industria", "en entornos profesionales", "en producción", "en sistemas de críticos", etc.
- Matener el uso de emoji al mínimo. 
-  Mantener la redacción impersonal y técnica: 
   - Incorrecto: "En este módulo aprenderás patrones de diseño avanzados para pipelines de datos"
   - Correcto: "Este módulo cubre patrones de diseño avanzados para pipelines de datos"
   - Incorrecto: "¿Has tenido que procesar un archivo tan grande que pandas crasheó por falta de memoria? ¿Cómo lo resolviste?"
   - Correcto: "¿Cómo manejar datasets cuyo tamaño excede la memoria disponible?"
- Términos técnicos: Mantener nombres originales en inglés
  - Correcto: "Azure Data Factory", "Machine Learning", "API REST"
  - Incorrecto: "Fábrica de Datos de Azure", "Aprendizaje Automático", "API REST"
  - Código y documentación técnica: Comentarios en español, variables y funciones en español también y usando solamente caracteres ASCII
La redacción debe ser impersonal, no dirigirse al estudiante directamente. Por ejemplo, en lugar de decir "en este módulo verás los siguientes", usar "en este módulo se cubrirán los siguientes temas".
Se debe procurar recalcar la relevancia en la industria de todo aprendizaje.
- Evitar frases como "aprenderás a", "te enseñaremos", "al finalizar este módulo serás capaz de", etc.
- Procurar usar palabras de género neutro como "profesional de datos", "integrantes del equipo", "el rol de data engineer", etc. Dentro de lo razonable para mantener fluidez y naturalidad en la redacción sin que sea una distracción.

2. Lineamientos de contenido:
- Cada título debería tener al menos un párrafo de motivación y explicación más a profundidad de lo que está por exponerse. Si se introduce una tecnología o patrón nuevo, debe haber una explicación clara de por qué es relevante, cómo y en qué contextos se usa
- Evitar el uso liberal de "spanglish". Tiene sentido únicamente cuando son palabras reservadas comunes como "print", o nombres de librerías. Verificar que el uso de inglés en este documento sea provechoso para un ambiente biligue, no solamente tirar palabras en inglés arbitrariamente.
- Debe escribir todo en español siempre.
- El tono debe ser académico pero accesible, como si fuera un profesor explicando a sus estudiantes.
- En cada sección debe haber una explicación completa y accesible de la *utilidad* de cada tecnología, patrón o práctica recomendada, enfocándose en el "por qué" y "cuándo" usarla en un entorno profesional. Cuando son versiones más sofsticadas de tecnologías o prácticas comunes, debe haber una comparación que explique claramente cuál es el beneficio de usar la versión avanzada.
- Los nombres de archivos deben usar solamente caracteres ASCII.
- Cuando se refieran a constructos matemáticos, mostrar la fórumla en formato LaTeX. y explicar cada componente de la fórmula.
- Cuando se presenten múltiples metodologías distintas con el mismo objetivo o con usos similares, explicar sus fortaliezas o dónde tiene más sentido usar una u otra.

3. Enfoque Temporal
- PROHIBIDO: Mencionar duraciones específicas, deadlines, o timelines
- PERMITIDO: Secuencias lógicas ("antes de", "después de", "prerequisito")

## Estructura del curso:
El curso debe organizarse en módulos, cada uno cubriendo una temática específica. 

## Proceso de construccion del curso
1. Primero se crea el archivo plan-moduloX.md con la estructura del módulo
2. Posterior a aprobación, se crea el contenido teórico en moduloX-contenido-teorico.md
3. Luego el laboratorio práctico en labX-nombre-del-lab.ipynb.
4. Luego un segundo notebook con una serie de ejercicios de evaluación de conocimiento. La idea es que este archivo sea el único entregable por parte de los estudiantes, y que a la vez les sirva como portafolio que mostrar en su github personal.
5. Y finalmente el guión narrativo en guion-moduloX.md


### Formato de plan-moduloX.md:
1. Información general: Descripción del tema, tecnologías utilizadas y objetivos de aprendizaje. No incluir nivel de dificultad ni prerrequisitos de conocimiento. Tampoco incluir el Proceso de Desarrollo del Módulo, eso es solamente para planificación interna.
2. Estructura de contenidos: Dividido en secciones con objetivos específicos, contenidos de la sección y casos de uso en industria. No debe haber ninguna otra sección.

### Formato de moduloX-contenido-teorico.md:
1. Introducción: Breve descripción del tema y su importancia en la industria como motivación del módulo.
2. Calibración de Conocimientos: Preguntas para autoevaluar conocimiento previo. 
3. Contenido Teórico: Explicación detallada de los conceptos, técnicas y herramientas, con ejemplos prácticos y casos de uso en la industria. Deben seguirse sin excepciones todos los lineamientos detallados en la sección "Instrucciones Generales". Dentro de la exposición teórica deben incluirse ejemplos claros y detallados que ilustren la aplicación de los conceptos teóricos en escenarios reales de la industria.
4. Evaluación de Entendimiento: Preguntas para validar el aprendizaje, en versiones de mayor profundidad y dificultad que la sección inicial, para así corroborar el aprendizaje. Es crucial que estas preguntas puedan ser respondidas exclusivamente con la información del módulo, y que sean balanceadas en la cantidad de preguntas por sección. Por ejemplo, no preguntar por qué se dice que SQL es un lenguaje declarativo si eso no se menciona en el módulo. Y en caso de que la pregunta no pueda ser respondida con la información del módulo, se debe valorar si es apropiado agregar dicha información al contenido del módulo.

### Formato de labX-nombre-del-lab.ipynb:
- Para los laboratorios, se debe procurar que los ejercicios sean prácticos y relevantes en la industria. Se deben evitar ejercicios que no tengan un caso de uso claro en el mundo real. Por ejemplo, en lugar de pedir "Escribe una consulta que devuelva todos los productos con precio mayor a 100", se puede plantear "Con el fin de entender el perfil de consumo de sus clientes, se requiere identificar productos premium en el catálogo, definidos como aquellos con precio mayor a 100, para una campaña de marketing dirigida a clientes de alto poder adquisitivo."
- Cada ejercicio debe tener un contexto claro y presentarse incompleto, de forma que el estudiante deba completarlo. Por ejemplo, en lugar de "Escribe una consulta que devuelva todos los productos con precio mayor a 100", se puede plantear "Se requiere identificar productos premium en el catálogo, definidos como aquellos con precio mayor a 100, para una campaña de marketing dirigida a clientes de alto poder adquisitivo. Completa la consulta SQL para obtener esta información."


### Sobre el guión
Deben ser una colección de archivos de aproximadamente 5 minutos de duración cada uno, que sigan exactamente el orden del contenido teórico del módulo. La idea es que el instructor pueda leer el guión directamente para grabar los videos del curso. 
