#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:24:56 2020

@author: kemistree4
"""

import numpy as np

randomNums = np.random.normal(scale=3, size= 10000)
Fish_mass = np.round(randomNums)

print(Fish_mass)