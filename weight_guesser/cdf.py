#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:24:56 2020

@author: kemistree4
"""

import scipy.stats as st

fish_cdf = st.norm.cdf(11, loc=10.0, scale =1.0) - st.norm.cdf(9, loc=10.0, scale =1.0)  #probability of a fish being measured between 9.5 lbs and 11 lbs when it weighs 10 lbs
one_off_cdf = (2 * st.norm.cdf(9, loc=10.0, scale =1.0))  #Probability of fish being more than 1 lb off true

print(fish_cdf, one_off_cdf)