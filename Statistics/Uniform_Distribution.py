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
from scipy.stats import binom

#random numbers from uniform distribution

data_binom = binom.rvs(n=10, p=0.8, size=10000)

ax = sns.distplot(data_binom, kde=False, color ='skyblue', hist_kws ={'linewidth': 1, 'alpha' :1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')