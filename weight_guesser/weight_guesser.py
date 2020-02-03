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