#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:32:48 2020

@author: kemistree4
"""

"""Predict the severity of diabetes for a set of patients
-"Severity" will be one of columns (target variable)
-Regression (Linear and then Ridge/Lasso/SGD)"""

import pandas as pd  
import numpy as np   
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
from sklearn.linear_model import SGDRegressor

df = pd.read_csv('https://www4.stat.ncsu.edu/~boos/var.select/diabetes.rwrite1.txt', sep=' ')

#Assigning dependent and independent variable
X = df[['age','sex','bmi','map','tc','ldl','hdl','tch','ltg','glu']]
y = df['y']

###Linear Regression###
#Assigning train and test variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_) #Prints the y-intercept of the regression line
print(regressor.coef_) #Prints the slope of the regression line

y_test_pred = regressor.predict(X_test)
y_train_pred = regressor.predict(X_train)

###Ridge Regression###
rr = RidgeCV()

rr.fit(X_train, y_train) 

pred_train_rr= rr.predict(X_train)

pred_test_rr= rr.predict(X_test)

###Lasso###
model_lasso = LassoCV(max_iter = 10000)

model_lasso.fit(X_train, y_train) 

pred_train_lasso= model_lasso.predict(X_train)

pred_test_lasso= model_lasso.predict(X_test)

###SGD###
model_SGD = SGDRegressor(max_iter=10000)

model_SGD.fit(X_train, y_train)

pred_train_SGD = model_SGD.predict(X_train)

pred_test_SGD = model_SGD.predict(X_test)

print("Linear Regression Test Set")
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_test_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_test_pred)))
print("Linear Regression Train Set") 
print('Mean Squared Error:', metrics.mean_squared_error(y_train, y_train_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_train, y_train_pred)))
print('Ridge Training Set')
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_train,pred_train_rr)))
print('Mean Absolute Error:', metrics.mean_absolute_error(y_train, pred_train_rr))
print('Ridge Test Set')
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,pred_test_rr))) 
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, pred_test_rr))
print("Lasso Training Set")
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_train,pred_train_lasso)))
print('Mean Absolute Error:', metrics.mean_absolute_error(y_train, pred_train_lasso))
print('Lasso Test Set')
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,pred_test_lasso))) 
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, pred_test_lasso))
print('SGD Training Set')
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_train,pred_train_SGD))) 
print('Mean Absolute Error:', metrics.mean_absolute_error(y_train, pred_train_SGD))
print('SGD Linear Regression Test Set')
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,pred_test_SGD))) 
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, pred_test_SGD))