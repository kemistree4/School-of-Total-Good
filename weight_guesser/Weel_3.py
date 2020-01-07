#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 07:36:39 2019

@author: kemistree4
"""

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

#Importing all html charts on Wikipedia page "Largest Organisms"
lo = pd.read_html("https://en.wikipedia.org/wiki/Largest_organisms")

#Slicing first chart from all of them and converting to dataframe
lo = lo[0]

column_names = lo.columns

print(column_names)

lo.dtypes #tells me the data type in my dataframe
lo.index.values # tells me the index labels

columns_to_drop = [column_names[i] for i in [0]] #Slicing the column I want to remove

lo.drop(columns_to_drop, inplace=True, axis=1) #Removes the 'Rank' column, it's useless for analysis

lo = lo.replace("\(.*\)","", regex=True) #Replaces parentheses and what they contain with nothing
lo = lo.replace("\[.*\]","", regex=True) #Replaces square brackets and what they contain with nothing

#lo.to_csv(r'/home/kemistree4/code/School-of-Total-Good/weight_guesser/Week_3_cleaned.csv')
#lo.to_html(r'/home/kemistree4/code/School-of-Total-Good/weight_guesser/Week_3_cleaned.html')
print(lo)

lo1 = lo.iloc[:,:3]
lo2 = lo.loc[:,['Animal', 'Average total length[m (ft)]']]
print(lo1)
print(lo2)

g =sns.scatterplot(x='Animal', y='Maximum mass[tonnes]', hue='Animal', data=lo1)
g2 =sns.scatterplot(x='Animal', y='Average total length[m (ft)]', hue='Animal', data=lo2)

print(g)
print(g2)
