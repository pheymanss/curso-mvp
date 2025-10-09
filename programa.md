# Programa STATO Pro - Ciencia de Datos con Python

## Estructura General del Programa

El programa se organiza en **6 módulos** progresivos, cada uno con una duración aproximada de 1 mes. Los módulos marcados con ❌ serán sustituidos por contenido de SQL y Cloud Computing.

---

## ❌ Módulo 1: Introducción a Python
**Estado:** Será sustituido por módulo de SQL

### Contenido

#### 1.1 Entornos de desarrollo
- Instalación de Python 3
- Gestión de ambientes con `uv`
- Uso de Jupyter Notebook, Quarto y VSCode
- Instalación de funcionalidades como `ruff`

#### 1.2 Fundamentos del lenguaje
- Variables y tipos de datos (numéricos, cadenas, booleanos)
- Diccionarios y listas
- Condicionales (`if/else`)
- Bucles (`for`, `while`) y recorrido de listas

#### 1.3 Funciones y módulos
- Creación de funciones en Python
- Manejo de parámetros
- Valores de retorno y excepciones
- Organización del código en módulos y scripts reutilizables

#### 1.4 Introducción a la programación orientada a objetos
- Conceptos básicos: clases, instancias, métodos, atributos
- Proyectos basados en POO

---

## Módulo 2: Manejo y Visualización de Datos en Python
**Duración:** 1 mes

### Descripción
Este módulo se enfoca en la manipulación de datos usando `pandas` y en la visualización exploratoria con bibliotecas gráficas. Los estudiantes aprenderán a cargar conjuntos de datos, limpiar y transformar datos, y a generar visualizaciones para identificar patrones iniciales.

### Contenido

#### 2.1 Manejo de datos con pandas
- Carga de datos desde CSV/Excel/SQL
- Visualización de las primeras filas
- Índices y selecciones (`loc`, `iloc`)
- Filtrado y subconjuntos
- Creación de nuevas columnas

#### 2.2 Limpieza y transformación
- Identificación y tratamiento de valores nulos
- Conversión de tipos de datos
- Operaciones de `merge`/join entre tablas
- Resumir datos con `group by` y agregaciones

#### 2.3 Aumentación de datos
- Cálculo de estadísticas descriptivas
- Normalización y escalado de variables
- Manejo de fechas y textos

---

## Módulo 3: Métodos No Supervisados en Python
**Duración:** 1 mes

### Descripción
Se introducen los algoritmos de aprendizaje no supervisado, aquellos que permiten extraer patrones sin una variable objetivo definida. Se estudiarán métodos de clustering para segmentar datos y técnicas de reducción de dimensionalidad.

### Contenido

#### 3.1 Fundamentos de aprendizaje no supervisado
- Segmentación de datos
- Detección de anomalías
- Exploración de estructura de datos

#### 3.2 Clustering K-Means
- Algoritmo de k-medias
- Distancia euclídea
- Elección del número de clústeres (método del codo, silhouette)
- Interpretación de centroides

#### 3.3 Clustering jerárquico
- Agrupamiento jerárquico aglomerativo vs divisivo
- Dendrogramas
- Medidas de distancia y enlace (single, complete, average)
- Corte del dendrograma para escoger clusters

#### 3.4 Análisis de componentes principales (PCA)
- Fundamentos del PCA (varianza explicada, componentes principales como combinaciones lineales)
- Criterios de selección del número de componentes
- Visualización en 2D/3D de los datos reducidos

#### 3.5 Reducción de dimensión con UMAP y PacMap
- Introducción a UMAP y PacMap
- Comparativa con PCA en casos no lineales
- Uso para visualización de alta dimensionalidad conservando relaciones locales

---

## Módulo 4: Aprendizaje Automático con Respuesta Continua
**Duración:** 1 mes

### Descripción
Este módulo abarca las técnicas de aprendizaje supervisado para variables numéricas. Se cubrirá regresión lineal, métodos de regularización, árboles de decisión y técnicas de ensemble.

### Contenido

#### 4.1 Regresión lineal múltiple
- Supuestos del modelo lineal
- Estimación por mínimos cuadrados ordinarios
- Interpretación de coeficientes
- Diagnóstico de residuos

#### 4.2 Regularización Ridge y Lasso
- Penalización L2 vs L1
- Impacto en los coeficientes (shrinkage, selección de variables)
- Validación cruzada para escoger hiperparámetro λ (alpha)

