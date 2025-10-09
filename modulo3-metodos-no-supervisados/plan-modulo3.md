# Plan Módulo 3: Métodos de Aprendizaje No Supervisado

## Información General
- **Duración:** ~4 horas
- **Nivel:** Intermedio
- **Prerrequisitos:** Conocimientos básicos de Python, Pandas, y conceptos fundamentales de estadística
- **Objetivo:** Desarrollar competencias en técnicas de aprendizaje no supervisado para descubrir patrones, segmentar datos y reducir dimensionalidad en conjuntos de datos complejos.

---

## Proceso de Desarrollo del Módulo

### Fase 1: Planificación ✅
- [x] Definir objetivos de aprendizaje
- [x] Estructurar contenidos
- [x] Establecer casos de uso empresariales

### Fase 2: Contenido Teórico 
- [ ] `modulo3-metodos-no-supervisados.md` - Contenido teórico completo

### Fase 3: Laboratorio Práctico 
- [ ] `lab3-aprendizaje-no-supervisado.ipynb` - Ejercicios prácticos con contexto empresarial

### Fase 4: Guión Narrativo 
- [ ] `guion-modulo3-no-supervisado.md` - Segmentos de ~5 minutos cada uno

---

## Estructura de Contenidos

### Sección 1: Fundamentos del Aprendizaje No Supervisado (30 minutos)
**Objetivo:** Introducir los conceptos fundamentales del aprendizaje no supervisado y sus aplicaciones en la industria.

**Contenidos:**
- ¿Qué es el aprendizaje no supervisado? (10 min)
- Diferencias con aprendizaje supervisado (5 min)
- Aplicaciones principales: segmentación, detección de anomalías, exploración de datos (15 min)

**Caso empresarial principal:** Descubrimiento de patrones en comportamiento de clientes sin etiquetas predefinidas

### Sección 2: Clustering K-Means (60 minutos)
**Objetivo:** Dominar el algoritmo de clustering más utilizado en la industria para segmentación de datos.

**Contenidos:**
- Fundamentos del algoritmo K-Means (10 min)
- El proceso iterativo: inicialización, asignación, actualización (15 min)
- Distancia euclidiana y su sensibilidad a la escala (10 min)
- Elección del número óptimo de clusters: método del codo y coeficiente de silueta (15 min)
- Interpretación de centroides para insights de negocio (10 min)

**Casos empresariales:**
- Segmentación de clientes para marketing personalizado
- Identificación de perfiles de consumo
- Agrupación de productos por características similares

### Sección 3: Clustering Jerárquico (50 minutos)
**Objetivo:** Aplicar técnicas de clustering jerárquico para explorar estructuras de datos a múltiples niveles de granularidad.

**Contenidos:**
- Fundamentos del clustering jerárquico (10 min)
- Agrupamiento aglomerativo vs divisivo (10 min)
- Dendrogramas: construcción e interpretación (15 min)
- Métodos de enlace: single, complete, average, Ward (10 min)
- Criterios para corte del dendrograma (5 min)

**Casos empresariales:**
- Taxonomía de productos sin categorías predefinidas
- Análisis de jerarquías de clientes
- Segmentación flexible de mercados

### Sección 4: Análisis de Componentes Principales - PCA (60 minutos)
**Objetivo:** Reducir la dimensionalidad de datos preservando la información más relevante para análisis y visualización.

**Contenidos:**
- Fundamentos de PCA y reducción de dimensionalidad (10 min)
- Varianza explicada y componentes principales (15 min)
- Componentes como combinaciones lineales de variables originales (15 min)
- Criterios para selección del número de componentes (10 min)
- Visualización en 2D/3D y aplicaciones (10 min)

**Casos empresariales:**
- Compresión de datos de sensores industriales
- Visualización de portfolios financieros
- Preprocesamiento para modelos de machine learning

### Sección 5: Métodos Modernos de Reducción de Dimensionalidad (40 minutos)
**Objetivo:** Aplicar técnicas avanzadas para visualización de datos de alta dimensionalidad con estructuras no lineales.

**Contenidos:**
- Limitaciones de PCA para datos no lineales (5 min)
- Introducción a UMAP: principios y parámetros clave (15 min)
- Introducción a PacMap: ventajas sobre UMAP (10 min)
- Comparativa PCA vs UMAP vs PacMap (5 min)
- Aplicaciones en visualización de datos complejos (5 min)

**Casos empresariales:**
- Visualización de embeddings de texto
- Análisis exploratorio de datos genómicos
- Detección de anomalías en datos de alta dimensión

---

## Competencias Desarrolladas

Al finalizar este módulo, los participantes serán capaces de:

1. **Segmentación con K-Means:** Aplicar clustering K-Means para segmentar clientes, productos o transacciones, seleccionando el número óptimo de clusters
2. **Clustering Jerárquico:** Construir e interpretar dendrogramas para explorar agrupaciones naturales a múltiples niveles
3. **Reducción con PCA:** Reducir dimensionalidad de datos preservando varianza, facilitando visualización y análisis
4. **Visualización Avanzada:** Utilizar UMAP y PacMap para visualizar estructuras complejas en datos de alta dimensión
5. **Interpretación de Resultados:** Traducir outputs de algoritmos no supervisados en insights accionables de negocio

---

## Evaluación del Aprendizaje

### Calibración Inicial (5 preguntas)
- Autoevaluación de conocimientos previos sobre clustering y reducción de dimensionalidad
- Identificación de familiaridad con conceptos estadísticos básicos

### Laboratorio Práctico (ejercicios por definir)
- Ejercicios progresivos con contexto empresarial real
- Cada ejercicio requiere aplicar técnicas de aprendizaje no supervisado
- Validación de resultados e interpretación de outputs

### Evaluación Final (10 preguntas)
- Preguntas de mayor profundidad que la calibración
- Todas respondibles con información del módulo
- Enfoque en aplicación práctica y toma de decisiones

---

## Tecnologías Utilizadas

- **Scikit-learn:** Implementaciones de K-Means, clustering jerárquico y PCA
- **UMAP:** Biblioteca especializada para reducción de dimensionalidad no lineal
- **PacMap:** Método moderno para visualización preservando estructura local y global
- **Pandas:** Manipulación de datos
- **Matplotlib/Seaborn:** Visualización de resultados, dendrogramas y scatter plots
- **Jupyter Notebook:** Entorno interactivo de aprendizaje
- **Datos de ejemplo:** Datasets de clientes, transacciones, productos y datos sintéticos para demostración

---

## Próximos Pasos

Una vez dominados estos conceptos, los participantes estarán preparados para:
- Técnicas avanzadas de detección de anomalías
- Clustering basado en densidad (DBSCAN, HDBSCAN)
- Métodos de ensemble para clustering
- Integración de aprendizaje no supervisado con técnicas supervisadas
- Aplicaciones en deep learning: autoencoders y embeddings
