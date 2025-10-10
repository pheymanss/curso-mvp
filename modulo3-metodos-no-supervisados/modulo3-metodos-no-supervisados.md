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

---

## 1. Fundamentos del Aprendizaje No Supervisado

### 1.1 ¿Por qué empezar con aprendizaje no supervisado?

En muchos programas de formación en ciencia de datos, el aprendizaje supervisado se presenta primero debido a su estructura más intuitiva: dado un conjunto de datos etiquetados, construir un modelo que prediga esas etiquetas. Sin embargo, en entornos profesionales, el aprendizaje no supervisado frecuentemente precede al supervisado en el flujo de trabajo analítico.

Esta secuencia tiene sentido por varias razones prácticas. Cuando se recibe un nuevo conjunto de datos en industria, rara vez se cuenta con etiquetas inmediatamente disponibles. Antes de invertir recursos en etiquetar datos (proceso costoso y que consume tiempo), resulta valioso explorar si existen patrones naturales en la información. El aprendizaje no supervisado permite esta exploración inicial: identificar si hay segmentos claros de clientes, detectar si ciertos productos se comportan de manera similar, o visualizar si existen grupos naturales en datos de alta dimensionalidad.

Además, los resultados de técnicas no supervisadas frecuentemente informan estrategias de aprendizaje supervisado posteriores. Por ejemplo, la segmentación de clientes mediante clustering puede revelar que diferentes grupos requieren modelos de predicción distintos. La reducción de dimensionalidad puede identificar qué variables contienen información redundante, simplificando modelos supervisados subsecuentes.

Finalmente, en muchas aplicaciones el objetivo no es predecir un valor específico, sino entender la estructura de los datos. Preguntas como "¿qué tipos de clientes tenemos?", "¿qué productos se venden de manera similar?", o "¿existen comportamientos anómalos en transacciones?" se responden naturalmente con técnicas no supervisadas.

### 1.2 Definición y características del aprendizaje no supervisado

El aprendizaje no supervisado engloba técnicas de machine learning que trabajan con conjuntos de datos $\mathbf{X} = \{x_1, x_2, ..., x_n\}$ donde cada observación $x_i \in \mathbb{R}^d$ es un vector de $d$ características, pero no se dispone de una variable objetivo $y$ asociada.

La ausencia de supervisión (etiquetas) significa que estos algoritmos deben inferir estructura basándose únicamente en las relaciones entre las observaciones. Esta estructura puede manifestarse de diferentes formas:

**Agrupamiento natural:** Algunas observaciones están más cerca entre sí que de otras, sugiriendo la existencia de grupos o clusters. Por ejemplo, clientes con patrones de compra similares tienden a agruparse naturalmente.

**Dimensionalidad reducida:** Variables que están correlacionadas entre sí pueden ser representadas por un número menor de dimensiones que capturan la mayor parte de la variación en los datos.

**Densidad variable:** Regiones del espacio de características donde las observaciones se concentran, versus regiones donde son escasas. Puntos en regiones de baja densidad pueden representar anomalías.

**Estructura jerárquica:** Relaciones de inclusión entre grupos, donde clusters grandes contienen sub-clusters más específicos.

### 1.3 Diferencias fundamentales con aprendizaje supervisado

Las diferencias entre aprendizaje supervisado y no supervisado van más allá de la presencia o ausencia de etiquetas. Estas diferencias impactan todo el flujo de trabajo analítico:

**Objetivo del análisis:**
- Supervisado: Predecir un valor específico (clasificación o regresión) para nuevas observaciones
- No supervisado: Descubrir patrones, estructura o representaciones alternativas de los datos

**Evaluación de resultados:**
- Supervisado: Métricas cuantitativas comparando predicciones con valores reales (accuracy, F1, RMSE)
- No supervisado: Métricas indirectas de calidad (cohesión, separación) y evaluación cualitativa de utilidad

**Interpretabilidad:**
- Supervisado: Interpretación centrada en cómo variables predicen el objetivo
- No supervisado: Interpretación centrada en qué caracteriza a cada grupo o componente descubierto

**Uso en producción:**
- Supervisado: Típicamente para automatizar decisiones o predicciones específicas
- No supervisado: Frecuentemente para exploración, segmentación, o preprocesamiento de datos

**Interacción humana:**
- Supervisado: Requiere expertos de dominio para etiquetar datos inicialmente
- No supervisado: Requiere expertos de dominio para interpretar y validar patrones descubiertos

Esta diferencia en interpretabilidad tiene implicaciones prácticas importantes. En aprendizaje supervisado, un modelo con 85% de accuracy tiene un significado claro. En clustering, sin embargo, una solución con 5 clusters no es objetivamente mejor o peor que una con 4 o 6 clusters; depende del contexto de negocio y de qué tan útiles resultan los segmentos identificados.

### 1.4 Tipos principales de problemas en aprendizaje no supervisado

El aprendizaje no supervisado abarca varios tipos de problemas, cada uno con objetivos y aplicaciones distintas:

#### Clustering (Agrupamiento)

El clustering busca particionar el conjunto de datos en grupos donde las observaciones dentro de cada grupo son similares entre sí, y diferentes de observaciones en otros grupos. Formalmente, dado un conjunto de datos $\mathbf{X} = \{x_1, ..., x_n\}$, el objetivo es encontrar una asignación $c: \{1,...,n\} \rightarrow \{1,...,k\}$ que asigne cada observación a uno de $k$ clusters.

**Aplicaciones en industria:**
- Segmentación de clientes por comportamiento de compra, uso de productos, o valor
- Agrupación de productos por patrones de venta o características
- Identificación de perfiles de uso en plataformas digitales
- Clasificación de documentos por similitud temática

#### Reducción de dimensionalidad

La reducción de dimensionalidad busca representar datos de alta dimensionalidad en un espacio de menor dimensión, preservando las características más importantes de los datos originales. Matemáticamente, se busca una transformación $f: \mathbb{R}^d \rightarrow \mathbb{R}^m$ donde $m < d$, tal que la representación en $\mathbb{R}^m$ retenga la mayor parte de la información relevante.

**Aplicaciones en industria:**
- Visualización de datos complejos en 2D o 3D
- Compresión de datos de sensores o imágenes
- Preprocesamiento para acelerar modelos de machine learning
- Identificación de factores latentes en datos de encuestas
- Detección de patrones en datos genómicos o biomédicos

#### Detección de anomalías

La detección de anomalías busca identificar observaciones que difieren significativamente del patrón general de los datos. Estas observaciones atípicas pueden representar errores, fraudes, fallas de equipos, o eventos raros de interés.

**Aplicaciones en industria:**
- Detección de fraude en transacciones financieras
- Identificación de fallas en sistemas industriales
- Detección de intrusiones en seguridad informática
- Identificación de comportamientos inusuales de usuarios
- Control de calidad en procesos de manufactura

#### Aprendizaje de asociaciones

El aprendizaje de asociaciones busca descubrir reglas que describen relaciones frecuentes entre variables en los datos. El ejemplo clásico es el análisis de canasta de mercado: ¿qué productos tienden a comprarse juntos?

**Aplicaciones en industria:**
- Sistemas de recomendación de productos
- Organización de inventarios y diseño de tiendas
- Identificación de patrones de comportamiento
- Análisis de secuencias de eventos

Este módulo se enfoca principalmente en clustering y reducción de dimensionalidad, que representan las técnicas de aprendizaje no supervisado más ampliamente utilizadas en entornos profesionales.

### 1.5 Desafíos particulares del aprendizaje no supervisado

El aprendizaje no supervisado presenta desafíos únicos que difieren significativamente de los encontrados en aprendizaje supervisado:

#### Ausencia de métricas de evaluación objetivas

En aprendizaje supervisado, métricas como accuracy o RMSE proporcionan evaluaciones objetivas del desempeño. En aprendizaje no supervisado, no existe una "respuesta correcta" contra la cual comparar. Esto lleva a varios problemas prácticos:

- **Métricas indirectas:** Se utilizan métricas como cohesión interna (qué tan similares son elementos dentro de un cluster) y separación externa (qué tan distintos son clusters entre sí), pero estas no garantizan utilidad práctica
- **Múltiples soluciones válidas:** Un mismo dataset puede tener varias particiones en clusters igualmente válidas desde una perspectiva matemática, pero con interpretaciones de negocio muy diferentes
- **Dependencia del contexto:** La calidad de una solución depende fuertemente del objetivo de negocio. Un clustering con 3 segmentos amplios puede ser perfecto para estrategia de marketing, pero insuficiente para personalización de productos

#### Interpretabilidad de resultados

Los resultados de algoritmos no supervisados requieren interpretación y validación humana:

- **Caracterización de clusters:** Identificar qué hace único a cada grupo requiere analizar estadísticas descriptivas de cada cluster y compararlas
- **Nomenclatura:** Los algoritmos producen "Cluster 1", "Cluster 2", etc. Asignar nombres significativos ("Clientes premium", "Compradores ocasionales") requiere conocimiento de dominio
- **Validación de utilidad:** Determinar si los patrones descubiertos son accionables desde una perspectiva de negocio

#### Sensibilidad a la escala y preprocesamiento

Muchos algoritmos de aprendizaje no supervisado son sensibles a la escala de las variables:

- **Distancias dominadas:** Variables con rangos grandes pueden dominar cálculos de distancia sobre variables con rangos pequeños, incluso si estas últimas son más relevantes
- **Estandarización necesaria:** Frecuentemente se requiere estandarizar variables (restar media, dividir por desviación estándar) antes de aplicar algoritmos
- **Outliers influyentes:** Valores atípicos pueden distorsionar resultados más severamente que en aprendizaje supervisado

#### Selección de hiperparámetros

Algoritmos de aprendizaje no supervisado requieren especificar hiperparámetros (número de clusters, número de componentes, parámetros de vecindad) sin una forma obvia de validación cruzada como en supervisado:

- **Validación heurística:** Métodos como el método del codo proporcionan guías, pero no respuestas definitivas
- **Exploración necesaria:** Típicamente se prueban múltiples valores de hiperparámetros y se comparan resultados cualitativamente
- **Trade-offs complejos:** Más clusters pueden capturar más detalle pero dificultar la interpretación; menos componentes simplifican visualización pero pierden información

### 1.6 Flujo de trabajo típico en proyectos no supervisados

A pesar de los desafíos, existe un flujo de trabajo generalizable para proyectos de aprendizaje no supervisado en industria:

**1. Definición del objetivo de negocio**
   - Clarificar qué se busca descubrir o lograr con el análisis
   - Identificar stakeholders y cómo utilizarán los resultados
   - Definir criterios de éxito (cualitativos si no hay métricas objetivas)

**2. Exploración y preprocesamiento de datos**
   - Análisis descriptivo de variables
   - Identificación y manejo de valores faltantes
   - Detección y tratamiento de outliers
   - Estandarización o normalización según el algoritmo a utilizar

**3. Selección de técnica y aplicación inicial**
   - Elegir algoritmo apropiado según objetivo (clustering, reducción de dimensionalidad)
   - Aplicar con parámetros por defecto o razonables
   - Evaluar resultados preliminares

**4. Exploración de hiperparámetros**
   - Probar diferentes configuraciones (número de clusters, componentes, etc.)
   - Utilizar métodos heurísticos (método del codo, coeficiente de silueta)
   - Comparar resultados cualitativamente

**5. Interpretación y caracterización**
   - Analizar características de cada cluster o componente
   - Asignar nombres o etiquetas interpretables
   - Visualizar resultados de forma comprensible para stakeholders

**6. Validación con expertos de dominio**
   - Presentar resultados a stakeholders
   - Validar si patrones descubiertos tienen sentido de negocio
   - Iterar según feedback

**7. Implementación y monitoreo**
   - Integrar resultados en procesos de negocio o sistemas
   - Monitorear estabilidad de segmentaciones o patrones en el tiempo
   - Re-entrenar periódicamente si los datos evolucionan

Este flujo es iterativo: frecuentemente se regresa a pasos anteriores basándose en hallazgos posteriores. La validación con expertos de dominio es especialmente crítica, ya que estos pueden identificar si los patrones descubiertos son artefactos de los datos o estructuras genuinas de valor.

### 1.7 Casos de uso representativos en industria

Para ilustrar la aplicabilidad práctica del aprendizaje no supervisado, consideremos casos de uso concretos en diferentes sectores:

#### Retail: Segmentación de clientes para marketing personalizado

Una cadena de retail cuenta con millones de transacciones de cientos de miles de clientes, pero sin clasificación previa de tipos de clientes. Mediante clustering sobre variables como frecuencia de compra, valor promedio de transacción, categorías preferidas, y estacionalidad, se identifican segmentos naturales: clientes de alto valor que compran frecuentemente, compradores estacionales que solo aparecen en ciertas temporadas, y clientes ocasionales de bajo valor.

Estos segmentos permiten personalizar campañas de marketing, ajustar ofertas, y optimizar inventarios por ubicación según el perfil predominante de clientes de cada tienda. Sin etiquetas previas, el análisis no supervisado reveló estructura útil que se traduce directamente en estrategias diferenciadas.

#### Manufactura: Detección de anomalías en datos de sensores

Una planta industrial monitorea equipos mediante sensores que registran temperatura, vibración, consumo eléctrico y otras variables cada minuto. Esto genera millones de observaciones multidimensionales. Aplicando técnicas de reducción de dimensionalidad y detección de outliers, se identifican patrones anómalos que preceden fallas de equipos.

El sistema no fue entrenado con ejemplos etiquetados de fallas (que son raros), sino que aprendió el comportamiento "normal" y detecta desviaciones significativas. Esto permite mantenimiento predictivo: intervenir antes de fallas costosas, basándose en patrones descubiertos automáticamente.

#### Finanzas: Visualización de portfolios de inversión

Un fondo de inversión maneja cientos de activos con múltiples variables de riesgo, retorno histórico, volatilidad, correlaciones, y métricas fundamentales. Visualizar este espacio multidimensional es imposible directamente. Mediante PCA o técnicas modernas como UMAP, se proyectan estos activos a 2D, revelando grupos de activos similares, identificando outliers (activos con características únicas), y facilitando la construcción de portfolios diversificados.

La reducción de dimensionalidad no busca predecir retornos, sino proporcionar una representación visual que facilite la toma de decisiones informadas sobre diversificación y exposición a riesgos.

#### Tecnología: Organización de contenidos sin categorías previas

Una plataforma de contenidos tiene miles de artículos, videos o productos, pero sin categorización manual. Aplicando clustering sobre características de contenido (palabras clave, metadatos, patrones de interacción de usuarios), se descubren agrupaciones naturales que permiten organizar el contenido automáticamente, mejorar sistemas de recomendación, y facilitar navegación de usuarios.

Esta categorización emerge de los datos sin requerir etiquetado manual costoso, y puede adaptarse dinámicamente conforme se agrega nuevo contenido.

---

## 2. Clustering con K-Means

### 2.1 Introducción y relevancia en industria

K-Means representa el algoritmo de clustering más ampliamente utilizado en entornos profesionales. Su popularidad se debe a una combinación de simplicidad conceptual, eficiencia computacional, y capacidad de escalar a millones de observaciones. En sistemas de producción, K-Means procesa regularmente datos de clientes, transacciones, sensores y comportamientos de usuarios para identificar segmentaciones accionables.

La fortaleza principal de K-Means radica en su velocidad. Donde algoritmos más sofisticados pueden requerir horas para procesar datasets grandes, K-Means frecuentemente converge en minutos. Esta eficiencia lo convierte en la primera opción para aplicaciones que requieren actualización frecuente de segmentaciones, como sistemas de personalización en tiempo real o análisis de comportamiento de usuarios en plataformas digitales.

Sin embargo, K-Means no es apropiado para todos los escenarios. Sus asunciones sobre la forma de los clusters (esféricos y de tamaños similares) y su sensibilidad a la inicialización y outliers requieren comprensión clara de cuándo utilizarlo y cuándo considerar alternativas. Esta sección desarrolla tanto los fundamentos matemáticos como las consideraciones prácticas para aplicar K-Means efectivamente en contextos profesionales.

### 2.2 Fundamentos matemáticos del algoritmo

K-Means busca particionar un conjunto de datos $\mathbf{X} = \{x_1, x_2, ..., x_n\}$ donde cada $x_i \in \mathbb{R}^d$ en $k$ clusters $C = \{C_1, C_2, ..., C_k\}$ minimizando la suma de distancias cuadradas dentro de cada cluster.

Formalmente, el objetivo es minimizar la función de costo:

$$J = \sum_{j=1}^{k} \sum_{x_i \in C_j} ||x_i - \mu_j||^2$$

donde:
- $J$ es la inercia o suma de cuadrados intra-cluster
- $k$ es el número de clusters especificado
- $C_j$ es el conjunto de observaciones asignadas al cluster $j$
- $\mu_j$ es el centroide del cluster $j$, calculado como $\mu_j = \frac{1}{|C_j|} \sum_{x_i \in C_j} x_i$
- $||x_i - \mu_j||^2$ es la distancia euclidiana al cuadrado entre la observación y el centroide

Esta función de costo tiene una interpretación intuitiva: se busca que las observaciones estén lo más cerca posible de los centroides de sus clusters respectivos. Cuanto menor sea $J$, más compactos y cohesivos son los clusters resultantes.

La distancia euclidiana al cuadrado entre dos puntos $x$ y $y$ en $\mathbb{R}^d$ se calcula como:

$$||x - y||^2 = \sum_{i=1}^{d} (x_i - y_i)^2$$

Esta métrica de distancia trata todas las dimensiones como igualmente importantes y asume que las variables están en escalas comparables, lo cual tiene implicaciones prácticas importantes que se discuten posteriormente.

### 2.3 El proceso iterativo de K-Means

K-Means es un algoritmo iterativo que alterna entre dos pasos hasta convergencia. El procedimiento completo es el siguiente:

#### Inicialización

Se seleccionan $k$ centroides iniciales $\mu_1, \mu_2, ..., \mu_k$. Existen varios métodos de inicialización:

**Inicialización aleatoria:** Seleccionar $k$ observaciones del dataset aleatoriamente como centroides iniciales. Este método es simple pero puede llevar a convergencia a óptimos locales subóptimos.

**K-Means++:** Método de inicialización inteligente que selecciona centroides iniciales espaciados entre sí. El primer centroide se elige aleatoriamente. Cada centroide subsecuente se elige con probabilidad proporcional a su distancia al cuadrado del centroide más cercano ya seleccionado. Este método típicamente resulta en mejor convergencia.

**Múltiples inicializaciones:** Ejecutar K-Means varias veces con diferentes inicializaciones aleatorias y seleccionar la solución con menor inercia. Scikit-learn utiliza 10 inicializaciones por defecto.

#### Paso de asignación

Para cada observación $x_i$, se calcula la distancia a cada centroide y se asigna al cluster del centroide más cercano:

$$c_i = \arg\min_{j \in \{1,...,k\}} ||x_i - \mu_j||^2$$

donde $c_i$ es la asignación de cluster para la observación $i$.

