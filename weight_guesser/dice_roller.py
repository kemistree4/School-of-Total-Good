#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:49:01 2019
### probability/statistics
- use a nested for loop to create all the possible pairs of dice rolls and their sum/score
- create a dataframe with 3 columns for the 2 die rolls and the sum
- use df.sum() and df.value_counts() to compute the probability of every possible sum (try to do this without a for loop)
- add doctest to confirm values in dataframe --use hist -o -p and copy the entire dataframe output

>>> type(generate_possibilities())
DataFrame
>>> generate_possibilites().shape
(36, 3)

@author: kemistree4
"""

def generate_possibilities():
    """ generates all pairs of die rolls and their sums
    >>> type(generate_possibilities())
    DataFrame
    >>> generate_possibilites().shape
    (36, 3)
    >>> generate_possibilities
    <function generate_possibilities...>

    """
    pass

import pandas as pd
from itertools import product

#Create a function that generates a list of dice possibilities and turns that list into a dataframe 
def roll_die():
    dice = [1,2,3,4,5,6]
    df = pd.DataFrame(list(product(dice,repeat = 2)), columns = ['Die_1', 'Die_2']) #list of all possibilities for two six-sided dice
    df.loc[:,'Sum']= df.sum(axis=1)
    dp = df['Sum'].value_counts(normalize=True)
    print(dp)
    return df


print(roll_die())
#Ask Hobson what the difference betweeen a permutation and a product