import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_validate, cross_val_score
from sklearn.metrics import plot_roc_curve, confusion_matrix, RocCurveDisplay

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
                   filled=True,
                   impurity=False)
fig.savefig("decision_tree.png")

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
#[[ 21   1]
# [  0 215]]


RocCurveDisplay.from_estimator(tree, X_test, y_test)
RocCurveDisplay.from_estimator(rf, X_test, y_test)
#plt.show()