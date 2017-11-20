from sklearn import linear_model
from scipy.stats.stats import pearsonr

import pandas as pd
import numpy as np

dir='/Users/juliogonzalez/Documents/IS Data Foundations/Homeworks/HW2/'
sales2 = pd.read_csv(dir+'Gonzalez_HW2_EC1.csv')

col_NaN_count=sales2.isnull().sum() # prints missing values by variables
print("Missing Values by Column",col_NaN_count)

sales2['Item_Weight']=sales2['Item_Weight'].fillna(sales2['Item_Weight'].median())

array = sales2.values
X = array[:,1:11]
Y = array[:,12]

# feature selection using Lasso
for i in range(0,20,5):
    test = linear_model.Lasso(alpha=i, fit_intercept=True)
    test.fit(X=X,y=Y)
    print("alpha:",i)
    print(test.coef_)

names = sales2.columns

#feature selection using pearson r correlation
for i in range(1,11):
    xi = array[:,i]
    print("Feature name:", names[i]," Column # in Lasso:",i)
    print(pearsonr(xi,y=Y))
