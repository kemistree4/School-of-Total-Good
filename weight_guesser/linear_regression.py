# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:03:36 2019

@author: Rikeem


--Difference between a classifier and a regression
--Find other regression models (based on linear regression)
--Install scikit-learn
--import sklearn
--learn about (reg.coef_) attribute in Linear Regression
--also for (reg.intercept_)
--investigate sklearn.linear_model.LinearRegression()
--use git to push to github
--git config --global user.email
--ssh-keygen
--cat ~/.ssh/id_rsa.pub
--debounce logic/ hysteresis loop python
"""

from sklearn import datasets, linear_model
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import html5lib
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score

#Loading in dataset from website
wg = pd.read_html("https://totalgood.org/midata/teaching/rikeem-u/heights_weights_genders.html")

#Slicing relevant rows
wg = wg[0]#This helped with slicing but not sure why. without this couldnt use .iloc because "list" object has no attrinute 'iloc'
wg_final = wg.iloc[:,1:]
print(wg_final)

X = wg.iloc[:,2].values.reshape(-1,1) #why reshape
Y = wg.iloc[:,3].values.reshape(-1,1)

#Create object for the class
linear_regressor = LinearRegression()

#Perform linear regression
linear_regressor.fit(X,Y)

Y_pred = linear_regressor.predict(X)
g =sns.lmplot(x='Height', y='Weight', hue='Gender', data=wg_final, palette =['blue','red'], line_kws={'color':'yellow'})
print(g)