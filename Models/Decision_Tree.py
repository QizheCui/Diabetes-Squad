import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_validate, cross_val_score
from sklearn.metrics import plot_roc_curve, confusion_matrix, RocCurveDisplay
import graphviz

#Read data and clean
diabetes = pd.read_csv(r'C:\Users\hussi\IRC\project\Diabetes-Squad\EDA\Mendeley.csv')
diabetes = diabetes.drop(diabetes.index[diabetes['CLASS'] == "P"])
cleanup_nums = {"Gender":{"M": 1, "F": 0}, "CLASS":{"Y":1, "N":0 }}
diabetes = diabetes.replace(cleanup_nums)

#Split the features from the classification
X = diabetes.iloc[:,2:13]
y = diabetes.iloc[:,-1]

#Randomly split the data into training and testing sets with proportion 75%:25%
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=0)

#Apply model
tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train,y_train)

#Visualisation of model
fig = plt.figure(figsize=(10,10))
_ = plot_tree(tree, 
                   feature_names=['Gender','AGE','Urea','Cr','HbA1c','Chol','TG','HDL','LDL','VLDL','BMI'],  
                   class_names=['N','Y'],
                   filled=True,
                   impurity=False,
                   rounded=True,
                   proportion=True,
                   max_depth=4)

fig.savefig("decision_tree(1).png")

#Random Forest
rf = RandomForestClassifier(random_state=0)
rf.fit(X_train,y_train)

# Evaluation
print("Decision Tree mean =", np.mean(cross_val_score(tree,X_test,y_test)))
print("Random Forest mean =", np.mean(cross_val_score(rf,X_test,y_test)))
#Decision Tree mean = 0.9958333333333332
#Random Forest mean = 0.9830673758865249

y_pred1 = tree.predict(X_test)
y_pred2 = rf.predict(X_test)

print(confusion_matrix(y_test, y_pred1))
print(confusion_matrix(y_test, y_pred2))
#Decision tree
#[[ 22   0]
# [  0 215]]
#Random Forest
#[[ 20   2]
# [  0 215]]


RocCurveDisplay.from_estimator(tree, X_test, y_test)
RocCurveDisplay.from_estimator(rf, X_test, y_test)
#plt.show()

