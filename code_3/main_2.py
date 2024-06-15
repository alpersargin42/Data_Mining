import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,StandardScaler

data = pd.read_csv("train.csv")

#print(data)
#print(data.head()) # İlk 5 kaydı getir.
#print(data.describe())
#print(data.describe().T)

#data.drop(['id','target'],axis=1,inplace=True)
#print(data.head())

encoder = LabelEncoder()
nitelik=data.columns.tolist()
#print(nitelik)

for each in nitelik:
    data[each]=encoder.fit_transform(data[each])

#print(data.head())

scaler=StandardScaler()
data = scaler.fit_transform(data)
print(data)

