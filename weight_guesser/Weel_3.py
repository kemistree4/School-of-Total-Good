#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 07:36:39 2019

@author: kemistree4
"""

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression 

lo = pd.read_html("https://en.wikipedia.org/wiki/Largest_organisms")
lo = lo[0]
print(lo)