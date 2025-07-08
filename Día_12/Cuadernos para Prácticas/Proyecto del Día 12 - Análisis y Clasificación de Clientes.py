# Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA 
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

# Cargar los datos
clientes = pd.read_csv('customer_data.csv')
clientes.head()

clientes.max()

clientes.min()

# Ver información básica del dataset
clientes.info()

# Ver la descripción de las estadísticas básicas del dataset
clientes.describe()

# Normalizar los datos
escalador = MinMaxScaler()
clientes_escalados = escalador.fit_transform(clientes[['Edad', 'Ingresos Anuales (k$)', 'Puntuación de Gasto (1-100)']])
clientes_escalados

# Aplicar PCA
pca = PCA(n_components=2)
pca_resultados = pca.fit_transform(clientes_escalados)

# Aplicar SVD
U, sigma, VT = np.linalg.svd(clientes_escalados)

# Seleccionar los dos primeros componentes singulares para reducción de dimensiones
k = 2
svd_resultados = U[:, :k] * sigma[:k]

# Aplicar K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_clusters = kmeans.fit_predict(clientes_escalados)

# Aplicar Clustering Jerárquico
linked = linkage(clientes_escalados, 'ward')

# Crear un gráfico de dispersión para los resultados de PCA
plt.figure(figsize=(10, 8))
sns.scatterplot(x=pca_resultados[:, 0], y = pca_resultados[:, 1], hue= kmeans_clusters, palette= 'viridis', s=100)
plt.title('Grafico de dispersion de los resultados de PCA')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(title='Cluster')
plt.grid(True)

# Crear un dendrograma del clústering jerárquico
plt.figure(figsize=(10, 7))
dendrogram(linked)
plt.title('Dendrograma de Clustering Jerarquico')
plt.xlabel('Indice de muestra')
plt.ylabel('Distancia de Ward')
plt.axhline(y=10, color='r', linestyle='--')

# analisis de cluster para realizar estrategias

cluster_info = pd.DataFrame({
    'Cluster' : kmeans_clusters,
    'Edad' : clientes['Edad'],
    'Ingresos' : clientes['Ingresos Anuales (k$)'],
    'Gasto' : clientes['Puntuación de Gasto (1-100)']
})

for cluster in cluster_info['Cluster'].unique():
    cluster_data = cluster_info[cluster_info['Cluster'] == cluster]
    print(f'Cluster {cluster}')
    print(f' - Edad Media: {cluster_data["Edad"].mean():.0f}')
    print(f' - Ingresos Media: {cluster_data["Ingresos"].mean():.2f}')
    print(f' - Gasto Media: {cluster_data["Gasto"].mean():.2f}')

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

iris = load_iris()
X = iris.data
Z = linkage(X, 'ward')

plt.figure(figsize=(10, 7))
dendrogram(Z,
            orientation="top",
            labels=iris.target,
            distance_sort="descending",
            show_leaf_counts=True)
plt.title("Dendrograma del Agrupamiento Jerárquico - Método de Enlace Ward")
plt.xlabel("Índice de la Muestra")
plt.ylabel("Distancia")