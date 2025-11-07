Este repositorio contiene todo el contenido de un curso para científicos de datos en el ámbito profesional. 

Audiencia objetivo: Profesionales con 2-5 años de experiencia en data science o ingeniería que buscan especialización senior.


Alinear contenido al perfil especificado en `programa.md`


# Instrucciones generales:

1. Estilo de redacción: 
- Personalmente no me gusta la palabra "empresarial". Mejor usar expresiones como "en industria", "en entornos profesionales", "en producción", "en sistemas de críticos", etc.
- Prohibido el uso de emoji al mínimo. 
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
1. Primero se crea el archivo plan-moduloX.md con la estructura del módulo.
2. Posterior a aprobación, se crea el contenido teórico en moduloX-contenido-teorico.md. Este archivo debe contener gráficos y visualizaciones relevantes para ilustrar conceptos cuando sea apropiado. Estos deben ser generados por código de python que se guarde en un archivo aparte llamado moduloX-graficos.py. No se deben usar imágenes de internet o generadas manualmente. Y estas imágenes generadas deben ser correctamente agregadas al repositorio y referenciadas en el archivo de contenido teórico.
3. Luego el laboratorio práctico en labX-nombre-del-lab.ipynb. Se deben generar todos los datasets necesarios mediante código en un archivo aparte llamado labX-generacion-datasets.py. Este archivo junto con moduloX-graficos.py deben estar adentro de la carpeta /data. No se deben usar datasets de internet o generados manualmente.
4. Luego un segundo notebook portafolio-nombre-del-lab.ipynb con una serie de ejercicios de evaluación de conocimiento. La idea es que este archivo sea el único entregable por parte de los estudiantes, y que a la vez les sirva como portafolio que mostrar en su github personal. En este notebook solamente deben estar los encabezados y descripciones de cada uno de los pasos, de manera que guíen al estudiante para generar su propio código. No debe haber código pre-escrito en este notebook. Esto no es una lista de ejercicios, es un reporte técnico incompleto que el estudiante debe llenar con su propio código y análisis. Los encabezados y descripciones deben ser lo suficientemente detallados para que el estudiante sepa exactamente qué se espera de él en cada sección pero no sonar como instrucciones, sino como detalles de un reporte técnico profesional.
5. Y finalmente el guión narrativo en guion-moduloX.md


### Formato de plan-moduloX.md:
1. Información general: Descripción del tema, tecnologías utilizadas y objetivos de aprendizaje. No incluir nivel de dificultad ni prerrequisitos de conocimiento. Tampoco incluir el Proceso de Desarrollo del Módulo, eso es solamente para planificación interna.
2. Estructura de contenidos: Dividido en secciones con objetivos específicos, contenidos de la sección y casos de uso en industria. No debe haber ninguna otra sección.

### Formato de moduloX-contenido-teorico.md:
1. Introducción: Breve descripción del tema y su importancia en la industria como motivación del módulo.
2. Calibración de Conocimientos: Preguntas para autoevaluar conocimiento previo. 
3. Contenido Teórico: Explicación detallada de los conceptos, técnicas y herramientas, con ejemplos prácticos y casos de uso en la industria. Deben seguirse sin excepciones todos los lineamientos detallados en la sección "Instrucciones Generales". Dentro de la exposición teórica deben incluirse ejemplos claros y detallados que ilustren la aplicación de los conceptos teóricos en escenarios reales de la industria.
4. Ejemplos de código: Fragmentos de código relevantes que ejemplifiquen los conceptos explicados, con comentarios claros y concisos. No deben ser reproducibles, sino mencionar las librerías y funciones usadas, y explicar su funcionamiento. No debe haber creación de datos ni nada, por ejemplo solo explicar cómo usar 

```python
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=3)
clusters = kmeans_model.fit_predict(df_kmeans)
```
Y luego explicar cómo usar el resultado:

