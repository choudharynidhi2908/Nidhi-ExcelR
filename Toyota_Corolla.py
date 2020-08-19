# Multilinear Regression
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt



# loading the data
Toyotta = pd.read_csv("C:\\Users\\nidhchoudhary\\Desktop\\Assignment\\MULTI_LINEAR_REGRESSION\\ToyotaCorolla.csv",encoding='ANSI')
##Creeating Data Set
Toyotta_Cars = Toyotta[["Price","Age_08_04","KM","HP","cc","Doors","Gears","Quarterly_Tax","Weight"]]


##Correlation values


#print(Toyotta_Cars.corr())
import seaborn as sns
sns.pairplot(Toyotta_Cars)

#plt.show()

import statsmodels.formula.api as smf 

model1 = smf.ols('Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data= Toyotta_Cars).fit()
print(model1.params)

#print(model1.summary())
##Calculate RMSE Value

predicted_value = model1.predict(Toyotta_Cars)
Error = Toyotta_Cars.Price - predicted_value ###1338.25
#print((np.sqrt(np.mean(Error*Error)),'Rmse Values'))

import statsmodels.api as sm
sm.graphics.influence_plot(model1)
#plt.show()

##From Influence Plot we saw 80 has highest radius so dropping index 80 row

Toyotta_Cars_new  = Toyotta_Cars.drop(Toyotta_Cars.index[80],axis=0)

model2 = smf.ols('Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data= Toyotta_Cars_new).fit()
print(model2.summary())

#since p value is 0 so final model

final_predict = model2.predict(Toyotta_Cars_new)

print(final_predict)




###since P value for CC and Doors are high 
# ###predicting values with CC only

# model_cc = smf.ols('Price~cc',data= Toyotta_Cars).fit()
# print(model_cc.summary()) ### Pvalue is 0

# model_doors = smf.ols('Price~Doors',data= Toyotta_Cars).fit()
# print(model_doors.summary()) ###Pvalue is 0

# model_combine = smf.ols('Price~cc+Doors',data= Toyotta_Cars).fit()
# print(model_combine.summary())

# import statsmodels.api as sm
# sm.graphics.influence_plot(model1)
# plt.show()