Este paso crea una partición del espacio en regiones de Voronoi, donde cada región contiene todos los puntos más cercanos a un centroide particular que a cualquier otro.

#### Paso de actualización

Se recalcula cada centroide como el promedio de todas las observaciones asignadas a ese cluster:

$$\mu_j = \frac{1}{|C_j|} \sum_{x_i \in C_j} x_i$$

Este paso mueve cada centroide al centro de masa de sus puntos asignados, minimizando la suma de distancias cuadradas dentro del cluster.

#### Convergencia

Los pasos de asignación y actualización se repiten hasta que se cumple un criterio de convergencia:

- Los centroides no cambian (o cambian menos que un umbral pequeño)
- Las asignaciones de cluster no cambian
- Se alcanza un número máximo de iteraciones

K-Means garantiza que la inercia $J$ nunca aumenta entre iteraciones, y típicamente converge rápidamente. En la práctica, la convergencia suele ocurrir en 10-20 iteraciones para la mayoría de datasets.

**Ejemplo ilustrativo del proceso iterativo:**

Consideremos una empresa de telecomunicaciones que desea segmentar clientes en 3 grupos basándose en dos variables: minutos de uso mensual y gasto mensual. Datos iniciales de 5 clientes:

| Cliente | Minutos | Gasto ($) |
|---------|---------|-----------|
| A | 200 | 45 |
| B | 500 | 85 |
| C | 150 | 35 |
| D | 600 | 95 |
| E | 180 | 40 |

**Iteración 0 (Inicialización):**  
Supongamos que K-Means++ selecciona: Cliente A (200, 45), Cliente B (500, 85), y Cliente C (150, 35) como centroides iniciales.

**Iteración 1 - Paso de asignación:**  
Cada cliente se asigna al centroide más cercano:
- Cliente A: distancia a sí mismo = 0 → Cluster 1
- Cliente B: distancia a sí mismo = 0 → Cluster 2  
- Cliente C: distancia a sí mismo = 0 → Cluster 3
- Cliente D: más cercano a B (distancia ~14.1) → Cluster 2
- Cliente E: más cercano a A (distancia ~7.1) → Cluster 1

**Iteración 1 - Paso de actualización:**  
Recalcular centroides como promedio de miembros:
- Cluster 1: centroide = ((200+180)/2, (45+40)/2) = (190, 42.5)
- Cluster 2: centroide = ((500+600)/2, (85+95)/2) = (550, 90)
- Cluster 3: centroide = (150, 35) [sin cambios, un solo miembro]

**Iteración 2 - Paso de asignación:**  
Reasignar con nuevos centroides... El proceso continúa hasta que las asignaciones se estabilizan.

En este ejemplo simplificado, podemos observar cómo:
- Los clusters se forman alrededor de patrones naturales (usuarios de alto uso vs bajo uso)
- Los centroides se mueven iterativamente hacia el "centro de masa" de sus miembros
- El algoritmo separa usuarios con patrones de consumo claramente diferentes

### 2.4 Distancia euclidiana y sensibilidad a la escala

La dependencia de K-Means en distancia euclidiana tiene implicaciones prácticas críticas. Consideremos un ejemplo de segmentación de clientes con dos variables:

- Ingreso anual: rango de 20,000 a 200,000 (rango de 180,000)
- Edad: rango de 18 a 70 (rango de 52)

Sin estandarización, la distancia euclidiana estará completamente dominada por la variable de ingreso, debido a su rango mucho mayor. Dos clientes con ingresos diferentes de $50,000 estarán "más lejos" que dos clientes con edades diferentes de 40 años, incluso si ambas diferencias son igualmente significativas desde una perspectiva de negocio.

**Ejemplo numérico del impacto de la escala:**

Consideremos dos clientes de un banco:

| Variable | Cliente 1 | Cliente 2 | Diferencia |
|----------|-----------|-----------|------------|
| Edad | 25 años | 55 años | 30 años |
| Ingreso anual | $50,000 | $52,000 | $2,000 |

Sin estandarización, la distancia euclidiana es:
$$d = \sqrt{(25-55)^2 + (50000-52000)^2} = \sqrt{900 + 4,000,000} \approx 2000$$

La diferencia de ingreso ($2,000) domina completamente la distancia, mientras que la diferencia sustancial de edad (30 años) es prácticamente ignorada. Si el objetivo de negocio es segmentar clientes por perfil de vida (donde edad es crítica), este resultado es problemático.

Después de estandarización z-score (asumiendo edad: media=40, std=15; ingreso: media=60000, std=25000):
- Cliente 1: edad_z = (25-40)/15 = -1.0, ingreso_z = (50000-60000)/25000 = -0.4
- Cliente 2: edad_z = (55-40)/15 = 1.0, ingreso_z = (52000-60000)/25000 = -0.32

$$d_{estandarizado} = \sqrt{(-1.0-1.0)^2 + (-0.4-(-0.32))^2} = \sqrt{4.0 + 0.0064} \approx 2.0$$

Ahora ambas variables contribuyen significativamente a la distancia, y la diferencia de edad tiene el peso apropiado según su variabilidad en la población.

#### Estandarización de variables

Para mitigar este problema, las variables típicamente se estandarizan antes de aplicar K-Means. La estandarización más común es z-score:

$$z_i = \frac{x_i - \bar{x}}{\sigma_x}$$

donde:
- $z_i$ es el valor estandarizado
- $x_i$ es el valor original
- $\bar{x}$ es la media de la variable
- $\sigma_x$ es la desviación estándar de la variable

Después de estandarización, todas las variables tienen media 0 y desviación estándar 1, poniéndolas en la misma escala y permitiendo que contribuyan equitativamente al cálculo de distancias.

Alternativamente, normalización min-max escala variables a un rango específico (típicamente [0,1]):

$$x'_i = \frac{x_i - \min(x)}{\max(x) - \min(x)}$$

La elección entre estandarización y normalización depende del contexto. Estandarización es preferible cuando las variables tienen distribuciones aproximadamente normales y puede manejar outliers mejor. Normalización es útil cuando se requiere un rango específico o cuando todas las variables deben tener el mismo rango exacto.

#### Variables categóricas

K-Means, al depender de distancias euclidianas, está diseñado para variables numéricas continuas. Variables categóricas requieren tratamiento especial:

**One-hot encoding:** Convertir cada categoría en una variable binaria. Por ejemplo, "color" con valores {rojo, azul, verde} se convierte en tres variables binarias: es_rojo, es_azul, es_verde.

**Cuidado con alta dimensionalidad:** One-hot encoding puede crear muchas variables, especialmente con categorías de alta cardinalidad. Esto puede diluir la importancia de otras variables numéricas.

**Alternativas:** Para datasets con muchas variables categóricas, algoritmos como K-Modes (variante de K-Means para datos categóricos) pueden ser más apropiados.

### 2.5 Selección del número óptimo de clusters

Una de las decisiones más críticas al aplicar K-Means es especificar $k$, el número de clusters. A diferencia de aprendizaje supervisado donde el número de clases está predefinido, en clustering no existe una respuesta única correcta. El $k$ óptimo depende del objetivo de negocio, la estructura inherente de los datos, y consideraciones prácticas de implementación.

Existen varios métodos para guiar la selección de $k$:

#### Método del codo (Elbow Method)

El método del codo consiste en ejecutar K-Means para diferentes valores de $k$ y graficar la inercia (suma de cuadrados intra-cluster) contra $k$.

A medida que $k$ aumenta, la inercia siempre disminuye: más clusters permiten que las observaciones estén más cerca de sus centroides. Sin embargo, la tasa de disminución cambia. El "codo" es el punto donde la reducción marginal en inercia comienza a aplanarse, sugiriendo que agregar más clusters no aporta mejora sustancial.

**Interpretación:** El codo sugiere un balance entre ajuste (inercia baja) y parsimonia (pocos clusters). Sin embargo, el codo no siempre es obvio; en algunos datasets la curva disminuye suavemente sin un punto de inflexión claro.

**Ejemplo de uso:**
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Calcular inercia para diferentes valores de k
inercias = []
rango_k = range(1, 11)

for k in rango_k:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(datos)
    inercias.append(kmeans.inertia_)

# Graficar metodo del codo
plt.figure(figsize=(10, 6))
plt.plot(rango_k, inercias, marker='o')
plt.xlabel('Numero de clusters (k)')
plt.ylabel('Inercia')
plt.title('Metodo del Codo')
plt.grid(True)
plt.show()
```

#### Coeficiente de silueta

El coeficiente de silueta mide qué tan bien cada observación encaja en su cluster asignado comparado con otros clusters. Para cada observación $i$:

$$s_i = \frac{b_i - a_i}{\max(a_i, b_i)}$$

donde:
- $a_i$ es la distancia promedio entre $i$ y todas las otras observaciones en su mismo cluster (cohesión intra-cluster)
- $b_i$ es la distancia promedio entre $i$ y todas las observaciones en el cluster más cercano del cual $i$ no es miembro (separación inter-cluster)

El coeficiente de silueta varía entre -1 y 1:
- Valores cercanos a 1: observación está bien asignada, lejos de clusters vecinos
- Valores cercanos a 0: observación está en el borde entre dos clusters
- Valores negativos: observación probablemente está mal asignada

El coeficiente de silueta promedio sobre todas las observaciones proporciona una métrica de la calidad global del clustering. Se pueden comparar diferentes valores de $k$ seleccionando el que maximiza el coeficiente promedio.

**Ventaja sobre el método del codo:** El coeficiente de silueta considera tanto cohesión intra-cluster como separación inter-cluster, proporcionando una métrica más balanceada de calidad.

**Limitación:** Computacionalmente más costoso que calcular inercia, especialmente para datasets grandes, ya que requiere calcular distancias entre todas las observaciones.

**Ejemplo de uso:**
```python
from sklearn.metrics import silhouette_score

# Calcular coeficiente de silueta para diferentes valores de k
siluetas = []
rango_k = range(2, 11)  # Silueta requiere al menos 2 clusters

for k in rango_k:
    kmeans = KMeans(n_clusters=k, random_state=42)
    etiquetas = kmeans.fit_predict(datos)
    silueta = silhouette_score(datos, etiquetas)
    siluetas.append(silueta)

# Graficar coeficientes de silueta
plt.figure(figsize=(10, 6))
plt.plot(rango_k, siluetas, marker='o')
plt.xlabel('Numero de clusters (k)')
plt.ylabel('Coeficiente de Silueta')
plt.title('Coeficiente de Silueta vs k')
plt.grid(True)
plt.show()
```

#### Consideraciones de negocio

Más allá de métricas estadísticas, la selección de $k$ debe considerar restricciones y objetivos prácticos:

**Capacidad de implementación:** ¿Puede la organización manejar estrategias diferenciadas para $k$ segmentos? Segmentar clientes en 20 grupos puede ser óptimo estadísticamente, pero si marketing solo puede manejar 3-4 campañas distintas, más segmentos no son útiles.

**Interpretabilidad:** Clusters deben ser interpretables y diferenciables. Si dos clusters son muy similares en términos de negocio, pueden combinarse incluso si métricas sugieren mantenerlos separados.

**Estabilidad:** Evaluar si los clusters son estables al agregar nuevos datos o con pequeñas perturbaciones. Segmentaciones que cambian drásticamente con datos nuevos son difíciles de operacionalizar.

**Conocimiento de dominio:** Expertos del negocio pueden tener hipótesis sobre cuántos segmentos existen. Por ejemplo, en retail puede haber comprensión de que existen aproximadamente 5 tipos de compradores basándose en experiencia previa.

**Ejemplo práctico de selección de k:**

Una empresa de e-commerce analiza 10,000 clientes con variables: frecuencia de compra, valor promedio de transacción, días desde última compra, y diversidad de categorías compradas.

Aplicando el método del codo:
- k=2: inercia = 125,000
- k=3: inercia = 85,000 (reducción de 40,000)
- k=4: inercia = 65,000 (reducción de 20,000)
- k=5: inercia = 55,000 (reducción de 10,000)
- k=6: inercia = 50,000 (reducción de 5,000)

El "codo" aparece en k=4-5, sugiriendo que agregar más clusters después de 5 aporta poco beneficio marginal.

Coeficiente de silueta:
- k=3: 0.52
- k=4: 0.58
- k=5: 0.61 (máximo)
- k=6: 0.57

La silueta sugiere k=5 como óptimo.

Consideración de negocio: El equipo de marketing puede diseñar y ejecutar efectivamente 5 campañas diferenciadas (una por segmento). Con k=8, la complejidad operativa superaría los beneficios de granularidad adicional.

**Decisión final:** k=5, validada tanto por métricas estadísticas como por capacidad organizacional de actuar sobre los segmentos.

En la práctica, la selección final de $k$ frecuentemente involucra explorar múltiples valores guiados por el método del codo y coeficiente de silueta, y luego validar con stakeholders cuál resulta más útil y accionable.

### 2.6 Interpretación de centroides y perfiles de clusters

Una vez ejecutado K-Means, el resultado son asignaciones de cluster para cada observación y las coordenadas de los centroides. La interpretación de estos resultados es crítica para extraer insights accionables.

#### Análisis de centroides

Cada centroide $\mu_j$ representa el "perfil promedio" del cluster $j$. Para datos estandarizados, las coordenadas del centroide indican cuántas desviaciones estándar por encima o debajo de la media se encuentra el cluster en cada variable.

**Ejemplo de interpretación:**  
En segmentación de clientes con variables estandarizadas {frecuencia_compra, valor_promedio, antiguedad}:

- Cluster 1: $\mu_1 = [2.1, 1.8, 1.5]$ → Clientes de alta frecuencia, alto valor, antiguos
- Cluster 2: $\mu_2 = [-0.9, -1.2, 2.0]$ → Clientes de baja frecuencia, bajo valor, pero muy antiguos
- Cluster 3: $\mu_3 = [0.5, -0.3, -1.8]$ → Clientes de frecuencia media, valor medio, recién llegados

Estos perfiles numéricos se traducen en descripciones de negocio: "clientes premium leales", "clientes dormidos de larga data", "clientes nuevos en exploración".

**Ejemplo detallado de interpretación de centroides:**

Una compañía de seguros segmenta clientes en 4 grupos basándose en: edad, número de pólizas, prima total anual, y años como cliente. Después de estandarización y aplicación de K-Means, los centroides son:

| Cluster | Edad (z) | Num Pólizas (z) | Prima (z) | Antigüedad (z) |
|---------|----------|-----------------|-----------|----------------|
| 0 | -1.2 | -0.8 | -0.9 | -1.5 |
| 1 | 0.8 | 1.5 | 1.8 | 1.2 |
| 2 | 1.5 | 0.3 | 0.5 | 2.1 |
| 3 | -0.5 | 0.2 | -0.3 | 0.1 |

**Interpretación por cluster:**

**Cluster 0** (valores negativos en todas las dimensiones):
- Clientes jóvenes (-1.2 std), con pocas pólizas (-0.8 std), primas bajas (-0.9 std), y recién llegados (-1.5 std)
- **Perfil de negocio:** "Clientes nuevos en desarrollo" - oportunidad de crecimiento mediante cross-selling
- **Estrategia:** Ofertas de entrada atractivas, educación sobre productos adicionales

**Cluster 1** (valores positivos altos):
- Clientes de edad media-alta (0.8 std), muchas pólizas (1.5 std), primas altas (1.8 std), antiguos (1.2 std)
- **Perfil de negocio:** "Clientes premium establecidos" - alto valor de vida del cliente
- **Estrategia:** Retención prioritaria, servicio VIP, ofertas de productos especializados

**Cluster 2** (antigüedad muy alta, otras variables moderadas):
- Clientes mayores (1.5 std), pólizas moderadas (0.3 std), prima media (0.5 std), muy antiguos (2.1 std)
- **Perfil de negocio:** "Clientes leales de valor medio" - larga relación pero sin expansión reciente
- **Estrategia:** Reconocimiento de lealtad, revisar necesidades cambiantes por edad

**Cluster 3** (todos valores cercanos a cero):
- Perfiles cercanos al promedio en todas las dimensiones
- **Perfil de negocio:** "Clientes estándar" - segmento masivo sin características distintivas
- **Estrategia:** Comunicación estándar, optimización de eficiencia operativa

Para validar estas interpretaciones, se analizan las estadísticas originales (no estandarizadas):
- Cluster 0: edad promedio 28 años, 1.2 pólizas, $800/año, 0.5 años antigüedad
- Cluster 1: edad promedio 52 años, 4.1 pólizas, $3,200/año, 12 años antigüedad
- Cluster 2: edad promedio 65 años, 2.3 pólizas, $1,500/año, 25 años antigüedad
- Cluster 3: edad promedio 42 años, 2.1 pólizas, $1,200/año, 5 años antigüedad

#### Visualización de centroides

Para facilitar interpretación, especialmente con múltiples variables, los centroides pueden visualizarse como gráficos de radar o barras:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con centroides
nombres_variables = ['frecuencia', 'valor', 'antiguedad', 'diversidad']
centroides_df = pd.DataFrame(
    kmeans.cluster_centers_,
    columns=nombres_variables
)

# Grafico de barras de centroides
fig, axes = plt.subplots(1, k, figsize=(15, 4))
for i, ax in enumerate(axes):
    centroides_df.iloc[i].plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {i}')
    ax.set_ylabel('Valor estandarizado')
    ax.axhline(0, color='black', linewidth=0.8)
plt.tight_layout()
plt.show()
```

#### Caracterización estadística de clusters

Más allá de centroides, analizar estadísticas descriptivas de cada cluster en las variables originales (no estandarizadas) proporciona comprensión más intuitiva:

```python
# Asignar etiquetas de cluster al DataFrame original
datos_originales['cluster'] = kmeans.labels_

# Estadisticas descriptivas por cluster
for cluster_id in range(k):
    print(f"\n=== Cluster {cluster_id} ===")
    cluster_data = datos_originales[datos_originales['cluster'] == cluster_id]
    print(f"Tamaño: {len(cluster_data)} observaciones")
    print(cluster_data.describe())
```

Este análisis revela no solo promedios sino también dispersión (desviación estándar), rangos, y distribuciones dentro de cada cluster, proporcionando comprensión más rica de cada segmento.

#### Nomenclatura de clusters

Los algoritmos producen etiquetas genéricas (Cluster 0, Cluster 1, etc.). Asignar nombres descriptivos basándose en características distintivas facilita comunicación y uso práctico:

- Cluster 0 → "Clientes VIP": alta frecuencia, alto valor, alta antigüedad
- Cluster 1 → "Compradores ocasionales": baja frecuencia, bajo valor
- Cluster 2 → "Clientes en crecimiento": frecuencia creciente, valor medio
- Cluster 3 → "Dormidos": antiguos pero sin actividad reciente

Esta nomenclatura requiere colaboración con stakeholders que entienden el contexto de negocio y pueden validar si las caracterizaciones tienen sentido.

### 2.7 Limitaciones y consideraciones prácticas

