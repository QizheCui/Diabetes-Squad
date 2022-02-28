## After running the orange file on your local machine, you should be expected to see something looks like this:
<img width="1115" alt="Screenshot 2022-02-28 at 23 16 39" src="https://user-images.githubusercontent.com/68168401/156075009-811665df-bd64-49e9-99c4-c2a7a402d936.png">


## To explain what I did in the orange file:
1. I did some initial boxplot, scatterplot to get an intial understanding of the dataset
2. Now I want to explore how **obesity**, **gender**, and **itching** contribute to the diagonasis of diabetes (feel free to play around with other variables)
3. I created the Data Sampler and started to think about which model give the best prediction
4. I chose logistic regression (because it is easy), SVM(people said this is great for classfication problem), and decision tree (another great tool)
5. I evaluate the prediciton of each model using the confusion matrix


## Problems related to the models:
1. I am not familiar with the SVM model (will be great if John can explain)
2. In the SVM model, the sensitivity is surpursingly low
3. In the logistics regression and decision tree model, the specificity is quite low
4. TBC


## What I think potentially went wrong:
1. The variables I selected did not significantly contribute to diabetes (so that the model doesn't make good prediction in general)
2. I did not properly use regularization to control each variable
3. My poor understanding of Orange that created incorrect predictions
4. TBC