#### 4.3 Evaluación de modelos
- División Training/Test/Validation
- Validación cruzada Leave-One-Out y k-fold
- Cálculo e interpretación de RMSE, MAE y coeficiente R²

#### 4.4 Árboles de decisión para regresión
- Algoritmo CART adaptado a regresión
- Criterio de división (minimización del MSE)
- Poda de árboles para mejorar predicción
- Interpretación de árboles (importancia de variables)

#### 4.5 Métodos de potenciación
- Bagging y Random Forest para regresión
- Introducción a Boosting (Gradient Boosting, XGBoost)

---

## Módulo 5: Aprendizaje Automático con Respuesta Discreta (Clasificación)
**Duración:** 1 mes

### Descripción
Este módulo aborda los algoritmos de clasificación donde la variable a predecir es categórica. Se cubrirá desde regresión logística hasta métodos avanzados como SVM y técnicas de ensemble.

### Contenido

#### 5.1 Regresión Logística
- Concepto de función logística para probabilidades
- Verosimilitud y ajuste de coeficientes
- Umbral de clasificación y curvas ROC
- Extensión One-vs-Rest para multiclase

#### 5.2 Evaluación de clasificadores
- Construcción e interpretación de la matriz de confusión
- Definición de precisión (accuracy), precisión positiva (precision), recuperación (recall), F1-score
- Curva ROC y cálculo del AUC
- Evaluación con conjuntos de prueba independientes
- Uso de cross-validation para clasificación

#### 5.3 Método de Naive Bayes
- Supuesto de independencia
- Cálculo de probabilidades a priori y verosimilitudes
- Casos de uso

#### 5.4 Máquinas de Soporte Vectorial (SVM)
- Separación lineal con máximo margen
- Casos linealmente no separables y el truco del kernel (RBF, polinomial)
- Elección de parámetros
- Interpretación de vectores de soporte

#### 5.5 Árboles de decisión para clasificación
- Criterios de impureza (gini, entropía) en la construcción de árboles
- Sobreajuste y poda
- Visualización del árbol de decisión

#### 5.6 Métodos de potenciación en clasificación
- Bagging: Random Forest
- Boosting: AdaBoost, Gradient Boosting, XGBoost
- Determinación de hiperparámetros
- Prevención de sobreajuste

---

## Módulo 6: Series de Tiempo en Python
**Duración:** 1 mes

### Descripción
Este módulo se enfoca en el análisis y pronóstico de datos temporales, cubriendo desde fundamentos hasta modelos avanzados como ARIMA y Prophet.

### Contenido

#### 6.1 Fundamentos de series de tiempo
- Terminología (rezago, frecuencia, estacionalidad)
- Ejemplos de series en distintas industrias
- Concepto de estacionariedad
- Prueba de raíz unitaria (Dickey-Fuller)

#### 6.2 Manipulación de datos temporales en Python
- Formato de fechas y conversión a datetime
- Índices temporales
- Cambio de frecuencia (diario, mensual, etc.)
- Ventanas móviles (rolling mean, moving average)
- Cálculo de estadísticas móviles

#### 6.3 Visualización y descomposición
- Gráficos de línea con intervalos de confianza
- Gráficos especializados para series de tiempo
- Descomposición clásica (aditiva o multiplicativa) en tendencia, estacionalidad y residuo
- Interpretación de cada componente

#### 6.4 Filtrado y suavizado
- Suavizamiento exponencial simple
- Método de Holt-Winters
- Ajuste de parámetros de suavizamiento

#### 6.5 Modelos ARIMA
- Concepto de autoregresión, diferencia y media móvil
- Identificar parámetros p, d, q mediante análisis de autocorrelación (ACF, PACF)
- Ajuste de modelo ARIMA y ARIMA estacional (SARIMA)
- Predicción y cálculo de intervalos de confianza

#### 6.6 Otros enfoques de pronóstico
- Modelos basados en regresión (variables de tiempo como features)
- Modelo Prophet para pronósticos automatizados
- Modelos de Machine Learning aplicados a series de tiempo

#### 6.7 Evaluación de pronósticos
- Métricas de error para series de tiempo (MAE, RMSE, MAPE)
- Validación temporal (train/test split por fecha, backtesting)
- Visualización de predicciones e identificación de patrones