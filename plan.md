# Plan de Contenido: Clase de SQL para Científicos de Datos (~3 Horas)


**Objetivo de la sesión:** Quien asista a esta clase será capaz de extraer, filtrar, agregar y combinar datos de bases de datos relacionales con el usarlos como insumos para procesos de ciencia de datos.

**Audiencia:** Aspirantes a científicos de datos, analistas y profesionales que requieran el uso de SQL para la manipulación de datos y no cuenten con experiencia previa.

**Metodología:** El curso es mayoritariamente práctico. Cada concepto se presenta como la solución a un problema real. Se utilizará un conjunto de datos estandarizado para todos los ejercicios (ej. ventas, catálogos de productos, personal, etc).

## Sección 1: Fundamentos y Consultas Esenciales

**Objetivo:** Introducir al participante a la sintaxis de SQL y a la estructura de las bases de datos relacionales, permitiendo la ejecución de sus primeras consultas de extracción de datos.

- **Introducción a SQL: Rol en la Ciencia de Datos**
  - Definición de SQL como el lenguaje estándar para la gestión y consulta de datos en sistemas de bases de datos relacionales.
- **Estructura de una Base de Datos Relacional**
  - Conceptos clave: Bases de datos, tablas, columnas y filas.
- **La consulta fundamental: `SELECT FROM`**
  - **Aplicación real:** "Se necesita ver los nombres y precios de todos los productos en el catálogo."
  - Práctica: `SELECT nombre_producto, precio FROM productos;`
- **Limitación de resultados: `LIMIT`**
  - **Aplicación real:** "Para obtener una idea rápida de los datos, se requiere mostrar solo las primeras 10 filas de la tabla de ventas."
  - Práctica: `SELECT \* FROM ventas LIMIT 10;`

## Sección 2: Filtrado de Datos

**Objetivo:** Capacitar al participante en la aplicación de filtros precisos para aislar subconjuntos de datos relevantes, una tarea fundamental en el análisis exploratorio.

- **Filtrado de filas con la cláusula WHERE**
  - **Aplicación real:** "Se debe generar una lista de todos los clientes que son de México."
  - Práctica: `SELECT \* FROM clientes WHERE pais = 'México';`
- **Condiciones múltiples: AND, OR, BETWEEN**
  - **Aplicación real:** "Se deben buscar las órdenes de alto valor (más de $500) que se realizaron durante el primer trimestre de 2023."
  - Práctica: `SELECT \* FROM ordenes WHERE fecha BETWEEN '2023-01-01' AND '2023-03-31' AND total > 500;`
- **Manejo de valores nulos: IS NULL, IS NOT NULL**
  - **Aplicación real:** "Se necesita identificar a todos los usuarios que no han registrado su número de teléfono."
  - Práctica: `SELECT \* FROM usuarios WHERE telefono IS NULL;`
- **Ordenamiento de resultados: ORDER BY**
  - **Aplicación real:** "¿Quiénes son los 5 empleados con los salarios más altos?"
  - Práctica: `SELECT \* FROM empleados ORDER BY salario DESC LIMIT 5;`

## Sección 3: Agregación y Resumen de Datos

**Objetivo:** Esta sección se centra en las técnicas de agregación, que permiten transformar datos crudos en métricas y resúmenes de negocio (KPIs).

- **Valores únicos: DISTINCT**
  - **Aplicación real:** "¿De cuántos países diferentes provienen los clientes?"
  - Práctica: `SELECT COUNT(DISTINCT pais) FROM clientes;`
- **Funciones de agregación: COUNT, SUM, AVG, MAX, MIN**
  - **Aplicación real:** "Se debe calcular el número total de reseñas y la calificación promedio de un producto."
  - Práctica: `SELECT COUNT(1), AVG(calificacion) FROM resenas;`
- **Agrupación de datos: GROUP BY**
  - **Aplicación real:** "Se requiere un reporte que muestre el precio promedio de los productos para cada categoría."
  - Práctica: `SELECT categoria, AVG(precio) FROM productos GROUP BY categoria;`
- **Filtrado de grupos: HAVING**
  - **Aplicación real:** "Se deben identificar los clientes que han realizado más de 3 órdenes para incluirlos en un programa de lealtad."
  - Práctica: `SELECT cliente_id, COUNT(\*) FROM ordenes GROUP BY cliente_id HAVING COUNT(\*) > 3;`

