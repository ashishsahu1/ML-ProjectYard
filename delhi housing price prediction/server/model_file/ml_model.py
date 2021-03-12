import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

#functions required for data preprocessing.
# function for removing not defined  values which here,represented by 9(only for binary nos.)
def na_remover(data):
    data.replace(9,0.5,inplace=True)

#pipeline function for data preprocessing and location decoding.
def data_processing(data):
    K=np.log(data['Price']/data['Area'])
    data['Location']=K
    house_feature=data.drop(['Price'],axis=1)
    my_pipeline=Pipeline([('rem',na_remover(house_feature)),
                          ('std',StandardScaler())   
                         ])
    return my_pipeline.fit_transform(house_feature)

#additional function for location decoding
def pred_processing(data):
    ld_coff=918615320.0
    data['Price']=ld_coff/np.sqrt(data['Area']*data['Bedrooms'])
    X_pred=data_processing(data)
    return X_pred
    

#function for price prediction.
def pr_pred(model,tr_feature):
    X=pred_processing(tr_feature)
    pred_price=np.exp(model.predict(X))
    return pred_price



