'''
201312030-Alper Sargın - 26_12_2023 Ödev
'''
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules


df = pd.read_csv("datasets_344_727_GroceryStoreDataSet.csv", names=['products'], header = None)

print(df.head())
print(df.shape)
print(df.columns)
print(df.values)

data = list(df["products"].apply(lambda x:x.split(',')))
print(data)

te = TransactionEncoder()
te_data = te.fit(data).transform(data)
df = pd.DataFrame(te_data, columns = te.columns_)
print(df)

df1 = apriori(df, min_support=0.02, use_colnames = True, verbose=1)
print(df1)

association_rules(df1, metric = "confidence", min_threshold = 0.6)

rules = association_rules(df1, metric = "confidence", min_threshold = 0.6)
filtered_rules1 = rules[ (rules['confidence'] >= 0.6) & (rules['support'] >= 0.2) ]
print(filtered_rules1)


# Supportu 0.01 şeklinde tekrar belirledim.
df2 = apriori(df, min_support=0.01, use_colnames=True, verbose=1)
print(df2)

# Confidence değerininin min_thresholdunu 0.7 olacak şekilde tekrar belirledim.
rules2 = association_rules(df2, metric="confidence", min_threshold=0.7)
print(rules2)

filtered_rules2 = rules2[(rules2['confidence'] >= 0.7) & (rules2['support'] >= 0.1)]
print(filtered_rules2)