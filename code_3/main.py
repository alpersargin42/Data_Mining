#Kütüphaneleri import ediyoruz.
from sklearn.datasets import load_iris
from sklearn import preprocessing
import numpy as np

iris=load_iris()
#print(iris)

#print(iris.data)
#print(iris.target)

#print(iris.data.shape)
#print(iris.target.shape)

x = iris.data
#print(x)

y = iris.target
#print(y)

normalied_x = preprocessing.normalize(x)
#print(normalied_x)

scaled_x = preprocessing.scale(x)
print(scaled_x)