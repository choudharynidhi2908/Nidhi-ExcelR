import pandas as pd 
import numpy as np 
import matplotlib.pyplot as pyplot
from sklearn.linear_model import LogisticRegression as LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
#from sklearn.metrics import classification_report
election = pd.read_csv('C:/Users/nidhchoudhary/Desktop/Assignment/LOGISTIC_REGRESSION/election_data.csv')

print(election.head())

election_new = election.drop(['Election-id'],axis=1)

print(election_new.head())

x = election_new.iloc[:,[1,2,3]]
y = election_new.iloc[:,0]

classifier = LogisticRegression()

y_model = (classifier.fit(x,y))

y_pred = classifier.predict(x)
election_new["Win"] = y_pred

print(y_pred)



y_prob = (classifier.predict_proba(x.iloc[:,:]))

from sklearn.metrics import confusion_matrix
confusion_matrix = metrics.confusion_matrix (y,y_pred)
print(confusion_matrix)

accuracy = sum(y==y_pred)/election_new.shape[0]
print(accuracy,"Accuracy Number")
########0.9 % accurate