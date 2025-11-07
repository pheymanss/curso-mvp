"""
Generación de gráficos para el Módulo 3: Métodos de Aprendizaje No Supervisado
Este script genera todas las visualizaciones utilizadas en el contenido teórico.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs, make_moons
import warnings
warnings.filterwarnings('ignore')

# Cambiar al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def grafico_kmeans_iteraciones():
    """
    Ilustra el proceso iterativo de K-Means mostrando las iteraciones
    del algoritmo convergiendo hacia la solución final.
    """
    np.random.seed(42)
    
    # Generar datos sintéticos con 3 clusters naturales
    X, y_true = make_blobs(n_samples=300, centers=3, n_features=2, 
                           cluster_std=0.6, random_state=42)
    
    # Ejecutar K-Means con seguimiento de iteraciones
    kmeans = KMeans(n_clusters=3, init='random', n_init=1, 
                    max_iter=1, random_state=10)
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.ravel()
    
    iteraciones = [0, 1, 2, 3, 5, 10]
    
    for idx, n_iter in enumerate(iteraciones):
        if n_iter == 0:
            # Mostrar solo centroides iniciales (sin iteraciones)
            kmeans_temp = KMeans(n_clusters=3, init='random', n_init=1, 
                                 max_iter=1, random_state=10)
            kmeans_temp.fit(X)
            # Tomar centroides iniciales antes de la primera iteración
            from sklearn.utils import check_random_state
            rs = check_random_state(10)
            centroides = X[rs.choice(X.shape[0], 3, replace=False)]
            axes[idx].scatter(X[:, 0], X[:, 1], c='gray', alpha=0.3, s=30)
            axes[idx].scatter(centroides[:, 0], centroides[:, 1], 
                            c='red', marker='X', s=300, 
                            edgecolors='black', linewidths=2)
        else:
            kmeans_temp = KMeans(n_clusters=3, init='random', n_init=1, 
                                 max_iter=n_iter, random_state=10)
            labels = kmeans_temp.fit_predict(X)
            centroides = kmeans_temp.cluster_centers_
            axes[idx].scatter(X[:, 0], X[:, 1], c=labels, 
                            cmap='viridis', alpha=0.6, s=30)
            axes[idx].scatter(centroides[:, 0], centroides[:, 1], 
                            c='red', marker='X', s=300, 
                            edgecolors='black', linewidths=2)
        
        axes[idx].set_title(f'Iteración {n_iter}', fontsize=12, fontweight='bold')
        axes[idx].set_xlabel('Feature 1')
        axes[idx].set_ylabel('Feature 2')
        axes[idx].grid(True, alpha=0.3)
    
    plt.suptitle('Proceso Iterativo de K-Means: Convergencia de Centroides', 
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('graficos/kmeans_iteraciones.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfico generado: kmeans_iteraciones.png")


def grafico_metodo_codo():
    """
    Ilustra el método del codo para selección del número óptimo de clusters,
    mostrando cómo la inercia disminuye con diferentes valores de k.
    """
    np.random.seed(42)
    X, _ = make_blobs(n_samples=500, centers=4, n_features=2, 
                      cluster_std=1.0, random_state=42)
    
    inercias = []
    rango_k = range(1, 11)
    
    for k in rango_k:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        inercias.append(kmeans.inertia_)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(rango_k, inercias, marker='o', linewidth=2, markersize=8)
    ax.axvline(x=4, color='red', linestyle='--', linewidth=2, 
               label='Codo sugerido (k=4)')
    
    ax.set_xlabel('Número de Clusters (k)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Inercia (Suma de Cuadrados Intra-Cluster)', 
                  fontsize=12, fontweight='bold')
    ax.set_title('Método del Codo para Selección de K', 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    
    # Anotar el punto del codo
    ax.annotate('Punto del codo', xy=(4, inercias[3]), 
                xytext=(6, inercias[3] + 500),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=11, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('graficos/metodo_codo.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfico generado: metodo_codo.png")


def grafico_coeficiente_silueta():
    """
    Muestra cómo el coeficiente de silueta varía con diferentes valores de k,
    ayudando a identificar el número óptimo de clusters.
    """
    np.random.seed(42)
    X, _ = make_blobs(n_samples=500, centers=4, n_features=2, 
                      cluster_std=1.0, random_state=42)
    
    siluetas = []
    rango_k = range(2, 11)
    
    for k in rango_k:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)
        silueta = silhouette_score(X, labels)
        siluetas.append(silueta)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(rango_k, siluetas, marker='o', linewidth=2, markersize=8, 
            color='teal')
    max_idx = np.argmax(siluetas)
    ax.axvline(x=rango_k[max_idx], color='red', linestyle='--', linewidth=2,
               label=f'Máximo en k={rango_k[max_idx]}')
    
    ax.set_xlabel('Número de Clusters (k)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Coeficiente de Silueta', fontsize=12, fontweight='bold')
    ax.set_title('Coeficiente de Silueta vs Número de Clusters', 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    ax.set_ylim([0, 1])
    
    # Anotar el máximo
    ax.annotate(f'Óptimo: {siluetas[max_idx]:.3f}', 
                xy=(rango_k[max_idx], siluetas[max_idx]),
                xytext=(rango_k[max_idx] + 1, siluetas[max_idx] - 0.1),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=11, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('graficos/coeficiente_silueta.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfico generado: coeficiente_silueta.png")


def grafico_sensibilidad_escala():
    """
    Demuestra cómo variables en diferentes escalas afectan el clustering,
    comparando resultados antes y después de estandarización.
    """
    np.random.seed(42)
    
    # Generar datos donde una variable tiene escala mucho mayor
    n_samples = 200
    # Variable 1: escala pequeña (0-10)
    var1 = np.random.normal(5, 2, n_samples)
    # Variable 2: escala grande (0-1000)
    var2 = np.random.normal(500, 150, n_samples)
    
    # Crear clusters artificiales
    cluster1_mask = (var1 < 5) & (var2 < 500)
    cluster2_mask = (var1 >= 5) & (var2 >= 500)
    
    X_original = np.column_stack([var1, var2])
    
    # K-Means sin estandarizar
    kmeans_sin = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels_sin = kmeans_sin.fit_predict(X_original)
    
    # K-Means con estandarización
    scaler = StandardScaler()
    X_escalado = scaler.fit_transform(X_original)
    kmeans_con = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels_con = kmeans_con.fit_predict(X_escalado)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Gráfico sin estandarización
    axes[0].scatter(X_original[:, 0], X_original[:, 1], c=labels_sin, 
                    cmap='viridis', alpha=0.6, s=50)
    axes[0].scatter(kmeans_sin.cluster_centers_[:, 0], 
                    kmeans_sin.cluster_centers_[:, 1],
                    c='red', marker='X', s=300, edgecolors='black', linewidths=2)
    axes[0].set_xlabel('Variable 1 (escala 0-10)', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Variable 2 (escala 0-1000)', fontsize=11, fontweight='bold')
    axes[0].set_title('Sin Estandarización\n(Variable 2 domina distancias)', 
                      fontsize=12, fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    
    # Gráfico con estandarización
    axes[1].scatter(X_escalado[:, 0], X_escalado[:, 1], c=labels_con, 
                    cmap='viridis', alpha=0.6, s=50)
    axes[1].scatter(kmeans_con.cluster_centers_[:, 0], 
                    kmeans_con.cluster_centers_[:, 1],
                    c='red', marker='X', s=300, edgecolors='black', linewidths=2)
    axes[1].set_xlabel('Variable 1 (estandarizada)', fontsize=11, fontweight='bold')
    axes[1].set_ylabel('Variable 2 (estandarizada)', fontsize=11, fontweight='bold')
    axes[1].set_title('Con Estandarización\n(Ambas variables contribuyen equitativamente)', 
                      fontsize=12, fontweight='bold')
    axes[1].grid(True, alpha=0.3)
    
    plt.suptitle('Impacto de la Estandarización en K-Means', 
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('graficos/sensibilidad_escala.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfico generado: sensibilidad_escala.png")


def grafico_dendrograma():
    """
    Genera un dendrograma que ilustra la estructura jerárquica
    del clustering aglomerativo.
    """
    np.random.seed(42)
    X, _ = make_blobs(n_samples=50, centers=4, n_features=2, 
                      cluster_std=0.8, random_state=42)
    
    # Calcular linkage matrix
    Z = linkage(X, method='ward')
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    dendrogram(Z, ax=ax, color_threshold=15, above_threshold_color='gray')
    
    # Añadir línea horizontal de corte sugerido
    ax.axhline(y=15, color='red', linestyle='--', linewidth=2, 
               label='Altura de corte sugerida')
    
    ax.set_xlabel('Índice de Observación', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distancia (Altura)', fontsize=12, fontweight='bold')
    ax.set_title('Dendrograma de Clustering Jerárquico (Método de Ward)', 
                 fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('graficos/dendrograma.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfico generado: dendrograma.png")


def grafico_metodos_enlace():
    """
    Compara visualmente los diferentes métodos de enlace en clustering jerárquico
    (single, complete, average, ward) aplicados al mismo dataset.
    """
    np.random.seed(42)
    X, _ = make_blobs(n_samples=200, centers=3, n_features=2, 
                      cluster_std=0.7, random_state=42)
    
    metodos = ['single', 'complete', 'average', 'ward']
    nombres = ['Single Linkage', 'Complete Linkage', 'Average Linkage', 'Ward']
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.ravel()
    
    for idx, (metodo, nombre) in enumerate(zip(metodos, nombres)):
        clustering = AgglomerativeClustering(n_clusters=3, linkage=metodo)
        labels = clustering.fit_predict(X)
        
        axes[idx].scatter(X[:, 0], X[:, 1], c=labels, 
                         cmap='viridis', alpha=0.6, s=50)
        axes[idx].set_title(nombre, fontsize=12, fontweight='bold')
        axes[idx].set_xlabel('Feature 1', fontsize=10)
        axes[idx].set_ylabel('Feature 2', fontsize=10)
        axes[idx].grid(True, alpha=0.3)
        
        # Calcular y mostrar silueta
        silueta = silhouette_score(X, labels)
        axes[idx].text(0.05, 0.95, f'Silueta: {silueta:.3f}',
                      transform=axes[idx].transAxes,
                      bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                      verticalalignment='top', fontsize=9)
    
    plt.suptitle('Comparación de Métodos de Enlace en Clustering Jerárquico', 
                 fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig('graficos/metodos_enlace.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfico generado: metodos_enlace.png")


def grafico_scree_plot_pca():
    """
    Muestra un scree plot típico de PCA con varianza explicada
    por componente y varianza acumulada.
    """
    np.random.seed(42)
    
    # Generar datos con correlación entre variables
    n_samples = 300
    n_features = 10
    
    # Crear matriz de covarianza con estructura
    cov_matrix = np.eye(n_features)
    for i in range(n_features-1):
        cov_matrix[i, i+1] = 0.7
        cov_matrix[i+1, i] = 0.7
    
    X = np.random.multivariate_normal(np.zeros(n_features), cov_matrix, n_samples)
    
    # Aplicar PCA
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA()
    pca.fit(X_scaled)
    
    varianza_explicada = pca.explained_variance_ratio_
    varianza_acumulada = np.cumsum(varianza_explicada)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Scree plot - varianza por componente
    componentes = range(1, len(varianza_explicada) + 1)
    ax1.bar(componentes, varianza_explicada, alpha=0.7, color='steelblue')
    ax1.plot(componentes, varianza_explicada, marker='o', 
             linestyle='-', color='darkblue', linewidth=2)
    ax1.set_xlabel('Componente Principal', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Proporción de Varianza Explicada', fontsize=12, fontweight='bold')
    ax1.set_title('Scree Plot: Varianza por Componente', 
                  fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.set_xticks(componentes)
    
    # Varianza acumulada
    ax2.plot(componentes, varianza_acumulada, marker='o', 
             linewidth=2, markersize=8, color='darkgreen')
    ax2.axhline(y=0.80, color='red', linestyle='--', linewidth=1.5, 
                label='80% varianza')
    ax2.axhline(y=0.90, color='orange', linestyle='--', linewidth=1.5, 
                label='90% varianza')
    ax2.axhline(y=0.95, color='purple', linestyle='--', linewidth=1.5, 
                label='95% varianza')
    ax2.set_xlabel('Número de Componentes', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Varianza Acumulada', fontsize=12, fontweight='bold')
    ax2.set_title('Varianza Acumulada por Componentes', 
                  fontsize=12, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_xticks(componentes)
    ax2.set_ylim([0, 1.05])
    
    plt.tight_layout()
    plt.savefig('graficos/scree_plot_pca.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfico generado: scree_plot_pca.png")


def grafico_pca_proyeccion():
    """
    Ilustra cómo PCA proyecta datos de alta dimensionalidad a 2D,
    mostrando la separación de clusters en el espacio reducido.
    """
    np.random.seed(42)
    
    # Generar datos en 5 dimensiones con 3 clusters
    X, y = make_blobs(n_samples=300, n_features=5, centers=3, 
                      cluster_std=1.2, random_state=42)
    
    # Estandarizar y aplicar PCA
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=y, 
                        cmap='viridis', alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
    
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% varianza)', 
                  fontsize=12, fontweight='bold')
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% varianza)', 
                  fontsize=12, fontweight='bold')
    ax.set_title('Proyección PCA: Reducción de 5D a 2D', 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Añadir colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Cluster', fontsize=11, fontweight='bold')
    
    # Añadir texto informativo
    total_var = pca.explained_variance_ratio_[:2].sum()
    ax.text(0.05, 0.95, f'Varianza total explicada: {total_var*100:.1f}%',
            transform=ax.transAxes,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
            verticalalignment='top', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('graficos/pca_proyeccion.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfico generado: pca_proyeccion.png")


def grafico_comparacion_tsne_umap():
    """
    Compara visualmente las proyecciones de t-SNE y UMAP en el mismo dataset,
    mostrando cómo cada método preserva estructura local y global.
    """
    from sklearn.manifold import TSNE
    try:
        import umap
        tiene_umap = True
    except ImportError:
        tiene_umap = False
        print("Advertencia: UMAP no está instalado. Se omitirá ese gráfico.")
    
    np.random.seed(42)
    
    # Generar datos complejos (no lineales)
    X, y = make_moons(n_samples=300, noise=0.1, random_state=42)
    
    # Aplicar t-SNE
    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    X_tsne = tsne.fit_transform(X)
    
    if tiene_umap:
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        
        # Datos originales
        axes[0].scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', 
                       alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
        axes[0].set_title('Datos Originales (2D)', fontsize=12, fontweight='bold')
        axes[0].set_xlabel('Feature 1', fontsize=10)
        axes[0].set_ylabel('Feature 2', fontsize=10)
        axes[0].grid(True, alpha=0.3)
        
        # t-SNE
        axes[1].scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='viridis', 
                       alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
        axes[1].set_title('t-SNE (perplexity=30)', fontsize=12, fontweight='bold')
        axes[1].set_xlabel('t-SNE 1', fontsize=10)
        axes[1].set_ylabel('t-SNE 2', fontsize=10)
        axes[1].grid(True, alpha=0.3)
        
        # UMAP
        reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, random_state=42)
        X_umap = reducer.fit_transform(X)
        axes[2].scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='viridis', 
                       alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
        axes[2].set_title('UMAP (n_neighbors=15)', fontsize=12, fontweight='bold')
        axes[2].set_xlabel('UMAP 1', fontsize=10)
        axes[2].set_ylabel('UMAP 2', fontsize=10)
        axes[2].grid(True, alpha=0.3)
    else:
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # Datos originales
        axes[0].scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', 
                       alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
        axes[0].set_title('Datos Originales (2D)', fontsize=12, fontweight='bold')
        axes[0].set_xlabel('Feature 1', fontsize=10)
        axes[0].set_ylabel('Feature 2', fontsize=10)
        axes[0].grid(True, alpha=0.3)
        
        # t-SNE
        axes[1].scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='viridis', 
                       alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
        axes[1].set_title('t-SNE (perplexity=30)', fontsize=12, fontweight='bold')
        axes[1].set_xlabel('t-SNE 1', fontsize=10)
        axes[1].set_ylabel('t-SNE 2', fontsize=10)
        axes[1].grid(True, alpha=0.3)
    
    plt.suptitle('Comparación de Métodos de Reducción de Dimensionalidad', 
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('graficos/comparacion_tsne_umap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfico generado: comparacion_tsne_umap.png")


def grafico_limitaciones_kmeans():
    """
    Ilustra casos donde K-Means falla debido a sus asunciones sobre
    la forma de los clusters (clusters no esféricos, densidades diferentes).
    """
    np.random.seed(42)
    
    # Generar diferentes tipos de datos problemáticos para K-Means
    # 1. Clusters en forma de media luna
    X_moons, y_moons = make_moons(n_samples=200, noise=0.05, random_state=42)
    
    # 2. Clusters de densidades muy diferentes
    X_blobs1, _ = make_blobs(n_samples=100, centers=[[0, 0]], 
                              cluster_std=0.3, random_state=42)
    X_blobs2, _ = make_blobs(n_samples=100, centers=[[3, 3]], 
                              cluster_std=1.5, random_state=42)
    X_densidades = np.vstack([X_blobs1, X_blobs2])
    y_densidades = np.hstack([np.zeros(100), np.ones(100)])
    
    # 3. Clusters concéntricos
    theta = np.linspace(0, 2*np.pi, 100)
    r1, r2 = 1, 3
    X_inner = np.column_stack([r1*np.cos(theta), r1*np.sin(theta)])
    X_outer = np.column_stack([r2*np.cos(theta), r2*np.sin(theta)])
    X_inner += np.random.normal(0, 0.1, X_inner.shape)
    X_outer += np.random.normal(0, 0.1, X_outer.shape)
    X_concentrico = np.vstack([X_inner, X_outer])
    y_concentrico = np.hstack([np.zeros(100), np.ones(100)])
    
    datasets = [
        (X_moons, y_moons, 'Clusters en Forma de Media Luna'),
        (X_densidades, y_densidades, 'Clusters con Densidades Diferentes'),
        (X_concentrico, y_concentrico, 'Clusters Concéntricos')
    ]
    
    fig, axes = plt.subplots(3, 2, figsize=(12, 16))
    
    for idx, (X, y_true, titulo) in enumerate(datasets):
        # Clustering real (a mano)
        axes[idx, 0].scatter(X[:, 0], X[:, 1], c=y_true, 
                            cmap='viridis', alpha=0.6, s=50)
        axes[idx, 0].set_title(f'{titulo}\n(Estructura Real)', 
                              fontsize=11, fontweight='bold')
        axes[idx, 0].set_xlabel('Feature 1')
        axes[idx, 0].set_ylabel('Feature 2')
        axes[idx, 0].grid(True, alpha=0.3)
        
        # K-Means result
        kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
        y_kmeans = kmeans.fit_predict(X)
        axes[idx, 1].scatter(X[:, 0], X[:, 1], c=y_kmeans, 
                            cmap='viridis', alpha=0.6, s=50)
        axes[idx, 1].scatter(kmeans.cluster_centers_[:, 0], 
                            kmeans.cluster_centers_[:, 1],
                            c='red', marker='X', s=300, 
                            edgecolors='black', linewidths=2)
        axes[idx, 1].set_title(f'{titulo}\n(Resultado K-Means)', 
                              fontsize=11, fontweight='bold')
        axes[idx, 1].set_xlabel('Feature 1')
        axes[idx, 1].set_ylabel('Feature 2')
        axes[idx, 1].grid(True, alpha=0.3)
        
        # Calcular silueta para K-Means
        silueta = silhouette_score(X, y_kmeans)
        axes[idx, 1].text(0.05, 0.95, f'Silueta: {silueta:.3f}',
                         transform=axes[idx, 1].transAxes,
                         bbox=dict(boxstyle='round', facecolor='salmon', alpha=0.8),
                         verticalalignment='top', fontsize=9)
    
    plt.suptitle('Limitaciones de K-Means: Casos donde el Algoritmo Falla', 
                 fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig('graficos/limitaciones_kmeans.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfico generado: limitaciones_kmeans.png")


def main():
    """
    Ejecuta todas las funciones de generación de gráficos.
    """
    print("\n" + "="*60)
    print("Generando gráficos para Módulo 3")
    print("="*60 + "\n")
    
    # Sección 2: K-Means
    print("Sección 2: K-Means")
    grafico_kmeans_iteraciones()
    grafico_metodo_codo()
    grafico_coeficiente_silueta()
    grafico_sensibilidad_escala()
    grafico_limitaciones_kmeans()
    
    # Sección 3: Clustering Jerárquico
    print("\nSección 3: Clustering Jerárquico")
    grafico_dendrograma()
    grafico_metodos_enlace()
    
    # Sección 4: PCA
    print("\nSección 4: PCA")
    grafico_scree_plot_pca()
    grafico_pca_proyeccion()
    
    # Sección 5: Métodos Modernos
    print("\nSección 5: Métodos Modernos")
    grafico_comparacion_tsne_umap()
    
    print("\n" + "="*60)
    print("✓ Todos los gráficos generados exitosamente")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
