import numpy as np            
import matplotlib.pyplot as plt     
from sklearn.decomposition import PCA                

rng = np.random.RandomState()
rng_1 = rng.rand(2,2)
rng_2 = rng.rand(2,200)

data = np.dot(rng_1,rng_2)
# print(data.shape)

data = data.T                    
# print(data.shape)

# plt.scatter(data[:,0],data[:,1])
# plt.show()
# pca = PCA(n_components=2)
# pca.fit(data)
# print(pca.components_)
# print(pca.explained_variance_)
# print(pca.explained_variance_ratio_)
pca = PCA(n_components=1)
pca.fit(data)
data_pca = pca.transform(data)
# print(data.shape)
# print(data_pca.shape)

data_yeni = pca.inverse_transform(data_pca)
plt.scatter(data[:,0],data[:,1],alpha=0.3)
plt.scatter(data_yeni[:,0],data_yeni[:,1],alpha=0.8)
plt.show()
