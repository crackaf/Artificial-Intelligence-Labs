# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 03:02:18 2021

@author: Usman
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import pickle


df=pd.read_csv('USA_Housing.csv')
df.head()

### divide into labels and features ###
x=df.drop(['Price','Address'],axis=1)
y=df['Price']

### dividing data into training-testing splits

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=101)

### KNN Regressor ###
#Import the Model
knn=KNeighborsRegressor()
### Model Training
knn.fit(X_train,Y_train)

# Saving model to disk
pickle.dump(knn, open('model_pricing.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model_pricing.pkl','rb'))

print(model.predict([[20000, 5, 7,3,10000]]))