A pesar de su popularidad, K-Means tiene limitaciones importantes que deben considerarse:

#### Sensibilidad a la inicialización

K-Means puede converger a óptimos locales dependiendo de la inicialización. Dos ejecuciones con diferentes inicializaciones aleatorias pueden producir resultados distintos. La solución estándar es ejecutar múltiples veces y seleccionar la mejor solución según inercia.

#### Asunción de clusters esféricos

K-Means asume clusters de forma aproximadamente esférica (circular en 2D) y tamaños similares. Para datos con clusters de formas alargadas, anillos concéntricos, o densidades muy diferentes, K-Means puede fallar en identificar estructura correctamente.

**Cuándo K-Means falla:**
- Clusters en forma de media luna o anillos
- Clusters con densidades muy diferentes
- Clusters de tamaños extremadamente desiguales

**Alternativas:** DBSCAN (clustering basado en densidad), clustering jerárquico, o Gaussian Mixture Models pueden manejar mejor formas arbitrarias.

#### Sensibilidad a outliers

Outliers extremos pueden distorsionar centroides significativamente. Un solo punto muy alejado puede "atraer" un centroide hacia él, afectando la asignación de otros puntos.

**Mitigación:**
- Detectar y remover outliers antes de clustering
- Usar variantes robustas como K-Medians (usa mediana en lugar de media)
- Considerar algoritmos robustos a outliers como DBSCAN

#### Requiere especificar k a priori

A diferencia de algoritmos que descubren el número de clusters automáticamente (como DBSCAN o clustering jerárquico), K-Means requiere especificar $k$ de antemano. Esto requiere exploración iterativa y validación.

#### Escalabilidad a alta dimensionalidad

En espacios de alta dimensionalidad (muchas variables), distancias euclidianas pueden volverse menos significativas (fenómeno conocido como "maldición de dimensionalidad"). Puntos tienden a estar aproximadamente equidistantes entre sí, haciendo que K-Means sea menos efectivo.

**Mitigación:**
- Reducción de dimensionalidad previa (PCA) antes de clustering
- Selección de variables relevantes
- Considerar métricas de distancia alternativas

### 2.8 Implementación en Scikit-learn

Scikit-learn proporciona una implementación eficiente y bien documentada de K-Means:

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Preparacion de datos
# Asumiendo 'datos' es un DataFrame con variables numericas
scaler = StandardScaler()
datos_escalados = scaler.fit_transform(datos)

# Aplicar K-Means
kmeans = KMeans(
    n_clusters=5,           # numero de clusters
    init='k-means++',       # metodo de inicializacion
    n_init=10,              # numero de inicializaciones
    max_iter=300,           # maximo de iteraciones
    random_state=42         # reproducibilidad
)

# Entrenar y predecir
etiquetas = kmeans.fit_predict(datos_escalados)

# Acceder a resultados
centroides = kmeans.cluster_centers_  # coordenadas de centroides
inercia = kmeans.inertia_             # suma de cuadrados intra-cluster

# Agregar etiquetas a datos originales
datos['cluster'] = etiquetas
```

**Parámetros importantes:**

- `n_clusters`: Número de clusters a formar
- `init`: Método de inicialización ('k-means++' recomendado, 'random' para aleatorio)
- `n_init`: Número de veces que se ejecuta con diferentes inicializaciones
- `max_iter`: Número máximo de iteraciones en cada ejecución
- `random_state`: Semilla para reproducibilidad

### 2.9 Casos de uso detallados en industria

#### Retail: Segmentación RFM de clientes

Una cadena de retail implementa segmentación RFM (Recency, Frequency, Monetary) usando K-Means sobre tres variables:

- **Recency:** días desde última compra
- **Frequency:** número de transacciones en último año
- **Monetary:** valor total gastado en último año

K-Means identifica 5 segmentos:

1. **Clientes VIP** (8% de base): alta frecuencia, alto valor, recency baja → estrategia de retención y programa de lealtad premium
2. **Clientes prometedores** (15%): frecuencia creciente, valor medio → estrategia de desarrollo con ofertas graduales
3. **Compradores ocasionales** (40%): baja frecuencia, bajo valor → estrategia de activación con promociones
4. **En riesgo** (22%): solían ser frecuentes pero recency alta → estrategia de reactivación urgente
5. **Perdidos** (15%): alta recency, baja frecuencia reciente → campaña de reconquista o exclusión de campañas costosas

Esta segmentación permite personalizar comunicación, asignar recursos de marketing eficientemente, y medir ROI por segmento.

#### Manufactura: Agrupación de perfiles de sensores

Una planta industrial monitorea máquinas mediante sensores que registran temperatura, vibración, consumo eléctrico, y presión cada minuto. En lugar de analizar cada variable independientemente, K-Means agrupa minutos con perfiles de sensor similares.

Los clusters identificados corresponden a:

- Operación normal en diferentes modos (carga alta, media, baja)
- Estados de calentamiento/enfriamiento
- Patrones anómalos que preceden fallas

El sistema clasifica nuevos datos en tiempo real, alertando cuando aparecen patrones consistentes con estados pre-falla, permitiendo mantenimiento predictivo.

#### Finanzas: Agrupación de activos para construcción de portfolios

Un fondo de inversión utiliza K-Means sobre métricas de activos (volatilidad, correlación con índices, beta, ratios fundamentales) para identificar grupos de activos con comportamiento similar.

Los clusters resultantes permiten:

- Diversificación informada seleccionando activos de diferentes clusters
- Identificación de activos representativos de cada cluster para portfolios simplificados
- Detección de activos mal valuados comparando con el promedio de su cluster

Esta aplicación muestra cómo K-Means facilita decisiones complejas reduciendo cientos de activos a un número manejable de grupos representativos.

---

## 3. Clustering Jerárquico

### 3.1 Motivación y comparación con K-Means

Mientras K-Means particiona datos en un número fijo de clusters especificado a priori, el clustering jerárquico construye una jerarquía completa de agrupaciones que puede explorarse a múltiples niveles de granularidad. Esta diferencia fundamental tiene implicaciones importantes para aplicaciones en industria.

La ventaja principal del clustering jerárquico radica en su flexibilidad. No requiere especificar el número de clusters de antemano; en su lugar, produce un árbol de agrupaciones (dendrograma) que representa relaciones jerárquicas entre observaciones y grupos. Este árbol puede "cortarse" a diferentes alturas para obtener distintos números de clusters, permitiendo explorar segmentaciones desde muy granulares hasta muy agregadas sin re-ejecutar el algoritmo.

Esta característica resulta especialmente valiosa en escenarios donde:

- No existe conocimiento previo claro sobre cuántos segmentos existen
- Interesa entender relaciones jerárquicas naturales (por ejemplo, categorías y subcategorías de productos)
- Se requiere flexibilidad para presentar resultados a diferentes niveles de detalle según la audiencia
- La estructura de los datos sugiere jerarquías naturales (taxonomías, organizaciones, clasificaciones biológicas)

Sin embargo, el clustering jerárquico tiene trade-offs significativos:

**Ventajas sobre K-Means:**
- No requiere especificar número de clusters a priori
- Produce visualización intuitiva de jerarquías (dendrograma)
- Más flexible para capturar clusters de formas no esféricas (dependiendo del método de enlace)
- Determinístico: mismos datos producen siempre el mismo resultado

**Desventajas comparado con K-Means:**
- Menor escalabilidad: complejidad típica O(n²) o O(n³) versus O(nkti) de K-Means
- Mayor uso de memoria: requiere almacenar matriz de distancias
- Decisiones de agrupamiento no pueden revertirse (una vez dos puntos se agrupan, permanecen juntos)
- Sensibilidad al método de enlace elegido

En la práctica, K-Means es preferible para datasets grandes (millones de observaciones) donde se requiere velocidad, mientras clustering jerárquico es más apropiado para datasets medianos (miles de observaciones) donde se valora exploración jerárquica y no se requiere actualización frecuente.

### 3.2 Fundamentos del clustering jerárquico aglomerativo

El clustering jerárquico tiene dos enfoques principales: aglomerativo (bottom-up) y divisivo (top-down). El enfoque aglomerativo es más común en la práctica y es el que implementan la mayoría de bibliotecas, incluyendo Scikit-learn.

#### Algoritmo aglomerativo

El algoritmo aglomerativo comienza tratando cada observación como un cluster individual y sucesivamente fusiona los dos clusters más similares hasta que todas las observaciones están en un solo cluster. El proceso es el siguiente:

**Paso 1: Inicialización**
- Comenzar con $n$ clusters, cada uno conteniendo una sola observación
- Calcular matriz de distancias o similitudes entre todos los pares de observaciones

**Paso 2: Iteración**
- Identificar el par de clusters más similares (menor distancia)
- Fusionar estos dos clusters en uno nuevo
- Actualizar matriz de distancias calculando distancias entre el nuevo cluster y todos los demás

**Paso 3: Terminación**
- Repetir Paso 2 hasta que quede un solo cluster conteniendo todas las observaciones

Este proceso produce una secuencia de fusiones que se representa como un dendrograma, donde la altura de cada fusión indica la distancia entre los clusters fusionados.

#### Métodos aglomerativos versus divisivos

**Aglomerativo (bottom-up):**
- Comienza con clusters pequeños (observaciones individuales) y los fusiona progresivamente
- Más común en implementaciones prácticas
- Computacionalmente manejable para datasets medianos
- Produce historia completa de fusiones

**Divisivo (top-down):**
- Comienza con todas las observaciones en un cluster y divide recursivamente
- Menos común debido a mayor complejidad computacional
- En cada paso debe decidir cómo dividir un cluster, lo cual puede ser costoso
- Puede ser preferible cuando se espera que existan pocos clusters grandes bien separados

La mayoría de aplicaciones en industria utilizan clustering aglomerativo por su simplicidad conceptual y disponibilidad en bibliotecas estándar.

### 3.3 Dendrogramas: construcción e interpretación

El dendrograma es la representación visual característica del clustering jerárquico. Es un diagrama en forma de árbol que muestra las fusiones sucesivas de clusters.

#### Estructura del dendrograma

En un dendrograma:

- El **eje horizontal** representa observaciones individuales (en la base) o clusters (en niveles superiores)
- El **eje vertical** representa la distancia o disimilitud en la cual clusters se fusionan
- Cada **unión en forma de U** representa la fusión de dos clusters
- La **altura de la U** indica la distancia entre los clusters fusionados

**Interpretación de altura:** Cuanto mayor sea la altura de una fusión, más diferentes son los clusters que se están combinando. Fusiones a alturas bajas indican clusters muy similares; fusiones a alturas altas indican clusters bien separados.

#### Lectura del dendrograma

Para determinar clusters a partir del dendrograma:

1. Seleccionar una altura de corte (threshold)
2. Trazar una línea horizontal a esa altura
3. Cada rama vertical que cruza esta línea representa un cluster

Por ejemplo, si el dendrograma muestra que las fusiones principales ocurren a alturas 10, 8, 5, y 2, cortar a altura 6 produciría los clusters que existían antes de las fusiones a alturas 8 y 10.

**Ejemplo práctico de lectura de dendrograma:**

Una cadena de restaurantes analiza sus 12 sucursales basándose en ventas mensuales, ticket promedio, y tráfico de clientes. El dendrograma resultante muestra:

```
Altura 15 |        ┌────────────────┐
          |        │                │
Altura 12 |    ┌───┴───┐        ┌───┴───┐
          |    │       │        │       │
Altura 8  |  ┌─┴─┐   ┌─┴─┐    ┌─┴─┐   ┌─┴─┐
          |  │   │   │   │    │   │   │   │
Altura 3  | ┌┴┐ ┌┴┐ ┌┴┐ ┌┴┐  ┌┴┐ ┌┴┐ ┌┴┐ ┌┴┐
          | A B C D E F G H  I J K L
```

**Análisis del dendrograma:**

**Corte a altura 15:** Resulta en 1 cluster (todas las sucursales juntas) - demasiado agregado, sin utilidad práctica.

**Corte a altura 12:** Resulta en 2 clusters grandes:
- Cluster 1: Sucursales A-H
- Cluster 2: Sucursales I-L
- Interpretación exploratoria: Revela dos tipos fundamentalmente diferentes de sucursales. Al analizar los datos, se descubre que I-L son ubicaciones premium con alto ticket promedio, mientras A-H son ubicaciones estándar.

**Corte a altura 8:** Resulta en 4 clusters:
- Cluster 1: A-B (fusión a altura 3)
- Cluster 2: C-D (fusión a altura 3)
- Cluster 3: E-H (fusiones a alturas 3 y 8)
- Cluster 4: I-L (fusiones a alturas 3 y 8)
- Interpretación: Dentro de ubicaciones estándar, se distinguen sucursales de alto volumen-bajo ticket (A-B) vs bajo volumen-ticket medio (C-D). Dentro de premium, se distinguen flagship stores (I-J) vs boutique locations (K-L).

**Corte a altura 3:** Resulta en 6 clusters (pares de sucursales muy similares).

**Decisión de negocio:** Gerencia opta por el corte a altura 8 (4 clusters) porque:
- Captura diferenciación estratégica (premium vs estándar)
- Permite estrategias operativas distintas por sub-segmento
- No es tan granular que dificulte implementación
- El salto de altura 8 a 12 es significativo, indicando que fusionar clusters a esa altura combinaría segmentos genuinamente diferentes

#### Identificación del número óptimo de clusters

El dendrograma proporciona guía visual para seleccionar el número de clusters:

**Buscar saltos grandes en altura:** Si hay una fusión que ocurre a una altura significativamente mayor que las fusiones previas, esto sugiere que clusters bien separados se están combinando. Cortar justo antes de esta fusión grande preserva la estructura natural de los datos.

**Ejemplo:** Si fusiones ocurren a alturas [1.2, 1.5, 1.8, 2.1, 7.5, 8.2], el salto de 2.1 a 7.5 sugiere que cortar antes de 7.5 (resultando en el número de clusters que existía antes de esa fusión) puede ser apropiado.

#### Implementación en Python

```python
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Calcular linkage usando metodo de Ward
Z = linkage(datos_escalados, method='ward')

# Crear dendrograma
plt.figure(figsize=(12, 8))
dendrogram(Z, 
           truncate_mode='lastp',  # mostrar solo ultimas p fusiones
           p=30,                    # numero de clusters a mostrar
           leaf_rotation=90,
           leaf_font_size=10)
plt.xlabel('Indice de muestra o tamaño de cluster')
plt.ylabel('Distancia')
plt.title('Dendrograma de Clustering Jerarquico')
plt.axhline(y=altura_corte, color='r', linestyle='--')  # linea de corte
plt.show()
```

Para datasets grandes, la opción `truncate_mode='lastp'` muestra solo las últimas `p` fusiones, haciendo el dendrograma más legible.

### 3.4 Métodos de enlace (linkage)

La elección de cómo medir distancia entre clusters (no solo entre observaciones individuales) es crítica en clustering jerárquico. Diferentes métodos de enlace definen esta distancia de formas distintas, produciendo resultados muy diferentes.

#### Single Linkage (Enlace simple)

La distancia entre dos clusters se define como la distancia mínima entre cualquier par de observaciones, una de cada cluster:

$$d_{single}(C_i, C_j) = \min_{x \in C_i, y \in C_j} d(x, y)$$

**Características:**
- Tiende a producir clusters alargados o "encadenados"
- Sensible a ruido y outliers que pueden actuar como puentes entre clusters
- Puede identificar clusters de formas no esféricas

**Cuándo usarlo:**
- Cuando se sabe que clusters tienen formas alargadas o irregulares
- Para identificar estructura de cadena en los datos
- Generalmente no recomendado para aplicaciones estándar debido a su sensibilidad al ruido

#### Complete Linkage (Enlace completo)

La distancia entre dos clusters se define como la distancia máxima entre cualquier par de observaciones, una de cada cluster:

$$d_{complete}(C_i, C_j) = \max_{x \in C_i, y \in C_j} d(x, y)$$

**Características:**
- Tiende a producir clusters compactos y aproximadamente esféricos
- Menos sensible a outliers que single linkage
- Favorece clusters de tamaños similares

**Cuándo usarlo:**
- Cuando se buscan clusters compactos y bien separados
- Cuando se prefiere evitar clusters de tamaños muy desiguales
- Como alternativa más robusta a single linkage

#### Average Linkage (Enlace promedio)

La distancia entre dos clusters se define como la distancia promedio entre todos los pares de observaciones, una de cada cluster:

$$d_{average}(C_i, C_j) = \frac{1}{|C_i| \cdot |C_j|} \sum_{x \in C_i} \sum_{y \in C_j} d(x, y)$$

**Características:**
- Compromiso entre single y complete linkage
- Más robusto que single linkage, más flexible que complete linkage
- Produce clusters razonablemente compactos

**Cuándo usarlo:**
- Como método por defecto cuando no hay información previa sobre estructura de datos
- Cuando se busca balance entre flexibilidad y compacidad

#### Ward Linkage (Método de Ward)

El método de Ward no se basa en distancia directa entre clusters, sino en minimizar la varianza total intra-cluster al fusionar. Específicamente, minimiza el incremento en la suma de cuadrados:

$$d_{ward}(C_i, C_j) = \frac{|C_i| \cdot |C_j|}{|C_i| + |C_j|} ||\mu_i - \mu_j||^2$$

donde $\mu_i$ y $\mu_j$ son los centroides de los clusters $C_i$ y $C_j$.

**Características:**
- Tiende a producir clusters de tamaños similares
- Minimiza varianza intra-cluster (similar objetivo a K-Means)
- Generalmente produce los resultados más interpretables
- Más sensible a outliers que average linkage

**Cuándo usarlo:**
- Método más recomendado para la mayoría de aplicaciones prácticas
- Cuando se buscan clusters compactos y cohesivos
- Cuando datos han sido estandarizados apropiadamente

### 3.5 Comparación práctica de métodos de enlace

La elección del método de enlace tiene impacto significativo en los resultados. Consideremos un ejemplo práctico:

```python
from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Probar diferentes metodos de enlace
metodos = ['single', 'complete', 'average', 'ward']
resultados = {}

for metodo in metodos:
    clustering = AgglomerativeClustering(
        n_clusters=4,
        linkage=metodo
    )
    etiquetas = clustering.fit_predict(datos_escalados)
    resultados[metodo] = etiquetas
    
    # Analizar tamaños de clusters
    unique, counts = np.unique(etiquetas, return_counts=True)
    print(f"\n{metodo.upper()} - Tamaños de clusters:")
    for cluster, count in zip(unique, counts):
        print(f"  Cluster {cluster}: {count} observaciones")
