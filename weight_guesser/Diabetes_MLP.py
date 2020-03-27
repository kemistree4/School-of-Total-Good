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
from sklearn import metrics
import numpy as np
from itertools import product
df = pd.read_csv('https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt', sep='\t')
file_name = "NN params.csv"
try:    
    hyper_table = pd.read_csv(file_name)
except FileNotFoundError:
    hyper_table = pd.DataFrame(columns=['Hidden Layers', 'Number of nodes', 'Solver', 'Alpha', 'Test Set RMSE', 'Train Set RMSE', 'Learning Rate', 'Early Stopping'])

column_names = list(pd.read_csv('https://www4.stat.ncsu.edu/~boos/var.select/diabetes.rwrite1.txt', sep=' ').columns)
df.columns = column_names

X = df[['age','sex','bmi','map','tc','ldl','hdl','tch','ltg','glu']]
y = df['y']

#Assigning train and test variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=0)

#Use Standard Scalar to normalize data
scaler = StandardScaler()
solvers =['lbfgs']
learning_rates = ['constant', 'invscaling']
early_stoppings = [True]
first_layers = [6,7]
second_layers = [2,3,4]
third_layers = [0]
alphas = [ 0.0015, 0.0017, 0.002, 0.0018]
warm_start = True
scaler.fit(X_train)
columns = hyper_table.columns
hyper_table = list(hyper_table.values)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
for neurons_1, neurons_2, neurons_3, alpha, solver,learning_rate, early_stopping in product(first_layers, second_layers, third_layers, alphas, solvers, learning_rates, early_stoppings):
    layer_neurons = [neurons_1, neurons_2, neurons_3]
    layer_neurons = [x for x in layer_neurons if x > 0]
    model = MLPRegressor(hidden_layer_sizes=layer_neurons, solver=solver, alpha=alpha, learning_rate=learning_rate, early_stopping = early_stopping, warm_start=warm_start, max_iter=500000).fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    y_train_pred = model.predict(X_train)

    #print(model.intercepts_)
    #print(model.coefs_)

    print("\n")
    print("MLP Test Set")
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_test_pred))  
    test_rmse = np.sqrt(metrics.mean_squared_error(y_test, y_test_pred))
    print('Root Mean Squared Error:', test_rmse)
    
    print("\n")
    print("MLP Train Set") 
    print('Mean Squared Error:', metrics.mean_squared_error(y_train, y_train_pred))  
    train_rmse = np.sqrt(metrics.mean_squared_error(y_train, y_train_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_train, y_train_pred)))
    hyper_table.append(np.array([
        len(layer_neurons),
        "-".join(str(i) for i in layer_neurons),
        solver,
        alpha,
        test_rmse,
        train_rmse,
        learning_rate,
        early_stopping]))
    print(columns)
    print(hyper_table[-1])
hyper_table = pd.DataFrame(hyper_table, columns=columns)
#file_name = file_name + str(np.random.randint(10000)) + ".csv"
hyper_table.to_csv(file_name, index=False)
print(hyper_table.sort_values("Test Set RMSE"))
