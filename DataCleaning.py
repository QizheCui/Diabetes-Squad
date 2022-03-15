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
from sklearn import preprocessing

data = pd.read_csv('.\EDA\Mendeley.csv')
fraction = 0.7 #fraction of data used for testing

del data['No_Pation'] #deleting patient numner
del data['ID'] #deleting ID number

#setting gender as boolean (2 columns)
data['Female'] = (data['Gender']=='F').astype(int) 
data['Male'] = (data['Gender']=='M').astype(int)
del data['Gender']
#removing predict diabetes data, diabetes diagnosis as 1 or 0
data['CLASS'] = data['CLASS'].replace(['P'],np.nan)
data.dropna(axis=1)
data['CLASS'] = (data['CLASS']=='Y').astype(int)
        

#centering columns at 0
for i in data.columns[:-3]:
    data[i]=data[i]-data[i].mean()

#rearranging columns so that the diabetes diagnosis is the last column
column_names=list(data.columns.values)
column_names[-1], column_names[-3] = column_names[-3], column_names[-1]
data = data.reindex(columns=column_names)


#saving the file
data.to_csv('.\EDA\Mendeley_normalised.csv')

#scaling
scaler = preprocessing.StandardScaler().fit(data[data.columns[:-1]])
X_scaled= scaler.transform(data[data.columns[:-1]])
data_scaled= np.concatenate((X_scaled,data['CLASS'].to_numpy().reshape(len(data),1)),1)
data_scaled = pd.DataFrame(data_scaled, columns = data.columns)

#Generating the random index for the sample
len_training = int(len(data)*fraction)
index = random.sample(range(len(data)), len_training)

#selecting training data using the index
training_data = data.iloc[index]
training_data_scaled = data_scaled.iloc[index]
#saving the data
training_data.to_csv('.\EDA\Mendeley_training'+str(int(fraction*100))+'.csv')
training_data_scaled.to_csv('.\EDA\Mendeley_training'+str(int(fraction*100))+'_ss.csv')

#taking all the indexes not used in training data
test_index =[]
for i in range(len(data)):
    if i in index == False:
        test_index.append(i)

#selecting the test data
testing_data = data.iloc[test_index]
testing_data_scaled = data_scaled.iloc[test_index]
#saving the test data
testing_data.to_csv('.\EDA\Mendeley_testing'+str(int(fraction*100))+'.csv')
testing_data_scaled.to_csv('.\EDA\Mendeley_testing'+str(int(fraction*100))+'_ss.csv')
        
