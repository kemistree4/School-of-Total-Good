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
import statsmodels.formula.api as smf
from mpl_toolkits.mplot3d import Axes3D

#Import data and assign to dataframe
df = pd.read_csv('/home/kemistree4/code/School-of-Total-Good/weight_guesser/01_heights_weights_genders.csv')
df_gender = pd.get_dummies(df) #Makes two new dummy variables to convert categorical variable into binary
df_gender.drop('Gender_Female',axis=1,inplace=True) #Drops the female column

#Seperate dependent data column in dataframe from independent data (attributes and labels)
X = df_gender[['Height','Gender_Male']]
y = df_gender['Weight'].values.reshape(-1,1) #Look into transpose. Careful with reshape

#Splits the data so that 80% of the data is the training set and 20% is the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0) 

#Import the LinearRegression class and call the fit() method for training data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_) #Prints the y-intercept of the regression line
print(regressor.coef_) #Prints the slope of the regression line

y_pred = regressor.predict(X_test)
y_train_pred = regressor.predict(X_train)

#Plot 2D with seaborn
sns.set()
# Plot weight as a function of height
g = sns.lmplot(x="Height", y="Weight", hue="Gender_Male", line_kws={'color': 'red'}, markers =["o", "x"], height=5, data=df_gender)
# Use more informative axis labels than are provided by default
g.set_axis_labels("Height (in)", "Weight (lbs)")

#Plot 3D with matplotlib
model = smf.ols(formula='Gender_Male ~ Height + Weight', data=df_gender)
results_formula = model.fit()
results_formula.params
x_surf, y_surf = np.meshgrid(np.linspace(df_gender.Height.min(), df_gender.Height.max(), 100),np.linspace(df_gender.Weight.min(), df_gender.Weight.max(), 100))
onlyX = pd.DataFrame({'Height': x_surf.ravel(), 'Weight': y_surf.ravel()})
fittedY=results_formula.predict(exog=onlyX)

# convert the predicted result in an array
fittedY=np.array(fittedY)

fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df_gender['Height'],df_gender['Weight'],df_gender['Gender_Male'],c='red', marker='o', alpha=0.5)
ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape), cmap = 'viridis', alpha=0.5)
ax.set_xlabel('Height')
ax.set_ylabel('Weight')
ax.set_zlabel('Gender')
plt.show()

print("Test set")
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print("Train set")
print('Mean Absolute Error:', metrics.mean_absolute_error(y_train, y_train_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_train, y_train_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_train, y_train_pred)))

def main():
    gender = (input("What is your gender (male or female)?"))
    given_height = float(input('What is your height in inches?'))
    if gender == "male":
        predicted_weight = regressor.intercept_ + regressor.coef_[0,0] * given_height + (regressor.coef_[0,1] * 1)
        print("I guess that your weight is: " + str(predicted_weight) + " lbs!")
    elif gender == "female":
        predicted_weight = regressor.intercept_ + regressor.coef_[0,0] * given_height + (regressor.coef_[0,1] * 0)
        print("I guess that your weight is: " + str(predicted_weight) + " lbs!")
    elif gender != "male" or "female":
        print("Please enter valid gender. Make sure letters are all lowercase") 
        
if __name__ == "__main__":
    main()