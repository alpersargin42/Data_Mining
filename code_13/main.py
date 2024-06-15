'''
201312030    Alper SARGIN      2 OCAK 2024
'''
import pandas as pd       
from sklearn.preprocessing import LabelEncoder    
import seaborn as sns                 
import matplotlib.pyplot as plt   
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.multiclass import OneVsRestClassifier
import numpy as np

data = pd.read_csv("telefon_bilgisi.csv")
# print(data)
# print(data.head())
# print(data.tail())
# print(data.shape)
# print(data.info())
# print(data.dtypes)
# eksik_veri=data.isnull().sum()
# print(eksik_veri)

# kayit_sil= data.dropna()
# print(kayit_sil)

# bir_onceki= data.fillna(method="ffill")
# print(bir_onceki)

# print(data.duplicated().sum())

# label_encoder = LabelEncoder()
# sutun = ['arac', 'ag_turu', 'ag_tipi']
# for column in sutun:
#     data[column] = label_encoder.fit_transform(data[column])
# correlation_matrix = data[sutun].corr()
# print(correlation_matrix)

# plt.figure(figsize=(8, 6))
# sns.heatmap(correlation_matrix, cmap='coolwarm',annot=True)
# plt.show()

'''
İRİS İŞLEMLERİ 
'''
iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Logistic Regression")
print("Doğruluk Oranı:", accuracy_score(y_test, y_pred))
print("Sınıflandırma Raporu:\n", classification_report(y_test, y_pred))


'''
Farklı K-FOLD Değerleri İçin
'''
kfold_degerleri = [2,3,5,7,10]

farkli_kfold = []
for kfold in kfold_degerleri:
    naive = GaussianNB()
    scores = cross_val_score(naive, X, y, cv=kfold)
    dogruluk = np.mean(scores)
    farkli_kfold.append(dogruluk)
    print(f"Naive Bayes-k-fold= {kfold} - Doğruluk Oranı: {dogruluk}")
