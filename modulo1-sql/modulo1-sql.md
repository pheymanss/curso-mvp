# Módulo 1: SQL para Científicos de Datos

## Objetivo del Módulo
Al finalizar este módulo, los participantes serán capaces de extraer, filtrar, agregar y combinar datos de bases de datos relacionales para utilizarlos como insumos en procesos de ciencia de datos.

---

## Calibración de Conocimientos

Antes de proceder con el contenido del módulo, se recomienda evaluar el nivel de conocimiento previo mediante las siguientes preguntas. Si estas preguntas pueden responderse con comodidad, será posible avanzar rápidamente por el material. En caso contrario, se sugiere seguir el módulo con atención detallada.

**Preguntas de autoevaluación:**

1. ¿Ha trabajado anteriormente con bases de datos para extraer información?
2. ¿Conoce la diferencia entre una tabla y una base de datos?
3. ¿Ha utilizado alguna vez comandos para solicitar información específica de un conjunto de datos?
4. ¿Está familiarizado con el concepto de filtrar registros según criterios específicos?
5. ¿Ha realizado cálculos sobre grupos de datos (como promedios o totales)?
6. ¿Conoce el concepto de combinar información de diferentes fuentes de datos?
7. ¿Ha trabajado con datos que contengan valores faltantes o nulos?
8. ¿Está familiarizado con la organización de datos en filas y columnas?
9. ¿Ha necesitado ordenar datos según algún criterio específico?
10. ¿Ha trabajado en contextos donde los datos se encuentran distribuidos en múltiples tablas relacionadas?

Si la mayoría de estas preguntas resultan familiares desde la experiencia práctica, el contenido del módulo servirá principalmente como formalización de conocimientos. Si resultan completamente nuevas, el módulo proporcionará la base necesaria para desarrollar estas competencias desde cero.

---

## Sección 1: Fundamentos y Consultas Esenciales

### Introducción a SQL: Rol en la Ciencia de Datos

SQL (Structured Query Language) es el lenguaje estándar para la gestión y consulta de datos en sistemas de bases de datos relacionales. Para los científicos de datos, SQL representa una herramienta fundamental en la industria moderna porque:

- **Acceso a datos empresariales**: La mayoría de los datos corporativos se almacenan en bases de datos relacionales, siendo SQL el medio estándar para accederlos
- **Eficiencia operacional**: Permite procesar grandes volúmenes de datos directamente en la base de datos, reduciendo costos de transferencia y procesamiento
- **Preparación de datos**: Facilita la limpieza, transformación y agregación de datos antes del análisis, etapa crítica en cualquier proyecto de ciencia de datos
- **Colaboración interdisciplinaria**: Es un lenguaje universal que facilita la comunicación con equipos técnicos, analistas de negocio y administradores de base de datos

### Estructura de una Base de Datos Relacional

Una base de datos relacional organiza la información en estructuras jerárquicas:

**Base de Datos** → **Tablas** → **Columnas** y **Filas**

- **Base de datos**: Contenedor principal que agrupa todas las tablas relacionadas
- **Tabla**: Estructura que organiza datos en formato tabular (como una hoja de Excel)
- **Columna (Campo)**: Define el tipo de dato que se almacena (ej. nombre, fecha, precio)
- **Fila (Registro)**: Representa una instancia única de datos (ej. un cliente específico)

**Ejemplo conceptual:**
```
Base de Datos: TiendaOnline
├── Tabla: clientes
│   ├── Columnas: id, nombre, email, pais
│   └── Filas: (1, 'Juan Pérez', 'juan@email.com', 'México')
├── Tabla: productos
│   ├── Columnas: id, nombre_producto, precio, categoria
│   └── Filas: (1, 'Laptop', 999.99, 'Electrónicos')
└── Tabla: ordenes
    ├── Columnas: id, cliente_id, fecha, total
    └── Filas: (1, 1, '2023-01-15', 999.99)
```

### La Consulta Fundamental: SELECT FROM

La consulta `SELECT FROM` es la base de toda extracción de datos en SQL.

**Sintaxis básica:**
```sql
SELECT columna1, columna2, ...
FROM nombre_tabla;
```

**Caso de uso real:** *"Se necesita ver los nombres y precios de todos los productos en el catálogo."*

```sql
SELECT nombre_producto, precio 
FROM productos;
```

**Variaciones importantes:**
- `SELECT *` - Selecciona todas las columnas
- `SELECT DISTINCT columna` - Elimina duplicados
- Las columnas se pueden renombrar usando `AS`

### Limitación de Resultados: LIMIT

Cuando trabajas con grandes conjuntos de datos, es útil limitar los resultados para:
- Obtener una vista previa rápida de los datos
- Evitar sobrecargar el sistema
- Realizar pruebas de consultas

**Sintaxis:**
```sql
SELECT columnas
FROM tabla
LIMIT número_de_filas;
```

**Caso de uso real:** *"Para obtener una idea rápida de los datos, se requiere mostrar solo las primeras 10 filas de la tabla de ventas."*

```sql
SELECT * 
FROM ventas 
LIMIT 10;
```

