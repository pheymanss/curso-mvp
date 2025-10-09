# Plan Módulo 1: SQL para Científicos de Datos

## Información General
- **Duración:** ~3 horas
- **Nivel:** Principiante
- **Prerrequisitos:** Ninguno
- **Objetivo:** Desarrollar competencias fundamentales en extracción, filtrado, agregación y combinación de datos de bases de datos relacionales para su uso en procesos de ciencia de datos.

---

## Proceso de Desarrollo del Módulo

### Fase 1: Planificación ✅
- [x] Definir objetivos de aprendizaje
- [x] Estructurar contenidos
- [x] Establecer casos de uso empresariales

### Fase 2: Contenido Teórico ✅
- [x] `modulo1-sql.md` - Contenido teórico completo

### Fase 3: Laboratorio Práctico ✅
- [x] `lab1-sql.ipynb` - 14 ejercicios prácticos con contexto empresarial

### Fase 4: Guión Narrativo ✅
- [x] `guion-modulo1-sql.md` - 6 segmentos de ~5 minutos cada uno

---

## Estructura de Contenidos

### Sección 1: Fundamentos y Consultas Esenciales (30 minutos)
**Objetivo:** Introducir al participante a la sintaxis de SQL y estructura de bases de datos relacionales.

**Contenidos:**
- Introducción a SQL: Rol en la Ciencia de Datos (5 min)
- Estructura de una Base de Datos Relacional (10 min)
- La consulta fundamental: SELECT FROM (10 min)
- Limitación de resultados: LIMIT (5 min)

**Caso empresarial principal:** Análisis de catálogo de productos para campaña de marketing

### Sección 2: Filtrado de Datos (40 minutos)
**Objetivo:** Capacitar en la aplicación de filtros precisos para aislar subconjuntos de datos relevantes.

**Contenidos:**
- Filtrado de filas con WHERE (10 min)
- Condiciones múltiples: AND, OR, BETWEEN (15 min)
- Manejo de valores nulos: IS NULL, IS NOT NULL (10 min)
- Ordenamiento de resultados: ORDER BY (5 min)

**Casos empresariales:**
- Segmentación geográfica de clientes
- Análisis de transacciones premium
- Control de calidad de datos

### Sección 3: Agregación y Resumen de Datos (50 minutos)
**Objetivo:** Transformar datos crudos en métricas y resúmenes de negocio (KPIs).

**Contenidos:**
- Valores únicos: DISTINCT (5 min)
- Funciones de agregación: COUNT, SUM, AVG, MAX, MIN (15 min)
- Agrupación de datos: GROUP BY (20 min)
- Filtrado de grupos: HAVING (10 min)

**Casos empresariales:**
- KPIs del negocio para junta directiva
- Análisis de precios por categoría
- Identificación de clientes recurrentes

### Sección 4: Combinación de Tablas (40 minutos)
**Objetivo:** Combinar información de múltiples tablas relacionadas.

**Contenidos:**
- Modelo relacional: Llaves primarias y foráneas (5 min)
- INNER JOIN (15 min)
- LEFT JOIN (15 min)
- Uso de alias: AS (5 min)

**Casos empresariales:**
- Reporte integrado de ventas
- Análisis de clientes activos vs. inactivos
- Dashboard ejecutivo de customer analytics

---

## Competencias Desarrolladas

Al finalizar este módulo, los participantes serán capaces de:

1. **Extracción de datos:** Usar SELECT y FROM para obtener información específica
2. **Filtrado inteligente:** Aplicar WHERE con múltiples condiciones para segmentar datos
3. **Agregación empresarial:** Generar KPIs usando funciones de agregación y GROUP BY
4. **Análisis multidimensional:** Combinar información de múltiples tablas usando JOINs
5. **Optimización de consultas:** Usar LIMIT y alias para escribir SQL eficiente y legible

---

## Evaluación del Aprendizaje

### Calibración Inicial (10 preguntas)
- Autoevaluación de conocimientos previos
- Identificación de nivel de experiencia con bases de datos

### Laboratorio Práctico (14 ejercicios)
- Ejercicios progresivos con contexto empresarial
- Cada ejercicio requiere completar consultas SQL incompletas
- Validación inmediata de resultados

### Evaluación Final (10 preguntas)
- Preguntas de mayor profundidad que la calibración
- Todas respondibles con información del módulo
- Enfoque en aplicación práctica de conceptos

---

## Tecnologías Utilizadas

- **SQLite:** Base de datos en memoria para ejercicios
- **Pandas:** Ejecución de consultas y visualización de resultados
- **Jupyter Notebook:** Entorno interactivo de aprendizaje
- **Datos de ejemplo:** Sistema e-commerce (clientes, productos, órdenes, empleados)

---

## Próximos Pasos

Una vez dominados estos conceptos fundamentales, los participantes estarán preparados para:
- Subconsultas y CTEs para análisis modulares
- Funciones de ventana para análisis temporal
- Optimización de consultas para big data
- Integración con herramientas de ciencia de datos (Python, R)