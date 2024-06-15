"""
https://www.turing.com/kb/an-introduction-to-naive-bayes-algorithm-for-beginners

Alper SARGIN 201312030
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Veri setini yükle
dataset = pd.read_csv('Social_Network_Ads.csv')

# Özellikleri (X) ve hedef değişkeni (y) çıkar
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Cinsiyet sütununu One-Hot Encoding ile dönüştür
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# One-Hot Encoding sonrası sütun adlarını kontrol et
print("One-Hot Encoding Sonrası Sütun Adları:", ct.get_feature_names_out())

# One-Hot Encoding sonrasında oluşan sütun sayısını kontrol et
print("One-Hot Encoding Sonrasında Oluşan Sütun Sayısı:", X.shape[1])

# Veri setini eğitim ve test setlerine bölelim
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Özellik ölçeklendirmesi için StandardScaler kullanalım
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Naive Bayes sınıflandırıcısını eğitelim
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# # Yeni bir veri noktasında tahmin yapalım
# print("Yeni Veri Noktası Tahmini:", classifier.predict(sc.transform([[0, 1, 30, 87000]])))

# Test seti üzerinde tahminler yapalım
y_pred = classifier.predict(X_test)

# Modelin performansını değerlendirelim
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print("Karışıklık Matrisi:\n", cm)
print("Doğruluk:", accuracy)

# Eğitim seti sonuçlarını görselleştirelim
X_set, y_set = sc.inverse_transform(X_train), y_train
X1, X2 = np.meshgrid(np.arange(start=X_set[:, 2].min() - 10, stop=X_set[:, 2].max() + 10, step=0.25),
                     np.arange(start=X_set[:, 3].min() - 1000, stop=X_set[:, 3].max() + 1000, step=0.25))
plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha=0.75, cmap=ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 2], X_set[y_set == j, 3], c=ListedColormap(('red', 'green'))(i), label=j)
plt.title('Naive Bayes (Eğitim seti)')
plt.xlabel('Yaş')
plt.ylabel('Tahmini Maaş')
plt.legend()
plt.show()

# Test seti sonuçlarını görselleştirelim
X_set, y_set = sc.inverse_transform(X_test), y_test
X1, X2 = np.meshgrid(np.arange(start=X_set[:, 2].min() - 10, stop=X_set[:, 2].max() + 10, step=0.25),
                     np.arange(start=X_set[:, 3].min() - 1000, stop=X_set[:, 3].max() + 1000, step=0.25))
plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha=0.75, cmap=ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 2], X_set[y_set == j, 3], c=ListedColormap(('red', 'green'))(i), label=j)
plt.title('Naive Bayes (Test seti)')
plt.xlabel('Yaş')
plt.ylabel('Tahmini Maaş')
plt.legend()
plt.show()
