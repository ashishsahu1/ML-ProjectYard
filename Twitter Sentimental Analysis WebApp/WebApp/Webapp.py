from flask import Flask, render_template, request, jsonify
from TwitterBasedSentimentalAnalysisWebApp import Model

app = Flask(__name__, template_folder="./templates", static_folder="./static")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/search", methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    model_object = Model.model()
    result = model_object.detailed_analysis_tweet_data(search_tweet)
    return jsonify({"success": True, "tweets": result})


if __name__ == "__main__":
    app.run(debug=True)
