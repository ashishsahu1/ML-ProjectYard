import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
import numpy as np
import dash_table


# Reading labels for word2vec model
labels_word2vec = []
with open("FlaskApp//utils//labels_word2vec.txt", "r") as f:
  for line in f:
    labels_word2vec.append(str(line.strip()))

# Loading words2vec model output
wordProjections = np.load("FlaskApp//utils//word2vec.npy")

# Defining our external stylesheet for our app
ext_styles = dbc.themes.BOOTSTRAP

# Logo for navbar
PLOTLY_LOGO = "assets//icon.ico"

# reading the DataFrame
df = pd.read_csv("FlaskApp//utils//Dataset//data.csv")

# Max length of output
def maxLen(data, col):
    if col == "title":
        return data[:51] + "..."
    elif col == "text":
        return data[:201] + "..."
    return data

# Function for showing data table
def generate_table(dataframe, max_rows=10):
    dataframe = dataframe.sample(max_rows)
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(maxLen(dataframe.iloc[i][col], col)) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# Styling CSS
colors = {
    'background': '#ffcccc',
    'text': 'black'
}


# Building navbar
navBar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="https://detectfakenews1412.herokuapp.com/")),
        dbc.NavItem(dbc.NavLink("DashBoard",
                href="https://detectfakenews1412.herokuapp.com/dashboard")),
        dbc.NavItem(dbc.NavLink(
            "Guide", href="https://detectfakenews1412.herokuapp.com/guide")),
    ],
    color="dark",
    dark=True,
)


# Building Scatter plot
x = []
y = []
z = []
for value in wordProjections:
    x.append(value[0])
    y.append(value[1])
    z.append(value[2])


scatter_plot = px.scatter_3d(
    wordProjections, x=0, y=1, z=2,
    color = labels_word2vec,
    hover_name = labels_word2vec,
    labels = {'color': ''}        
)

scatter_plot.update_layout(
    plot_bgcolor="black",
    paper_bgcolor="black",
    font_color="#666699",
    height=800,
)


# Building Histogram
histogram = px.histogram(   
    df,
    x = 'label',
    color = 'label'
)

histogram.update_layout(
    plot_bgcolor="black",
    paper_bgcolor="black",
    font_color="blue",
)

# Building PieChart
pie_chart = px.pie(
    df,
    # values = "label",
    names = "label"
)

pie_chart.update_layout(
    plot_bgcolor="black",
    paper_bgcolor="black",
    font_color="blue",
)


# Display dataframe
dataTable = dbc.Container(
    fluid = True,
    children=[
        html.H2("Sample Dataset"),
        dcc.Markdown(children = "Showing five random data samples...", style = {'marginTop' : '10px'}),
        dbc.Table.from_dataframe(
                    df.sample(5),
                    bordered=True,
                    dark=True,
                    hover=True,
                    responsive=True,
                    striped=True
            )
    ], style= {'marginTop' : '30px'}
    
)

# Word Embedding
wordEmbedding = dbc.Container(children=[
        html.H2("Word Embeddings", style={"marginBottom" : "10px"}),
        dcc.Graph(  
            id = "scatter_plot",
            figure = scatter_plot
        ),
    ], fluid= True, style={'marginTop' : '30px'})


# This is out base template
base_template=html.Div([

    # NavBar
    navBar,

    # Word Embedding
    wordEmbedding,


    # Two SideBySide divs for showing 'Label distribution' and 'wordCloud'
    dbc.Row([    
        
        # Label Distribution
        dbc.Col([  
            html.H2("Distribution of Data", style={"marginBottom" : "10px"}),
            dcc.Dropdown(   
                id = "distribution_query",
                options = [{'label' : i, 'value' : i} for i in ["Pie Chart", "Histogram"]],
                value = 'Pie Chart',
            ),
           dcc.Graph(
                id = "distibution",
            )], style={'marginTop' : '40px'},
            # className = "container-fluid", 
            # style={
            #     'display': 'inline-block',                  
            #     'padding' : '20px', 
            #     'marginTop' : "30px", 
            #     'width' : '50%',                
            #     "backgroundColor": "#ffcccc",
            #     "textAlign" : "center"
            # }
            ),

        # WordCloud
        dbc.Col([  
            html.H2("WordCloud", style={"marginBottom" : "10px"}),            
            dcc.Dropdown(   
                id = "wc_query",
                options = [{'label' : i, 'value' : i} for i in ["FAKE", "REAL"]],
                value = 'REAL'
                ),
            dcc.Markdown("This will show you a word cloud from random words of your choice ...😉"),
            dbc.CardImg(id="wordcloud", style={'width' : '100%', 'marginTop' : '5px'}, className = "lg")
        ], style={'marginTop' : '40px'},
        # className = "containerFluid", 
        #     style={
        #         'display': 'inline-block', 
        #         'padding' : '20px', 
        #         'marginTop' : "30px", 
        #         'width' : '50%',
        #         'height': '100%',
        #         "backgroundColor": "#ffcccc"
            # }
            ),
        ]),

        dataTable

], style = {"backgroundColor": "white", "textAlign" : "center"})
