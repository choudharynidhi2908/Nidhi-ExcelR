import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#loading the data

startup = pd.read_csv('C:\\Users\\nidhchoudhary\\Desktop\\Assignment\\MULTI_LINEAR_REGRESSION\\50_startups.csv')

print(startup.head())

##File Contains non.numerical data so dropping the entire column of state


startup_new = startup.drop(['State'],axis=1)

print(startup_new.head())

##find correlation

print(startup_new.corr())

##correlation between R&D and marketing spend is 0.72 which is quite high
import statsmodels.formula.api as smf
model1 = smf.ols('Profit~Spend+Administration+Marketing_Spend',data= startup_new).fit()

#print(model1.summary())
##Correlation for  Marketing spend and Spend is high
##Also Pvalue for Administration and Marketing Se=pend is high.
##r2 is 0.951

import seaborn as sns
sns.pairplot(startup_new)
#plt.show()

##Check if there any data of which influencing the other data

import statsmodels.api as sm
sm.graphics.influence_plot(model1)
#plt.show()

##Observed that few of the records has r&D expense very low or nil but have some profit which is not an ideal scenario
##So dropping those records

model2_new = startup_new.drop(startup_new.index[[45,46,47,48,49]],axis=0)

##Check the P Values after dropping some records

model2_new_sls = smf.ols('Profit~Spend+Administration+Marketing_Spend',data= model2_new).fit()

#print(model2_new_sls.summary())


##Preparing Model between Profit and R&D spend

model_RD = smf.ols('Profit~Spend',data = model2_new ).fit()

print(model_RD.summary())

##P Value id <0.05 significant

##Preparing Model between profit Administration

model_Admin = smf.ols('Profit~Administration',data = model2_new ).fit()
#print(model_Admin.summary())

## P value is > 0.05  insignificant



model_mark_sped = smf.ols('Profit~Marketing_Spend',data = model2_new ).fit()

#print(model_mark_sped.summary())

##P Value id <0.05 significant


# calculating VIF's values of independent variables

r_spend = smf.ols('Spend~Administration+Marketing_Spend',data = model2_new).fit().rsquared
vif_spend = 1/(1-r_spend)
#print(vif_spend)###2.38

r_administartion = smf.ols('Administration~Spend+Marketing_Spend',data =model2_new).fit().rsquared
vif_administartion = 1/(1-r_administartion)
##print(vif_administartion)###1.23

r_Marketing_Spend = smf.ols('Marketing_Spend~Spend+Administration',data =model2_new).fit().rsquared
vif_Marketing_spend = 1/(1-r_Marketing_Spend)

print(vif_Marketing_spend)#####2.318


## SInce Vif for administraion is quite so wull ignore this column and will predict the final mdoel
final_model = smf.ols('Profit~Spend+Marketing_Spend',data= model2_new).fit()

print(model2_new_sls.summary())

final_predict = final_model.predict(model2_new)

print(final_predict)




