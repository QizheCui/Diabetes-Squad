# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:48:12 2022

@author: Linne
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
data = pd.read_csv('diabetes.txt', delimiter = '\t')

sex1 = data.query('SEX == 1')
sex2 = data.query('SEX == 2')

bmi_mean1 = np.mean(sex1['BMI'])
print(bmi_mean1)
bmi_mean2 = np.mean(sex2['BMI'])
print(bmi_mean2)

#2 might be male as the mean BMI is larger