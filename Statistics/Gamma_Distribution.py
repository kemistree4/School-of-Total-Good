# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:54:18 2020

@author: rsholes
"""

#import matplotlib.pyplot as plt
#from IPython.display import Math, Latex
#from IPython.core.display import Image
import seaborn as sns

sns.set(color_codes=True)
sns.set(rc={'figure.figsize':(10,10)})

#import uniform distribution
from scipy.stats import gamma

#random numbers from uniform distribution

n = 1000
start = 0
width = 1
data_gamma = gamma.rvs(a=4, size=n, loc=start, scale=width)

ax = sns.distplot(data_gamma, bins=100, kde=True, color ='skyblue', hist_kws ={'linewidth': 1, 'alpha' :1})
ax.set(xlabel='Gamma Distribution', ylabel='Frequency')