from matplotlib.pyplot import *                        
import pandas as pd      
from sklearn.metrics import confusion_matrix   
import seaborn as sns               


y_true = ["happy", "sad", "happy", "happy", "sad", "neutral", "happy", "sad", "happy", "happy", "sad", "neutral",
          "happy", "sad", "happy", "happy", "sad", "neutral", "happy", "sad", "happy", "happy", "sad", "neutral",
          "happy", "sad", "happy", "happy", "sad", "neutral", "happy", "sad", "happy", "happy", "sad", "neutral",
          "happy", "sad", "happy", "happy", "sad", "neutral", "happy", "sad", "happy", "happy", "sad", "neutral"]
y_pred = ["happy", "sad", "happy", "happy", "sad", "happy", "sad", "happy", "happy", "sad", "happy", "sad", "sad",
          "sad", "happy", "sad", "sad", "happy", "sad", "happy", "happy", "sad", "neutral", "neutral", "happy", "sad",
          "happy", "happy", "sad", "neutral", "happy", "sad", "happy", "happy", "sad", "neutral", "happy", "sad",
          "happy", "happy", "sad", "neutral", "happy", "sad", "happy", "happy", "sad", "neutral"]
labels = ["happy", "sad", "neutral"]
cm=confusion_matrix(y_true,y_pred,labels=labels)
print(cm)

cm_df=pd.DataFrame(cm,index=labels,columns=labels)
matplotlib.pyplot.figure(figsize=(8,6))
sns.heatmap(cm_df,annot=True,cmap='viridis')
matplotlib.pyplot.show()