from flask import Flask, request, jsonify
from model_file.ml_model import pr_pred
import joblib
     
app=Flask("price_predictions")

@app.route('/',methods=['POST'])
def predict():
    house_feature=request.get_jason()
    model=joblib.load('../model/delhi_house_price')
    predictions=pr_pred(model,house_feature)
    response={
        price_predictions:list(predictions)
    }
    return jsonify(response)

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=9696)