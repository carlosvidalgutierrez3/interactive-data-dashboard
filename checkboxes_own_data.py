"""
File Name: checkboxes_own_data.py
Author: Plotly
Date Created: 2024-09-25
Last Modified: 2024-09-25
Version: 1.0
Description:
    Use checkboxes to toogle datasets, imported from a csv file.
"""

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Create the Dash app
app = Dash(__name__)

# Load your data from CSV
df = pd.read_csv('csv_files/life_exp_synthetic.csv')

# Define the app layout
app.layout = html.Div([
    html.H4('Your Data Visualization Title'),
    dcc.Graph(
        id="graph",
        style={'width': '80vw', 'height': '80vh'} 
        ),
    dcc.Checklist(
        id="checklist",
        options=[{'label': continent, 'value': continent} for continent in df['continent'].unique()],
        value=["Americas", "Oceania"],  # Default selected values
        inline=True
    ),
])

# Define the callback to update the graph based on the selected checklist values
@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))

def update_line_chart(continents):

    # Filter the data based on the selected continents
    mask = df['continent'].isin(continents)

    # Create a line plot using Plotly Express
    fig = px.line(df[mask], 
        x="year", y="lifeExp", color='country')
    
    # Set all traces to be hidden by default (legend only)
    for trace in fig.data:
        trace.visible = 'legendonly'
        
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
