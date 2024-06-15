import matplotlib.pyplot as plt                 
import numpy as np

xplot=np.array([4,8,7,9,5,1,2,3,6,6])
yplot=np.array([7,8,9,1,4,1,1,7,9,1])

plt.xlabel("Nufüs")
plt.ylabel("Kar oranı")
plt.title("Nufüsa Göre Kar Oranı")
plt.scatter(xplot, yplot)
plt.show()
