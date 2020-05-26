import pandas as pd 
import numpy as np
import matplotlib.pyplot as py
import statsmodels.formula.api as smf

cal = pd.read_csv('C:/Users/nidhchoudhary/Desktop/Assignment/SIMPLE_LINEAR_Regression/calories_consumed.csv')

cal = cal.rename(columns={'Weight gained (grams)': 'Weight','Calories Consumed':'Calories'})

print(cal.head())
print(cal.shape)
print('Start Prepring Scatter Plot..')
py.plot(cal.Calories,cal.Weight,"bo");
py.ylabel = ("Weight Gained")
py.xlabel = ("Calories Consumed")
py.show()

print('Training For SLR Started..')

first_model =smf.ols("Weight~Calories",data=cal).fit()

print(first_model.summary())

#cal = cal.rename(columns={'Weight gained (grams)': 'Weight','Calories Consumed':'Calories'})


first_model.predict(cal.iloc[:,0])
print(pred)