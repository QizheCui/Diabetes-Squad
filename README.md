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

# Initial Visualzation
By our initial scatter plot, we found out that age, HbA1c and BMI are strong indicators of diabetes as shown below:

![image](https://user-images.githubusercontent.com/68168401/159133009-43742fdb-d47f-4f52-a3c0-f7f6d45e35d6.png)


Therefore, we focus on the distribution of each of these feature and find out that patients who are older, with higher BMI or HbA1c are more likely to have diabetes then thoese who are not

![image](https://user-images.githubusercontent.com/68168401/159133017-916d78f9-0ebd-4449-9fd4-8aeffa793736.png)

# Machine Learning Models
In the data prepocessing stage, we scaled the mean of each feature to 0. We have implemented 4 models and they are:
## Logistic Regression
model description, what parameter did we choose? its performance? any additional info ...
## Support Vector Machine
model description, what parameter did we choose? its performance? any additional info ...
## Random Forest / Decision Tree
model description, what parameter did we choose? its performance? any additional info ...
## K Nearest Neighbour
model description, what parameter did we choose? its performance? any additional info ...

# ROC Analysis
Based on our ROC analysis, we can see that random forest gives the highest AUC =1 , while KNN has AUC around 0.95. All models have accuracy >= 90%.


# Comparision to external dataset
When we compare our models to external dataset, we observe lower precision.
![image](https://user-images.githubusercontent.com/68168401/159133062-388bb14f-924a-4610-a2f3-8ca77741cf8f.png)