## Sección 4: Combinación de Tablas

**Objetivo:** Los datos en ambientes reales se encuentran distribuidos en múltiples tablas. Esta sección enseña cómo combinar estas tablas para construir una visión integral de la información.

- **Modelo relacional: Llaves primarias y foráneas**
  - Explicación de los campos clave que permiten establecer relaciones entre tablas.
- **Combinación de tablas: INNER JOIN**
  - **Aplicación real:** "Se requiere ver el nombre de cada cliente junto al ID de sus órdenes."
  - Práctica: `SELECT ordenes.id, clientes.nombre FROM ordenes INNER JOIN clientes ON ordenes.cliente_id = clientes.id;`
- **Combinaciones externas: LEFT JOIN**
  - **Aplicación real:** "Se debe generar una lista de todos los clientes e indicar quiénes de ellos nunca han realizado una orden."
  - Práctica: `SELECT clientes.nombre, ordenes.id FROM clientes LEFT JOIN ordenes ON clientes.id = ordenes.cliente_id;`
- **Uso de alias: `AS`**
  - **Función:** Asignar nombres temporales a tablas y columnas para mejorar la legibilidad y evitar ambigüedad en consultas complejas.

## Anexo: Próximos Pasos y Temas Avanzados

Una vez dominados los conceptos de este curso, la siguiente ruta de aprendizaje permitirá profundizar en técnicas más avanzadas de manipulación y análisis de datos con SQL.

**1\. Dominio de la Transformación de Datos (Data Wrangling)**

- **Lógica condicional (`CASE WHEN`):** Para crear columnas personalizadas y segmentar datos (ej. agrupar clientes por nivel de gasto).
- **Funciones de Texto y Búsqueda de Patrones:** Para la limpieza y extracción de características (ej. LIKE, SUBSTRING, CONCAT).
- **Funciones de Fecha:** Para manipular y extraer componentes de fechas (ej. EXTRACT, DATE_TRUNC).
- **Conversión de Tipos de Datos (`CAST`):** Para asegurar la consistencia y compatibilidad de los datos antes del análisis.

**2\. Estructuración de Consultas Complejas**

- **Subconsultas (Subqueries):** Para anidar una consulta dentro de otra y realizar filtros o cálculos basados en resultados intermedios.
- **Common Table Expressions (CTEs):** Para mejorar la legibilidad y modularidad de las consultas largas usando la cláusula WITH, un paso fundamental hacia el código SQL limpio y mantenible.

**3\. Técnicas de Análisis Avanzado**

- **Funciones de Ventana (Window Functions):** Para realizar cálculos analíticos avanzados como rankings, promedios móviles y totales acumulados, sin colapsar las filas.
- **Tipos de JOIN avanzados:** Explorar `FULL OUTER JOIN` y `CROSS JOIN`  para escenarios de análisis de datos más complejos.
- **Pivoteo de Datos (conceptual):** Entender el concepto de transformar filas en columnas (`PIVOT`) para la creación de reportes y matrices.

----
**Distribución del Tiempo Aproximada**

**Tiempo total del curso:** ~3 horas

- **Sección 1: Fundamentos y Consultas Esenciales (30 minutos)**
  - Introducción a SQL: 5 min
  - Estructura de una Base de Datos: 10 min
  - Consulta SELECT y FROM: 10 min
  - Limitación con LIMIT: 2 min
- **Sección 2: Filtrado de Datos (40 minutos)**
  - Filtrado con WHERE: 10 min
  - Condiciones múltiples (AND, OR): 15 min
  - Manejo de nulos (IS NULL): 10 min
  - Ordenamiento (ORDER BY): 5 min
- **Sección 3: Agregación y Resumen de Datos (50 minutos)**
  - Valores únicos (DISTINCT): 5 min
  - Funciones de agregación: 15 min
  - Agrupación (GROUP BY): 20 min
  - Filtrado de grupos (HAVING): 10 min
- **Sección 4: Combinación de Tablas (40 minutos)**
  - Modelo relacional: 5 min
  - INNER JOIN: 15 min
  - LEFT JOIN: 15 min
  - Uso de alias (AS): 5 min