import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from matplotlib import pyplot as plt
#pd.set_option('display.max_rows', 500)


dir='/Users/juliogonzalez/Documents/IS Data Foundations/Homeworks/HW2/'
pima=pd.read_csv(dir+'pima-indians-diabetes.data.csv')
sales = pd.read_csv(dir+'HW2_2013Sales_AllQuant.csv')

#1
# a.
print(pima.shape)

names = pima.columns.values
pima["Diabetes"].value_counts()
sm = SMOTE(random_state=42)
X_smote, Y_smote=sm.fit_sample(pima, pima["Diabetes"])

one_a = pd.DataFrame(X_smote)
one_a.columns = names
one_a.to_csv("Gonzalez_HW2_pima_balanced-SMOTE.csv")
print(one_a["Diabetes"].value_counts())
print(one_a.shape)

# b. Randomly pick 268 observations w/o Diabetes to equal the 268 observations w/Diabetes
df_0 = pima[pima.Diabetes == 0].sample(n=268)     # randomly selects 268 observations with 0 in Diabetes column.
df_1 = pima[pima.Diabetes == 1]     # selects all observations with 1 in Diabetes column
t = [df_0,df_1]
one_b = pd.concat(t)    # combines both dataframes
print(one_b.shape)
print(one_b["Diabetes"].value_counts())
one_b.to_csv("Gonzalez_HW2_pima_balanced-RUS.csv")

#2
# a.
print(sales.shape)

# b.
print(sales.describe())

# do f. first before moving on to c

# c.
col_NaN_count=sales.isnull().sum() # prints missing values by variables
print("Missing Values by Column",col_NaN_count)
col_NaN_count=sales.isnull().sum().sum() # prints total missing values
print("Total number of missing values:",col_NaN_count)

# d.
plt.figure();sales.Item_Weight.hist(color='k',alpha=0.5)
plt.figure();sales.Outlet_Size_Code.hist(color='k',alpha=0.5)

# Item_Weight (missing obs = 1479, ~17% of total data)
print(sales['Item_Weight'].value_counts())
# given that the Item Weight of 13650 is very large when compared to the other values
# plus the fact that there is a high frequency of them, the median would the best estimate
# because these values will pull the average to be artifically high. In addition, about 1%
# 77/7064 of the current values are of the value 13650 meaning that without knowing anything else,
# there's a 99% chance the missing values are not 13650.
sales['Item_Weight']=sales['Item_Weight'].fillna(sales['Item_Weight'].median())
print(sales['Item_Weight'].value_counts())

# Outlet_Size_Code (missing values = 2414, ~28% of total column data)
print(sales['Outlet_Size_Code'].value_counts())
print(sales['Outlet_Size_Code'].mode())
# Given that Outlet_Size_Code is a categorical variable, the mean would provide
# uninterpretable values. The mode would be better suited for this situation because given the current data
# and without knowing anything else about the observations, if one is to randomly pick a value from this
# column, the highest probability would be the mode. In addition, the mode and the median
# are the same values providing more evidence for the the use of Size Code of 2.0 as the replacement
# for the missing values
sales['Outlet_Size_Code']=sales['Outlet_Size_Code'].fillna(sales['Outlet_Size_Code'].median())
print(sales['Outlet_Size_Code'].value_counts())

# e.

# 1) Item_Weight as a large max number.

outliers = sales[sales.Item_Weight == 13650]
print(outliers)

dummy = sales[sales["Item_Identifier_Code"].isin([923,966,1219,471,425,754,918,697,
                                          161,1074,1544,815,418,326,980])]
print(dummy['Item_Weight'].value_counts())


sales.loc[sales.Item_Identifier_Code == 923,"Item_Weight"]=13.650
sales.loc[sales.Item_Identifier_Code == 966,"Item_Weight"]=13.650
sales.loc[sales.Item_Identifier_Code == 471,"Item_Weight"]=13.650
sales.loc[sales.Item_Identifier_Code == 425,"Item_Weight"]=13.650
sales.loc[sales.Item_Identifier_Code == 697,"Item_Weight"]=13.650
sales.loc[sales.Item_Identifier_Code == 1544,"Item_Weight"]=13.650
sales.loc[sales.Item_Identifier_Code == 815,"Item_Weight"]=13.650
sales.loc[sales.Item_Identifier_Code == 418,"Item_Weight"]=13.650
sales.loc[sales.Item_Weight == 13650,"Item_Weight"]=13.650

# f.
row_NaN_count = pd.DataFrame(sales.isnull().sum(axis=1))
row_NaN_count["counts"]=pd.DataFrame(sales.isnull().sum(axis=1))
df_j = row_NaN_count[row_NaN_count.counts > 1]
print(df_j)

sales = sales.drop([4498,4499,4500,4501,4502,4503,4504,4505,4506,4507,4508,4509,4510,4511,4512,4513,4514,4515,4516,4517])

# g.
print(sales.skew()) # skewness less than -1 or greater than 1, distribution is highly skewed
print(sales.kurt())
plt.figure();sales.Item_Visibility.hist(color='k',alpha=0.5)
plt.figure();sales.Item_Outlet_Sales.hist(color='k',alpha=0.5)
# We can see a positive skew for both Item_Visibility and Item_Outlet_Sales so we standardize these variables to minimize
# the presence of bias.
sales.Item_Visibility = (sales.Item_Visibility-sales.Item_Visibility.mean())/sales.Item_Visibility.std()
sales.Item_Outlet_Sales= (sales.Item_Outlet_Sales-sales.Item_Outlet_Sales.mean())/sales.Item_Outlet_Sales.std()
print(sales.Item_Visibility)
print(sales.Item_Outlet_Sales)

sales.to_csv("Gonzalez_HW2_sales_cleaned.csv")