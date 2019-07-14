#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:50:05 2019

@author: denkal
"""

import pandas as pd 
import numpy as np 

df = pd.read_csv("data/train.csv")

#This creates a df to show how many null values there are in the columns
total = df.isnull().sum().sort_values(ascending=False)
percent_1 = df.isnull().sum()/df.isnull().count()*100
percent_2 = (round(percent_1, 1)).sort_values(ascending=False)
missing_data = pd.concat([total, percent_2], axis=1, keys=['Total', '%'])

#Dropping passenger ID from the dataset
df = df.drop(['PassengerId'], axis = 1)

#Dealing with the Null values 


