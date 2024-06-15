import matplotlib.pyplot as plt                 
import numpy as np

dataset=np.array([10,20,15,20])
label = ["A","B","C","D"]
plt.pie(dataset,labels=label)
plt.show()


