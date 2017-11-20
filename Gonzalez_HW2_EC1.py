import pandas as pd
import numpy as np

dir='/Users/juliogonzalez/Documents/IS Data Foundations/Homeworks/HW2/'
sales2 = pd.read_csv(dir+'HW2_2013Sales_MixedTypes.csv')




# Item_Identifier
sales2['Item_Identifier'].value_counts()

names_II = sales2.Item_Identifier.unique()

count = 0
for i in names_II:
    sales2.loc[sales2.Item_Identifier== i, "Item_Identifier"] = count
    count +=1

########for codebook
count = 0
for i in names_II:
    print(i,"=",count)
    count +=1





# Item_Fat_Content
sales2['Item_Fat_Content'].value_counts()

sales2.loc[sales2.Item_Fat_Content == "Low Fat","Item_Fat_Content"]= 0
sales2.loc[sales2.Item_Fat_Content == "low fat","Item_Fat_Content"]= 0
sales2.loc[sales2.Item_Fat_Content == "LF","Item_Fat_Content"]= 0

sales2.loc[sales2.Item_Fat_Content == "Regular","Item_Fat_Content"]= 1
sales2.loc[sales2.Item_Fat_Content == "reg","Item_Fat_Content"]= 1





# Item_Type
sales2['Item_Type'].value_counts()

names_IT = sales2.Item_Type.unique()

count = 0
for i in names_IT:
    sales2.loc[sales2.Item_Type == i, "Item_Type"] = count
    count +=1

########for codebook
count = 0
for i in names_IT:
    print(i,"=",count)
    count +=1









# Outlet_Identifier
sales2['Outlet_Identifier'].value_counts()

names_OI = sales2.Outlet_Identifier.unique()
print(names_OI)

# sets the value to the last 3 numbers
for i in names_OI:
    sales2.loc[sales2.Outlet_Identifier == i, "Outlet_Identifier"] = int(i[3:])



# Outlet_Size
sales2['Outlet_Size'].value_counts()

names_OS = sales2.Outlet_Size.unique()

count = 0
for i in names_OS:
    sales2.loc[sales2.Outlet_Size == i, "Outlet_Size"] = count
    count +=1

########for codebook
count = 0
for i in names_OS:
    print(i,"=",count)
    count +=1

sales2['Outlet_Size']=sales2['Outlet_Size'].fillna(1)




# Outlet_Location_Type
sales2['Outlet_Location_Type'].value_counts()

names_OLT = sales2.Outlet_Location_Type.unique()

for i in names_OLT:
    sales2.loc[sales2.Outlet_Location_Type== i, "Outlet_Location_Type"] = int(i[5])





# Outlet_Type
sales2['Outlet_Type'].value_counts()

names_OT = sales2.Outlet_Type.unique()
names_OT2 = np.delete(names_OT, 2)

for i in names_OT2:
    sales2.loc[sales2.Outlet_Type== i, "Outlet_Type"] = int(i[16])

sales2.loc[sales2.Outlet_Type == "Grocery Store","Outlet_Type"]= 0



print(sales2.describe())
print(sales2.shape)

sales2.to_csv("Gonzalez_HW2_EC1.csv")

