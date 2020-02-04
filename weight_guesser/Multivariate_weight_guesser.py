#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 07:05:14 2020

@author: kemistree4
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import seaborn as sns

#Import data and assign to dataframe
df = pd.read_csv('/home/kemistree4/code/School-of-Total-Good/weight_guesser/01_heights_weights_genders.csv')
df_gender = pd.get_dummies(df) #Makes two new dummy variables to convert categorical variable into binary
df_gender.drop('Gender_Female',axis=1,inplace=True) #Drops the female column

#Seperate dependent data column in dataframe from independent data (attributes and labels)
X = df_gender[['Height','Gender_Male']]
y = df_gender['Weight'].values.reshape(-1,1)

#Splits the data so that 80% of the data is the training set and 20% is the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0) 

#Import the LinearRegression class and call the fit() method for training data
regressor = LinearRegression()
regressor.fit(df_gender[['Height','Gender_Male']], df_gender['Weight'])

print(regressor.intercept_) #Prints the y-intercept of the regression line
print(regressor.coef_) #Prints the slope of the regression line

y_pred = regressor.predict(X_test)

#Plot with seaborn
sns.set()

# Plot weight as a function of height
g = sns.lmplot(x="Height", y="Weight", hue="Gender_Male", line_kws={'color': 'red'}, markers =["o", "x"], height=5, data=df_gender)

# Use more informative axis labels than are provided by default
g.set_axis_labels("Height (in)", "Weight (lbs)")

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

def main():
    gender = (input("What is your gender (male or female)?"))
    given_height = float(input('What is your height in inches?'))
    if gender == "male":
        predicted_weight = regressor.intercept_ + regressor.coef_[0] * given_height + (regressor.coef_[1] * 1)
        print("I guess that your weight is: " + str(predicted_weight) + " lbs!")
    elif gender == "female":
        predicted_weight = regressor.intercept_ + regressor.coef_[0] * given_height + (regressor.coef_[1] * 0)
        print("I guess that your weight is: " + str(predicted_weight) + " lbs!")
    elif gender != "male" or "female":
        print("Please enter valid gender. Make sure letters are all lowercase") 
        
if __name__ == "__main__":
    main()