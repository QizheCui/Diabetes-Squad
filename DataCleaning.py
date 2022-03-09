# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:48:12 2022

@author: Linne
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import random

data = pd.read_csv('.\EDA\Mendeley.csv')
fraction = 0.7 #fraction of data used for testing

del data['No_Pation'] #deleting patient numner
del data['ID'] #deleting ID number

#setting gender as boolean (2 columns)
data['Female'] = (data['Gender']=='F').astype(int) 
data['Male'] = (data['Gender']=='M').astype(int)
del data['Gender']

#centering columns at 0
for i in data.columns[:-3]:
    data[i]=data[i]-data[i].mean()

#rearranging columns so that the diabetes diagnosis is the last column
column_names=list(data.columns.values)
column_names[-1], column_names[-3] = column_names[-3], column_names[-1]
data = data.reindex(columns=column_names)

#saving the file
data.to_csv('.\EDA\Mendeley_normalised.csv')

#Generating the random index for the sample
len_training = int(len(data)*fraction)
index = random.sample(range(len(data)), len_training)

#selecting training data using the index
training_data = data.iloc[index]
#saving the data
training_data.to_csv('.\EDA\Mendeley_training'+str(fraction)+'.csv')

#taking all the indexes not used in training data
test_index =[]
for i in range(len(data)):
    if i in index == False:
        test_index.append(i)

#selecting the test data
testing_data = data.iloc(test_index)
#saving the test data
training_data.to_csv('.\EDA\Mendeley_testing'+str(fraction)+'.csv')

        
