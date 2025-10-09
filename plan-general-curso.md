# Plan General del Curso MVP

## Estructura del Curso

Este curso está diseñado como un programa modular que cubre competencias fundamentales en el análisis de datos y ciencia de datos, con énfasis en aplicaciones industriales.

---

## Módulo 1: SQL para Científicos de Datos (~3 Horas)

**Objetivo:** Desarrollar competencias fundamentales en extracción, filtrado, agregación y combinación de datos de bases de datos relacionales para su uso en procesos de ciencia de datos.

**Audiencia:** Aspirantes a científicos de datos, analistas y profesionales que requieran SQL para manipulación de datos sin experiencia previa.

**Metodología:** Enfoque mayoritariamente práctico con cada concepto presentado como solución a un problema empresarial real.

### Contenidos:
1. **Fundamentos y Consultas Esenciales (30 min)**
   - Introducción a SQL y su rol en ciencia de datos
   - Estructura de bases de datos relacionales
   - Consultas SELECT y FROM
   - Limitación de resultados con LIMIT

2. **Filtrado de Datos (40 min)**
   - Filtrado con WHERE
   - Condiciones múltiples (AND, OR, BETWEEN)
   - Manejo de valores nulos (IS NULL, IS NOT NULL)
   - Ordenamiento con ORDER BY

3. **Agregación y Resumen de Datos (50 min)**
   - Valores únicos con DISTINCT
   - Funciones de agregación (COUNT, SUM, AVG, MAX, MIN)
   - Agrupación con GROUP BY
   - Filtrado de grupos con HAVING

4. **Combinación de Tablas (40 min)**
   - Modelo relacional: llaves primarias y foráneas
   - INNER JOIN y LEFT JOIN
   - Uso de alias (AS)

**Entregables:**
- `modulo1-sql.md`: Contenido teórico
- `lab1-sql.ipynb`: Laboratorio práctico con 14 ejercicios
- `guion-modulo1-sql.md`: Guión narrativo para grabación

---

## Módulo 3: Métodos No Supervisados en Python (~4 Horas)

**Objetivo:** Desarrollar competencias en técnicas de aprendizaje no supervisado para descubrimiento de patrones, segmentación de datos y reducción de dimensionalidad en contextos empresariales.

**Audiencia:** Científicos de datos, analistas avanzados y profesionales con conocimientos básicos de Python y estadística.

**Metodología:** Combinación de teoría conceptual y aplicación práctica con datasets empresariales reales.

### Contenidos:
1. **Fundamentos del Aprendizaje No Supervisado (45 min)**
   - Diferencias con aprendizaje supervisado
   - Tipos de problemas: clustering, reducción de dimensionalidad, detección de anomalías
   - Casos de uso empresariales

2. **Clustering: Segmentación de Datos (90 min)**
   - K-Means: teoría y aplicación práctica
   - Clustering jerárquico
   - DBSCAN para detección de anomalías
   - Evaluación de clusters: métricas y visualización

3. **Reducción de Dimensionalidad (75 min)**
   - Análisis de Componentes Principales (PCA)
   - t-SNE para visualización
   - Aplicaciones en feature engineering
   - Interpretación de resultados

4. **Aplicaciones Avanzadas (30 min)**
   - Sistemas de recomendación básicos
   - Detección de anomalías en datos empresariales
   - Integración con pipelines de ML

**Entregables:**
- `modulo3-metodos-no-supervisados.md`: Contenido teórico
- `lab3-clustering-pca.ipynb`: Laboratorio práctico
- `guion-modulo3-metodos-no-supervisados.md`: Guión narrativo

---

## Metodología Pedagógica General

### Principios de Diseño:
- **Relevancia Industrial:** Todos los ejemplos y casos de uso provienen de contextos empresariales reales
- **Aprendizaje Progresivo:** Cada módulo construye sobre conocimientos previos
- **Práctica Inmediata:** Cada concepto teórico se refuerza con ejercicios prácticos
- **Evaluación Continua:** Preguntas de calibración inicial y evaluación final por módulo

### Estructura por Módulo:
1. **Calibración de Conocimientos:** Preguntas de autoevaluación
2. **Contenido Teórico:** Conceptos con contexto empresarial
3. **Laboratorio Práctico:** Ejercicios hands-on con datasets reales
4. **Guión Narrativo:** Contenido preparado para grabación en segmentos de ~5 minutos
5. **Evaluación de Entendimiento:** Preguntas de validación del aprendizaje

---

## Tecnologías y Herramientas

### Módulo 1 (SQL):
- SQLite para bases de datos en memoria
- Pandas para ejecución de consultas y visualización de resultados
- Jupyter Notebooks para entorno interactivo

### Módulo 3 (Métodos No Supervisados):
- Python (NumPy, Pandas, Scikit-learn)
- Matplotlib y Seaborn para visualización
- Jupyter Notebooks para desarrollo interactivo

---

## Próximos Módulos (Roadmap)

### Módulo 2: Estadística Descriptiva y Exploratoria
- Medidas de tendencia central y dispersión
- Visualización de datos con Python
- Análisis exploratorio de datos (EDA)

### Módulo 4: Machine Learning Supervisado
- Regresión lineal y logística
- Árboles de decisión y Random Forest
- Evaluación de modelos

### Módulo 5: Deep Learning Fundamentals
- Redes neuronales básicas
- Frameworks (TensorFlow/PyTorch)
- Aplicaciones en visión computacional y NLP

---

## Criterios de Éxito

### Para Estudiantes:
- Capacidad de resolver problemas empresariales reales usando las técnicas aprendidas
- Comprensión de cuándo y cómo aplicar cada método
- Habilidad para comunicar resultados a stakeholders no técnicos

### Para el Programa:
- Alta tasa de finalización de módulos
- Aplicación exitosa de conocimientos en contextos profesionales
- Feedback positivo sobre relevancia industrial del contenido