# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 03:02:18 2021

@author: Usman
"""

import math
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
import pickle


df = pd.read_csv('train.csv')
df.head()

df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
df.head()

median_age = math.floor(df.Age.median())
df.Age = df.Age.fillna(median_age)
df.head()

df["Sex"].replace({"male": 0, "female": 1}, inplace=True)
df["Embarked"].replace({"S": 0, "C": 1, "Q": 2}, inplace=True)
median_embark = math.floor(df.Embarked.median())
df.Embarked = df.Embarked.fillna(median_embark)

### divide into labels and features ###
x = df.drop(['Survived'], axis=1)
y = df['Survived']
# dividing data into training-testing splits

X_train, X_test, Y_train, Y_test = train_test_split(
    x, y, test_size=0.3, random_state=101)

### KNN Regressor ###
# Import the Model
# knn=KNeighborsRegressor()
knn = KNeighborsClassifier(n_neighbors=8)
# Model Training
knn.fit(X_train, Y_train)

# Saving model to disk
pickle.dump(knn, open('model_pricing.pkl', 'wb'))

# Loading model to compare the results
model = pickle.load(open('model_pricing.pkl', 'rb'))

print(model.predict([[1, 0, 20, 0, 0, 100, 0]]))
