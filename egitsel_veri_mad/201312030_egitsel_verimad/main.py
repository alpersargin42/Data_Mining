'''
201312030-Alper Sargın- 26_12_2023 Ödev

Eğitsel veri madenciliği (educational data mining), öğrencilerin öğrenme süreçleriyle ilgili verileri analiz ederek öğrenme süreçlerini anlama, öğrenme başarısını artırma ve öğretim yöntemlerini iyileştirme amacıyla kullanılan bir alanı ifade eder. Bu alanda çeşitli veri madenciliği teknikleri ve yöntemleri kullanılarak öğrenci performansı, öğrenme alışkanlıkları, etkileşimler ve diğer öğrenci verileri üzerinde analizler yapılır.Eğitsel veri madenciliği genellikle öğrenci başarısını etkileyen faktörleri belirlemek, öğrenci performansını tahmin etmek, öğrenci segmentasyonu yapmak gibi konuları kapsar.
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report

tennis = pd.read_csv('tennis.csv')
print(tennis)

X = tennis[['outlook', 'temp', 'humidity', 'windy']]
y = tennis['play']
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Model Doğruluğu:', accuracy)

conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

class_report = classification_report(y_test, y_pred)
print("\nClassification Report:")
print(class_report)

labels = ['Oynama', 'Oynamayamaz']
sizes = [sum(y_pred == 'yes'), sum(y_pred == 'no')]
colors = ['gold', 'lightskyblue']
explode = (0.1, 0)  
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Hava durumu koşullarına göre Tenis Oynama Tahmini')
plt.show()


test_data = pd.DataFrame({
    'outlook': ['sunny'],
    'temp': ['hot'],
    'humidity': ['high'],
    'windy': ['true']
})

test_data = pd.get_dummies(test_data)
egitim_sutunlar = X.columns
test_data = test_data.reindex(columns=egitim_sutunlar, fill_value=0)
predicted_result = model.predict(test_data)
print('Hava durumu koşullarına göre tenis oynama tahmini:', predicted_result[0])