```python
df_kmeans.insert(df_kmeans.columns.get_loc("Age"), "Cluster", clusters)
df_kmeans.head(3)
```
En general, todo el código principal que vaya a estar en el laboratorio práctico no debe estar en el contenido teórico, sino solamente fragmentos que ilustren conceptos específicos. Ya las versiones completas de código estarán en el laboratorio práctico.
Muy Importante: agregar siempre los imports necesarios en cada fragmento de código
5. Evaluación de Entendimiento: Preguntas para validar el aprendizaje, en versiones de mayor profundidad y dificultad que la sección inicial, para así corroborar el aprendizaje. Es crucial que estas preguntas puedan ser respondidas exclusivamente con la información del módulo, y que sean balanceadas en la cantidad de preguntas por sección. Por ejemplo, no preguntar por qué se dice que SQL es un lenguaje declarativo si eso no se menciona en el módulo. Y en caso de que la pregunta no pueda ser respondida con la información del módulo, se debe valorar si es apropiado agregar dicha información al contenido del módulo.
6. Sobre los gráficos: deben generarse previamente en moduloX-graficos.py y guardarse en una carpeta llamada graficos/ dentro del módulo. No se deben usar imágenes de internet o generadas manualmente. Los gráficos deben ser relevantes y generados en datos de relativo bajo volumen, asegurando que aporten valor a la explicación teórica. Deben crearse en funciones independientes y tanto las funciones como los archivos deben tener nombres claros y relevantes sobre lo que están ilustrando. En el documento md de los estudiantes deben tener "captions" que mencionen claramente qué están ilustrando y por qué es relevante para el tema tratado. Por ejemplo, "Figura 1: Distribución de frecuencias de compras mensuales en clientes premium, ilustrando el comportamiento de este segmento en comparación con otros perfiles de clientes."

### Formato de labX-nombre-del-lab.ipynb:
- Para los laboratorios, se debe procurar que los ejercicios sean prácticos y relevantes en la industria. Se deben evitar ejercicios que no tengan un caso de uso claro en el mundo real. Por ejemplo, en lugar de pedir "Escribe una consulta que devuelva todos los productos con precio mayor a 100", se puede plantear "Con el fin de entender el perfil de consumo de sus clientes, se requiere identificar productos premium en el catálogo, definidos como aquellos con precio mayor a 100, para una campaña de marketing dirigida a clientes de alto poder adquisitivo."
- Datasets: Para los laboratorios se usarán datasets generados por código, estas generaciones deben ser invisibles para el estudiante y deben ser generados previamente y guardados en el repositorio como archivos CSV. No se deben usar datasets de internet o generados manualmente. labX-generacion-datasets.py debe contener todo el código necesario para generar los datasets usados en labX-nombre-del-lab.ipynb, en funciones claras y ordenadas de acuerdo a su uso en el archivo de laboratorio. Los datos generados deben ser adecuados para ejemplificar la metodología correspondiente y tener un tamaño razonable para que los ejercicios puedan ser realizados en un entorno local sin requerir recursos computacionales excesivos. Estos archivos deben ser guardados en una carpeta llamada data/ dentro del módulo correspondiente. Los archivos deben tener nombres descriptivos y usar solamente caracteres ASCII, y ser de temas relevantes pero específicos para sentirse reales, no genéricos. Por ejemplo, en lugar de "datos_clientes.csv", usar "cartera_clientes_ecommerce.csv" y usar el tema de los datos en los ejercicios para mantener al estudiante interesado.
- Cada ejercicio debe tener un contexto claro y presentarse incompleto, de forma que el estudiante deba completarlo. Por ejemplo, en lugar de "Escribe una consulta que devuelva todos los productos con precio mayor a 100", se puede plantear "Se requiere identificar productos premium en el catálogo, definidos como aquellos con precio mayor a 100, para una campaña de marketing dirigida a clientes de alto poder adquisitivo. Completar la consulta SQL para obtener esta información."
- El texto previo a cada celda debe ser explicativo del valor del ejercicio, no solamente instrucciones de qué hacer.
- PROHIBIDO comentarios con # TODO.  


### Sobre el guión
Deben ser una colección de archivos de aproximadamente 5 minutos de duración cada uno, que sigan exactamente el orden del contenido teórico del módulo. La idea es que el instructor pueda leer el guión directamente para grabar los videos del curso. 