---

## Sección 2: Filtrado de Datos

### Filtrado de Filas con WHERE

La cláusula `WHERE` permite filtrar filas basándose en condiciones específicas, lo cual resulta esencial para el análisis exploratorio de datos en entornos industriales donde se requiere segmentar información según criterios de negocio.

**Sintaxis:**
```sql
SELECT columnas
FROM tabla
WHERE condicion;
```

**Operadores comunes:**
- `=` (igual)
- `!=` o `<>` (diferente)
- `>`, `<`, `>=`, `<=` (comparaciones numéricas)
- `LIKE` (patrones de texto)
- `IN` (valores dentro de una lista)

**Caso de uso real:** *"Se debe generar una lista de todos los clientes que son de México."*

```sql
SELECT * 
FROM clientes 
WHERE pais = 'México';
```

### Condiciones Múltiples: AND, OR, BETWEEN

Para análisis más complejos que reflejen la realidad empresarial, se requiere combinar múltiples condiciones:

**AND**: Todas las condiciones deben ser verdaderas
```sql
WHERE condicion1 AND condicion2
```

**OR**: Al menos una condición debe ser verdadera
```sql
WHERE condicion1 OR condicion2
```

**BETWEEN**: Para rangos de valores
```sql
WHERE columna BETWEEN valor1 AND valor2
```

**Caso de uso real:** *"Se deben buscar las órdenes de alto valor (más de $500) que se realizaron durante el primer trimestre de 2023."*

```sql
SELECT * 
FROM ordenes 
WHERE fecha BETWEEN '2023-01-01' AND '2023-03-31' 
  AND total > 500;
```

### Manejo de Valores Nulos: IS NULL, IS NOT NULL

Los valores nulos representan datos faltantes, un problema común en ciencia de datos que requiere tratamiento especial en entornos de producción.

**Detectar valores nulos:**
```sql
WHERE columna IS NULL
```

**Detectar valores no nulos:**
```sql
WHERE columna IS NOT NULL
```

**Caso de uso real:** *"Se necesita identificar a todos los usuarios que no han registrado su número de teléfono."*

```sql
SELECT * 
FROM usuarios 
WHERE telefono IS NULL;
```

**Importante:** No se debe usar `= NULL` o `!= NULL`, ya que estas comparaciones no funcionarán correctamente en SQL.

### Ordenamiento de Resultados: ORDER BY

El ordenamiento resulta crucial para identificar patrones y valores extremos en los datos, especialmente en análisis de rendimiento empresarial y detección de anomalías.

**Sintaxis:**
```sql
SELECT columnas
FROM tabla
ORDER BY columna [ASC|DESC];
```

- `ASC`: Orden ascendente (por defecto)
- `DESC`: Orden descendente

**Caso de uso real:** *"¿Quiénes son los 5 empleados con los salarios más altos?"*

```sql
SELECT * 
FROM empleados 
ORDER BY salario DESC 
LIMIT 5;
```

---

## Sección 3: Agregación y Resumen de Datos

### Valores Únicos: DISTINCT

`DISTINCT` elimina duplicados, útil para obtener listas de valores únicos.

**Caso de uso real:** *"¿De cuántos países diferentes provienen los clientes?"*

```sql
SELECT COUNT(DISTINCT pais) 
FROM clientes;
```

### Funciones de Agregación

Las funciones de agregación transforman múltiples filas en un solo valor resumen:

- **COUNT()**: Cuenta registros
- **SUM()**: Suma valores numéricos
- **AVG()**: Calcula promedio
- **MAX()**: Encuentra valor máximo
- **MIN()**: Encuentra valor mínimo

**Caso de uso real:** *"Se debe calcular el número total de reseñas y la calificación promedio de un producto."*

```sql
SELECT COUNT(1), AVG(calificacion) 
FROM resenas;
```

### Agrupación de Datos: GROUP BY

`GROUP BY` agrupa filas que tienen valores similares en columnas especificadas, permitiendo calcular métricas por categoría. Esta funcionalidad es fundamental en la generación de reportes empresariales y KPIs (Key Performance Indicators).

**Sintaxis:**
```sql
SELECT columna_agrupacion, funcion_agregacion(columna)
FROM tabla
GROUP BY columna_agrupacion;
```

**Caso de uso real:** *"Se requiere un reporte que muestre el precio promedio de los productos para cada categoría."*

```sql
SELECT categoria, AVG(precio) 
FROM productos 
GROUP BY categoria;
```

### Filtrado de Grupos: HAVING

`HAVING` filtra grupos después de la agregación (mientras que `WHERE` filtra antes). Esta distinción es crucial para el análisis avanzado en contextos empresariales.

**Caso de uso real:** *"Se deben identificar los clientes que han realizado más de 3 órdenes para incluirlos en un programa de lealtad."*

```sql
SELECT cliente_id, COUNT(*) 
FROM ordenes 
GROUP BY cliente_id 
HAVING COUNT(*) > 3;
```

---

## Sección 4: Combinación de Tablas

### Modelo Relacional: Llaves Primarias y Foráneas

