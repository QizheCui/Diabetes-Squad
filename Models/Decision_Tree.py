import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#Read data and clean
diabetes = pd.read_csv(r'C:\Users\hussi\IRC\project\Diabetes-Squad\EDA\Mendeley_normalised.csv')
diabetes = diabetes.drop(diabetes.index[diabetes['CLASS'] == "P"])
cleanup_nums = {"CLASS":{"Y":1, "N":0 }}
diabetes = diabetes.replace(cleanup_nums)

#Split the features from the classification
X = diabetes.iloc[:,1:13]
y = diabetes.iloc[:,-1]

#Randomly split the data into training and testing sets with proportion 75%:25%
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=0)

#Apply model
tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train,y_train)

#Visualisation of model
fig = plt.figure(figsize=(16,9))
_ = plot_tree(tree, 
                   feature_names=['AGE','Urea','Cr','HbA1c','Chol','TG','HDL','LDL','VLDL','BMI','Male','Female'],  
                   class_names=['N','Y'],
                   filled=True)
fig.savefig("decision_tree.png")

#Random Forest
rf = RandomForestClassifier(random_state=0)
rf.fit(X_train,y_train)

fig = plt.figure(figsize=(16,9))
_1 = plot_tree(tree, 
                   feature_names=['AGE','Urea','Cr','HbA1c','Chol','TG','HDL','LDL','VLDL','BMI','Male','Female'],  
                   class_names=['N','Y'],
                   filled=True)
fig.savefig("random_forest.png")