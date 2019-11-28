#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 07:36:39 2019

@author: kemistree4
"""

import pandas as pd
from pandas import DataFrame
lo = pd.read_html("https://en.wikipedia.org/wiki/Largest_organisms")
lo = lo[0]
df = DataFrame(lo)

print(df)