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

df = pd.read_csv('https://www4.stat.ncsu.edu/~boos/var.select/diabetes.rwrite1.txt', sep=' ')

#Assigning dependent and independent variable
X = df[['age','sex','bmi','map','tc','ldl','hdl','tch','ltg','glu']]
y = df['y']

#Assigning train and test variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Use Standard Scalar to normalize data
scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)