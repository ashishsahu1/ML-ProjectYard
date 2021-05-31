'''
Implementation of 'Multiple Linear Regression'

'''

import numpy as np

# class for implementing multiple linear regression model with gradient descent
class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=10000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights, self.bias = None, None
        self.loss = []
        
    # method for evaluating error at each iteration
    @staticmethod
    def _mean_squared_error(y, y_hat):
        '''
        Input parameters:
        y --> array, true values
        y_hat --> array, predicted values
        Returns: 
        float, error
        '''
        error = 0
        for i in range(len(y)):
            error += (y[i] - y_hat[i]) ** 2
        return error / len(y)
    
    # method for calculating the coefficient of the linear regression model
    def fit(self, X, y):
        '''
        Input parameters:
        X --> array, features
        y --> array, true values
        Returns: 
        None
        '''
        # 1. initializing weights and bias to zeros
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        
        # 2. performing gradient descent
        for i in range(self.n_iterations):
            # line equation
            y_hat = np.dot(X, self.weights) + self.bias
            loss = self._mean_squared_error(y, y_hat)
            self.loss.append(loss)
            
            # calculating derivatives
            partial_w = (1 / X.shape[0]) * (2 * np.dot(X.T, (y_hat - y)))
            partial_d = (1 / X.shape[0]) * (2 * np.sum(y_hat - y))
            
            # updating the coefficients
            self.weights -= self.learning_rate * partial_w
            self.bias -= self.learning_rate * partial_d
        
    # method for making predictions using the line equation
    def predict(self, X):
        '''
        Input parameters:
        X --> array, features
        Returns: 
        array, predictions
        '''
        return np.dot(X, self.weights) + self.bias()
    
'''

EXAMPLE: 

# Importing Libraries

import pandas as pd
from sklearn import preprocessing 
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split


# Getting our Data

df = pd.read_csv('startups.csv')


# Data Preprocessing

# no null values are present
# but, we need to encode 'State' attribute
label_encoder = preprocessing.LabelEncoder()  # encoding data
df['State'] = df['State'].astype('|S')
df['State'] = label_encoder.fit_transform(df['State'])
# checking for null values
df.isnull().any()
# checking vif
variables = df[['R&D Spend', 'Administration', 'Marketing Spend', 'State']]
vif = pd.DataFrame()
vif['VIF'] = [variance_inflation_factor(variables.values, i) for i in range(variables.shape[1])]
vif['Features'] = variables.columns
# as vif for all attributes<10, we need not drop any of them


# Splitting Data for Training and Testing

data = df.values
X,y = data[:,:-1], data[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)  # splitting in the ration 80:20


# Fitting the Data

model = LinearRegression(learning_rate=0.01, n_iterations=10000)
model.fit(X_train,y_train)


# Making Predictions

y_pred = model.predict(X_test)

'''