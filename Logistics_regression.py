# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:51:14 2022

@author: Linne
"""
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize

logisticRegr = LogisticRegression()
data = pd.read_csv('.\EDA\Mendeley_training70.csv')
columns = data.columns
x_train = data[data.columns[:-1]]
t_train = data[data.columns[-1]]

logisticRegr.fit(x_train, y_train)

testdata = pd.read_csv('.\EDA\Mendeley_testing70.csv')