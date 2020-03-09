#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 00:32:06 2020

@author: kemistree4
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from matplotlib import pyplot as plt
from sklearn import metrics
import numpy as np

df = pd.read_csv('https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt', sep='\t')

column_names = list(pd.read_csv('https://www4.stat.ncsu.edu/~boos/var.select/diabetes.rwrite1.txt', sep=' ').columns)
df.columns = column_names

X = df[['age','sex','bmi','map','tc','ldl','hdl','tch','ltg','glu']]
y = df['y']

#Assigning train and test variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

#Use Standard Scalar to normalize data
scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = MLPRegressor(hidden_layer_sizes = (5,2), solver ='adam', max_iter = 500000).fit(X_train, y_train)

y_test_pred = model.predict(X_test)
y_train_pred = model.predict(X_train)

#print(model.intercepts_)
#print(model.coefs_)

print("\n")
print("MLP Test Set")
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_test_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_test_pred)))

print("\n")
print("MLP Train Set") 
print('Mean Squared Error:', metrics.mean_squared_error(y_train, y_train_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_train, y_train_pred)))