```

**Criterios de selección:**

1. **Naturaleza de los datos:**
   - Clusters bien separados y esféricos → Ward o Complete
   - Clusters de formas irregulares → Single o Average
   - Datos con outliers → Average o Complete (más robustos)

2. **Objetivo del análisis:**
   - Segmentación equilibrada → Ward (tiende a clusters de tamaño similar)
   - Identificar estructura natural sin restricciones → Average
   - Detectar patrones alargados → Single (con precaución)

3. **Validación empírica:**
   - Probar múltiples métodos y comparar resultados
   - Evaluar con métricas (coeficiente de silueta)
   - Validar interpretabilidad con expertos de dominio

En la práctica industrial, Ward es el método más utilizado por producir resultados generalmente interpretables y clusters cohesivos.

### 3.6 Criterios para determinar el punto de corte

Una vez construido el dendrograma, determinar dónde cortarlo (cuántos clusters formar) requiere combinar análisis cuantitativo y consideraciones de negocio.

#### Criterio de distancia

Cortar el dendrograma a una altura específica produce clusters cuya distancia máxima intra-cluster es menor o igual a esa altura.

**Método del salto máximo:** Identificar el salto más grande en las alturas de fusión. Este salto indica que clusters bien separados están siendo combinados. Cortar justo antes de este salto.

```python
from scipy.cluster.hierarchy import linkage, fcluster

# Calcular linkage
Z = linkage(datos_escalados, method='ward')

# Analizar diferencias entre fusiones consecutivas
alturas = Z[:, 2]
diferencias = np.diff(alturas)
max_salto_idx = np.argmax(diferencias)

# Altura de corte sugerida
altura_corte = alturas[max_salto_idx]

# Formar clusters en base a altura de corte
etiquetas = fcluster(Z, t=altura_corte, criterion='distance')
print(f"Numero de clusters formados: {len(np.unique(etiquetas))}")
```

#### Criterio de número de clusters

Especificar directamente cuántos clusters se desean:

```python
# Cortar dendrograma para obtener exactamente k clusters
k = 5
etiquetas = fcluster(Z, t=k, criterion='maxclust')
```

#### Consistencia con coeficiente de silueta

Evaluar múltiples puntos de corte usando coeficiente de silueta para identificar el número de clusters que maximiza cohesión intra-cluster y separación inter-cluster:

```python
from sklearn.metrics import silhouette_score

# Evaluar diferentes numeros de clusters
siluetas = []
rango_k = range(2, 11)

for k in rango_k:
    etiquetas = fcluster(Z, t=k, criterion='maxclust')
    silueta = silhouette_score(datos_escalados, etiquetas)
    siluetas.append(silueta)
    print(f"k={k}: silueta={silueta:.3f}")

# Seleccionar k que maximiza silueta
k_optimo = rango_k[np.argmax(siluetas)]
```

#### Consideraciones de negocio

Similar a K-Means, el número final de clusters debe considerar:

- Capacidad de la organización para actuar sobre múltiples segmentos
- Interpretabilidad y diferenciación clara entre clusters
- Estabilidad de segmentaciones ante nuevos datos
- Alineación con estructuras organizacionales o estratégicas existentes

### 3.7 Implementación completa en Scikit-learn

Scikit-learn proporciona `AgglomerativeClustering` para clustering jerárquico:

```python
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# Preparacion de datos
scaler = StandardScaler()
datos_escalados = scaler.fit_transform(datos)

# Clustering jerarquico
clustering = AgglomerativeClustering(
    n_clusters=5,           # numero de clusters deseado
    linkage='ward',         # metodo de enlace
    affinity='euclidean'    # metrica de distancia
)

# Ajustar y predecir
etiquetas = clustering.fit_predict(datos_escalados)

# Agregar etiquetas a datos originales
datos['cluster'] = etiquetas

# Analizar resultados
for cluster_id in range(5):
    cluster_data = datos[datos['cluster'] == cluster_id]
    print(f"\n=== Cluster {cluster_id} ===")
    print(f"Tamaño: {len(cluster_data)}")
    print(cluster_data.describe())
```

**Parámetros importantes:**

- `n_clusters`: Número de clusters a formar (None para dendrograma completo)
- `linkage`: Método de enlace ('ward', 'complete', 'average', 'single')
- `affinity`: Métrica de distancia ('euclidean', 'manhattan', 'cosine')

**Nota:** Para generar dendrograma con Scikit-learn, se usa `scipy.cluster.hierarchy` como se mostró anteriormente, ya que Scikit-learn no proporciona visualización directa de dendrogramas.

### 3.8 Comparación detallada: K-Means vs Clustering Jerárquico

Para decidir entre K-Means y clustering jerárquico en un proyecto, considerar los siguientes factores:

#### Escalabilidad

**K-Means:**
- Escala a millones de observaciones eficientemente
- Complejidad: O(nkti) donde n=observaciones, k=clusters, t=iteraciones, i=dimensiones
- Uso de memoria: O(nk)

**Clustering Jerárquico:**
- Práctico hasta decenas de miles de observaciones
- Complejidad: O(n²log n) para métodos eficientes, O(n³) para métodos básicos
- Uso de memoria: O(n²) para almacenar matriz de distancias

**Decisión:** Para datasets grandes (>100,000 observaciones), K-Means es prácticamente obligatorio. Para datasets medianos, ambos son viables.

#### Flexibilidad en número de clusters

**K-Means:**
- Requiere especificar k a priori
- Explorar diferentes valores de k requiere re-ejecutar el algoritmo

**Clustering Jerárquico:**
- Produce jerarquía completa
- Puede cortarse a cualquier número de clusters sin re-ejecutar

**Decisión:** Si el número de clusters es incierto y se requiere exploración flexible, clustering jerárquico es ventajoso.

#### Forma de clusters

**K-Means:**
- Asume clusters esféricos y de tamaños similares
- Falla con clusters alargados o formas irregulares

**Clustering Jerárquico:**
- Con single o average linkage puede identificar formas irregulares
- Ward produce clusters similares a K-Means

**Decisión:** Para clusters de formas no esféricas, clustering jerárquico con single o average linkage es preferible.

#### Determinismo

**K-Means:**
- No determinístico (depende de inicialización aleatoria)
- Requiere múltiples ejecuciones para estabilidad

**Clustering Jerárquico:**
- Determinístico: mismos datos siempre producen mismo resultado
- Facilita reproducibilidad

**Decisión:** Para reproducibilidad garantizada, clustering jerárquico es ventajoso.

#### Interpretabilidad

**K-Means:**
- Centroides proporcionan perfiles promedio claros
- Fácil de explicar a stakeholders no técnicos

**Clustering Jerárquico:**
- Dendrograma visualiza relaciones jerárquicas
- Más complejo de explicar pero más informativo sobre estructura

**Decisión:** K-Means es más simple de comunicar; clustering jerárquico proporciona más información sobre relaciones.

#### Tabla comparativa resumida

| Aspecto | K-Means | Clustering Jerárquico |
|---------|---------|----------------------|
| Escalabilidad | Excelente (millones) | Limitada (miles) |
| Especificar k | Requerido a priori | Opcional (corte post-hoc) |
| Forma clusters | Esféricos | Flexible (depende linkage) |
| Determinismo | No | Sí |
| Velocidad | Muy rápido | Moderado a lento |
| Memoria | Baja | Alta (O(n²)) |
| Visualización | Scatter plots | Dendrograma |
| Interpretabilidad | Centroides claros | Jerarquías informativas |

### 3.9 Casos de uso en industria

#### E-commerce: Taxonomía de productos sin categorías predefinidas

Una plataforma de e-commerce tiene 10,000 productos sin categorización clara. Aplicando clustering jerárquico con método Ward sobre características de productos (precio, dimensiones, palabras clave en descripción, patrones de compra), se construye una jerarquía que revela:

**Nivel superior (3 clusters):** Categorías amplias (Electrónica, Hogar, Ropa)

**Nivel intermedio (12 clusters):** Subcategorías (Electrónica → Computación, Audio, Fotografía)

**Nivel granular (40 clusters):** Productos específicos (Computación → Laptops, Desktops, Tablets)

Esta jerarquía permite:
- Navegación de usuarios de lo general a lo específico
- Recomendaciones a múltiples niveles de similitud
- Organización flexible de catálogo según contexto (homepage muestra nivel superior, páginas de categoría muestran nivel intermedio)

#### Banca: Segmentación jerárquica de clientes

Un banco implementa segmentación jerárquica sobre variables de clientes (saldo, productos contratados, transacciones, morosidad, antigüedad).

**Nivel estratégico (3 segmentos):** Para decisiones de C-suite
- Clientes premium de alto valor
- Clientes masivos rentables
- Clientes de bajo valor

**Nivel táctico (8 segmentos):** Para estrategias de producto
- Dentro de "premium": inversionistas, ejecutivos, empresarios
- Dentro de "masivos": familias, jóvenes profesionales, pensionados

**Nivel operativo (20 segmentos):** Para acciones de marketing
- Subdivisiones para campañas específicas y ofertas personalizadas

El dendrograma permite presentar la misma segmentación a diferentes niveles organizacionales según sus necesidades de detalle.

#### Investigación: Análisis de jerarquías de especies

En bioinformática y análisis de datos genómicos, clustering jerárquico sobre similitud genética construye árboles filogenéticos que representan relaciones evolutivas entre especies.

Las fusiones a alturas bajas representan especies estrechamente relacionadas; fusiones a alturas altas representan divergencias evolutivas antiguas. Esta jerarquía natural de los datos biológicos es capturada elegantemente por clustering jerárquico, mientras K-Means perdería información sobre relaciones multi-nivel.

---

## 4. Análisis de Componentes Principales (PCA)

### 4.1 Introducción y motivación

El Análisis de Componentes Principales (Principal Component Analysis, PCA) representa una de las técnicas de reducción de dimensionalidad más utilizadas en ciencia de datos. A diferencia del clustering que agrupa observaciones, PCA transforma el espacio de características, proyectando datos de alta dimensionalidad a un espacio de menor dimensión mientras preserva la máxima cantidad de información (varianza) posible.

La necesidad de reducción de dimensionalidad surge frecuentemente en entornos profesionales:

**Visualización:** Datos con decenas o cientos de variables no pueden visualizarse directamente. PCA permite proyectar estos datos a 2D o 3D, facilitando exploración visual y comunicación de patrones.

**Eficiencia computacional:** Algoritmos de machine learning frecuentemente sufren en alta dimensionalidad. Reducir de 100 variables a 20 componentes principales puede acelerar entrenamiento significativamente sin pérdida importante de información.

**Multicolinealidad:** Variables altamente correlacionadas causan problemas en modelos de regresión. PCA transforma variables correlacionadas en componentes ortogonales (no correlacionados), eliminando multicolinealidad.

**Compresión de datos:** Sensores industriales pueden generar terabytes de datos. PCA permite comprimir esta información a sus dimensiones más informativas, reduciendo costos de almacenamiento y transmisión.

**Reducción de ruido:** Variables con poca varianza típicamente contienen principalmente ruido. PCA permite filtrar estas dimensiones, reteniendo solo señal informativa.

PCA es particularmente valioso en industrias como finanzas (análisis de portfolios, reducción de factores de riesgo), manufactura (compresión de datos de sensores), investigación científica (análisis de datos genómicos o espectrales), y como preprocesamiento estándar en pipelines de machine learning.

### 4.2 Fundamentos matemáticos de PCA

PCA busca encontrar un nuevo sistema de coordenadas donde los datos muestran máxima varianza. Formalmente, dados datos $\mathbf{X} \in \mathbb{R}^{n \times d}$ con $n$ observaciones y $d$ variables, PCA encuentra una transformación lineal que proyecta los datos a un espacio de $m$ dimensiones (donde $m < d$) maximizando la varianza retenida.

#### Objetivo de maximización de varianza

PCA identifica direcciones (vectores) en el espacio original donde los datos tienen máxima varianza. La primera componente principal es la dirección de máxima varianza; la segunda componente principal es la dirección de máxima varianza ortogonal a la primera; y así sucesivamente.

Matemáticamente, buscamos vectores $\mathbf{w}_1, \mathbf{w}_2, ..., \mathbf{w}_m$ tales que:

$$\mathbf{w}_1 = \arg\max_{||\mathbf{w}||=1} \text{Var}(\mathbf{X}\mathbf{w})$$

sujeto a que $||\mathbf{w}_1|| = 1$ (vector unitario).

Las componentes subsecuentes se encuentran de forma similar, con la restricción adicional de ser ortogonales a las componentes previas:

$$\mathbf{w}_k = \arg\max_{||\mathbf{w}||=1, \mathbf{w} \perp \mathbf{w}_j \forall j < k} \text{Var}(\mathbf{X}\mathbf{w})$$

#### Descomposición mediante autovalores y autovectores

La solución a este problema de optimización viene de la descomposición espectral de la matriz de covarianza de los datos.

**Paso 1: Centrar los datos**  
Restar la media de cada variable:
$$\mathbf{X}_{centrado} = \mathbf{X} - \bar{\mathbf{X}}$$

donde $\bar{\mathbf{X}}$ es el vector de medias de cada variable.

**Paso 2: Calcular matriz de covarianza**  
$$\mathbf{C} = \frac{1}{n-1} \mathbf{X}_{centrado}^T \mathbf{X}_{centrado}$$

La matriz de covarianza $\mathbf{C} \in \mathbb{R}^{d \times d}$ captura las relaciones lineales entre todas las variables.

**Paso 3: Descomposición espectral**  
Encontrar autovalores $\lambda_1 \geq \lambda_2 \geq ... \geq \lambda_d$ y autovectores correspondientes $\mathbf{v}_1, \mathbf{v}_2, ..., \mathbf{v}_d$ de la matriz de covarianza:

$$\mathbf{C}\mathbf{v}_i = \lambda_i \mathbf{v}_i$$

Los autovectores $\mathbf{v}_i$ son las componentes principales (direcciones de máxima varianza), y los autovalores $\lambda_i$ representan la cantidad de varianza explicada por cada componente.

**Paso 4: Proyección**  
Los datos se proyectan al espacio de componentes principales:

$$\mathbf{Z} = \mathbf{X}_{centrado} \mathbf{V}$$

donde $\mathbf{V} = [\mathbf{v}_1, \mathbf{v}_2, ..., \mathbf{v}_m]$ es la matriz de las primeras $m$ componentes principales.

#### Interpretación geométrica

PCA realiza una rotación del espacio de coordenadas original para alinearlo con las direcciones de máxima varianza. Los datos originales $\mathbf{X}$ se expresan en un nuevo sistema de coordenadas donde:

- Primera componente principal: dirección de máxima varianza en los datos
- Segunda componente principal: dirección de máxima varianza ortogonal a la primera
- Las componentes son no correlacionadas entre sí (ortogonales)

Esta rotación no cambia los datos fundamentalmente, solo proporciona una representación alternativa que enfatiza las direcciones más informativas.

### 4.3 Componentes principales como combinaciones lineales

Cada componente principal es una combinación lineal de las variables originales:

$$PC_k = w_{k1}X_1 + w_{k2}X_2 + ... + w_{kd}X_d$$

donde:
- $PC_k$ es la k-ésima componente principal
- $X_i$ son las variables originales (centradas)
- $w_{ki}$ son los pesos (loadings) del autovector correspondiente

**Ejemplo ilustrativo:**  
En análisis financiero con variables {retorno, volatilidad, beta, liquidez}:

$$PC_1 = 0.52 \cdot \text{retorno} + 0.48 \cdot \text{volatilidad} + 0.51 \cdot \text{beta} + 0.49 \cdot \text{liquidez}$$

Los pesos similares sugieren que $PC_1$ representa un factor general de "actividad del activo" que combina todas las características.

$$PC_2 = 0.65 \cdot \text{retorno} - 0.64 \cdot \text{volatilidad} + 0.38 \cdot \text{beta} - 0.15 \cdot \text{liquidez}$$

Los pesos contrastantes sugieren que $PC_2$ captura la dicotomía entre "alto retorno vs alta volatilidad".

### 4.4 Varianza explicada y su interpretación

Cada componente principal captura una fracción de la varianza total de los datos. El autovalor $\lambda_k$ asociado a la componente $k$ representa la varianza explicada por esa componente.

#### Proporción de varianza explicada

La proporción de varianza explicada por la componente $k$ es:

$$\text{Proporción}_k = \frac{\lambda_k}{\sum_{i=1}^{d} \lambda_i}$$

La varianza total es la suma de todos los autovalores: $\sum_{i=1}^{d} \lambda_i = \sum_{i=1}^{d} \text{Var}(X_i)$ para datos estandarizados.

#### Varianza acumulada

La varianza acumulada por las primeras $m$ componentes es:

$$\text{Varianza Acumulada}_m = \frac{\sum_{i=1}^{m} \lambda_i}{\sum_{i=1}^{d} \lambda_i}$$

Esta métrica indica qué fracción de la información total se retiene al usar $m$ componentes.

**Ejemplo conceptual simple:**
- PC1 explica 45% de varianza
- PC2 explica 25% de varianza
- PC3 explica 15% de varianza
- Varianza acumulada con 3 componentes: 85%

Esto significa que usando solo 3 componentes (en lugar de, digamos, 20 variables originales), se retiene 85% de la información original.

**Ejemplo detallado en contexto de manufactura:**

Una planta automotriz monitorea calidad mediante 15 mediciones por pieza producida: 5 dimensiones físicas, 4 propiedades de material, 3 características de acabado superficial, y 3 métricas de resistencia. Para cada lote de 1000 piezas, esto genera 15,000 datos.

Aplicando PCA a los datos estandarizados de un mes (30,000 piezas):

| Componente | Autovalor | Varianza Explicada | Varianza Acumulada |
|------------|-----------|-------------------|-------------------|
| PC1 | 5.25 | 35.0% | 35.0% |
| PC2 | 3.15 | 21.0% | 56.0% |
| PC3 | 2.10 | 14.0% | 70.0% |
| PC4 | 1.35 | 9.0% | 79.0% |
| PC5 | 0.90 | 6.0% | 85.0% |
| PC6 | 0.75 | 5.0% | 90.0% |
| PC7-15 | ... | ... | 100.0% |

**Interpretación e impacto operacional:**

**PC1 (35% varianza):** Análisis de loadings revela altos pesos en las 5 dimensiones físicas. PC1 representa un "factor de tamaño general" - cuando una dimensión es grande, típicamente todas lo son (correlación por tolerancias de manufactura).

**PC2 (21% varianza):** Altos loadings en propiedades de material. Representa "calidad de materia prima" - batch-to-batch variation en el material de entrada.

**PC3 (14% varianza):** Altos loadings en acabado superficial. Representa "performance del proceso de acabado".

**Decisión operacional:** Usando solo 5 componentes (85% varianza en lugar de 15 variables completas):

- **Almacenamiento:** Reducción de 15 a 5 valores por pieza = 67% menos espacio
- **Transmisión:** Datos de sensores se comprimen antes de envío a servidor central
- **Monitoreo en tiempo real:** Gráficos de control sobre 5 componentes en lugar de 15 variables
- **Detección de anomalías:** Modelo de control de calidad entrenado sobre 5 componentes corre 3x más rápido

**Validación:** Reconstruyendo mediciones originales desde las 5 componentes, el error cuadrático medio es solo 2% del rango de especificación - aceptable para control de proceso.

Este ejemplo ilustra cómo PCA no es solo una técnica matemática, sino una herramienta que habilita decisiones operacionales concretas con beneficios medibles en eficiencia y costo.

#### Visualización de varianza explicada

```python
import matplotlib.pyplot as plt
import numpy as np

