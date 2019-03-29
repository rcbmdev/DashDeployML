# -*- coding: utf-8 -*-
## imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import os

## Importing the dataset
DATA_DIR = 'data'
FILE_NAME = 'diamonds.csv'
data_path = os.path.join(DATA_DIR, FILE_NAME)
diamonds = pd.read_csv(data_path)

## Creating the app
app = dash.Dash(__name__)

# Creating a Plotly figure
trace = go.Histogram(
        x = diamonds['price']
        )

layout = go.Layout(
        title = 'Preços de Diamantes',
        xaxis = dict(title='Price'),
        yaxis = dict(title='Count')
        )

figure = go.Figure(
        data = [trace],
        layout = layout
        )

app.layout = html.Div([
        html.H1('Histograma de Preços de Diamante', style={'text-align': 'center'}),
        dcc.Graph(id='my-histogram', figure=figure)
        ])
        
      
if __name__ == '__main__':
    app.run_server(debug=True, port=8040) 
        