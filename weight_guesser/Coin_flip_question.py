#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:07:03 2020

@author: kemistree4
"""

"""My thought was that I'd create a database with every possible outcome for the number of coins I flipped. After that I
decided to convert the sequence of numbers in each row into a comma seperated string. Then I found a method to allow me to
check if each string contained a triple heads substring which was represented as 1,1,1. For each output I was able to divide
the number of times a triple heads substring showed up by the total number of items in the list and that gave me my probability
of flipping heads three times in a row given a certain number of coin flips. Probably not the most elegant solution but it works
...i think....my probability rationale might be flawed"""

import pandas as pd
from itertools import product

def coin_number(number):
    coin_list = [] #Creates an empty list for coin 
    for i in range(number):
        coin_list.append("Coin # " + str(i + 1))#stole this line from the dice_roller code to create a new colum for every flip. Probably not necessary

def coin_flip(number):
    for i in range(number):
        coin = [0,1]
        number_list = coin_number(number)
        df = pd.DataFrame(list(product(coin, repeat= number)), columns=number_list) 
        df_csv= df.to_csv(header=None, index=False).strip('\n').split('\n') # Converts the dataframe to a list of strings
        
    tplt_count = 0
    df_length = len(df_csv)
    
    for i in df_csv: #iterates through the list
        if '1,1,1' in i:
            tplt_count = tplt_count + 1
    
    percentage = (tplt_count/df_length)
    print('Your chance of flipping three heads in a row when flipping ' + str(number) + ' coins is ' + str(percentage * 100) + ' percent.')

def main():
    number = int(input("How many coins should I flip?"))
    coin_flip(number)
    
if __name__ == "__main__":
    main()