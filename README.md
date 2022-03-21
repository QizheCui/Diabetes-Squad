# Diabetes-Squad
This repository is for group 2 in the Imperial College London Year 2 Interdisciplinary Research Computing Project.

# Topic:
Early Diagnosis and prediction of Diabetes usinng one or more features

# Group members:
1. Ethan Cui
2. Lei Johansson
3. Tamjid Miah
4. Sara Cheakdkaipejchara

# Datasets:
Click [here](https://data.mendeley.com/datasets/wj9rwkp9c2/1/files/2eb60cac-96b8-46ea-b971-6415e972afc9)

# Background
Diabetes is one of the leading causes of death in the world, with an estimated 422 million people affected worldwide (WHO) (2020). Recently, there has been a surge in research to increase the chance of early detection. We tested 4 different supervised ML models including Logistic Regression, K- nearest neighbours, Random forest and SVM, to see which performed most accurately in predicting diabetes.

# Initial Visualzation
By our initial scatter plot, we found out that age, HbA1c and BMI are strong indicators of diabetes as shown below:

![image](https://user-images.githubusercontent.com/68168401/159133009-43742fdb-d47f-4f52-a3c0-f7f6d45e35d6.png)


Therefore, we focus on the distribution of each of these feature and find out that patients who are older, with higher BMI or HbA1c are more likely to have diabetes then thoese who are not

![image](https://user-images.githubusercontent.com/68168401/159133017-916d78f9-0ebd-4449-9fd4-8aeffa793736.png)

# Machine Learning Models
In the data prepocessing stage, we scaled the mean of each feature to 0. We have implemented 4 models and they are:
## Logistic Regression
This model uses a logistic curve (example shown below) to model a dependent variable that can take one of two results. In our case, this would be whether or not the patient has diabetes. The different features are thus plotted and a logistic curve fitted to determine the relationship between the features and the diabetes diagnosis.
![image](https://github.com/QizheCui/Diabetes-Squad/blob/main/logistic_function_desmos.png)

Logistic Function plotted in Desmos
## Support Vector Machine
The model create a hyperplane that tries to seperate the data into 2 groups. Although RBF is the most commonly used kernel, the linear kernel performs better in our dataset which gives accuracy around 0.94.

## Random Forest / Decision Tree
A decision tree model works by considering features that seem to be the best indicators of a class then creating branches based on whether or not a certain condition is met by the sample points. This creates branches from combinations of features and the aim is to identify subgroups where the majority of sample points fall into a certain class. When given test data, the model can then make a classification prediction by identifying which subgroup the test points fall into. A random forest model creates random samples of decision trees from the sample data to reduce the risk of overfitting.

## K Nearest Neighbour
This model is a non-parametric machine learning method. The model is trained using a set of data, any data input after is then compared to the existing data, and it's membership of the class (Diabetic or Non-Diabetic) is determined by the class of it's nearest k neighbour(s) in terms of the different features. For example, if k=1, the data point most similar to the input data point is Diabetic, that input data point will be classed as Diabetic. We applied the most commonly used distance metric (Euclidean) in our model.

# ROC Analysis
Based on our ROC analysis, we can see that logistic regression model gives the highest AUC = 0.977 , while SVC has AUC around 0.975. All models have accuracy >= 95%.
<img width="1172" alt="ROC curve =" src="https://user-images.githubusercontent.com/68168401/159257898-ca6c38e2-3faf-4f6c-b32f-36ba79c1dcf7.png">


# Comparision to external dataset
When we compare our models to external dataset, we observe lower precision.
![image](https://user-images.githubusercontent.com/68168401/159133062-388bb14f-924a-4610-a2f3-8ca77741cf8f.png)

# Finally... Our Poster!
[IRC_project_poster_group2.pdf](https://github.com/QizheCui/Diabetes-Squad/files/8315231/IRC_project_poster_group2.pdf)
![image](https://github.com/QizheCui/Diabetes-Squad/blob/main/poster.png)
