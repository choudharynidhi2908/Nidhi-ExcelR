import pandas as pd 
import numpy as np 
import matplotlib.pyplot as py
import statsmodels.formula.api as smf
import warnings
warnings.filterwarnings("ignore")

delv = pd.read_csv('C:/Users/nidhchoudhary/Desktop/Assignment/SIMPLE_LINEAR_Regression/delivery_time.csv')

print(delv.head())

delv1 = delv.rename(columns= {'Delivery Time': 'Delivery_Time','Sorting Time':'Sorting_Time'})

print(delv1.head())
print(delv1.shape)

py.plot(delv1.Sorting_Time,delv1.Delivery_Time,"bo")
py.title('Simple Plotting')
py.xlabel ("Sorting_Time")
py.ylabel ("Delivery_Time")
#py.show()

correlation = delv1.Delivery_Time.corr(delv1.Sorting_Time)
#print(correlation)
coef = np.corrcoef(delv1.Delivery_Time,delv1.Sorting_Time)
#print(coef)
delv1.model = smf.ols("Delivery_Time~Sorting_Time",data = delv1).fit()
print('1st Model')
#print(delv1.model.summary())###R2 0.682

pred = delv1.model.predict(delv1.iloc[:,1])

#print(pred)


py.scatter(x = delv1['Sorting_Time'],y = delv1['Delivery_Time'],color = 'black')
py.plot(delv1['Sorting_Time'],pred,color = 'red')
py.title('Best Fit Model')
py.xlabel ("Sorting_Time")
py.ylabel ("Delivery_Time")
#py.show()

###Transforming variables for Accuracy
second_model = smf.ols("Delivery_Time~np.log(Sorting_Time)",data = delv1).fit()
# print('2nd Model')
#print(second_model.summary())##0.695


pred2 = second_model.predict(delv1.Sorting_Time)

# print(pred2)

py.scatter(x= delv1['Sorting_Time'],y = delv1['Delivery_Time'],color = 'black')
py.plot(delv1['Sorting_Time'],pred2,color = 'red')
py.title('X Log Best Fit Model')
py.xlabel ("Sorting_Time")
py.ylabel ("Delivery_Time")

# py.show()

# # input()
# ###Exponential Transformation Model
third_model = smf.ols("np.log(Delivery_Time)~Sorting_Time",data = delv1).fit()
print('3rd Model')
print(third_model.summary())###0.711
pred3 = third_model.predict(delv1.Sorting_Time)
pred3_actual= np.exp(pred3)
py.scatter(x=delv1['Sorting_Time'],y = delv1['Delivery_Time'],color = 'black')
py.plot(delv1,pred3_actual,color= 'red')
py.title('Y Log Best Fit Model')
py.xlabel ("Sorting_Time")
py.ylabel ("Delivery_Time")
# #py.show()




# # #Quadratic Model

delv1['sorting_Sq'] = delv1.Sorting_Time*delv1.Sorting_Time
Quard_Model = smf.ols("Delivery_Time~sorting_Sq+Sorting_Time",data = delv1).fit()
print(Quard_Model.summary())##0.693
predict4 = Quard_Model.predict(delv1)
py.scatter(x=delv1['Sorting_Time'],y = delv1['Delivery_Time'],color = 'black' )
py.plot(delv1,predict4,color = 'red')
py.title('Quadratic Model')
py.xlabel('Sorting')
py.ylabel('Delivery Time')
py.show()

# ####Third Model Has highest R2 value so Exponential Transform Model is the best model###
