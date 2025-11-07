# Plan Módulo 3: Métodos de Aprendizaje No Supervisado

## Información General

**Descripción del módulo:**  
Este módulo cubre técnicas de aprendizaje no supervisado aplicadas al descubrimiento de patrones, segmentación de datos y reducción de dimensionalidad en conjuntos de datos complejos. El aprendizaje no supervisado constituye una herramienta fundamental en entornos profesionales donde los datos no vienen etiquetados previamente, permitiendo extraer estructura y conocimiento de información sin clasificaciones predefinidas.

**Tecnologías utilizadas:**  
- Scikit-learn (K-Means, clustering jerárquico, PCA, t-SNE)
- UMAP (reducción de dimensionalidad no lineal)
- PacMap (visualización preservando estructura local y global)
- Pandas (manipulación de datos)
- Matplotlib/Seaborn (visualización)
- Jupyter Notebook (entorno de desarrollo)

**Objetivos de aprendizaje:**  
Este módulo desarrolla competencias para aplicar técnicas de aprendizaje no supervisado en contextos profesionales, incluyendo segmentación de clientes, reducción de dimensionalidad para visualización y análisis exploratorio, e interpretación de resultados para generación de insights accionables de negocio.

---

## Estructura de Contenidos

### Sección 1: Fundamentos del Aprendizaje No Supervisado

**Objetivo:**  
Introducir los conceptos fundamentales del aprendizaje no supervisado y sus aplicaciones en la industria.

**Contenidos:**
- Por qué empezar con aprendizaje no supervisado en lugar de con supervisado? 
- Definición de aprendizaje no supervisado y diferencias fundamentales con aprendizaje supervisado
- Aprender sobre columnas o aprender sobre filas
- Tipos principales de problemas: clustering, reducción de dimensionalidad, detección de anomalías
- Aplicaciones en industria: segmentación de clientes, compresión de datos, visualización exploratoria
- Desafíos particulares: ausencia de métricas de evaluación obvias, interpretabilidad de resultados

**Casos de uso en industria:**
- Descubrimiento de segmentos de clientes sin categorías predefinidas para estrategias de marketing diferenciadas
- Identificación de patrones de comportamiento en datos de transacciones para detección de anomalías
- Análisis exploratorio de datasets de alta dimensionalidad en investigación y desarrollo

---

### Sección 2: Clustering con K-Means

**Objetivo:**  
Dominar el algoritmo K-Means para segmentación de datos en entornos profesionales.

**Contenidos:**
- Fundamentos matemáticos del algoritmo K-Means y objetivo de minimización
- Proceso iterativo: inicialización de centroides, asignación de puntos, actualización de centroides
- Distancia euclidiana como métrica de similitud y sensibilidad a escalas de variables
- Métodos para selección del número óptimo de clusters: método del codo (elbow method) y coeficiente de silueta
- Interpretación de centroides como perfiles representativos de cada segmento
- Limitaciones del algoritmo: sensibilidad a inicialización, formas de clusters, outliers

**Casos de uso en industria:**
- Segmentación de base de clientes para personalización de estrategias de marketing y retención
- Identificación de perfiles de consumo para optimización de inventario y recomendaciones
- Agrupación de productos por características de venta para gestión de categorías
- Clasificación de comportamientos de uso en plataformas digitales

---

### Sección 3: Clustering Jerárquico

**Objetivo:**  
Aplicar técnicas de clustering jerárquico para explorar estructuras de datos a múltiples niveles de granularidad.

**Contenidos:**
- Comparación intuitiva con K-means. Ventajas y limitaciones frente a K-Means: flexibilidad vs escalabilidad
- Fundamentos de clustering jerárquico: construcción bottom-up de agrupaciones
- Diferencia entre métodos aglomerativos (bottom-up) y divisivos (top-down)
- Dendrogramas: interpretación visual de jerarquías de agrupación
- Métodos de enlace (linkage): single, complete, average, Ward
- Comparación de métodos de enlace: cuándo usar cada uno según la estructura esperada
- Criterios para determinar el punto de corte del dendrograma