# Proporcion de varianza explicada por cada componente
varianza_explicada = pca.explained_variance_ratio_

# Varianza acumulada
varianza_acumulada = np.cumsum(varianza_explicada)

# Grafico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Grafico de barras: varianza por componente
ax1.bar(range(1, len(varianza_explicada) + 1), varianza_explicada)
ax1.set_xlabel('Componente Principal')
ax1.set_ylabel('Proporcion de Varianza Explicada')
ax1.set_title('Varianza Explicada por Componente')

# Grafico de linea: varianza acumulada
ax2.plot(range(1, len(varianza_acumulada) + 1), varianza_acumulada, marker='o')
ax2.axhline(y=0.80, color='r', linestyle='--', label='80% varianza')
ax2.axhline(y=0.90, color='g', linestyle='--', label='90% varianza')
ax2.set_xlabel('Numero de Componentes')
ax2.set_ylabel('Varianza Acumulada')
ax2.set_title('Varianza Acumulada')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
```

### 4.5 Criterios para selección del número de componentes

Decidir cuántas componentes principales retener es crucial. Muy pocas componentes pierden información importante; demasiadas componentes mantienen ruido y dificultan interpretación.

#### Umbral de varianza acumulada

Seleccionar el número mínimo de componentes que explican un porcentaje objetivo de varianza total.

**Umbrales comunes:**
- 80-85%: Para visualización y exploración inicial
- 90-95%: Para preprocesamiento antes de modelos de machine learning
- 95-99%: Cuando es crítico preservar máxima información

```python
# Encontrar numero de componentes para retener 90% de varianza
varianza_objetivo = 0.90
n_componentes = np.argmax(varianza_acumulada >= varianza_objetivo) + 1
print(f"Componentes necesarias para {varianza_objetivo*100}% varianza: {n_componentes}")
```

#### Scree Plot (Criterio del codo)

El scree plot grafica autovalores (o varianza explicada) contra el número de componente. Similar al método del codo en clustering, se busca el punto donde la curva se "aplana", indicando que componentes adicionales agregan poco valor.

```python
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(pca.explained_variance_) + 1), 
         pca.explained_variance_, marker='o')
plt.xlabel('Componente Principal')
plt.ylabel('Autovalor (Varianza)')
plt.title('Scree Plot')
plt.grid(True)
plt.show()
```

#### Regla de Kaiser

Retener solo componentes con autovalores mayores a 1 (para datos estandarizados). La lógica es que una componente con autovalor menor a 1 explica menos varianza que una variable original individual, por lo que no vale la pena retenerla.

Esta regla funciona mejor con datos estandarizados y puede ser demasiado conservadora o liberal dependiendo del dataset.

```python
# Componentes con autovalor > 1
autovalores = pca.explained_variance_
n_kaiser = np.sum(autovalores > 1)
print(f"Componentes con autovalor > 1: {n_kaiser}")
```

#### Consideraciones específicas del contexto

**Para visualización:** Típicamente 2-3 componentes (permiten gráficos 2D/3D)

**Para preprocesamiento de ML:** Balancear velocidad (menos componentes) vs información (más componentes). Validación cruzada puede guiar: entrenar modelo con diferentes números de componentes y evaluar desempeño.

**Para compresión:** Definir balance entre ratio de compresión y pérdida aceptable de información según limitaciones de almacenamiento o ancho de banda.

**Para interpretabilidad:** Menos componentes facilitan interpretación, pero deben explicar suficiente varianza para ser representativas.

### 4.6 Interpretación de loadings

Los loadings (pesos o cargas) indican cuánto contribuye cada variable original a cada componente principal. Analizar loadings es crítico para entender qué representan las componentes.

#### Loadings como correlaciones

Para datos estandarizados, los loadings pueden interpretarse como correlaciones entre variables originales y componentes principales. Valores cercanos a ±1 indican fuerte relación; valores cercanos a 0 indican poca relación.

```python
# Obtener loadings
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

# Crear DataFrame para mejor visualizacion
loadings_df = pd.DataFrame(
    loadings,
    columns=[f'PC{i+1}' for i in range(loadings.shape[1])],
    index=nombres_variables
)

print(loadings_df)
```

#### Visualización de loadings

**Heatmap de loadings:**
```python
import seaborn as sns

plt.figure(figsize=(12, 8))
sns.heatmap(loadings_df.iloc[:, :5],  # primeras 5 componentes
            annot=True, fmt='.2f', cmap='RdBu_r', center=0,
            cbar_kws={'label': 'Loading'})
plt.title('Loadings de Componentes Principales')
plt.xlabel('Componente Principal')
plt.ylabel('Variable Original')
plt.tight_layout()
plt.show()
```

**Biplot:** Visualización que combina observaciones proyectadas y vectores de loadings:
```python
def biplot(scores, loadings, labels):
    plt.figure(figsize=(10, 8))
    
    # Graficar observaciones
    plt.scatter(scores[:, 0], scores[:, 1], alpha=0.5)
    
    # Graficar vectores de variables
    for i, label in enumerate(labels):
        plt.arrow(0, 0, loadings[i, 0], loadings[i, 1],
                  head_width=0.05, head_length=0.05, fc='r', ec='r')
        plt.text(loadings[i, 0]*1.15, loadings[i, 1]*1.15,
                 label, fontsize=10, ha='center')
    
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('Biplot: PC1 vs PC2')
    plt.grid(True)
    plt.show()

biplot(datos_pca, loadings, nombres_variables)
```

#### Interpretación de componentes

**Ejemplo conceptual en análisis de clientes:**

Variables: {edad, ingreso, frecuencia_compra, valor_promedio, antiguedad}

**PC1:** loadings altos en {frecuencia_compra, valor_promedio, antiguedad}  
→ Interpretación: "Engagement del cliente" o "Valor de vida del cliente"

**PC2:** loadings altos en {edad, ingreso}, bajos en variables de comportamiento  
→ Interpretación: "Perfil demográfico"

**PC3:** loading alto positivo en frecuencia, alto negativo en valor_promedio  
→ Interpretación: "Tipo de comprador" (frecuente-bajo_valor vs ocasional-alto_valor)

**Ejemplo detallado: Análisis de mercado inmobiliario**

Una compañía inmobiliaria analiza 2,500 propiedades con 12 características:

| Variable | Descripción |
|----------|-------------|
| precio_m2 | Precio por metro cuadrado |
| superficie_total | Metros cuadrados totales |
| num_habitaciones | Número de habitaciones |
| num_banos | Número de baños |
| edad_propiedad | Años desde construcción |
| dist_centro | Distancia al centro (km) |
| dist_metro | Distancia a metro más cercano (km) |
| indice_seguridad | Índice de seguridad del barrio (0-100) |
| indice_educacion | Calidad de escuelas cercanas (0-100) |
| espacios_verdes | Superficie de parques cercanos (m²) |
| comercios_cercanos | Número de comercios a 500m |
| calificacion_energia | Eficiencia energética (A-G convertida a 1-7) |

Después de estandarización y PCA, la matriz de loadings de las primeras 3 componentes:

| Variable | PC1 | PC2 | PC3 |
|----------|-----|-----|-----|
| precio_m2 | 0.82 | 0.15 | -0.12 |
| superficie_total | -0.25 | 0.85 | -0.08 |
| num_habitaciones | -0.22 | 0.88 | -0.11 |
| num_banos | 0.35 | 0.72 | -0.15 |
| edad_propiedad | -0.75 | -0.15 | -0.22 |
| dist_centro | -0.88 | -0.10 | 0.05 |
| dist_metro | -0.83 | -0.12 | 0.08 |
| indice_seguridad | 0.78 | 0.08 | 0.25 |
| indice_educacion | 0.81 | 0.12 | 0.28 |
| espacios_verdes | 0.45 | -0.18 | 0.75 |
| comercios_cercanos | 0.72 | 0.28 | -0.15 |
| calificacion_energia | 0.62 | -0.25 | -0.08 |

Varianza explicada: PC1=48%, PC2=22%, PC3=12% (total=82%)

**Interpretación de PC1 (48% varianza) - "Factor de Prestigio/Ubicación":**
- Loadings altos positivos: precio_m2 (0.82), indice_seguridad (0.78), indice_educacion (0.81), comercios_cercanos (0.72)
- Loadings altos negativos: dist_centro (-0.88), dist_metro (-0.83), edad_propiedad (-0.75)
- **Significado:** PC1 captura la "deseabilidad general" de la ubicación. Propiedades con PC1 alto son céntricas, bien conectadas, en barrios seguros con buenas escuelas, nuevas, y por tanto caras. PC1 bajo indica propiedades periféricas, menos conectadas, más antiguas y más económicas.
- **Uso práctico:** Clasificar propiedades en "premium", "medio", "económico" basándose en score de PC1.

**Interpretación de PC2 (22% varianza) - "Factor de Tamaño/Espacio":**
- Loadings altos positivos: num_habitaciones (0.88), superficie_total (0.85), num_banos (0.72)
- Loadings cercanos a cero en la mayoría de otras variables
- **Significado:** PC2 captura el tamaño físico de la propiedad, independientemente de su ubicación o calidad. Un apartamento pequeño en ubicación premium puede tener PC1 alto pero PC2 bajo; una casa grande en periferia tiene PC2 alto pero PC1 bajo.
- **Uso práctico:** Segmentar por "tipo de familia" (PC2 alto para familias grandes, PC2 bajo para individuos/parejas).

**Interpretación de PC3 (12% varianza) - "Factor Ambiental":**
- Loading alto positivo: espacios_verdes (0.75)
- Loadings moderados positivos: indice_seguridad (0.25), indice_educacion (0.28)
- **Significado:** PC3 captura el aspecto "calidad de vida ambiental", especialmente relacionado con espacios verdes y naturaleza cercana.
- **Uso práctico:** Identificar propiedades "eco-friendly" o "orientadas a naturaleza" para marketing especializado.

**Aplicación operacional:**

La empresa utiliza estas 3 componentes (82% varianza desde 12 variables) para:

1. **Sistema de recomendación:** Calcular PC1, PC2, PC3 para cada propiedad. Cuando un cliente consulta una propiedad, recomendar otras con scores similares en las 3 componentes.

2. **Pricing dinámico:** Modelo de regresión de precio basado en PC1, PC2, PC3 (más rápido y sin multicolinealidad comparado con usar las 12 variables originales).

3. **Dashboard gerencial:** Visualizar portafolio de propiedades en gráfico 3D (PC1 vs PC2 vs PC3) para identificar gaps en oferta y oportunidades de adquisición.

4. **Segmentación de marketing:** 
   - Alto PC1 + Bajo PC2 → "Profesionales urbanos" (apartamentos céntricos pequeños)
   - Alto PC1 + Alto PC2 → "Familias acomodadas" (casas grandes en zonas premium)
   - Bajo PC1 + Alto PC2 → "Familias en crecimiento" (casas grandes periféricas)
   - Alto PC3 independiente de otros → "Amantes de naturaleza" (campañas eco-friendly)

Este ejemplo muestra cómo PCA no solo reduce dimensionalidad, sino que extrae "factores latentes" interpretables que capturan estructura significativa del negocio.

### 4.7 Limitaciones de PCA

A pesar de su utilidad, PCA tiene limitaciones importantes que deben considerarse:

#### Linealidad

PCA solo captura relaciones lineales entre variables. Para datos con estructura no lineal (por ejemplo, datos en forma de espiral o manifolds curvos), PCA puede fallar en capturar la verdadera estructura.

**Señales de problema:**
- Varianza explicada por primeras componentes es baja incluso con muchas componentes
- Visualizaciones 2D/3D no revelan estructura clara que se sabe existe

**Alternativas para datos no lineales:**
- Kernel PCA (extensión no lineal de PCA)
- t-SNE, UMAP, PacMap (métodos modernos de reducción no lineal)
- Autoencoders (redes neuronales para reducción de dimensionalidad)

#### Sensibilidad a outliers

Outliers extremos pueden distorsionar componentes principales significativamente, ya que PCA maximiza varianza y outliers contribuyen desproporcionadamente a la varianza.

**Mitigación:**
- Detectar y remover outliers antes de PCA
- Usar Robust PCA (variante robusta a outliers)
- Winsorizar datos (limitar valores extremos)

#### Pérdida de interpretabilidad directa

Variables originales típicamente tienen interpretaciones claras de negocio. Componentes principales, siendo combinaciones lineales, pierden esta interpretabilidad directa.

**Ejemplo:** Una variable "edad" es intuitiva; PC1 que combina edad, ingreso, y educación es menos intuitiva.

**Mitigación:**
- Análisis cuidadoso de loadings para interpretar componentes
- Comunicar componentes con nombres descriptivos basados en loadings dominantes
- Considerar si la pérdida de interpretabilidad justifica los beneficios de reducción

#### Requiere estandarización

PCA es sensible a la escala de variables. Variables con rangos grandes dominan componentes principales. Esto requiere estandarización cuidadosa, pero puede perder información sobre magnitudes absolutas.

#### No preserva distancias exactas

La proyección a menor dimensión inevitablemente pierde información. Distancias entre observaciones en el espacio reducido son aproximaciones de distancias en el espacio original, no iguales.

### 4.8 Implementación completa en Scikit-learn

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# Paso 1: Estandarizacion (critico para PCA)
scaler = StandardScaler()
datos_escalados = scaler.fit_transform(datos)

# Paso 2: Aplicar PCA
# Opcion A: Especificar numero de componentes
pca = PCA(n_components=5)

# Opcion B: Especificar varianza minima a retener
# pca = PCA(n_components=0.95)  # retiene componentes hasta 95% varianza

# Ajustar y transformar
datos_pca = pca.fit_transform(datos_escalados)

# Paso 3: Analizar resultados
print(f"Forma original: {datos.shape}")
print(f"Forma reducida: {datos_pca.shape}")
print(f"\nVarianza explicada por componente:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var:.4f} ({var*100:.2f}%)")

print(f"\nVarianza acumulada: {pca.explained_variance_ratio_.sum():.4f}")

# Paso 4: Crear DataFrame con componentes
columnas_pc = [f'PC{i+1}' for i in range(datos_pca.shape[1])]
datos_pca_df = pd.DataFrame(datos_pca, columns=columnas_pc)

# Paso 5: Reconstruccion (opcional)
# Transformar de vuelta a espacio original
datos_reconstruidos = pca.inverse_transform(datos_pca)
datos_reconstruidos = scaler.inverse_transform(datos_reconstruidos)

# Calcular error de reconstruccion
error = np.mean((datos.values - datos_reconstruidos) ** 2)
print(f"\nError cuadratico medio de reconstruccion: {error:.6f}")
```

**Parámetros importantes:**

- `n_components`: Número de componentes (entero) o varianza mínima a retener (float entre 0 y 1)
- `whiten`: Si True, componentes se escalan para tener varianza unitaria (útil para algunos algoritmos posteriores)
- `random_state`: Para reproducibilidad cuando se usa método aleatorio (raro en PCA estándar)

### 4.9 Casos de uso detallados en industria

#### Finanzas: Reducción de factores de riesgo en portfolios

Un fondo de inversión maneja portfolio de 200 activos, cada uno con 50 métricas de riesgo (volatilidad, correlaciones con índices, beta, ratios fundamentales, indicadores técnicos). Esto resulta en 10,000 dimensiones de información.

PCA reduce estas 50 métricas por activo a 8 componentes principales que explican 92% de varianza:

- **PC1:** Factor de mercado general (alta correlación con todos los índices)
- **PC2:** Factor de crecimiento vs valor
- **PC3:** Factor de tamaño (capitalización)
- **PC4-PC8:** Factores específicos de sector/industria

Esta reducción permite:
- Visualizar posicionamiento de activos en espacio de riesgo reducido
- Construir portfolios asegurando diversificación en los factores principales
- Acelerar optimización de portfolio (8 dimensiones vs 50)
- Comunicar perfil de riesgo de portfolio en términos de pocos factores interpretables

#### Manufactura: Compresión de datos de sensores

Una planta industrial monitorea maquinaria con 100 sensores que registran datos cada segundo. Esto genera 8.6 millones de lecturas diarias de 100 dimensiones.

PCA identifica que 12 componentes principales capturan 95% de varianza:

- **PC1-PC3:** Variación normal de operación (carga de trabajo, temperatura ambiente)
- **PC4-PC6:** Patrones de desgaste gradual
- **PC7-PC12:** Señales de fallas específicas

Beneficios:
- Transmisión de datos comprimida (12 valores vs 100) desde sensores a servidor central
- Almacenamiento reducido (factor 8x de compresión con mínima pérdida)
- Modelos de predicción de fallas más rápidos y precisos
- Visualización de estado de máquinas en espacios 2D/3D interpretables

#### Investigación: Análisis de expresión genética

Estudio biomédico analiza expresión de 20,000 genes en 500 pacientes con diferentes condiciones.

PCA sobre datos de expresión genética (20,000 dimensiones) revela:

- **PC1:** Separa pacientes sanos de enfermos (explica 40% varianza)
- **PC2:** Diferencia subtipos de enfermedad (explica 15% varianza)
- **PC3-PC5:** Factores relacionados con tratamientos previos

Análisis de loadings identifica conjuntos de genes que contribuyen a cada componente, sugiriendo:
- Pathways biológicos asociados con enfermedad
- Biomarcadores potenciales para diagnóstico
- Subgrupos de pacientes que pueden responder diferente a tratamientos

Visualización en 2D (PC1 vs PC2) permite identificación rápida de outliers, validación de hipótesis biológicas, y comunicación de resultados a investigadores sin entrenamiento técnico profundo.

---

## 5. Métodos Modernos de Reducción de Dimensionalidad

### 5.1 Limitaciones de PCA para datos no lineales

PCA, al basarse en proyecciones lineales que maximizan varianza, funciona excepcionalmente bien cuando las relaciones entre variables son aproximadamente lineales. Sin embargo, muchos datasets del mundo real contienen estructura no lineal que PCA no puede capturar adecuadamente.

**Ejemplo ilustrativo de limitación de PCA:**

Consideremos un dataset sintético en forma de espiral en 3D. Los datos siguen una trayectoria curvada: puntos consecutivos en la espiral están cerca entre sí, pero PCA, al buscar proyecciones lineales, "desenrolla" la espiral de forma que pierde las relaciones de vecindad local. Puntos que están cerca en la espiral original pueden quedar lejos en la proyección PCA, y viceversa.

**Casos reales donde PCA falla:**

**1. Embeddings de texto en NLP:** Cuando modelos de lenguaje (BERT, GPT) generan representaciones de 768 dimensiones para palabras o documentos, estas representaciones capturan similitudes semánticas complejas y no lineales. Palabras relacionadas temáticamente forman "clusters" en manifolds curvos. PCA proyecta estas estructuras linealmente, mezclando clusters que deberían estar separados.

