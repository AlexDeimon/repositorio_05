import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

dataset = pd.read_csv("clientes.csv")
X = dataset.iloc[:,3:5].values
plt.scatter(X[:,0], X[:,1])

#aplicando el kmeans
kmeans = KMeans(n_clusters=3, max_iter=50)
kmeans.fit(X)
centroides = kmeans.cluster_centers_
labels = kmeans.labels_
plt.scatter(X[:, 0], X[:,1], c=labels, cmap='viridis')
plt.scatter(centroides[:,0], centroides[:,1], color= 'red', marker='x')


