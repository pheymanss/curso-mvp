# Módulo 3: Métodos de Aprendizaje No Supervisado

## Introducción

El aprendizaje no supervisado representa uno de los pilares fundamentales del análisis de datos moderno en entornos profesionales. A diferencia del aprendizaje supervisado, donde cada observación viene acompañada de una etiqueta o valor objetivo, el aprendizaje no supervisado trabaja con datos sin clasificaciones previas, buscando descubrir estructura, patrones y relaciones inherentes en la información disponible.

Esta característica resulta especialmente relevante en la industria por varias razones. Primero, la gran mayoría de datos generados en organizaciones no vienen etiquetados: transacciones de clientes, logs de sistemas, datos de sensores, interacciones en plataformas digitales, entre otros. Etiquetar estos datos manualmente resulta costoso, lento y en muchos casos simplemente inviable debido al volumen. Segundo, el aprendizaje no supervisado permite descubrir patrones que no se habían considerado previamente, revelando estructuras naturales en los datos que pueden no ser obvias desde una perspectiva de negocio inicial.

Las técnicas de aprendizaje no supervisado se aplican extensivamente en múltiples contextos profesionales: segmentación de clientes para personalización de estrategias, compresión de datos de alta dimensionalidad para visualización y análisis, detección de anomalías en transacciones o comportamientos, organización automática de contenidos, y como paso exploratorio previo al desarrollo de modelos supervisados. En sistemas de producción, estas técnicas permiten procesar y extraer valor de grandes volúmenes de datos sin requerir intervención manual constante.

Este módulo cubre las técnicas fundamentales y avanzadas de aprendizaje no supervisado más utilizadas en la industria, desde algoritmos clásicos de clustering hasta métodos modernos de reducción de dimensionalidad. El enfoque está en comprender no solo el funcionamiento técnico de cada algoritmo, sino también cuándo y por qué utilizarlo en contextos profesionales, cómo interpretar sus resultados, y cómo traducir estos resultados en decisiones y acciones de negocio.

---

## Calibración de Conocimientos

Antes de comenzar con el contenido del módulo, es útil autoevaluar el nivel de familiaridad con los conceptos que se cubrirán. Las siguientes preguntas permiten identificar conocimientos previos y áreas que pueden requerir mayor atención.

### Pregunta 1
¿Cuál es la diferencia principal entre aprendizaje supervisado y no supervisado en términos de los datos disponibles?

<details>
<summary>Respuesta esperada</summary>

En aprendizaje supervisado, cada observación en el conjunto de datos incluye tanto las variables de entrada (features) como una variable objetivo conocida (etiqueta o valor a predecir). En aprendizaje no supervisado, solo se cuenta con las variables de entrada, sin etiquetas ni valores objetivo predefinidos. El objetivo es descubrir estructura o patrones en los datos sin guía externa.
</details>

### Pregunta 2
¿Qué significa "clustering" o agrupamiento de datos?

<details>
<summary>Respuesta esperada</summary>

Clustering es el proceso de agrupar observaciones en conjuntos (clusters) donde los elementos dentro de cada grupo son más similares entre sí que con elementos de otros grupos, según alguna métrica de similitud o distancia. Es una técnica fundamental de aprendizaje no supervisado para descubrir segmentos naturales en los datos.
</details>

### Pregunta 3
¿Por qué puede ser necesario reducir la dimensionalidad de un conjunto de datos?

<details>
<summary>Respuesta esperada</summary>

La reducción de dimensionalidad es necesaria por varias razones: facilitar la visualización de datos complejos (proyectándolos a 2D o 3D), acelerar el entrenamiento de modelos, reducir problemas de multicolinealidad, comprimir datos para almacenamiento eficiente, eliminar ruido o variables redundantes, y mejorar la interpretabilidad del análisis al trabajar con menos variables.
</details>

### Pregunta 4
¿Qué desafío principal presenta la evaluación de algoritmos de aprendizaje no supervisado comparado con algoritmos supervisados?

<details>
<summary>Respuesta esperada</summary>

En aprendizaje supervisado, se puede evaluar el desempeño comparando predicciones con valores reales conocidos mediante métricas objetivas (accuracy, RMSE, etc.). En aprendizaje no supervisado, no existe una "respuesta correcta" predefinida, por lo que la evaluación es más compleja y depende de métricas indirectas (cohesión interna, separación entre grupos) o de validación cualitativa de si los resultados son útiles para el objetivo de negocio.
</details>

### Pregunta 5
¿Qué es un centroide en el contexto de clustering?

<details>
<summary>Respuesta esperada</summary>

Un centroide es el punto representativo de un cluster, típicamente calculado como el promedio (centro de masa) de todas las observaciones asignadas a ese grupo. Representa el "perfil promedio" de los miembros del cluster y se utiliza tanto para asignar nuevas observaciones a grupos como para interpretar las características típicas de cada segmento.
</details>
