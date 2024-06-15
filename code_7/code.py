from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

data = pd.read_csv("exam_score.csv", header=None)
print(data.shape)
print(data.head)

X = data.iloc[:, [0, 1]].values
y = data.iloc[:, 2].values

kfold = KFold(n_splits=5, shuffle=True, random_state=42)

model = RandomForestClassifier(n_estimators=10)

scores = cross_val_score(model, X, y, cv=kfold)

for i, score in enumerate(scores, 1):
    print(f"Fold {i}: {score}")

print(f"Ortalama Doğruluk: {scores.mean()}")

print("===================================")

kfold2 = KFold(n_splits=5, shuffle=False)

model2 = RandomForestClassifier(n_estimators=10)

scores2 = cross_val_score(model2, X, y, cv=kfold2)

for i, score2 in enumerate(scores2, 1):
    print(f"Fold {i}: {score2}")

print(f"Ortalama Doğruluk: {scores2.mean()}")
