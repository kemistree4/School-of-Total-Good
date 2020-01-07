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
from scipy.stats import poisson

#random numbers from uniform distribution

n = 10000
start = 0
data_poisson = poisson.rvs(size=n, loc=start, mu=3)

ax = sns.distplot(data_poisson, bins=30, kde=False, color ='skyblue', hist_kws ={'linewidth': 0.2, 'alpha' :1})
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')