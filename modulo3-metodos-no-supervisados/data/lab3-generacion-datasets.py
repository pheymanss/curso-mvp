"""
Generación de datasets para Laboratorio 3: Métodos de Aprendizaje No Supervisado

Este script genera todos los datasets sintéticos utilizados en el laboratorio.
Los datos se guardan como archivos CSV para ser cargados durante los ejercicios.

Datasets generados:
1. segmentacion_clientes_ecommerce.csv - Segmentación de clientes (200 registros)
2. catalogo_productos_retail.csv - Catálogo de productos (50 registros)
3. metricas_usuarios_plataforma_digital.csv - Dataset con 20 variables (300 registros)
4. cartera_prestamos_hipotecarios.csv - Préstamos hipotecarios (500 registros)
"""

import numpy as np
import pandas as pd
import os

# Crear directorio data/ para datasets si no existe
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, 'data')
os.makedirs(output_dir, exist_ok=True)


def generar_datos_clientes():
    """
    Genera dataset de clientes para segmentación con K-Means.
    Incluye tres perfiles: premium, regular y ocasional.
    """
    np.random.seed(42)
    
    # Perfil 1: Clientes premium (alto valor, alta frecuencia)
    n_premium = 50
    premium = pd.DataFrame({
        'frecuencia_compra': np.random.normal(25, 5, n_premium),
        'valor_promedio': np.random.normal(150, 30, n_premium),
        'dias_ultima_compra': np.random.normal(10, 5, n_premium),
        'productos_unicos': np.random.normal(20, 5, n_premium),
        'tasa_devolucion': np.random.normal(5, 2, n_premium)
    })
    
    # Perfil 2: Clientes regulares (valor medio, frecuencia media)
    n_regular = 80
    regular = pd.DataFrame({
        'frecuencia_compra': np.random.normal(12, 3, n_regular),
        'valor_promedio': np.random.normal(75, 15, n_regular),
        'dias_ultima_compra': np.random.normal(30, 10, n_regular),
        'productos_unicos': np.random.normal(10, 3, n_regular),
        'tasa_devolucion': np.random.normal(8, 3, n_regular)
    })
    
    # Perfil 3: Clientes ocasionales (bajo valor, baja frecuencia)
    n_ocasional = 70
    ocasional = pd.DataFrame({
        'frecuencia_compra': np.random.normal(4, 2, n_ocasional),
        'valor_promedio': np.random.normal(40, 10, n_ocasional),
        'dias_ultima_compra': np.random.normal(90, 30, n_ocasional),
        'productos_unicos': np.random.normal(4, 2, n_ocasional),
        'tasa_devolucion': np.random.normal(12, 4, n_ocasional)
    })
    
    # Combinar todos los perfiles
    datos_clientes = pd.concat([premium, regular, ocasional], ignore_index=True)
    
    # Calcular valor_total como frecuencia * valor_promedio
    datos_clientes['valor_total'] = (datos_clientes['frecuencia_compra'] * 
                                      datos_clientes['valor_promedio'])
    
    # Asegurar valores positivos
    datos_clientes = datos_clientes.abs()
    
    # Agregar ID de cliente
    datos_clientes.insert(0, 'cliente_id', range(1, len(datos_clientes) + 1))
    
    return datos_clientes


