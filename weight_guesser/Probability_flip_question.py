#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: kemistree4
"""

import pandas as pd
from itertools import product

def coin_number():
    coin_list = [] #Creates an empty list for coin 
    for i in range(3):
        coin_list.append("Coin # " + str(i + 1))#stole this line from the dice_roller code to create a new colum for every flip. Probably not necessary

def prob_trip():
    prob_question = int(input('What is the minimum probability for a triple-heads coin flip are you hoping to achieve?'))
    prob_tplt_count = 0
    for i in range(3,):
        coin = [0,1]
        number_list = coin_number(i)
        prob_df = pd.DataFrame(list(product(coin, repeat= i)), columns=number_list) #creates a dataframe containing the cartesian product of the coin flip
        prob_df_csv= prob_df.to_csv(header=None, index=False).strip('\n').split('\n')
        
    prob_df_length = len(prob_df_csv)
    
    for i in prob_df_csv: #iterates through the list
        if '1,1,1' in i: #looks to see if the triple-heads substring is contained in the string
            prob_tplt_count = prob_tplt_count + 1
            
    prob_perc = (prob_tplt_count/prob_df_length)
    
    if prob_perc >= prob_question:
        print("You have to flip x-coins to have a " + str(prob_question) + " chance of flipping triple-heads.")
        
def main():
    prob_trip()
    
if __name__ == "__main__":
    main()