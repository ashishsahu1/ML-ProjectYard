from dash import Dash
from .components import *
import os
from io import BytesIO
import pandas as pd
from wordcloud import WordCloud
import base64
from collections import Counter
import dash.dependencies as dd


# Helper function
def plot_wordcloud(data, query = "REAL"):
    data = data.sample(len(data))
    titles = list(data[data['label'] == query].head(201)['title'].values)
    # print(titles)
    words = []
    for title in titles:
        for d in title.split():
            words.append(d.lower())
    freq_words = Counter(words)
    # print(f"freq_words : {freq_words}")
    wc = WordCloud(background_color='black', width=1200, height=500)
    wc.fit_words(freq_words)
    return wc.to_image()




def init_dashboard(server):
    app = Dash(server = server,
                routes_pathname_prefix = "/dashboard/",
                external_stylesheets = [ext_styles],
                title = "DashBoard"
    )
    app._favicon = "./icon.ico"
    app.layout = base_template

    init_callbacks(app)

    return app.server



def init_callbacks(app):
    @app.callback(dd.Output('wordcloud', 'src'), dd.Input('wordcloud', 'id'), dd.Input('wc_query', 'value'))
    def make_image(b, query):
        print(f"query : {query}")
        img = BytesIO()
        plot_wordcloud(data=df, query=query).save(img, format='PNG')
        return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())
    
    @app.callback(dd.Output('distibution', 'figure'), dd.Input('distribution_query', 'value'))
    def distribution_selector(d_query = 'Pie Chart'):
        print(f"d_query : {d_query}")
        if (d_query == "Histogram"):
            return histogram
        return pie_chart
        