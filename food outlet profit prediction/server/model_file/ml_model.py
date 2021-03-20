import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

#since in model we are using population which is scaleowned, so input would also be scaledown here.
def  pr_pred(model,population):
     population=population/(10**4)
     predict=model.predict(population)
     return predict*1000


