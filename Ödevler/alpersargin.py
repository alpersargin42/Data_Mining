'''
201312030 Alper SARGIN
12 ARALIK 2023 ÖDEVİ
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_curve, auc
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

veri = pd.read_csv('exam_score.csv')


X = veri.iloc[:, [0, 1]].values
y = veri.iloc[:, 2].values

# Veriyi ölçeklendirme
olcekleyici = StandardScaler()
X_olcekli = olcekleyici.fit_transform(X)

k_fold_degerleri = list(range(2, 6))
komsu_sayilari = list(range(1, 11))
kernel_secenekleri = ['linear', 'poly', 'rbf', 'sigmoid']
roc_auc_sonuclari = []

for komsu_sayisi in komsu_sayilari:
    knn = KNeighborsClassifier(n_neighbors=komsu_sayisi)
    y_scores_knn = cross_val_predict(knn, X, y, cv=5, method="predict_proba")[:, 1]#predict_progba [:,1] -> olumlu sınıfın olasılıklarını döndürür.
    fpr_knn, tpr_knn, thresholds_knn = roc_curve(y, y_scores_knn)
    roc_auc_knn = auc(fpr_knn, tpr_knn)
    
    
    y_scores_knn_olcekli = cross_val_predict(knn, X_olcekli, y, cv=5, method="predict_proba")[:, 1]
    fpr_knn_olcekli, tpr_knn_olcekli, thresholds_knn_olcekli = roc_curve(y, y_scores_knn_olcekli)
    roc_auc_knn_olcekli = auc(fpr_knn_olcekli, tpr_knn_olcekli)
    
    roc_auc_sonuclari.append({
        'Model': 'KNN',
        'Komşu Sayısı': komsu_sayisi,
        'ROC AUC (Orijinal Veri)': roc_auc_knn,
        'ROC AUC (Ölçeklendirilmiş Veri)': roc_auc_knn_olcekli
    })

# SVM modeli için ROC ve AUC hesaplama(sadece ölçeklendirilmiş veri)
for kernel in kernel_secenekleri:
    svm = SVC(kernel=kernel, probability=True)
    
    y_scores_svm_olcekli = cross_val_predict(svm, X_olcekli, y, cv=5, method="predict_proba")[:, 1]#predict_progba [:,1] -> olumlu sınıfın olasılıklarını döndürür.
    fpr_svm_olcekli, tpr_svm_olcekli, thresholds_svm_olcekli = roc_curve(y, y_scores_svm_olcekli)
    roc_auc_svm_olcekli = auc(fpr_svm_olcekli, tpr_svm_olcekli)
    
    roc_auc_sonuclari.append({
        'Model': 'SVM',
        'Kernel': kernel,
        'ROC AUC (Ölçeklendirilmiş Veri)': roc_auc_svm_olcekli
    })

roc_auc_df = pd.DataFrame(roc_auc_sonuclari)
print(roc_auc_df)

# ROC çizdirme
plt.figure(figsize=(10, 6))

for model in roc_auc_df['Model'].unique():
    model_df = roc_auc_df[roc_auc_df['Model'] == model]
    for i, row in model_df.iterrows():
        if model == 'KNN':
            plt.plot(fpr_knn_olcekli, tpr_knn_olcekli, label=f'{model} (K={row["Komşu Sayısı"]}) - AUC={row["ROC AUC (Ölçeklendirilmiş Veri)"]:.2f}')
        elif model == 'SVM':
            plt.plot(fpr_svm_olcekli, tpr_svm_olcekli, label=f'{model} ({row["Kernel"]}) - AUC={row["ROC AUC (Ölçeklendirilmiş Veri)"]:.2f}')

plt.plot(label='Rastgele Tahmin')
plt.xlabel('False Positive')
plt.ylabel('True Positive')
plt.title('ROC Eğrisi')
plt.show()