**2. Imágenes de rostros:** Características faciales (expresiones, ángulos, iluminación) crean manifolds no lineales en el espacio de píxeles. PCA puede capturar variación gruesa (presencia de características generales), pero falla en preservar similitudes sutiles que son no lineales.

**3. Datos de sensores de máquinas:** Estados operativos de maquinaria (arranque, operación normal a diferentes cargas, pre-falla) forman trayectorias curvas en el espacio de sensores. PCA puede no separar adecuadamente estados similares que están en diferentes ramas de estas trayectorias.

**Señales de que PCA no es suficiente:**

- Las primeras componentes principales explican relativamente poca varianza (ej: 5 componentes solo explican 40%)
- Visualizaciones 2D/3D con PCA no revelan clusters o estructura que se sabe existe
- Clusters conocidos en el espacio original se mezclan en la proyección PCA
- Relaciones de vecindad no se preservan: puntos similares en original quedan distantes en proyección

En estos casos, métodos de reducción de dimensionalidad no lineal como t-SNE, UMAP y PacMap ofrecen alternativas más efectivas.

### 5.2 t-SNE: Visualización mediante preservación de vecindarios locales

t-Distributed Stochastic Neighbor Embedding (t-SNE) es una técnica de reducción de dimensionalidad no lineal diseñada específicamente para visualización. Desarrollada por Laurens van der Maaten y Geoffrey Hinton en 2008, t-SNE se ha convertido en el estándar de facto para visualizar datasets de alta dimensionalidad en investigación científica y análisis exploratorio.

#### Fundamentos conceptuales

A diferencia de PCA que busca preservar varianza global, t-SNE busca preservar relaciones de vecindad local. La idea central es: si dos puntos están cerca en el espacio de alta dimensión, deberían estar cerca en la visualización 2D/3D; si están lejos, pueden estar lejos o cerca (t-SNE no garantiza preservar distancias globales).

t-SNE modela la similitud entre pares de puntos en el espacio original mediante distribuciones de probabilidad. Para cada punto, define una distribución de probabilidad sobre sus vecinos: puntos cercanos tienen alta probabilidad, puntos lejanos tienen baja probabilidad. Luego construye una representación en espacio reducido donde las distribuciones de probabilidad son lo más similares posible.

#### Formulación matemática

**En el espacio original (alta dimensión):**

La similitud entre punto $x_i$ y $x_j$ se modela con una distribución gaussiana:

$$p_{j|i} = \frac{\exp(-||x_i - x_j||^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-||x_i - x_k||^2 / 2\sigma_i^2)}$$

donde $\sigma_i$ es la varianza de la distribución gaussiana centrada en $x_i$, ajustada según la densidad local.

La similitud simétrica se define como:
$$p_{ij} = \frac{p_{j|i} + p_{i|j}}{2n}$$

**En el espacio de baja dimensión:**

Las similitudes en la representación reducida $y_i, y_j$ se modelan con una distribución t de Student (colas más pesadas que gaussiana):

$$q_{ij} = \frac{(1 + ||y_i - y_j||^2)^{-1}}{\sum_{k \neq l} (1 + ||y_k - y_l||^2)^{-1}}$$

El uso de la distribución t (en lugar de gaussiana) permite que puntos moderadamente distantes en alta dimensión puedan estar moderadamente distantes en baja dimensión, evitando el problema de "crowding" donde todos los puntos se amontonan en el centro.

**Optimización:**

t-SNE minimiza la divergencia de Kullback-Leibler entre las distribuciones $P$ y $Q$:

$$C = KL(P||Q) = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$$

Esta optimización se realiza mediante descenso de gradiente, iniciando desde una configuración aleatoria o de PCA.

#### Parámetros clave de t-SNE

**1. Perplexity (perplejidad):**

El parámetro más crítico de t-SNE. Controla el balance entre preservar estructura local vs global, y puede interpretarse como una estimación del número de vecinos cercanos que cada punto debería tener.

$$\text{Perplexity} = 2^{H(P_i)}$$

donde $H(P_i)$ es la entropía de la distribución de probabilidad del punto $i$.

- **Valores típicos:** 5-50 para datasets pequeños/medianos, 30-50 para datasets grandes
- **Perplexity baja (5-10):** Enfatiza estructura muy local, puede fragmentar clusters grandes
- **Perplexity alta (50-100):** Intenta preservar más estructura global, puede mezclar clusters distintos
- **Recomendación:** Probar múltiples valores (ej: 5, 10, 30, 50) y comparar visualmente

**Ejemplo de impacto de perplexity:**

Un dataset de 1,000 imágenes de dígitos manuscritos (MNIST):
- Perplexity=5: Los 10 dígitos aparecen muy fragmentados, cada uno dividido en múltiples sub-clusters
- Perplexity=30: Los 10 dígitos aparecen como clusters cohesivos y bien separados (óptimo)
- Perplexity=100: Los dígitos similares (6 vs 8, 3 vs 5) comienzan a solaparse

**2. Learning rate (tasa de aprendizaje):**

Controla el tamaño de pasos en la optimización por descenso de gradiente.

- **Valores típicos:** 10-1000, frecuentemente 200-500
- **Muy bajo (<10):** Convergencia lenta, puede quedar atrapado en mínimos locales pobres
- **Muy alto (>1000):** Inestabilidad, la optimización "salta" sin converger
- **Recomendación:** Comenzar con valores por defecto (200-500). Si la visualización parece no converger o es de mala calidad, ajustar.

**3. n_iter (número de iteraciones):**

Número de pasos de optimización.

- **Valores típicos:** 1000-5000
- **Datasets grandes:** Pueden requerir más iteraciones (3000-5000)
- **Señal de convergencia:** Observar la función de costo (KL divergence). Debe decrecer y estabilizarse

```python
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Aplicar t-SNE con diferentes perplexities
perplexities = [5, 30, 50]
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for idx, perp in enumerate(perplexities):
    tsne = TSNE(n_components=2, 
                perplexity=perp, 
                learning_rate=200,
                n_iter=2000,
                random_state=42)
    datos_tsne = tsne.fit_transform(datos_escalados)
    
    axes[idx].scatter(datos_tsne[:, 0], datos_tsne[:, 1], 
                     c=etiquetas, cmap='viridis', alpha=0.6, s=10)
    axes[idx].set_title(f'Perplexity = {perp}')
    axes[idx].set_xlabel('t-SNE 1')
    axes[idx].set_ylabel('t-SNE 2')

plt.tight_layout()
plt.show()
```

#### Interpretación correcta de visualizaciones t-SNE

t-SNE produce visualizaciones poderosas pero requiere interpretación cuidadosa:

**Lo que t-SNE preserva:**
- **Estructura local:** Puntos cercanos en alta dimensión estarán cercanos en visualización
- **Clusters:** Grupos cohesivos en alta dimensión aparecerán como clusters en visualización

**Lo que t-SNE NO preserva:**
- **Distancias globales:** Distancias entre clusters en la visualización no tienen significado absoluto
- **Densidades relativas:** Cluster grande y disperso puede parecer tan compacto como cluster pequeño y denso
- **Tamaños de clusters:** No reflejan necesariamente el tamaño real en número de puntos

**Errores comunes de interpretación:**

❌ **Incorrecto:** "Cluster A está 3 veces más lejos de cluster B que de cluster C"  
✅ **Correcto:** "Cluster A está bien separado tanto de B como de C"

❌ **Incorrecto:** "Cluster A es más grande que cluster B porque ocupa más espacio visual"  
✅ **Correcto:** "Cluster A y B están ambos bien definidos; necesito verificar sus tamaños en los datos originales"

❌ **Incorrecto:** "Ejecuté t-SNE una vez, este es el patrón real"  
✅ **Correcto:** "Ejecuté t-SNE con múltiples perplexities y random seeds; el patrón de 5 clusters es consistente"

**Ejemplo práctico de análisis de clientes con t-SNE:**

Una plataforma de streaming analiza 50,000 usuarios con vectores de 300 dimensiones representando sus preferencias de contenido (generados por un modelo de embeddings). PCA de 300 dimensiones a 2 revela solo una "nube" difusa sin estructura clara.

Aplicando t-SNE (perplexity=30, 2000 iteraciones):

```
Resultado visual observado:
- 5 clusters claramente separados emergen en la visualización 2D
- Cluster 1 (grande, esquina superior izquierda): ~15,000 usuarios
- Cluster 2 (mediano, centro): ~12,000 usuarios  
- Cluster 3 (pequeño, derecha): ~8,000 usuarios
- Cluster 4 (mediano, abajo): ~10,000 usuarios
- Cluster 5 (pequeño, esquina superior derecha): ~5,000 usuarios
```

**Análisis posterior revelando significado:**

Caracterizando cada cluster según preferencias originales (variables en espacio de 300D):
- Cluster 1: Preferencia dominante por contenido de acción/aventura
- Cluster 2: Contenido familiar y comedias
- Cluster 3: Documentales y contenido educativo
- Cluster 4: Series dramáticas de larga duración
- Cluster 5: Contenido internacional/subtitulado

**Valor de negocio:**
- Sistema de recomendación ahora utiliza membresía de cluster como feature adicional
- Marketing diseña campañas diferenciadas por cluster
- Producción de contenido prioriza géneros para clusters con alta retención

**Validación de t-SNE:** Aplicar K-Means sobre datos originales de 300D resultó en 5 clusters con alta correspondencia (>85%) con clusters visuales de t-SNE, validando que la estructura visualizada es real y no artefacto.

### 5.3 Limitaciones de t-SNE

A pesar de su popularidad, t-SNE tiene limitaciones importantes:

#### 1. No determinístico

t-SNE utiliza inicialización aleatoria y optimización estocástica, produciendo resultados diferentes en cada ejecución.

**Implicación práctica:** Siempre ejecutar múltiples veces con diferentes `random_state` y verificar que patrones importantes (número de clusters, separación) son consistentes.

#### 2. Sensibilidad a parámetros

Perplexity puede cambiar dramáticamente la visualización. No existe valor "correcto" universal.

**Implicación práctica:** Probar rango de perplexities. Si estructura es robusta, será visible en múltiples valores.

#### 3. Lento en datasets grandes

Complejidad computacional es O(n²) en versiones básicas, haciéndolo impráctico para datasets con >50,000 observaciones.

**Soluciones:**
- Usar Barnes-Hut t-SNE (implementación por defecto en sklearn, complejidad O(n log n))
- Submuestrear datos estratégicamente
- Considerar UMAP (más rápido) para datasets muy grandes

#### 4. Interpretación de distancias globales engañosa

Distancias entre clusters separados no tienen significado cuantitativo.

**Implicación práctica:** No inferir relaciones cuantitativas entre clusters distantes. Solo confiar en estructura local (dentro de clusters) y separación cualitativa (clusters están o no separados).

### 5.4 UMAP: Equilibrio entre estructura local y global

Uniform Manifold Approximation and Projection (UMAP), desarrollado por Leland McInnes en 2018, representa una evolución significativa sobre t-SNE. UMAP preserva mejor estructura global mientras mantiene la capacidad de t-SNE para revelar estructura local, y es significativamente más rápido.

#### Ventajas de UMAP sobre t-SNE

**1. Preservación de estructura global:**  
UMAP mantiene mejor las relaciones entre clusters distantes. Distancias entre clusters tienen más significado que en t-SNE.

**2. Velocidad:**  
UMAP es típicamente 10-100x más rápido que t-SNE en datasets grandes, con complejidad aproximadamente lineal.

**3. Determinismo (configuración):**  
UMAP puede configurarse para ser reproducible, eliminando variabilidad entre ejecuciones.

**4. Escalabilidad:**  
UMAP maneja efectivamente datasets con millones de puntos donde t-SNE es impráct ico.

**Ejemplo comparativo directo: Dataset de 100,000 documentos de noticias**

Vectores TF-IDF de 5,000 dimensiones:

**t-SNE:**
- Tiempo de ejecución: 45 minutos
- Visualización: Clusters temáticos claros (deportes, política, tecnología)
- Problema: Clusters temáticamente relacionados (ej: deportes vs entretenimiento) aparecen arbitrariamente lejos

**UMAP (n_neighbors=15, min_dist=0.1):**
- Tiempo de ejecución: 4 minutos (11x más rápido)
- Visualización: Mismos clusters temáticos claros
- Ventaja: Clusters relacionados (deportes, entretenimiento, cultura) forman una "región" más amplia, preservando estructura jerárquica

#### Fundamentos matemáticos de UMAP

UMAP se basa en topología algebraica y teoría de manifolds. Aunque la matemática subyacente es compleja, la intuición es accesible:

1. **Construir grafo de vecinos en espacio original:** Cada punto se conecta a sus k vecinos más cercanos con pesos basados en distancia
2. **Optimizar layout en espacio reducido:** Buscar configuración 2D/3D donde las conexiones del grafo se preserven lo más posible

Esta formulación permite a UMAP capturar tanto estructura local (vecinos cercanos) como global (conectividad de largo alcance en el grafo).

#### Parámetros clave de UMAP

**1. n_neighbors:**

Controla cuán "local" vs "global" es la estructura preservada. Análogo conceptual a perplexity en t-SNE.

- **Valores típicos:** 5-50
- **Valores bajos (5-10):** Enfatiza estructura muy local, puede fragmentar clusters
- **Valores altos (50-100):** Preserva más estructura global, pero puede perder detalles locales
- **Recomendación por defecto:** 15 (buen balance para mayoría de aplicaciones)

**2. min_dist:**

Controla qué tan "empaquetados" están los puntos en la visualización.

- **Valores típicos:** 0.0-0.5
- **min_dist=0.0:** Puntos pueden estar muy juntos, clusters muy compactos
- **min_dist=0.3-0.5:** Más espacio entre puntos, visualización menos densa
- **Recomendación:** 0.1 para visualización general, 0.0 para preservar máxima estructura de clusters

**3. n_components:**

Número de dimensiones de salida (típicamente 2 o 3 para visualización, puede ser mayor para preprocesamiento).

**4. metric:**

Métrica de distancia en espacio original.

- **'euclidean':** Por defecto, apropiada para mayoría de casos
- **'cosine':** Para datos de texto (TF-IDF, embeddings)
- **'manhattan':** Para datos categóricos codificados
- Muchas otras disponibles según el tipo de datos

```python
import umap
import matplotlib.pyplot as plt

# Aplicar UMAP con diferentes configuraciones
configs = [
    {'n_neighbors': 5, 'min_dist': 0.1, 'name': 'Local (n=5)'},
    {'n_neighbors': 15, 'min_dist': 0.1, 'name': 'Balanceado (n=15)'},
    {'n_neighbors': 50, 'min_dist': 0.1, 'name': 'Global (n=50)'}
]

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for idx, config in enumerate(configs):
    reducer = umap.UMAP(n_components=2,
                        n_neighbors=config['n_neighbors'],
                        min_dist=config['min_dist'],
                        random_state=42)
    datos_umap = reducer.fit_transform(datos_escalados)
    
    axes[idx].scatter(datos_umap[:, 0], datos_umap[:, 1],
                     c=etiquetas, cmap='viridis', alpha=0.6, s=10)
    axes[idx].set_title(config['name'])
    axes[idx].set_xlabel('UMAP 1')
    axes[idx].set_ylabel('UMAP 2')

plt.tight_layout()
plt.show()
```

**Ejemplo detallado: Análisis de productos de e-commerce**

Una plataforma tiene 25,000 productos caracterizados por 200 atributos: categoría, precio, dimensiones, características técnicas, palabras clave de descripción (vectorizadas), patrones de co-compra, etc.

**Objetivo:** Visualizar landscape completo de productos para identificar:
- Productos similares (competencia interna)
- Gaps en el catálogo
- Oportunidades de bundling

**Aplicación de UMAP (n_neighbors=20, min_dist=0.05, metric='euclidean'):**

Visualización 2D revela:

**Macro-estructura (preservación global):**
- Cuatro "continentes" principales claramente separados:
  - Continente 1: Electrónica y tecnología
  - Continente 2: Hogar y cocina
  - Continente 3: Ropa y accesorios
  - Continente 4: Deportes y aire libre

**Micro-estructura (preservación local):**
Dentro del continente de electrónica:
- Cluster denso: Smartphones y accesorios
- Cluster mediano: Laptops y computación
- Cluster pequeño: Audio y headphones
- Región dispersa: Cables, adaptadores, misceláneos

**Insights operacionales:**

1. **Gap identification:** Región vacía entre clusters de "computación" y "gaming" sugiere oportunidad para productos "gaming portátil" (laptops gaming de gama media).

2. **Bundling inteligente:** Productos cercanos en UMAP pero en clusters diferentes son candidatos para bundles (ej: laptop + mochila técnica, separados por categoría pero cercanos en UMAP por perfil de usuario).

3. **Competencia interna:** Dentro del cluster de smartphones, 15 productos están extremadamente cercanos (< 0.5 unidades UMAP) - investigar si hay canibalizacíón.

4. **Anomalías:** 3 productos de "electrónica" aparecen en el continente de "hogar" - revisar si están mal categorizados o tienen características híbridas únicas.

**Validación:** Equipo de merchandising valida que la estructura macro (4 continentes) y micro (clusters dentro de electrónica) corresponden a estructura real de negocio y comportamiento de compra.

### 5.5 PacMap: Robustez y balance mejorado

Pairwise Controlled Manifold Approximation (PacMap), desarrollado en 2021, representa la técnica más reciente de este trio. PacMap fue diseñado específicamente para superar limitaciones tanto de t-SNE como de UMAP, particularmente en preservación de estructura global y robustez a configuración de parámetros.

#### Diseño de PacMap

PacMap utiliza tres tipos de pares de puntos para guiar la proyección:

1. **Pares de vecinos (Neighbor pairs):** Puntos cercanos en alta dimensión que deben quedar cercanos en baja dimensión
2. **Pares de mid-near:** Puntos a distancia media que ayudan a preservar estructura global
3. **Pares lejanos (Further pairs):** Puntos distantes que deben quedar separados

Esta formulación explícita de múltiples escalas permite a PacMap preservar estructura desde lo muy local hasta lo global mejor que t-SNE o UMAP.

#### Ventajas de PacMap

**1. Mejor preservación de estructura global:**  
Distancias entre clusters en PacMap tienen más significado que en t-SNE, incluso más que en UMAP en algunos casos.

**2. Menor sensibilidad a parámetros:**  
Configuración por defecto funciona bien en amplio rango de datasets. Menos necesidad de tuning extensivo.

**3. Menor distorsión:**  
Formas y tamaños relativos de clusters se preservan mejor que en t-SNE o UMAP.

**4. Reproducibilidad:**  
Determinístico con semilla fijada, sin variabilidad entre ejecuciones.

#### Parámetros de PacMap

PacMap tiene menos parámetros que requieren ajuste que t-SNE o UMAP:

**n_neighbors:** Número de vecinos (default=10, típicamente no requiere ajuste)

**MN_ratio:** Proporción de pares mid-near (default=0.5, rara vez requiere cambio)

