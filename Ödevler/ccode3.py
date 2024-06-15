'''
201312030 - Alper SARGIN - 5 Aralık 2023 Ödevi

Sonuçları EKRAN'A yazdıran python kodu

(En iyi değerleri bulan ve ekrana yazdıran kod)
'''
import pandas as pd
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('exam_score.csv')
X = data.iloc[:, [0, 1]].values
y = data.iloc[:, 2].values

fold_values = list(range(2, 6))
n_neighbors_values = list(range(1, 11))
distance_metrics = ['minkowski', 'euclidean', 'manhattan', 'chebyshev']
weights = ['uniform', 'distance']

en_iyi_deger= {
    'accuracy': 0,
    'precision': 0,
    'recall': 0,
    'f1': 0
}

for fold in fold_values:
    for metric in distance_metrics:
        for n_neighbors in n_neighbors_values:
            for weight in weights:
                knn = KNeighborsClassifier(n_neighbors=n_neighbors, metric=metric, weights=weight)
                
                # k-fold cross-validation işlemi
                scores = cross_val_score(knn, X, y, cv=fold)
                
                # Confusion Matrix
                y_pred = cross_val_predict(knn, X, y, cv=fold)
                conf_matrix = confusion_matrix(y, y_pred)
                
                # Confusion Matrix
                y_pred = cross_val_predict(knn, X, y, cv=fold)
                
                # Performans metrikleri hesaplaması
                accuracy = accuracy_score(y, y_pred)
                precision = precision_score(y, y_pred, average='weighted')
                recall = recall_score(y, y_pred, average='weighted')
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
                # En yüksek değerleri bulma
                if accuracy > en_iyi_deger['accuracy']:
                    en_iyi_deger['accuracy'] = accuracy
                
                if precision > en_iyi_deger['precision']:
                    en_iyi_deger['precision'] = precision

                if recall > en_iyi_deger['recall']:
                    en_iyi_deger['recall'] = recall

                if f1 > en_iyi_deger['f1']:
                    en_iyi_deger['f1'] = f1

print("En Yüksek Accuracy Değeri:", en_iyi_deger['accuracy'])
print("=================================")
print("En Yüksek Precision Değeri:", en_iyi_deger['precision'])
print("=================================")
print("En Yüksek Recall Değeri:", en_iyi_deger['recall'])
print("=================================")
print("En Yüksek F1 Score Değeri:", en_iyi_deger['f1'])
print("=================================")
