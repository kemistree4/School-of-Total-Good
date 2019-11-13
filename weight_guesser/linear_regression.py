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

#Use only one feature
wg_x = wg[:, np.newaxis, 2]

#Split the data into training/testing sets
wg_X_train = wg_X[:-20]
wg_X_test = wg_X[-20:]

#Split the targets into training/testing sets
wg_y_train: wg_target[:-20]
wg_y_train: wg.target[-20:]
# Create linear regression object
regr = linear_model.LinearRegression()

#Train the model using the training sets
regr.fit(wg_X_train, wg_y_train)

#Make predictions using the testing set
wg_y_pred = regr.predict(wg_X_test)
