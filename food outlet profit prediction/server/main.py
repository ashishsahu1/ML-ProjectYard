from flask import Flask, request, jsonify
from model_file.ml_model import pr_pred
import joblib
     
app=Flask("profit_predictions")

@app.route('/',methods=['POST'])
def predict():
    population=request.get_jason()
    model=joblib.load('../model/profit_predictor.joblib')
    predictions=pr_pred(model,population)
    response={
        profit_predictions:list(predictions)
    }
    return jsonify(response)

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=9696)