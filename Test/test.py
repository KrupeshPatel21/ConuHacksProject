# This file is supposedly for implementing both datasets.
# However, this script does not offer any functionality.
# And can be used as a skeleton. 

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load your datasets
dataset1 = pd.read_csv(r"C:\Users\chris\Downloads\ConuHacksProject\actes-criminels.csv", nrows=2141) 
dataset2 = pd.read_csv(r"C:\Users\chris\Downloads\ConuHacksProject\weatherstats_montreal_normal_daily.csv",nrows=31)  

# Add a 'Dataset' column to identify the source dataset
dataset1['Dataset'] = 'Dataset 1'
dataset2['Dataset'] = 'Dataset 2'
dataset2['Dataset'] = 'Dataset 3'


# Combine both datasets
combined_dataset = pd.concat([dataset1, dataset2], ignore_index=True)

# Get unique categories, values, and dates from the combined dataset
# Need to add each value such as "Light Snow", "Heavy Snow", etc.
all_categories_dataset1 = dataset1['CATEGORIE'].unique()
all_values_dataset2 = dataset2['rain_s'].unique()
all_values_dataset3 = dataset2['snow_s'].unique()
all_values_dataset4 = dataset2['snow_on_ground_s'].unique()
all_dates = combined_dataset['Date'].unique()

# Create Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("Dashboard with Pie Charts and Scatter Plot"),

    # Dropdown for selecting category in dataset 1
    html.Label("Select Category (Dataset 1 - CATEGORIE):"),
    dcc.Dropdown(
        id='category-dataset1-dropdown',
        options=[{'label': category, 'value': category} for category in all_categories_dataset1],
        value=all_categories_dataset1[0],  # Default to the first category
        multi=False
    ),

    # Dropdown for selecting value in dataset 2
    html.Label("Select Value (Dataset 2 - Weather):"),
    dcc.Dropdown(
        id='value-dataset2-dropdown',
        options=[{'label': value, 'value': value} for value in all_values_dataset2],
        value=all_values_dataset2[0],  # Default to the first value
        multi=False
    ),

    # Dropdown for selecting date
    html.Label("Select Date:"),
    dcc.Dropdown(
        id='date-dropdown',
        options=[{'label': date, 'value': date} for date in all_dates],
        value=all_dates[0],  # Default to the first date
        multi=False
    ),

    # Pie chart for Dataset 1
    dcc.Graph(id='pie-chart-dataset1'),

    # Pie chart for Dataset 2
    dcc.Graph(id='pie-chart-dataset2'),

    # Scatter plot
    dcc.Graph(id='scatter-plot'),
])

# Callback to update pie chart for Dataset 1
@app.callback(
    Output('pie-chart-dataset1', 'figure'),
    [Input('category-dataset1-dropdown', 'value'),
     Input('date-dropdown', 'value')]
)
def update_pie_chart_dataset1(selected_category, selected_date):
    filtered_df = dataset1[(dataset1['CATEGORIE'] == selected_category) & (dataset1['Date'] == selected_date)]

    pie_chart = px.pie(filtered_df, names='CATEGORIE', title=f'Pie Chart (Dataset 1) - Category: {selected_category}, Date: {selected_date}')
    return pie_chart

# Callback to update pie chart for Dataset 2
@app.callback(
    Output('pie-chart-dataset2', 'figure'),
    [Input('value-dataset2-dropdown', 'value'),
     Input('date-dropdown', 'value')]
)
def update_pie_chart_dataset2(selected_value, selected_date):
    filtered_df = dataset2[(dataset2['rain_s','snow_s','snow_on_ground_s'] == selected_value) & (dataset2['Date'] == selected_date)]

    pie_chart = px.pie(filtered_df, names='Weather', title=f'Pie Chart (Dataset 2) - Value: {selected_value}, Date: {selected_date}')
    return pie_chart

# Callback to update scatter plot
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('category-dataset1-dropdown', 'value'),
     Input('value-dataset2-dropdown', 'value'),
     Input('date-dropdown', 'value')]
)
def update_scatter_plot(selected_category, selected_value, selected_date):
    filtered_df_dataset1 = dataset1[(dataset1['CATEGORIE'] == selected_category) & (dataset1['Date'] == selected_date)]
    filtered_df_dataset2 = dataset2[(dataset2['Weather'] == selected_value) & (dataset2['Date'] == selected_date)]

    scatter_plot = px.scatter(
        x=filtered_df_dataset1['X'], y=filtered_df_dataset1['Y'],
        color=filtered_df_dataset1['CATEGORIE'], labels={'color': 'Category'},
        title=f'Scatter Plot - Category: {selected_category}, Value: {selected_value}, Date: {selected_date}'
    )

    scatter_plot.add_trace(
        px.scatter(
            x=filtered_df_dataset2['X'], y=filtered_df_dataset2['Y'],
            color=filtered_df_dataset2['Weather'], labels={'color': 'Weather'}
        ).data[0]
    )

    return scatter_plot

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)









