from flask import Flask, render_template, redirect, current_app as app, request
from .utils.model import Model
import json

pac = Model()

# Route for main page
@app.route("/home")
@app.route("/")
def index():
    return render_template("index.html")

# Route for guide page
@app.route("/guide")
def guide():
    return render_template("guide.html")

@app.route("/predict", methods = ["GET", "POST"])
def results():
    if (request.method == "GET"):
        return redirect("/")

    news = request.form.get('news')
    print(news)
    prediction = pac.predict(news)
    params = prediction
    params['news'] = news
    params['fakewords'] = news
    print(params)
    return render_template("results.html", params = params)

# Route for dashboard
@app.route("/dashboard")
def dashboard():
    return redirect("/dashboard/")
