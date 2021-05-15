from flask import Flask, request, jsonify, make_response
from Ml_Template_For_Google_Assitant_connection.Model.Model import model
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

# as the DialogueFlow requires a Https WebHook Url we use Flask Nagrok to make a temporary WebLink for
# testing purpose but later on we can also use a paid service like Heroku or AWS

run_with_ngrok(app)


@app.route('/', methods=['POST', 'GET'])
def get_data():
    req = request.get_json(force=True)
    queryResult = req.get('queryResult')
    input_text = queryResult['queryText']
    fulfillment_message = queryResult.get("fulfillmentMessages")
    temp = fulfillment_message[0].get('text').get("text")
    temp[0] = model.sentiment_analyse(input_text)
    print("This is the output json response := "+str(queryResult))
    print("--------------------------------------------------------------")
    return queryResult


@app.route('/webhook', methods=['GET', 'POST'])
def web_hook():
    # return response
    return make_response(jsonify(get_data()))


# run the app
if __name__ == '__main__':
    app.run()
