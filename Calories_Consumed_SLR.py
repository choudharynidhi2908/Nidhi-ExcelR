import pandas as pd 
import matplotlib.pyplot as py
import numpy as np 
import statsmodels.formula.api as smf
import math
import warnings
warnings.filterwarnings("ignore")


cal = pd.read_csv('C:/Users/nidhchoudhary/Desktop/Assignment/SIMPLE_LINEAR_Regression/calories_consumed.csv')

cal = cal.rename(columns={'Weight gained (grams)': 'Weight','Calories Consumed':'Calories'})
cal.columns

py.hist(cal.Calories)
py.boxplot(cal.Calories,0,"rs",0)
py.hist(cal.Weight)
py.boxplot(cal.Weight,0,"rs",0)


py.plot(cal.Calories,cal.Weight);
py.xlabel('Calories_Consumed');
py.ylabel('weight_Gained');
#py.show()

correlation = cal.Weight.corr(cal.Calories)
print(correlation)
coef = np.corrcoef(cal.Weight,cal.Calories)
print(coef)

model = smf.ols('Weight~Calories',data=cal).fit()
print(model.params)##############need to find
print(model.summary())

print(model.conf_int())

pred1 = model.predict(cal.iloc[:,1])###Predict Values of Weight Gained Using the model
print(pred1)

# import matplotlib.pylab as plt
# plt.scatter(x=cal['Calories'],y= cal['Weight'],color= 'red');plt.plot(cal['Calories'],pred1,color ='black')
# py.plot(cal.Calories,pred1,color = 'black')
# plt.xlabel('calories_consumed')
# plt.ylabel('Weight Gained')
# plt.title('2nd Model')
# #plt.show()

# #Transforming values for accuracy model
# model2 = smf.ols('Weight~np.log(Calories)',data= cal).fit()
# print(model2.params)
# print(model2.summary())
# pred2 = model2.predict(cal.Calories)

# plt.scatter(x=cal['Calories'],y= cal['Weight'],color= 'red')
# plt.plot(cal['Calories'],pred2,color ='orange')
# #plt.show()

# ##Exponential Model

# model3 = smf.ols('np.log(Weight)~Calories',data = cal).fit()
# print(model3.params)
# print(model3.summary())
# print(model2.conf_int(0.01))
# pred3_log = model3.predict(cal.Calories)
# pred3 = np.exp(pred3_log)
# plt.scatter(x=cal['Calories'],y=cal['Weight'],color= 'purple')
# plt.plot(cal['Calories'],pred3,color = 'pink')
# plt.xlabel('calories_consumed')
# plt.ylabel('Weight Gained')
# plt.title('3rd Model')
# plt.show()

# ##Quadratic Model
cal['Calories_sq'] = cal.Calories*cal.Calories
cal['Calories_final'] = cal.Calories+cal.Calories_sq

model4 = smf.ols('Weight~Calories_final',data = cal).fit()
print(model4.params)

print('Model For Summary')
print(model4.summary())
print(model4.conf_int(0.01))
pred4 = model4.predict(cal.Calories)

pred4 = model4.predict(cal.Calories)


pred4 = model4.predict(cal.Calories)

#pred_quad = model_quad.predict(wcat.Waist)

print('Error2..........................................................................................')
plt.scatter(x=cal['Calories'],y=cal['Weight'],color= 'purple')
plt.plot(cal['Calories'],pred4,color = 'green')
plt.xlabel('calories_consumed')
plt.ylabel('Weight Gained')
plt.title('4th Model')
plt.show()


# ###Since Model 1n has highest R2 value so that's  a best fit model need to fit the residual data

# resid = 