En bases de datos relacionales, las tablas se conectan mediante llaves:

- **Llave Primaria (Primary Key)**: Identificador único de cada fila en una tabla
- **Llave Foránea (Foreign Key)**: Referencia a la llave primaria de otra tabla

**Ejemplo:**
```
Tabla clientes:
- id (Primary Key)
- nombre
- email

Tabla ordenes:
- id (Primary Key)  
- cliente_id (Foreign Key → clientes.id)
- fecha
- total
```

### Combinación de Tablas: JOIN

Los JOINs permiten combinar información de múltiples tablas relacionadas, una capacidad esencial en sistemas empresariales donde los datos se encuentran normalizados y distribuidos en múltiples entidades.

**Sintaxis general:**
```sql
SELECT tabla1.columna, tabla2.columna
FROM tabla1
JOIN tabla2 ON tabla1.llave = tabla2.llave;
```

#### Aplicación INNER JOIN
Devuelve solo las filas que tienen coincidencias en ambas tablas.

**Caso de uso real:** *"Se requiere ver el nombre de cada cliente junto al ID de sus órdenes."*

```sql
SELECT ordenes.id, clientes.nombre 
FROM ordenes 
INNER JOIN clientes ON ordenes.cliente_id = clientes.id;
```

#### Aplicación LEFT JOIN
Devuelve todas las filas de la tabla izquierda, incluso si no tienen coincidencias en la tabla derecha.

**Caso de uso real:** *"Se debe generar una lista de todos los clientes e indicar quiénes de ellos nunca han realizado una orden."*

```sql
SELECT clientes.nombre, ordenes.id 
FROM clientes 
LEFT JOIN ordenes ON clientes.id = ordenes.cliente_id;
```

### Uso de Alias: AS

Los alias mejoran la legibilidad y evitan ambigüedad en consultas complejas, práctica estándar en el desarrollo de consultas SQL para entornos de producción:

**Para columnas:**
```sql
SELECT nombre AS nombre_cliente, precio AS precio_producto
FROM productos;
```

**Para tablas:**
```sql
SELECT c.nombre, o.id 
FROM clientes AS c
JOIN ordenes AS o ON c.id = o.cliente_id;
```

---

## Próximos Pasos

Una vez dominados estos conceptos fundamentales, los participantes estarán preparados para:
- Técnicas avanzadas de transformación de datos aplicables en entornos de producción
- Consultas complejas con subconsultas y CTEs para análisis empresariales sofisticados
- Funciones de ventana para análisis temporal y de tendencias
- Optimización de consultas para grandes volúmenes de datos en sistemas empresariales

El dominio de SQL representa una competencia fundamental en el arsenal de cualquier científico de datos que aspire a generar valor en organizaciones modernas.

---

## Evaluación de Entendimiento

Para corroborar la asimilación efectiva de los conceptos presentados en este módulo, se proponen las siguientes preguntas de evaluación con mayor profundidad y complejidad que las de calibración inicial. Todas las preguntas pueden responderse utilizando exclusivamente la información y conceptos presentados en este módulo.

**Preguntas de evaluación:**

1. **Consultas básicas:** Explique la diferencia entre `SELECT *` y `SELECT columna1, columna2` en términos de eficiencia y casos de uso apropiados según lo presentado en el módulo.

2. **Filtrado de datos:** Diseñe una consulta que combine los operadores AND, OR y BETWEEN para filtrar órdenes según múltiples criterios, explicando por qué eligió cada operador.

3. **Manejo de valores nulos:** ¿Por qué no se debe usar `= NULL` en lugar de `IS NULL`? Proporcione un ejemplo de caso empresarial donde esto sea relevante.

4. **Funciones de agregación:** Explique la diferencia entre COUNT(*) y COUNT(DISTINCT columna) usando un ejemplo práctico del contexto empresarial.

5. **Agrupación de datos:** Describa un escenario donde GROUP BY sería esencial para generar un KPI empresarial, especificando las columnas de agrupación y las métricas a calcular.

6. **Filtrado de grupos:** ¿Cuándo se debe usar HAVING en lugar de WHERE? Proporcione un ejemplo concreto basado en los casos presentados en el módulo.

7. **Tipos de JOIN:** Compare INNER JOIN y LEFT JOIN explicando cuándo cada uno es apropiado para el análisis de datos empresariales, utilizando el ejemplo de clientes y órdenes del módulo.

8. **Combinación de tablas:** Usando las tablas de ejemplo del módulo (clientes, órdenes), diseñe una consulta que identifique clientes sin órdenes y explique por qué esto es valioso para el negocio.

9. **Uso de alias:** Demuestre cómo los alias mejoran la legibilidad en una consulta que combine múltiples tablas y funciones de agregación.

10. **Aplicación integral:** Diseñe una consulta que combine filtrado, agregación y JOIN para responder: "¿Cuáles son los países con más de 2 clientes que hayan gastado en promedio más de $500 por orden?" Explique cada parte de la consulta.

La capacidad de responder estas preguntas con base en los conceptos del módulo indica dominio suficiente para aplicar SQL en contextos profesionales de ciencia de datos.