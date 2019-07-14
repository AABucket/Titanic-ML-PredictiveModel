#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:46:26 2019

@author: denkal
"""
import pandas as pd
from sklearn.naive_bayes import GaussianNB

train_df = pd.read_csv("data/num_train.csv")
test_df = pd.read_csv("data/num_test.csv")

#Making the training and testing datasets for the model
X_train = train_df.drop("Survived", axis=1)
Y_train = train_df["Survived"]
X_test  = test_df.copy()

gaussian = GaussianNB() 
gaussian.fit(X_train, Y_train)  
Y_pred = gaussian.predict(X_test)  
print(round(gaussian.score(X_train, Y_train) * 100, 2))