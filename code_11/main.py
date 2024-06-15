import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist


df = pd.read_csv('Social_Network_Ads.csv')
veri = df[['Age', 'EstimatedSalary']].values

#K-Means eğitimi(from sklearn.cluster import KMeans)
kmeans = KMeans(n_clusters=3)
kmeans.fit(veri)

#K-Medoids eğitimi(from sklearn_extra.cluster import KMedoids)
kmedoids = KMedoids(n_clusters=3)
kmedoids.fit(veri)


plt.figure(figsize=(12, 5))

# K-means grafiği
plt.subplot(1, 2, 1)
plt.scatter(df['Age'], df['EstimatedSalary'], c=kmeans.labels_, cmap='rainbow')
plt.title('K-means Kümeleme')
plt.xlabel('Yaş')
plt.ylabel('Tahmini Maaş')

# K-medoids grafiği
plt.subplot(1, 2, 2)
plt.scatter(df['Age'], df['EstimatedSalary'], c=kmedoids.labels_, cmap='rainbow')
plt.title('K-medoids Kümeleme')
plt.xlabel('Yaş')
plt.ylabel('Tahmini Maaş')
plt.show()
















