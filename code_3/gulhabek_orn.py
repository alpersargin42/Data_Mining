import matplotlib.pyplot as plt                 
import numpy as np
import pandas as pd

dataset = pd.read_csv("Mall_Customers.csv")
gender = dataset['Gender']
gender_counts = gender.value_counts()

plt.bar(gender_counts.index, gender_counts.values, color=['pink', 'blue'])
plt.show()
print(gender)



