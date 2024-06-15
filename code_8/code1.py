'''
201312030 - Alper SARGIN - 5 Aralık 2023 Ödevi

Sonuçları EKRAN'A yazdıran python kodu
'''
import pandas as pd
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('exam_score.csv')
X = data.iloc[:, [0, 1]].values
y = data.iloc[:, 2].values

fold_degerleri = list(range(2, 6))
n_neighbors_degerleri = list(range(1, 11))
uzaklik_olcutleri = ['minkowski', 'euclidean', 'manhattan', 'chebyshev']
agirlik = ['uniform', 'distance']

for fold in fold_degerleri:
    for metric in uzaklik_olcutleri:
        for n_neighbors in n_neighbors_degerleri:
            for weight in agirlik:
                knn = KNeighborsClassifier(n_neighbors=n_neighbors, metric=metric, weights=weight)
                
                # k-fold cross-validation işlemi
                scores = cross_val_score(knn, X, y, cv=fold)
                
                # Confusion Matrix
                y_pred = cross_val_predict(knn, X, y, cv=fold)
                conf_matrix = confusion_matrix(y, y_pred)
                
                # Doğruluk (Accuracy) hesaplama
                accuracy = accuracy_score(y, y_pred)
                
                # Hassasiyet (Precision) hesaplama
                precision = precision_score(y, y_pred, average='weighted')
                
                # Duyarlılık (Recall) hesaplama
                recall = recall_score(y, y_pred, average='weighted')
                
                # F1 Skoru hesaplama
                f1 = f1_score(y, y_pred, average='weighted')
                
                print(f"{knn}")
                print(f"K-Fold: {fold}\n Uzaklık Ölçütü: {metric}\n Komşu Sayısı: {n_neighbors}\n Ağırlıklandırma: {weight}")
                print("5-fold Cross-Validation Skorları:")
                print(scores)
                print("Ortalama Skor:", scores.mean())
                print("Confusion Matrix:")
                print(conf_matrix)
                print("Accuracy:", accuracy)
                print("Precision:", precision)
                print("Recall:", recall)
                print("F1 Score:", f1)
                print("=================================")
