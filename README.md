<h1><center>Travel Insurance - Predictive Model</center></h1>
<center>July 2024</center>
<center>Celine Ng</center>


## Objective<br>

The dataset was downloaded from Kaggle, <br>[Travel Insurance Prediction Data](https://www.kaggle.com/datasets/tejashvi14/travel-insurance-prediction-data)
on 23rd July 2024. The goal of the project is to build a model to predict 
if the customer will 
be interested in buying travel insurance package based on the features
given. 

## Technology Used
1. python
2. pandas
3. matplotlib
4. seaborn
5. sklearn
6. GridSearch
7. Voting Classifier

## Approach & Methodology
I approached this problem by following a structured methodology of data 
exploration, preprocessing, and modeling.
1. Data Exploration: Examined data distribution, linear correlation between features and 
   between features/target variable, and multicollinearity (using variance 
   inflation factor). Also, tested relevance of all features with hypothesis 
   testing
2. Preprocessing: Scale numerical features and encode categorical features.
3. Modeling: Train data with logistic regression, random forest, and 
   support vector machine (SVM). Hyperparameter tune with GridSearch. 
   Combine all 3 models to create an ensemble hard voting model.


## Results
The project used the Voting ensemble model, which includes, a logistic <br>
regression, a random forest model, and a support vector machine model. <br>
The model has the accuracy rate of 0.776. 

## Challenges & Learnings
As a first machine learning project, I was still trying to grasp all the new 
concepts and methods. <br>
**Furture Work:**<br>
1. Use pipeline for scalability
2. For more reliable model evaluation: Prepare 3 sets of data for train, 
   evaluate, and test; baseline model; pick evaluation metrics based on 
   dataset and problem
3. Iteratively train and test model to optimize results


