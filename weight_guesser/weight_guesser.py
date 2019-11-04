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

df = pd.read_csv('C:/Users/Rikeem/code/School-of-Total-Good/weight_guesser/01_heights_weights_genders.csv')

#plot using pandas
df.plot(kind='scatter' , x='Height' ,y='Weight')

#plot using seaborn
g =sns.scatterplot(x='Height', y='Weight', hue='Gender', data=df, palette =['blue','red'])