**FP_ratio:** Proporción de pares lejanos (default=2.0, rara vez requiere cambio)

```python
import pacmap
import matplotlib.pyplot as plt

# Aplicar PacMap con configuracion estandar
reducer = pacmap.PaCMAP(n_components=2, 
                        n_neighbors=10,
                        MN_ratio=0.5,
                        FP_ratio=2.0,
                        random_state=42)

datos_pacmap = reducer.fit_transform(datos_escalados)

plt.figure(figsize=(10, 8))
plt.scatter(datos_pacmap[:, 0], datos_pacmap[:, 1],
           c=etiquetas, cmap='viridis', alpha=0.6, s=10)
plt.xlabel('PacMap 1')
plt.ylabel('PacMap 2')
plt.title('Proyeccion PacMap')
plt.colorbar(label='Cluster')
plt.show()
```

**Ejemplo comparativo: Embeddings de lenguaje**

Un modelo de lenguaje genera embeddings de 768 dimensiones para 10,000 documentos científicos. Se comparan PCA, t-SNE, UMAP y PacMap:

**Estructura conocida:** Los documentos pertenecen a 5 áreas científicas con jerarquía:
- Ciencias Naturales
  - Física
  - Química
- Ciencias Sociales
  - Economía
  - Sociología
- Ingeniería

**Resultados comparativos:**

**PCA:** Las 5 áreas principales se distinguen parcialmente, pero hay considerable solapamiento. Estructura jerárquica no es evidente.

**t-SNE (perplexity=30):** Las 5 áreas aparecen como clusters claros y separados. Sin embargo, la proximidad entre áreas relacionadas (Física-Química, Economía-Sociología) no es consistente entre ejecuciones. En una ejecución, Física está cerca de Química; en otra, están en extremos opuestos.

**UMAP (n_neighbors=15):** Las 5 áreas son claras. Áreas relacionadas (Física-Química, Economía-Sociología) están consistentemente más cercanas entre sí que a áreas no relacionadas. Estructura jerárquica (Naturales vs Sociales vs Ingeniería) es parcialmente visible.

**PacMap (defaults):** Las 5 áreas son claras y la estructura jerárquica es evidente:
- Física y Química forman una "región" compacta (Ciencias Naturales)
- Economía y Sociología forman otra región (Ciencias Sociales)
- Ingeniería está entre ambas regiones, reflejando su naturaleza de aplicar ciencias naturales y sociales

