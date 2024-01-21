# This runs on dataset 1 to display the data solely on the crime acts.
# This displays three separate charts to demonstrates the data.

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load your datasets
dataset1 = pd.read_csv(r"C:\Users\chris\Downloads\ConuHacksProject\actes-criminels.csv", nrows=2141)  
dataset2 = pd.read_csv(r"C:\Users\chris\Downloads\ConuHacksProject\weatherstats_montreal_normal_daily.csv",nrows=31)  

# Create Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("Dashboard with Pie Chart, Histogram, and Scatter Plot"),

    # Dropdown for selecting dataset
    html.Label("Select Dataset:"),
    dcc.Dropdown(
        id='dataset-dropdown',
        options=[
            {'label': 'Dataset 1', 'value': 'dataset1'},
            {'label': 'Dataset 2', 'value': 'dataset2'},
        ],
        value='dataset1',
        multi=False
    ),

    # Pie chart
    dcc.Graph(id='pie-chart'),

    # Histogram
    dcc.Graph(id='histogram'),

    # Scatter plot
    dcc.Graph(id='scatter-plot'),
])

# Callback to update graphs based on dataset selection
@app.callback(
    [Output('pie-chart', 'figure'),
     Output('histogram', 'figure'),
     Output('scatter-plot', 'figure')],
    [Input('dataset-dropdown', 'value')]
)
def update_graphs(selected_dataset):
    if selected_dataset == 'dataset1':
        df = dataset1
    else:
        df = dataset2

    # Pie chart
    pie_chart = px.pie(df, names='CATEGORIE', title='Pie Chart')

    # Histogram
    histogram = px.histogram(df, x='CATEGORIE', title='Histogram')

    # Scatter plot
    scatter_plot = px.scatter(df, x='LONGITUDE', y='LATITUDE', title='Scatter Plot')

    return pie_chart, histogram, scatter_plot

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
