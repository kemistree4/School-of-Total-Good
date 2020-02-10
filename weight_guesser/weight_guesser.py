<<<<<<< HEAD
#Assignment 2

#- Learn how to read .csv file into dataframe (cmd involves importing pandas/ read_csv)
#- Learn what each of these commands do: 
#    - .head()
#    - .describe()
#    - .info()
#    - .shape()
#    - .plot()
    
#- Launch ipython and type above commands (assign dataframe to variable and use as prefix to command)

#ipython
#>>>import pandas as pd
#>>>df=pd.read_csv(filename)
#>>>df.plot(...)

#- Plot height on x axis
#- Plot weight on y axis
#- All female dots are red
#- All male dots are blue

import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('C:/code/School-of-Total-Good/weight_guesser/01_heights_weights_genders.csv')


#plot using seaborn
g =sns.lmplot(x='Height', y='Weight', hue='Gender', data=df, palette =['blue','red'])
print(g)

X = df.loc['Height']
Y = df.loc['Weight']

linear_regressor = LinearRegression()

linear_regressor.fit(X,Y)
Y_pred = linear_regressor.predict(X)
print(Y_pred)
=======

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#Import data and assign to dataframe
df = pd.read_csv('/home/kemistree4/code/School-of-Total-Good/weight_guesser/01_heights_weights_genders.csv')

#Seperate dependent data column in dataframe from independent data (attributes and labels)
X = df['Height'].values.reshape(-1,1)
y = df['Weight'].values.reshape(-1,1)

#Splits the data so that 80% of the data is the training set and 20% is the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 

#Import the LinearRegression class and call the fit() method for training data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_) #Prints the y-intercept of the regression line
print(regressor.coef_) #Prints the slope of the regression line

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df1 = df.head(25)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

def main():
    given_height = float(input('What is your height in inches?'))
    predicted_weight = (regressor.coef_ * given_height) + regressor.intercept_
    print("I guess that your weight is: " + str(predicted_weight) + " lbs!")

if __name__ == "__main__":
    main()

