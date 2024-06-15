"""
Naive Bayes
https://www.kdnuggets.com/2019/04/naive-bayes-baseline-model-machine-learning-classification-performance.html
Tenis Oynayıp/Oynayamama Durumu Bayes Modeli
Alper Sargın 201312030
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Tenis veri setini oku
tennis = pd.read_csv('tennis.csv')
print(tennis)

# Veri setini özellikler ve hedef değişken olarak ayır
X = tennis[['outlook', 'temp', 'humidity', 'windy']]
y = tennis['play']

# Kategorik özellikleri one-hot encoding ile dönüştür
X = pd.get_dummies(X)

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Gaussian Naive Bayes modelini oluştur
model = GaussianNB()

# Modeli eğit
model.fit(X_train, y_train)

# Test seti üzerinde tahmin yap
y_pred = model.predict(X_test)

# Modelin doğruluk skorunu hesapla
accuracy = accuracy_score(y_test, y_pred)
print('Model Doğruluğu:', accuracy)

# Tenis oynama durumunu gösteren bir grafik çiz
labels = ['Oynama', 'Oynamayamaz']
sizes = [sum(y_pred == 'yes'), sum(y_pred == 'no')]
colors = ['gold', 'lightskyblue']
explode = (0.1, 0)  # Sadece "Oynama" durumunu vurgula
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Daireyi daire olarak çiz
plt.title('Hava durumu koşullarına göre Tenis Oynama Tahmini')
plt.show()

# Örnek bir test yapısı
test_data = pd.DataFrame({
    'outlook': ['sunny'],
    'temp': ['hot'],
    'humidity': ['high'],
    'windy': ['true']
})

# Kategorik özellikleri one-hot encoding ile dönüştür
test_data = pd.get_dummies(test_data)

# Eğitim veri setindeki sütun isimlerini al
egitim_sutunlar = X.columns

# Test veri setinin sütun isimlerini eğitim veri setinin sütun isimleri ile güncelle
test_data = test_data.reindex(columns=egitim_sutunlar, fill_value=0)

# Model üzerinde tahmin yap
predicted_result = model.predict(test_data)

# Tahmin sonucunu ekrana yaz
print('Hava durumu koşullarına göre tenis oynama tahmini:', predicted_result[0])
