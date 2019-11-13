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

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression 


#Loading in dataset from website
wg = pd.read_html("https://totalgood.org/midata/teaching/rikeem-u/heights_weights_genders.html")

#Slicing relevant rows
wg = wg[0]#This helped with slicing but not sure why. without this couldnt use .iloc because "list" object has no attrinute 'iloc'
wg_final = wg.iloc[:,1:]

X = wg.iloc[:,2].values.reshape(-1,1) #why reshape?
Y = wg.iloc[:,3].values.reshape(-1,1)

#Create object for the class
linear_regressor = LinearRegression()

#Perform linear regression
linear_regressor.fit(X,Y)
Y_pred = linear_regressor.predict(X)

#Assigns plot seperated by gender color with yellow linear regression line to variable
g =sns.lmplot(x='Height', y='Weight', hue='Gender', data=wg_final, palette =['blue','red'], line_kws={'color':'yellow'})

#Playing around with scale and shape of graph
sns.set() 
g.set(yscale ="log",xscale ="log", ylim=(0,400), xlim =(0,80)) 

print(g)
print(linear_regressor.coef_)
print(linear_regressor.intercept_)