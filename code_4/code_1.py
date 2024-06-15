from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd
import seaborn as sns 
from sklearn import metrics
import matplotlib.pyplot as plt

kanser = load_breast_cancer()
x=kanser.data
y=kanser.target
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print(f"Eğitim verisi {X_train.shape} , {y_train.shape}")
print(f"Eğitim verisi {X_test.shape} , {y_test.shape}")
classifier = RandomForestClassifier()
classifier.fit(X_train,y_train)
predictions = classifier.predict(X_test)
print(predictions)
print(accuracy_score(y_test,predictions))
cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix : \n", cm)
d=pd.crosstab(y_test,predictions,rownames=["true"],colnames=["predicted"],margins=True)
print(d)
cnf_matrix = metrics.confusion_matrix(y_test,predictions)
p = sns.heatmap(pd.DataFrame(cnf_matrix),cmap="YlGnBu",annot=True)
plt.title('CNF MATRİX')
plt.ylabel("Gerçek Değerler")
plt.xlabel("Tahmin Değerleri")
plt.show()
