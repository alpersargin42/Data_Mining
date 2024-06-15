import matplotlib.pyplot as plt                 
import numpy as np

xplot=np.array([3,2,5,8])
yplot=np.array([2,4,8,10])

plt.plot(xplot,yplot)
plt.xlabel('X EKSENİ')
plt.ylabel('Y EKSENİ')
plt.title('Örnek Çizgi Grafiği')
plt.grid()
plt.show()