**Casos de uso en industria:**
- Desarrollo de taxonomías de productos sin categorías predefinidas para e-commerce
- Análisis de jerarquías naturales en bases de clientes para estrategias de múltiples niveles
- Segmentación flexible de mercados explorando diferentes niveles de granularidad
- Organización de documentos o artículos por similitud temática

---

### Sección 4: Análisis de Componentes Principales (PCA)

**Objetivo:**  
Aplicar PCA para reducción de dimensionalidad preservando la información más relevante para análisis y visualización.

**Contenidos:**
- Fundamentos matemáticos de PCA: proyección en direcciones de máxima varianza
- Componentes principales como combinaciones lineales de variables originales
- Concepto de varianza explicada y su interpretación
- Criterios para selección del número de componentes: varianza acumulada, scree plot
- Interpretación de pesos (loadings) para entender qué variables originales contribuyen a cada componente
- Visualización en 2D/3D de datos de alta dimensionalidad
- Limitaciones: linealidad, sensibilidad a outliers, pérdida de interpretabilidad directa
- Preprocesamiento/supuesto necesario: estandarización de variables

**Casos de uso en industria:**
- Compresión de datos de sensores industriales para almacenamiento y transmisión eficiente
- Visualización de portafolios financieros en espacios de menor dimensión
- Reducción de dimensionalidad como preprocesamiento para modelos de machine learning
- Identificación de factores latentes en encuestas o estudios de mercado
- Detección de patrones en imágenes hiperespectrales o datos genómicos

---

### Sección 5: Métodos Modernos de Reducción de Dimensionalidad

**Objetivo:**  
Aplicar técnicas avanzadas de reducción de dimensionalidad para visualización de datos con estructuras no lineales.

**Contenidos:**
- Limitaciones fundamentales de PCA para datos no lineales y estructuras complejas
- t-SNE: visualización mediante preservación de vecindarios locales
  - Fundamentos: minimización de divergencia entre distribuciones de probabilidad
  - Parámetros clave: perplexity (tamaño de vecindario), learning_rate, n_iter
  - Interpretación correcta: preservación de estructura local, no de distancias globales
  - Limitaciones: no determinístico, sensible a parámetros, lento en datasets grandes
- UMAP: principios de preservación de estructura local y global
  - Parámetros clave: n_neighbors (escala local), min_dist (densidad), n_components
  - Ventajas sobre t-SNE: más rápido, mejor preservación global, determinístico
  - Cuándo usar UMAP: datos con manifolds no lineales, visualización de clusters complejos
- PacMap: diseño para preservación balanceada de pares de puntos
  - Ventajas sobre UMAP y t-SNE: mejor preservación de estructura global, menor distorsión
  - Parámetros y configuraciones recomendadas
- Comparativa PCA vs t-SNE vs UMAP vs PacMap:
  - PCA: rápido, interpretable, lineal, mejor para varianza estructurada linealmente
  - t-SNE: excelente preservación local, ideal para exploración visual, lento en datos grandes
  - UMAP: balance local-global, rápido, reproducible, requiere tuning de parámetros
  - PacMap: mejor preservación global, robusto, menos sensible a parámetros
- Interpretación de visualizaciones: distancias relativas vs estructura de clusters vs densidades locales

**Casos de uso en industria:**
- Visualización exploratoria de embeddings de texto generados por modelos de lenguaje (BERT, GPT)
- Análisis exploratorio de datos genómicos o proteómicos de alta dimensionalidad
- Detección visual de anomalías en espacios complejos (cyberseguridad, fraude)
- Exploración de espacios latentes en sistemas de recomendación
- Validación cualitativa de segmentaciones o clasificaciones complejas
- Visualización de datasets de imágenes para identificación de patrones y grupos naturales