def generar_datos_productos():
    """
    Genera dataset de productos para clustering jerárquico.
    Incluye tres categorías: electrónica, ropa y accesorios.
    """
    np.random.seed(42)
    n_productos = 50
    
    # Categoria 1: Electronica (alto precio, baja frecuencia, margen moderado)
    electronica = pd.DataFrame({
        'precio': np.random.normal(500, 100, 15),
        'ventas_mensuales': np.random.normal(20, 5, 15),
        'margen_beneficio': np.random.normal(25, 5, 15),
        'rating_promedio': np.random.normal(4.2, 0.3, 15),
        'num_reviews': np.random.normal(150, 50, 15)
    })
    
    # Categoria 2: Ropa (precio medio, alta frecuencia, margen alto)
    ropa = pd.DataFrame({
        'precio': np.random.normal(50, 15, 20),
        'ventas_mensuales': np.random.normal(80, 20, 20),
        'margen_beneficio': np.random.normal(45, 10, 20),
        'rating_promedio': np.random.normal(3.8, 0.4, 20),
        'num_reviews': np.random.normal(80, 30, 20)
    })
    
    # Categoria 3: Accesorios (bajo precio, muy alta frecuencia, margen muy alto)
    accesorios = pd.DataFrame({
        'precio': np.random.normal(15, 5, 15),
        'ventas_mensuales': np.random.normal(200, 50, 15),
        'margen_beneficio': np.random.normal(60, 10, 15),
        'rating_promedio': np.random.normal(4.0, 0.3, 15),
        'num_reviews': np.random.normal(50, 20, 15)
    })
    
    # Combinar datasets
    datos_productos = pd.concat([electronica, ropa, accesorios], ignore_index=True)
    datos_productos = datos_productos.abs()  # Asegurar valores positivos
    
    # Agregar IDs de productos
    productos_ids = [f'PROD_{str(i).zfill(3)}' for i in range(1, n_productos + 1)]
    datos_productos.insert(0, 'producto_id', productos_ids)
    
    return datos_productos


def generar_datos_alta_dimensionalidad():
    """
    Genera dataset de alta dimensionalidad para PCA y t-SNE.
    Incluye 20 variables y 3 grupos diferenciados.
    """
    np.random.seed(42)
    n_usuarios = 300
    n_variables = 20
    
    # Generar 3 grupos de usuarios con patrones diferentes
    grupo1 = np.random.randn(100, n_variables) + np.array([2, 3, 1, 4, 2, 1, 3, 2, 4, 1, 
                                                             2, 3, 1, 2, 3, 4, 1, 2, 3, 1])
    grupo2 = np.random.randn(100, n_variables) + np.array([1, 1, 2, 1, 3, 4, 1, 3, 1, 4,
                                                             3, 1, 2, 3, 1, 1, 4, 3, 1, 2])
    grupo3 = np.random.randn(100, n_variables) + np.array([4, 2, 3, 2, 1, 2, 4, 1, 2, 3,
                                                             1, 2, 4, 1, 2, 2, 3, 1, 4, 3])
    
    X_alta_dim = np.vstack([grupo1, grupo2, grupo3])
    etiquetas_reales = np.array([0]*100 + [1]*100 + [2]*100)
    
    # Crear nombres de variables
    nombres_vars = [f'var_{i+1:02d}' for i in range(n_variables)]
    
    # Convertir a DataFrame
    df_alta_dim = pd.DataFrame(X_alta_dim, columns=nombres_vars)
    df_alta_dim['grupo_real'] = etiquetas_reales
    
    return df_alta_dim


