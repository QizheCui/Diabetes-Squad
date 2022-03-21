import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#Load data
diabetes = pd.read_csv(r'/Users/saracheakdkaipejchara/PycharmProjects/Diabetes-Squad/EDA/Mendeley.csv')

#Clean data
df = diabetes.iloc[:,2:]
df_copy = df.copy()
df_copy = df_copy.drop(df_copy.index[df_copy['CLASS'] == "P"])
cleanup_nums = {"Gender":{"M": 1, "F": 0}, "CLASS":{"Y":1, "N":0 }}
df_copy = df_copy.replace(cleanup_nums)


#split training and testing data
X = df_copy.iloc[:,0:11].to_numpy()
y = df_copy.iloc[:,11].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#KNN
clf = KNeighborsClassifier(4)
clf.fit(X_train, y_train)
clf.predict(X_test)

accuracy = np.mean(y_test == clf.predict(X_test))

#Final output
print(accuracy)