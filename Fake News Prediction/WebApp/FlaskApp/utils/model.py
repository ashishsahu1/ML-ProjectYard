import pickle
import os
import warnings

warnings.filterwarnings("ignore")

class Model:
    def __init__(self, tfidf_path:'string' = ".//FlaskApp//utils//Model//tfidf.pkl", model_path:'string' = ".//FlaskApp//utils//Model//model.pkl"):
        
        print(os.getcwd())
        self.model = pickle.load(open(model_path, 'rb'))
        self.tfidf = pickle.load(open(tfidf_path, 'rb'))
        
    
    def predict(self, data:'string')->'list':
        features = self.tfidf.transform([data])
        to_return = {}
        to_return["pred"] = self.model.predict(features)[0]
        to_return["score"] = round(self.model.decision_function(features)[0], 3)

        return to_return

