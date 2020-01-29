#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:49:01 2019
### probability/statistics
- fish mass measurement camera has an accuracy of 1 lb std dev (zscore = 1). How likely for 
measurement of fish more than a 1 lb off of truth? Use cdf to figure out range of both sides of bell curve. (confidence interval)
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
from matplotlib import pyplot as plt
import statistics
from scipy import stats

def get_num_list(number):
    number_list = []
    for i in range(0, number): #loop that runs the number of times the user has input 
        number_list.append("Rolled_Die_" + str(i + 1))
    return number_list
        
#Create a function that generates a list of dice possibilities and turns that list into a dataframe 
def roll_die(number):
    for i in range(0,number):
        dice = [1,2,3,4,5,6]
        number_list = get_num_list(number)
        df = pd.DataFrame(list(product(dice, repeat= number)), columns=number_list) #list of all possibilities for two six-sided dice
        df['Sum'] = df.sum(axis=1)
    return df
        
def main():
    figs = []
    for i in range(5):
        number = i + 1
        df = roll_die(number)
        print(df)
        fig = df['Sum'].hist(bins=6 * (i + 1) * 2) 
        plt.savefig(f"dice{i + 1}.jpg")
        figs.append(fig)
        plt.clf()
        if number == 5:
            print("Standard deviation:",statistics.stdev(df['Sum']))
            print("Mean:",statistics.mean(df['Sum']))
            print("z-score:",stats.zscore(df['Sum']))     
    print("Standard deviation is",statistics.stdev(df['Sum']))
    print("Mean is",statistics.mean(df['Sum']))
    print("z-score is",stats.zscore(df['Sum']))
    return figs

if __name__ == "__main__":
    figs = main()