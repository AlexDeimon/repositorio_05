import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
X = np.array([[5,3],[10,15],[24,10],[30,45],[40,20],[55,70],[71,80],[60,78],[90,91],[50,30],[15,45],[20,60],[60,20],[10,24],[70,60]])

plt.scatter(X[:,0], X[:,1])

#implementacion algoritmo
Kmeans = KMeans(n_clusters = 2)
Kmeans.fit(X)

#Imprimir los centroides
centroides = Kmeans.cluster_centers_
print(centroides)

labels = Kmeans.labels_
print(labels)

plt.scatter(X[:, 0], X[:,1], c=Kmeans.labels_,cmap='rainbow')
plt.scatter(centroides[:,0], centroides[:,1], color= 'black', marker='*')

