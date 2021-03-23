import pandas as pd
import numpy as np

#Importing The data set
red_wine = pd.read_csv("winequality-red.csv",sep=';',engine='python')
white_wine = pd.read_csv("winequality-white.csv",sep=';',engine='python')

#Checking is there any missing value in data set

print("Checking missing values of Red Wine")

print(red_wine.isnull().sum())

print("---------------------")

print("Checking missing values of White wine")

print(white_wine.isnull().sum())

#Printing shape 

print("Red Wine Shape:-",red_wine.shape)
print("------------")
print("White Wine Shape:-",white_wine.shape)


#Dependent And Independent Variable of Red Wine

X_red = red_wine.iloc[: , :-1].values
y_red = red_wine.iloc[: , -1].values

#Dependent And Independent Variable of White Wine

X_white = white_wine.iloc[: , :-1].values
y_white = white_wine.iloc[: , -1].values

#Feature Scalling on Red Wine

from sklearn.preprocessing import StandardScaler
sc_Rx = StandardScaler()
X_red = sc_Rx.fit_transform(X_red)

#Feature Scalling on White Wine

from sklearn.preprocessing import StandardScaler
sc_Wx = StandardScaler()
X_white = sc_Wx.fit_transform(X_white)

#Splitting Red wine dataset into training and test set

from sklearn.model_selection import train_test_split
XR_train,XR_test,yR_train,yR_test = train_test_split(X_red,y_red,
                                                 random_state=0,
                                                 test_size=0.25)

#Splitting White wine dataset into training and test set

from sklearn.model_selection import train_test_split
XW_train,XW_test,yW_train,yW_test = train_test_split(X_white,y_white,
                                                 random_state=0,
                                                 test_size=0.25)


#Training The Red_Wine set

from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(XR_train,yR_train)

#Testing The model 
Red_predict = regressor.predict(XR_test)

errors = abs(Red_predict - yR_test)
print('Metrics for SupportVectorRegressor Trained on Red WineData')
# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / yR_test)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy for Red Wine:', round(accuracy, 5), '%.')

#Training The White_Wine set

from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(XW_train,yW_train)


#Testing The model 
White_predict = regressor.predict(XW_test)

errors = abs(White_predict - yW_test)
print('Metrics for SupportVectorRegressor Trained on White Wine Data')
# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / yW_test)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy for White Wine:', round(accuracy, 5), '%.')

