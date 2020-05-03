import pandas as pd 
import numpy as np 
import seaborn as sb 
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('C:/Users/nidhchoudhary/Desktop/Assignment/LOGISTIC_REGRESSION/creditcard.csv')


Moddata= dataset.drop(["ID"],inplace= False,axis =1)


print(Moddata.head())

Classif = LogisticRegression()

print('Started')
x= Moddata.iloc[:,[1,2,3,4,5,6,7,8,9,10,11]]
y= Moddata.iloc[:,0]
Classif.fit(x,y)
#y_prob = pd.Moddata(Classif.predict_proba(x.iloc[:,:]))

#Classif.fit(x,y)
# input()

# #print(y)


y_pred = Classif.predict(x)




