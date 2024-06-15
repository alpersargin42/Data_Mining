import matplotlib.pyplot as plt                 
import numpy as np

x_ekseni=np.array(["A","B","C","D"])
y_ekseni=np.array([3,8,1,10])

#plt.bar(x_ekseni,y_ekseni)
plt.barh(x_ekseni,y_ekseni,color="lightblue")
plt.title("Bar Chart Example")
plt.show()