def generar_datos_prestamos():
    """
    Genera dataset de préstamos hipotecarios para análisis integrado.
    Incluye tres perfiles de riesgo: bajo, medio y alto.
    """
    np.random.seed(42)
    n_prestamos = 500
    
    # Perfil 1: Bajo riesgo (buenos pagadores)
    bajo_riesgo = pd.DataFrame({
        'monto_prestamo': np.random.normal(200000, 40000, 200),
        'ingreso_anual': np.random.normal(80000, 15000, 200),
        'ltv_ratio': np.random.normal(60, 10, 200),  # Loan-to-Value
        'score_credito': np.random.normal(750, 30, 200),
        'tasa_interes': np.random.normal(3.5, 0.5, 200),
        'plazo_anos': np.random.normal(25, 5, 200),
        'edad_solicitante': np.random.normal(40, 8, 200),
        'antiguedad_empleo': np.random.normal(10, 3, 200),
        'num_dependientes': np.random.poisson(1, 200),
        'deuda_total': np.random.normal(15000, 5000, 200),
        'pagos_atrasados_12m': np.random.poisson(0.2, 200)
    })
    
    # Perfil 2: Riesgo medio
    riesgo_medio = pd.DataFrame({
        'monto_prestamo': np.random.normal(180000, 35000, 200),
        'ingreso_anual': np.random.normal(55000, 12000, 200),
        'ltv_ratio': np.random.normal(75, 8, 200),
        'score_credito': np.random.normal(680, 25, 200),
        'tasa_interes': np.random.normal(4.2, 0.6, 200),
        'plazo_anos': np.random.normal(28, 4, 200),
        'edad_solicitante': np.random.normal(35, 7, 200),
        'antiguedad_empleo': np.random.normal(5, 2, 200),
        'num_dependientes': np.random.poisson(1.5, 200),
        'deuda_total': np.random.normal(25000, 8000, 200),
        'pagos_atrasados_12m': np.random.poisson(1, 200)
    })
    
    # Perfil 3: Alto riesgo
    alto_riesgo = pd.DataFrame({
        'monto_prestamo': np.random.normal(160000, 30000, 100),
        'ingreso_anual': np.random.normal(40000, 10000, 100),
        'ltv_ratio': np.random.normal(85, 5, 100),
        'score_credito': np.random.normal(620, 30, 100),
        'tasa_interes': np.random.normal(5.5, 0.8, 100),
        'plazo_anos': np.random.normal(30, 3, 100),
        'edad_solicitante': np.random.normal(30, 6, 100),
        'antiguedad_empleo': np.random.normal(2, 1, 100),
        'num_dependientes': np.random.poisson(2, 100),
        'deuda_total': np.random.normal(35000, 10000, 100),
        'pagos_atrasados_12m': np.random.poisson(3, 100)
    })
    
    # Combinar y procesar
    datos_prestamos = pd.concat([bajo_riesgo, riesgo_medio, alto_riesgo], ignore_index=True)
    datos_prestamos = datos_prestamos.abs()
    datos_prestamos['prestamo_id'] = [f'LOAN_{str(i).zfill(4)}' for i in range(1, len(datos_prestamos) + 1)]
    
    # Calcular ratio deuda-ingreso
    datos_prestamos['ratio_deuda_ingreso'] = (datos_prestamos['deuda_total'] / 
                                               datos_prestamos['ingreso_anual'] * 100)
    
    # Calcular cuota mensual aproximada
    datos_prestamos['cuota_mensual'] = (datos_prestamos['monto_prestamo'] * 
                                         datos_prestamos['tasa_interes'] / 100 / 12)
    
    # Reordenar columnas
    datos_prestamos = datos_prestamos[['prestamo_id'] + [col for col in datos_prestamos.columns if col != 'prestamo_id']]
    
    return datos_prestamos


def main():
    """Función principal que genera y guarda todos los datasets."""
    
    print("Generando datasets para Laboratorio 3...")
    print("=" * 80)
    
    # 1. Dataset de clientes
    print("\n1. Generando segmentacion_clientes_ecommerce.csv...")
    datos_clientes = generar_datos_clientes()
    datos_clientes.to_csv(os.path.join(output_dir, 'segmentacion_clientes_ecommerce.csv'), index=False)
    print(f"   ✓ {len(datos_clientes)} registros generados")
    
    # 2. Dataset de productos
    print("\n2. Generando catalogo_productos_retail.csv...")
    datos_productos = generar_datos_productos()
    datos_productos.to_csv(os.path.join(output_dir, 'catalogo_productos_retail.csv'), index=False)
    print(f"   ✓ {len(datos_productos)} registros generados")
    
    # 3. Dataset de alta dimensionalidad
    print("\n3. Generando metricas_usuarios_plataforma_digital.csv...")
    datos_alta_dim = generar_datos_alta_dimensionalidad()
    datos_alta_dim.to_csv(os.path.join(output_dir, 'metricas_usuarios_plataforma_digital.csv'), index=False)
    print(f"   ✓ {len(datos_alta_dim)} registros generados")
    
    # 4. Dataset de préstamos
    print("\n4. Generando cartera_prestamos_hipotecarios.csv...")
    datos_prestamos = generar_datos_prestamos()
    datos_prestamos.to_csv(os.path.join(output_dir, 'cartera_prestamos_hipotecarios.csv'), index=False)
    print(f"   ✓ {len(datos_prestamos)} registros generados")
    
    print("\n" + "=" * 80)
    print("✓ Todos los datasets generados exitosamente")
    print(f"\nArchivos guardados en: {output_dir}")


if __name__ == "__main__":
    main()
