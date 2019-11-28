#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 07:36:39 2019

@author: kemistree4
"""

import pandas as pd

#Importing all html charts on Wikipedia
lo = pd.read_html("https://en.wikipedia.org/wiki/Largest_organisms")

#Selecting first chart from all of them and converting to dataframe
lo = lo[0]

