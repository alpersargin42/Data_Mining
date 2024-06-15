import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

kolon_isimleri = ['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
diabet = pd.read_csv("diabets.csv",names=kolon_isimleri)
#print(diabet.head())

feature_col = ['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age']
X=diabet[feature_col]
y=diabet.label      
#print(X) # Giriş
#print(y) # Hedef

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
# model = DecisionTreeClassifier()
# model = model.fit(X_train,y_train)
# y_pred = model.predict(X_test)
# print(metrics.accuracy_score(y_test,y_pred))

# model = DecisionTreeClassifier(criterion="entropy",max_depth=3)
# model = model.fit(X_train,y_train)
# y_pred = model.predict(X_test)
# print(metrics.accuracy_score(y_test,y_pred))

model = DecisionTreeClassifier(criterion="entropy")
model = model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print(metrics.accuracy_score(y_test,y_pred))