Además, tamaños visuales de clusters corresponden aproximadamente a tamaños reales (# de documentos), algo que t-SNE no garantiza.

**Decisión operacional:** El equipo adopta PacMap para su herramienta de exploración de literatura científica, ya que la estructura jerárquica preservada ayuda a usuarios a navegar de lo general (Naturales vs Sociales) a lo específico (Física específicamente).

### 5.6 Comparativa PCA vs t-SNE vs UMAP vs PacMap

Para seleccionar el método apropiado en un proyecto, considerar los siguientes factores:

| Aspecto | PCA | t-SNE | UMAP | PacMap |
|---------|-----|-------|------|--------|
| **Velocidad** | Muy rápido (O(nd²)) | Lento (O(n²)) | Rápido (O(n log n)) | Rápido (O(n log n)) |
| **Escalabilidad** | Millones de puntos | <50k puntos | Millones de puntos | Millones de puntos |
| **Preservación local** | Pobre | Excelente | Excelente | Excelente |
| **Preservación global** | Excelente | Pobre | Buena | Muy buena |
| **Determinismo** | Sí | No | Configurable | Sí |
| **Sensibilidad a parámetros** | Mínima | Alta | Media | Baja |
| **Interpretabilidad** | Alta (componentes=combinaciones lineales) | Baja (solo visual) | Baja (solo visual) | Baja (solo visual) |
| **Linealidad** | Solo lineal | No lineal | No lineal | No lineal |
| **Distorsión de formas** | Mínima | Alta | Media | Baja |
| **Mejor para** | Preprocesamiento, compresión | Visualización exploratoria | Visualización + ML pipeline | Visualización preservando jerarquías |

#### Guía de selección práctica

**Usar PCA cuando:**
- Se requiere interpretabilidad (entender qué variables contribuyen a cada componente)
- Se necesita velocidad extrema o escalabilidad a millones de observaciones
- Los datos tienen estructura principalmente lineal
- Se busca compresión reversible (reconstrucción de datos originales)
- Se necesita como preprocesamiento rápido antes de otros algoritmos

**Usar t-SNE cuando:**
- Objetivo principal es visualización exploratoria de clusters
- Dataset es pequeño-mediano (<50,000 observaciones)
- Preservación de estructura local es crítica
- Se tiene tiempo para experimentar con múltiples perplexities
- Distancias globales entre clusters no son importantes

**Usar UMAP cuando:**
- Se necesita balance entre preservación local y global
- Dataset es grande (>50,000 observaciones) pero t-SNE es muy lento
- Se requiere reproducibilidad (con random_state fijo)
- La proyección se usará no solo para visualización sino como features en ML
- Se valora velocidad sin sacrificar calidad visual

**Usar PacMap cuando:**
- Preservación de jerarquías y estructura global es crítica
- Se busca mínima distorsión de formas y tamaños relativos
- Se prefiere minimizar tuning de parámetros (defaults funcionan bien)
- Se requiere máxima reproducibilidad
- Dataset tiene estructura multi-escala (local, media, global) importante

**Ejemplo de decisión en contexto real:**

**Proyecto:** Sistema de recomendación de contenido para plataforma educativa con 500,000 cursos.

**Características:** Cada curso representado por 200 variables (tema, dificultad, duración, ratings, keywords vectorizadas, etc.)

**Objetivo 1 - Compresión para modelo de recomendación:**  
**Decisión:** PCA a 50 componentes  
**Razón:** Velocidad, escalabilidad, interpretabilidad. Las 50 componentes se usan como features en modelo de collaborative filtering. PCA procesa 500k cursos en minutos; UMAP tomaría horas.

**Objetivo 2 - Dashboard de exploración para curadores de contenido:**  
**Decisión:** UMAP (n_neighbors=30, min_dist=0.1)  
**Razón:** Necesidad de visualizar 500k cursos interactivamente. UMAP es suficientemente rápido para actualizar visualización nightly. Preservación global permite a curadores ver "paisaje completo" de contenido e identificar gaps.

**Objetivo 3 - Herramienta de análisis jerárquico para estrategia de contenido:**  
**Decisión:** PacMap (defaults)  
**Razón:** Equipo de estrategia necesita entender estructura jerárquica (nivel superior: Ciencias, Humanidades, Técnico; nivel medio: sub-disciplinas; nivel específico: cursos individuales). PacMap preserva esta jerarquía mejor que alternativas.

Este ejemplo muestra que no hay una única "mejor" técnica - depende del objetivo específico y restricciones del proyecto.

### 5.7 Interpretación de visualizaciones y distancias

Independientemente del método elegido, interpretar visualizaciones de reducción de dimensionalidad requiere precaución:

**Principios generales:**

1. **Clusters bien separados son confiables:** Si grupos aparecen claramente separados en la visualización, típicamente reflejan separación real en alta dimensión.

2. **Distancias dentro de clusters son informativas:** Puntos cercanos dentro de un cluster están genuinamente cercanos en espacio original.

3. **Distancias entre clusters distantes son menos confiables:** La distancia específica entre cluster A y B puede ser artefacto del método de proyección.

4. **Tamaños visuales pueden engañar:** Cluster que ocupa más espacio visual no necesariamente tiene más puntos.

5. **Densidades son relativas:** Cluster visualmente denso vs disperso puede reflejar más el método de proyección que densidad real.

**Validación de visualizaciones:**

Nunca confiar ciegamente en una visualización. Validar mediante:

1. **Múltiples configuraciones:** Probar diferentes valores de parámetros. Estructura robusta persiste.

2. **Múltiples métodos:** Comparar PCA, t-SNE, UMAP. Patrones consistentes son más confiables.

3. **Análisis en espacio original:** Calcular estadísticas de clusters identificados visualmente en el espacio de alta dimensión original.

4. **Validación de dominio:** Consultar expertos si clusters visuales tienen interpretación lógica de negocio.

**Ejemplo de validación rigurosa:**

Análisis de 20,000 transacciones bancarias con 80 variables para detección de fraude. UMAP revela 3 clusters principales + varios puntos outliers.

**Validación ejecutada:**

1. **Diferentes parámetros UMAP:** n_neighbors=10, 20, 30 - estructura de 3 clusters persiste

2. **Comparación con t-SNE:** t-SNE (perplexity=20, 40) también muestra 3 clusters principales

3. **Análisis en espacio original:**
   - Cluster 1: Transacciones promedio $50, frecuencia alta, horarios diurnos
   - Cluster 2: Transacciones promedio $5,000, frecuencia baja, horarios variables
   - Cluster 3: Transacciones promedio $200, frecuencia media, horarios nocturnos/fines de semana
   
4. **Validación de negocio:**
   - Cluster 1: Compras cotidianas (supermercado, gasolina)
   - Cluster 2: Compras mayores (electrodomésticos, viajes)
   - Cluster 3: Entretenimiento (restaurantes, bares, eventos)

5. **Análisis de outliers:** Los 50 puntos alejados de los 3 clusters en UMAP tienen características extremas en original:
   - Monto extremadamente alto para tipo de comercio
   - Horarios inusuales (3am transacciones internacionales)
   - Patrones de secuencia rápida atípicos
   
   **Resultado:** 45 de los 50 outliers confirmados como fraude por equipo de seguridad.

Esta validación multi-capa da alta confianza en que la estructura visualizada refleja patrones reales en los datos.

---

## Evaluación de Entendimiento

Las siguientes preguntas permiten validar la comprensión de los conceptos, técnicas y consideraciones prácticas presentadas en este módulo. Se recomienda intentar responderlas sin consultar el contenido, y luego verificar las respuestas expandiendo cada sección.

### Sección 1: Fundamentos del Aprendizaje No Supervisado

**1. En un proyecto de análisis de logs de servidor, se identifican dos patrones claramente distintos de tráfico mediante clustering. Sin embargo, al presentar los resultados, el equipo de operaciones cuestiona si estos patrones corresponden a "tráfico normal vs ataque DDoS" o simplemente a "horarios diurnos vs nocturnos". ¿Qué aspecto fundamental del aprendizaje no supervisado ilustra esta situación y cómo debería abordarse?**

<details>
<summary>Ver respuesta</summary>

Esta situación ilustra la **ausencia de una verdad conocida** en aprendizaje no supervisado. Los algoritmos de clustering identifican patrones estadísticos en los datos (separación en dos grupos), pero no pueden asignar automáticamente significado o etiquetas a esos grupos.

**Abordaje apropiado:**

1. **Caracterización en espacio original:** Analizar las variables originales (horarios, IPs origen, tipos de request, volumen) para cada cluster identificado y determinar qué los diferencia

2. **Validación de dominio:** Consultar con expertos en operaciones que conozcan patrones de tráfico normal y ataques

3. **Análisis temporal:** Si los clusters se correlacionan perfectamente con horarios, la hipótesis "diurno vs nocturno" es más plausible; si aparecen en horarios aleatorios con características de volumen/patrón diferentes, "normal vs ataque" gana peso

4. **Validación cruzada con datos externos:** Correlacionar con logs de sistema de detección de intrusiones o alertas de seguridad conocidas

Este proceso de **interpretación posterior** es esencial en aprendizaje no supervisado y requiere combinar resultados algorítmicos con conocimiento del dominio.

</details>

**2. Un científico de datos reporta que un algoritmo de clustering ha "fallado" porque agrupa juntos clientes de diferentes regiones geográficas que el equipo de marketing maneja por separado. ¿Es esto necesariamente un fallo del algoritmo? Explique considerando los objetivos y naturaleza del aprendizaje no supervisado.**

<details>
<summary>Ver respuesta</summary>

No es necesariamente un fallo del algoritmo. Esta situación refleja una **desalineación entre los objetivos del algoritmo y las expectativas basadas en conocimiento previo**, no un error técnico.

**Análisis:**

**Lo que el algoritmo hizo:** Identificó similitudes en el espacio de características proporcionadas (comportamiento de compra, preferencias de producto, patrones de gasto) que trascienden las fronteras geográficas.

**Interpretación correcta:** Existen segmentos de clientes con comportamientos similares independientemente de su ubicación geográfica. Por ejemplo, "compradores de productos premium" pueden existir en todas las regiones.

**Valor potencial:** Este insight podría revelar:
- Oportunidades para estrategias de marketing unificadas por perfil de comportamiento
- Ineficiencias en gestión regional separada de clientes similares
- Segmentación alternativa más efectiva basada en comportamiento real vs geografía

**Si la geografía es realmente importante:** Existen opciones:
1. Incluir variables geográficas (latitud, longitud, región codificada) como features adicionales
2. Realizar clustering separado por región
3. Usar clustering jerárquico: primer nivel por geografía, segundo nivel por comportamiento

El "fallo" percibido es en realidad el algoritmo revelando estructura en los datos que contradice asunciones previas - exactamente el tipo de insight valioso que el aprendizaje no supervisado puede proporcionar.

</details>

### Sección 2: Clustering con K-Means

**3. Una empresa de telecomunicaciones aplica K-Means a datos de clientes con variables en escalas muy diferentes: minutos de llamada (0-5000), cantidad de SMS (0-500), y gasto mensual en dólares (10-300). Después de analizar los centroides, observan que todos los clusters se diferencian principalmente por minutos de llamada, mientras que SMS y gasto tienen valores muy similares entre clusters. ¿Qué está ocurriendo y cómo se corrige?**

<details>
<summary>Ver respuesta</summary>

**Problema identificado:** La variable "minutos de llamada" con rango mucho mayor (0-5000) domina completamente el cálculo de distancias euclidianas, eclipsando las otras variables.

**Explicación técnica:**

Si Cliente A tiene (2000 minutos, 100 SMS, $50) y Cliente B tiene (2100 minutos, 10 SMS, $200):

Distancia sin escalar:
$$d = \sqrt{(2100-2000)^2 + (100-10)^2 + (200-50)^2} = \sqrt{10000 + 8100 + 22500} = 201.7$$

Contribución porcentual:
- Minutos: 10000/40600 = 24.6%
- SMS: 8100/40600 = 20.0%
- Gasto: 22500/40600 = 55.4%

Aunque gasto contribuye más en este caso, cuando las diferencias en minutos son mayores, dominan totalmente.

**Solución - Estandarización:**

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
datos_escalados = scaler.fit_transform(datos_clientes)
```

Después de estandarizar (media=0, std=1), todas las variables contribuyen equitativamente:

$$d = \sqrt{z_{minutos}^2 + z_{SMS}^2 + z_{gasto}^2}$$

donde cada $z$ tiene la misma escala.

**Validación post-corrección:** Después de estandarizar, los centroides deberían mostrar diferenciación en las tres variables, no solo en minutos de llamada. Si SMS y gasto siguen siendo similares entre todos los clusters, entonces genuinamente no hay variación importante en esas dimensiones (no es artefacto de escala).

</details>

**4. Al aplicar el método del codo para seleccionar k en un dataset de transacciones de clientes, se observa la siguiente secuencia de inercia: k=2: 45000, k=3: 38000, k=4: 33000, k=5: 30000, k=6: 28000, k=7: 27000, k=8: 26500. No hay un "codo" obvio. Adicionalmente, los coeficientes de silueta son: k=2: 0.45, k=3: 0.38, k=4: 0.35, k=5: 0.32, k=6: 0.28, k=7: 0.25, k=8: 0.22. ¿Qué valor de k se debería elegir y por qué?**

<details>
<summary>Ver respuesta</summary>

**Análisis de evidencia:**

**Inercia:** Decrece consistentemente sin codo claro, indicando que el dataset no tiene estructura de clusters claramente separados. Cada k adicional mejora el ajuste gradualmente.

**Silueta:** Disminuye consistentemente con k creciente. Valores absolutos:
- k=2: 0.45 (estructura razonable)
- k=3: 0.38 (estructura aceptable)
- k=4-8: <0.35 (estructura débil)

**Recomendación: k=2 o k=3**

**Justificación:**

1. **Criterio de silueta:** k=2 tiene mejor score (0.45), pero k=3 mantiene score aceptable (0.38) con más granularidad

2. **Balance complejidad-calidad:** La caída de silueta de 0.45→0.38 (7 puntos) al pasar de k=2 a k=3 es menor que caídas subsecuentes (0.38→0.35 es 3 puntos pero luego aceleran)

3. **Utilidad práctica:** k=2 puede ser demasiado grueso para acción de negocio; k=3 ofrece segmentación más accionable

**Consideraciones adicionales:**

- **Contexto de negocio:** Si la empresa solo puede manejar 2 campañas de marketing distintas, k=2 es apropiado. Si puede manejar 3-4, k=3 ofrece mejor balance.

- **Realidad de los datos:** La ausencia de codo claro y siluetas decrecientes sugiere que este dataset puede no tener estructura natural de clusters bien definidos. Podría ser más un continuum que grupos discretos.

- **Alternativa:** Considerar que clustering jerárquico permitiría explorar múltiples niveles de granularidad sin comprometerse a un k específico desde el inicio.

**Decisión final recomendada:** Comenzar con k=3 (balance entre calidad de silueta y granularidad útil), pero estar preparado para que los clusters tengan fronteras difusas y requieran interpretación cuidadosa.

</details>

### Sección 3: Clustering Jerárquico

**5. En un análisis de clustering jerárquico de 200 sucursales de una cadena de retail, se comparan los resultados de linkage completo y linkage de Ward. Con complete linkage, se identifican 8 clusters de tamaños muy desiguales (cluster más grande: 80 sucursales, varios clusters con 5-10 sucursales). Con Ward, se identifican 8 clusters de tamaños más balanceados (20-35 sucursales cada uno). ¿Por qué ocurre esta diferencia y cuál método es preferible?**

<details>
<summary>Ver respuesta</summary>

**Explicación de la diferencia:**

**Complete linkage:** Define distancia entre clusters como la distancia entre los puntos **más lejanos** de cada cluster. Esto tiende a:
- Crear clusters compactos y esféricos
- Ser sensible a outliers (una sucursal atípica puede quedar aislada)
- Producir clusters de tamaños desiguales (sucursales atípicas forman clusters pequeños, mainstream forma clusters grandes)

**Ward:** Minimiza la varianza intra-cluster (inercia). En cada paso, fusiona los dos clusters cuya unión produce el menor incremento en varianza total. Esto tiende a:
- Producir clusters de tamaños más balanceados
- Maximizar homogeneidad dentro de cada cluster
- Ser robusto a outliers individuales

**¿Cuál es preferible?**

Depende del objetivo:

**Preferir Ward cuando:**
- Se requieren clusters de tamaños balanceados para operaciones (ej: asignar 8 gerentes regionales, uno por cluster)
- El objetivo es maximizar similitud dentro de cada grupo
- Outliers no requieren tratamiento especial separado

**Preferir Complete linkage cuando:**
- Es importante identificar explícitamente outliers como grupos pequeños separados
- Se prefiere garantía de compacidad de clusters (todos los miembros relativamente cercanos entre sí)
- Tamaños desiguales son aceptables o incluso deseables

**En el contexto de retail:**

**Si el objetivo es:** Agrupar sucursales para estrategias de operación y marketing → **Ward es preferible**. Clusters balanceados permiten distribuir recursos equitativamente.

**Si el objetivo es:** Identificar sucursales excepcionales (muy alto o muy bajo rendimiento) para análisis especial → **Complete linkage es preferible**. Los clusters pequeños señalan sucursales que requieren atención individualizada.

**Recomendación práctica:** Ejecutar ambos métodos. Si los 8 clusters de Ward son suficientemente homogéneos (bajo SSW) y los clusters pequeños de complete linkage no son particularmente interesantes, usar Ward. Si los clusters pequeños de complete linkage revelan outliers valiosos, combinar enfoques: Ward para la mayoría, tratamiento especial para outliers identificados por complete linkage.

</details>

**6. Al construir un dendrograma de 500 empleados basado en competencias y desempeño, un analista observa que la altura de fusión aumenta gradualmente hasta aproximadamente h=15, luego hay un salto grande a h=28, seguido de otro salto a h=45. ¿Qué información proporcionan estos saltos y cómo se deberían usar para decidir el número de clusters?**

<details>
<summary>Ver respuesta</summary>

**Interpretación de alturas de fusión:**

Las alturas en el dendrograma representan la distancia (o disimilitud) entre los clusters que se están fusionando en cada paso.

- **Fusiones a baja altura (gradual hasta h=15):** Empleados o grupos muy similares
- **Salto grande h=15 → h=28:** Fusión de grupos moderadamente distintos
- **Salto grande h=28 → h=45:** Fusión de grupos muy distintos

**Principio clave:** Saltos grandes en altura indican que se están fusionando clusters naturalmente separados. Cortar **antes** de un salto grande preserva esa separación natural.

**Aplicación a este caso:**

**Opción 1 - Cortar antes del primer salto grande (h < 28):**
Número de clusters resultante depende de cuántos "ramas" hay en el dendrograma en h=15-27. Supongamos que resulta en **4 clusters**.

**Interpretación:** 4 grupos principales de perfiles de empleados con diferencias moderadas-altas entre ellos.

**Opción 2 - Cortar antes del segundo salto (h entre 28-44):**
Supongamos que resulta en **2 clusters**.

**Interpretación:** 2 grupos macro muy distintos (ej: empleados técnicos vs no-técnicos, o alto rendimiento vs desarrollo necesario).

**Decisión recomendada:**

1. **Probar ambos cortes:** Examinar tanto la solución de 4 clusters como la de 2 clusters

2. **Análisis jerárquico:** Si se elige 2 clusters, examinar los sub-clusters dentro de cada uno (que serían los 4 clusters de la opción 1). Esto permite entender jerarquía: 2 grandes grupos, cada uno con sub-grupos internos.

3. **Validación de negocio:**
   - Si HR puede diseñar programas de desarrollo diferenciados para 4 perfiles, usar 4 clusters
   - Si solo hay recursos para 2 estrategias principales, usar 2 clusters

4. **Análisis de características:** Para cada solución, caracterizar los clusters en términos de competencias y desempeño:
   - ¿Los 4 clusters tienen interpretación clara de negocio?
   - ¿Los 2 clusters son demasiado gruesos y pierden información útil?

**Indicador cuantitativo adicional:** Calcular el coeficiente de silueta para k=2, k=3, k=4. Si k=4 tiene silueta significativamente mejor que k=2, esto valida que la estructura de 4 grupos es robusta.

**Respuesta final:** Los saltos grandes sugieren probar k=2 (muy alto nivel) y k=4 (primer salto). La decisión final debe combinar interpretabilidad de negocio con validación cuantitativa (silueta, homogeneidad intra-cluster).

</details>

### Sección 4: Análisis de Componentes Principales (PCA)

**7. En un análisis PCA de datos de manufactura con 20 variables (temperaturas, presiones, velocidades de diferentes etapas del proceso), las primeras 5 componentes principales explican 35%, 18%, 12%, 8% y 6% de la varianza respectivamente. El equipo de ingeniería necesita monitorear el proceso en tiempo real pero el sistema de visualización solo puede graficar 2 dimensiones. ¿Es razonable usar solo PC1 y PC2 para monitoreo? ¿Qué análisis adicional se requiere para tomar esta decisión?**

<details>
<summary>Ver respuesta</summary>

**Análisis inicial:**

PC1 + PC2 explican 35% + 18% = **53% de varianza total**. Esto significa que **47% de la variación en los datos NO está capturada** en el monitoreo 2D propuesto.

**¿Es suficiente 53%?**

No hay respuesta universal - depende de qué tipo de variación está en el 47% no capturado:

**Análisis adicional requerido:**

**1. Varianza explicada acumulada extendida:**

Calcular para más componentes:
- PC1-5: 35+18+12+8+6 = 79%
- PC1-8: Supongamos 88%
- PC1-10: Supongamos 93%

Si se necesitan 10+ componentes para explicar >90%, esto sugiere que la variación importante está distribuida en muchas dimensiones.

**2. Análisis de loadings de PC1 y PC2:**

Examinar qué variables tienen loadings altos en PC1 y PC2:

**Escenario A - Favorable:**
- PC1 captura principalmente temperaturas (variables críticas para calidad)
- PC2 captura presiones (variables críticas para seguridad)
- Las componentes ignoradas (PC3-20) capturan principalmente ruido o variables secundarias

→ **Usar PC1-PC2 es razonable**

**Escenario B - Desfavorable:**
- PC1 y PC2 capturan principalmente velocidades y tiempos (variables operativas)
- PC3 captura temperaturas críticas (14% de varianza)
- PC4 captura presiones críticas (9% de varianza)

→ **Usar solo PC1-PC2 es arriesgado** - pierde información crítica

**3. Análisis de casos conocidos de falla:**

Si existen datos históricos de fallas o problemas de calidad:
- Proyectar estos casos al espacio PC1-PC2
- ¿Son visibles como outliers o patrones anormales?
- Si NO son detectables en PC1-PC2, el monitoreo 2D es insuficiente

**4. Comparación de alternativas:**

**Opción A:** Usar PC1-PC2 únicamente (53% varianza)

**Opción B:** Crear múltiples vistas 2D:
- Vista 1: PC1 vs PC2
- Vista 2: PC3 vs PC4
- Vista 3: PC5 vs PC6

Esto captura ~79% de varianza en tres gráficos monitoreables.

**Opción C:** Usar índice de distancia multivariado:

$$T^2 = \sum_{i=1}^{k} \left(\frac{score_i}{\sqrt{\lambda_i}}\right)^2$$

Donde k=5-10 componentes principales, $\lambda_i$ son los eigenvalues. Este índice escalar resume desviación del proceso normal en múltiples dimensiones.

**Recomendación:**

1. **Realizar análisis de loadings y casos de falla** antes de decidir
2. **Si análisis es favorable:** Usar PC1-PC2 para monitoreo visual principal + alarma automática basada en índice T² con más componentes
3. **Si análisis es desfavorable:** Implementar múltiples vistas 2D o considerar métodos de reducción no lineal (UMAP podría capturar más estructura en 2D)

**Respuesta directa:** No es automáticamente razonable usar solo PC1-PC2 cuando capturan solo 53% de varianza. Se requiere validar que el 53% capturado incluye la variación crítica para el objetivo de monitoreo.

</details>

**8. Al interpretar los loadings de la primera componente principal en un análisis de perfiles de inversión de clientes, se observan los siguientes valores: acciones_tecnologia: 0.42, acciones_energia: 0.38, bonos_gubernamentales: -0.35, bonos_corporativos: -0.31, efectivo: -0.48, bienes_raices: 0.18. ¿Cómo se interpreta esta componente y qué representa un score alto vs bajo en PC1?**

<details>
<summary>Ver respuesta</summary>

**Interpretación de loadings:**

Los loadings indican cuánto contribuye cada variable original a la componente principal. Signos opuestos indican variables que varían en direcciones contrarias.

**Agrupación por signo:**

**Loadings positivos (contribuyen positivamente a PC1):**
- acciones_tecnologia: +0.42 (fuerte)
- acciones_energia: +0.38 (fuerte)
- bienes_raices: +0.18 (moderado)

**Loadings negativos (contribuyen negativamente a PC1):**
- efectivo: -0.48 (muy fuerte)
- bonos_gubernamentales: -0.35 (fuerte)
- bonos_corporativos: -0.31 (fuerte)

**Interpretación conceptual de PC1:**

PC1 representa un **espectro de riesgo en la estrategia de inversión**:

**Score alto en PC1 (positivo):**
- Alto % en acciones (tecnología, energía) - activos de alto riesgo/alto retorno
- Bajo % en efectivo y bonos - activos de bajo riesgo/bajo retorno
- **Perfil:** Inversor agresivo, tolerancia alta al riesgo, horizonte largo

**Score bajo en PC1 (negativo):**
- Alto % en efectivo y bonos - activos seguros y líquidos
- Bajo % en acciones - evita volatilidad
- **Perfil:** Inversor conservador, prioriza preservación de capital, puede necesitar liquidez

**Aplicación práctica:**

Un cliente con score PC1 = +2.5:
- Portafolio dominado por acciones, particularmente tecnología
- Mínimo efectivo y bonos
- **Recomendación de asesor:** Verificar que este perfil agresivo es apropiado para edad, objetivos y tolerancia real al riesgo del cliente

Un cliente con score PC1 = -1.8:
- Portafolio conservador con alta proporción de efectivo y bonos
- Pocas acciones
- **Recomendación de asesor:** Si el cliente es joven con horizonte de 30+ años, educar sobre beneficios de mayor exposición a equities

**Nota sobre magnitudes de loadings:**

Los loadings más altos en valor absoluto son efectivo (-0.48) y acciones_tecnologia (+0.42), indicando que estas son las variables que más influyen en PC1. Bienes_raices tiene loading moderado (+0.18), sugiriendo que su presencia es algo consistente con perfil agresivo pero no es el factor dominante.

**Comparación con scores reales:**

Si se calcula:
$$PC1 = 0.42 \times acciones_{tec} + 0.38 \times acciones_{ener} + 0.18 \times bienes_{raices} - 0.35 \times bonos_{gub} - 0.31 \times bonos_{corp} - 0.48 \times efectivo$$

(Asumiendo variables estandarizadas)

Un cliente con alto % de acciones_tec y bajo % de efectivo tendrá score positivo alto. Un cliente con alto % de efectivo y bajo % de acciones tendrá score negativo alto (en valor absoluto).

</details>

### Sección 5: Métodos Modernos de Reducción de Dimensionalidad

**9. Un equipo de científicos de datos está decidiendo entre t-SNE y UMAP para visualizar 100,000 vectores de embeddings de productos de 512 dimensiones. La visualización se actualizará semanalmente con nuevos productos, y se usará tanto para exploración interactiva por analistas como para alimentar un algoritmo de clustering aguas abajo. ¿Qué método es más apropiado y por qué? ¿Qué configuración de parámetros se debería usar?**

<details>
<summary>Ver respuesta</summary>

**Análisis de requerimientos:**

1. **Tamaño del dataset:** 100,000 observaciones - grande
2. **Actualización semanal:** Se re-ejecutará frecuentemente
3. **Exploración interactiva:** Necesidad de visualización clara de estructura
4. **Clustering aguas abajo:** Las componentes reducidas se usarán como features en ML
5. **Dimensionalidad original:** 512D - alta

**Comparación t-SNE vs UMAP:**

| Factor | t-SNE | UMAP |
|--------|-------|------|
| Velocidad en 100k puntos | Muy lento (~horas con Barnes-Hut) | Rápido (~10-20 minutos) |
| Actualizaciones semanales | Impráctico por tiempo | Factible |
| Calidad visualización | Excelente para estructura local | Excelente, mejor estructura global |
| Uso en clustering posterior | No recomendado (distorsión) | Apropiado (preserva mejor distancias) |
| Reproducibilidad | Requiere múltiples ejecuciones | Determinístico con random_state |

**Recomendación: UMAP**

**Justificación:**

1. **Velocidad:** Con 100,000 puntos, t-SNE será prohibitivamente lento para actualizaciones semanales. UMAP es 10-50x más rápido.

2. **Clustering aguas abajo:** UMAP preserva mejor estructura global que t-SNE, haciendo sus embeddings más apropiados como input para clustering. t-SNE distorsiona distancias globales severamente.

3. **Reproducibilidad:** UMAP con `random_state` fijo produce resultados consistentes, facilitando comparación semana-a-semana.

4. **Preservación global:** Para exploración interactiva donde analistas quieren entender relaciones entre categorías de productos, UMAP ofrece visualización más interpretable.

**Configuración de parámetros recomendada:**

```python
import umap

reducer = umap.UMAP(
    n_components=2,          # Para visualización 2D
    n_neighbors=30,          # Valor moderado-alto para dataset grande
    min_dist=0.1,           # Balance entre compactación y separación
    metric='cosine',         # Apropiado para embeddings (alternativa a euclidean)
    random_state=42,        # Reproducibilidad
    n_jobs=-1               # Paralelización para velocidad
)

embeddings_2d = reducer.fit_transform(embeddings_productos)
```

**Justificación de parámetros:**

- **n_neighbors=30:** Para dataset grande (100k), valor moderado-alto preserva estructura global sin sacrificar detalle local. Valores muy bajos (5-10) pueden fragmentar; valores muy altos (>50) pueden sobre-suavizar.

- **min_dist=0.1:** Default que funciona bien para mayoría de casos. Permite clusters compactos pero sin amontonamiento excesivo.

- **metric='cosine':** Para embeddings de productos (típicamente vectores de redes neuronales), distancia coseno captura similitud semántica mejor que euclidiana. Si los embeddings ya están normalizados, euclidean y cosine son equivalentes.

**Flujo de trabajo completo:**

1. **Semana 1:** Aplicar UMAP a productos iniciales, visualizar
2. **Semana 2-N:** Para nuevos productos, usar `reducer.transform(nuevos_embeddings)` si UMAP lo soporta en la versión, o re-entrenar UMAP completo (factible por velocidad)
3. **Clustering:** Aplicar K-Means o DBSCAN sobre embeddings_2d resultantes
4. **Validación:** Comparar clusters de semana a semana para detectar cambios en catálogo

**Alternativa si t-SNE fuera necesario:**

Si por alguna razón específica t-SNE fuera requerido (ej: stakeholders familiarizados con su output):
- Usar Barnes-Hut t-SNE (implementación por defecto sklearn)
- Considerar submuestreo estratificado a 50k productos para acelerar
- Ejecutar overnight en infraestructura más potente
- Configuración: `perplexity=50, n_iter=2000, learning_rate=200`

Pero UMAP es objetivamente superior para este caso de uso específico.

</details>

**10. Después de aplicar PacMap a un dataset de imágenes médicas, un radiólogo observa que la visualización muestra tres regiones principales (tejido normal, lesiones benignas, lesiones malignas) con tamaños visuales proporcionales al número de imágenes en cada categoría. Sin embargo, al aplicar t-SNE al mismo dataset, las tres categorías aparecen como clusters de tamaño visual similar, independientemente del número de imágenes. ¿Por qué ocurre esta diferencia y cuál visualización es más informativa para comunicar resultados a un equipo médico no técnico?**

<details>
<summary>Ver respuesta</summary>

**Explicación de la diferencia:**

**PacMap:** Diseñado específicamente para preservar estructura global con mínima distorsión. Esto incluye preservar proporciones relativas y formas de regiones de datos. Si hay 10,000 imágenes de tejido normal, 2,000 de lesiones benignas y 500 de lesiones malignas, PacMap tenderá a representar estas proporciones en la visualización (región grande, mediana, pequeña).

**t-SNE:** Optimiza para preservar vecindarios locales (relaciones dentro de cada cluster) pero no preserva:
- Tamaños relativos de clusters
- Densidades relativas
- Distancias absolutas entre clusters

t-SNE puede hacer que un cluster pequeño y denso (500 imágenes malignas muy similares entre sí) aparezca con el mismo tamaño visual que un cluster grande y disperso (10,000 imágenes normales con más variación).

**Razón técnica:**

t-SNE modela similitudes mediante probabilidades que se normalizan localmente. Cada punto tiene una distribución de probabilidad sobre sus vecinos que suma 1, independientemente de la densidad global de su región. Esto significa que puntos en un cluster pequeño "expanden" visualmente su espacio.

PacMap utiliza pares de puntos a múltiples escalas (vecinos, mid-near, further) de manera que preserva mejor la estructura multi-escala, incluyendo proporciones.

**¿Cuál visualización es más informativa para equipo médico?**

**Para comunicación a equipo no técnico: PacMap es preferible**

**Justificación:**

1. **Proporciones realistas:** Equipo médico entiende intuitivamente que tejido normal es mucho más prevalente que lesiones malignas. PacMap comunica esto visualmente; t-SNE lo oculta.

2. **Menos malinterpretaciones:** Con t-SNE, un médico podría interpretar erróneamente que las tres categorías tienen prevalencia similar, lo cual es clínicamente incorrecto y puede afectar percepción de riesgo.

3. **Preservación de jerarquía:** Si hay subtipos dentro de cada categoría principal (ej: diferentes tipos de lesiones benignas), PacMap preserva mejor estas relaciones jerárquicas.

**Presentación recomendada para equipo médico:**

```
Visualización PacMap con anotaciones:
- Región grande (normal): ~10,000 imágenes - 75% del dataset
- Región mediana (benigno): ~2,000 imágenes - 15% del dataset
- Región pequeña (maligno): ~500 imágenes - 10% del dataset
```

**Agregar estadísticas complementarias:**
- Dentro de cada región, mostrar métricas de homogeneidad
- Resaltar casos fronterizos entre normal/benigno o benigno/maligno
- Identificar outliers que requieren revisión manual

**Cuándo t-SNE sería apropiado:**

Si el objetivo fuera diferente - por ejemplo, **validar que el modelo de clasificación puede distinguir entre las tres categorías** - entonces t-SNE podría ser apropiado:
- Si las tres categorías forman clusters bien separados en t-SNE, el modelo tiene buena separabilidad
- El tamaño visual uniforme no es un problema porque no se está comunicando prevalencia

Pero para comunicar composición del dataset y estructura general a audiencia no técnica, **PacMap es superior** por su menor distorsión de proporciones y estructura global.

**Validación adicional:**

Para confirmar que PacMap está preservando correctamente:
- Contar programáticamente cuántos puntos hay en cada región visual
- Verificar que corresponde a counts reales de categorías
- Si PacMap también está distorsionando (ej: región visual de malignos parece tener 30% del espacio cuando solo es 10% de puntos), entonces quizás la visualización necesita ajuste de parámetros o interpretación cuidadosa

</details>

---

