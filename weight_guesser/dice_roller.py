#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:49:01 2019
### probability/statistics
- use a nested for loop to create all the possible pairs of dice rolls and their sum/score
- create a dataframe with 3 columns for the 2 die rolls and the sum
- use df.sum() and df.value_counts() to compute the probability of every possible sum (try to do this without a for loop)
- add doctest to confirm values in dataframe --use hist -o -p and copy the entire dataframe output
- Plot histogram of sums (5 hist for 1,2,3,4, and 5 dice)
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

number = int(input('How many die(dice) would you like to roll?'))

def get_num_list():
    number_list = []
    
    for i in range(0, number): #loop that runs the number of times the user has input 
        number_list.append("Rolled_Die_" + str(i + 1))
    return number_list

#Create a function that generates a list of dice possibilities and turns that list into a dataframe 
def roll_die():
    dice = [1,2,3,4,5,6]
    number_list = get_num_list()
    df = pd.DataFrame(list(product(dice, repeat=number)), columns=number_list) #list of all possibilities for two six-sided dice
    df.loc[:,'Sum']= df.sum(axis=1)
#    dp = df['Sum'].value_counts(normalize=True)
#    dp1 = df['Sum'].value_counts(normalize=False)
    #print(dp)
    #print(dp1.plot())
    return df


def main():
    df = roll_die()
    print(df)

if __name__ == "__main__":
    main()
