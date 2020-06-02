# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:38:42 2020

@author: Mbongiseni Dlamini
"""

import seaborn as sea # import the seaborn library
iris = sea.load_dataset('iris') # use load_dataset() to get the data
iris.head() # show first few data