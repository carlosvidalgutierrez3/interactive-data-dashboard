"""
File Name: checkboxes.py
Author: Carlos Vidal
Date Created: 2024-09-25
Last Modified: 2024-09-26
Version: 1.6.1
Description:
    Use checkboxes to toogle datasets.

Changes:
- Add logo
"""

from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

# Create the Dash app
app = Dash(__name__)

# Load combined data from CSV
# CSV format: Date, Value, Type, sensor_id
# df = pd.read_csv('csv_files/combined_data.csv')
rain_df = pd.read_csv('csv_files/private/rain.csv')
Pessl_p1_df = pd.read_csv('csv_files/private/P1.csv')
Pessl_px_df = pd.read_csv('csv_files/private/PX.csv')
SM_df = pd.read_csv('csv_files/private/SM.csv')

# List of colors
color_sm = ['rgb(200,0,0)','rgb(0,200,0)','rgb(0,0,255)','rgb(127,127,0)','rgb(127,0,127)']
color_p1 = ['rgb(0,51,0)','rgb(0,102,0)','rgb(0,153,0)','rgb(0,204,0)','rgb(0,255,0)','rgb(51,255,51)','rgb(102,255,102)','rgb(153,255,153)','rgb(204,255,204)']
color_px = ['rgb(0,127,127)','rgb(0,0,0)','rgb(102,0,204)']

# Define the app layout
app.layout = html.Div([
    # html.H4('Soil Moisture and Rain Data v1.6.1'),
    
    # Header Section with logo
    html.Div(
        children=[
            html.Img(
                src="/assets/logo.png",  # Ensure this path is correct and matches your file name
                style={
                    'height': '60px',  # Set the height of the logo
                    'margin': '0 auto',  # Center the logo horizontally
                    'display': 'block',  # Ensure it behaves like a block element
                }
            ),
        ],
        style={
            'background-color': '#38ccfc',  # Set your desired color
            'padding': '10px',  # Add padding to make it look good
            'text-align': 'center',  # Center the content inside the header
            'width': '100%',  # Full width
            'position': 'relative',  # Position it relative to the page
            'top': 0,  # Keep it at the top
            'left': 0,  # Align it to the left
            'z-index': '1000',  # Make sure it's on top
            'margin-bottom': '20px',  # Add space between the header and the graph
        }
    ),
    dcc.Graph(
        id="graph",
        style={'width': '80vw', 'height': '80vh'}
    ),
    dcc.Checklist(
        id="checklist",
        options=[
            {'label': 'Show SM', 'value': 'SM'},
            {'label': 'Show Pessl', 'value': 'Pessl'}
            #{'label': 'Show Rain Data', 'value': 'rain'}
        ],
        value=[],  # Start with no data displayed
        inline=True
    )
])

# Define the callback to update the graph based on the selected checklist values
@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value")
)
def update_chart(selected_groups):
    fig = go.Figure()

    # Add SM data (lines)
    if 'SM' in selected_groups:
        # Color list position
        i = 0
        for sensor_id in SM_df['sensor_id'].unique():
            sensor_data = SM_df[SM_df['sensor_id'] == sensor_id]

            # Add 10cm
            fig.add_trace(
                go.Scatter(
                    x=sensor_data['Date'],
                    y=sensor_data['10cm'],
                    mode='lines',
                    name=f'10cm {sensor_id}',
                    yaxis='y1',
                    visible='legendonly',  # Default visibility set to legendonly
                    line=dict(color=color_sm[i]),
                    opacity=0.5
                )
            )

            # Add 30cm
            fig.add_trace(
                go.Scatter(
                    x=sensor_data['Date'],
                    y=sensor_data['30cm'],
                    mode='lines',
                    name=f'30cm {sensor_id}',
                    yaxis='y1',
                    visible='legendonly',  # Default visibility set to legendonly
                    line=dict(color=color_sm[i])
                )
            )

            # Next color in the list
            i = i+1

    # Add Pessl data (lines)
    if 'Pessl' in selected_groups:
        
        # Add P1 (9 depths) data
        for i in range(10, 91, 10):          
            fig.add_trace(
                go.Scatter(
                    x=Pessl_p1_df['Date'],
                    y=Pessl_p1_df[f'{i}cm'],
                    mode='lines',
                    name=f'{i}cm P1',
                    yaxis='y1',
                    visible='legendonly',  # Default visibility set to legendonly
                    line=dict(color=color_p1[int(i/10) - 1])
                )
            )
        
        # Color list position
        i = 0
        
        # Add all other Pessl sensors at 10cm
        for sensor_id in Pessl_px_df['sensor_id'].unique():
            sensor_data = Pessl_px_df[Pessl_px_df['sensor_id'] == sensor_id]
            fig.add_trace(
                go.Scatter(
                    x=sensor_data['Date'],
                    y=sensor_data['10cm'],
                    mode='lines',
                    name=f'10cm {sensor_id}',
                    yaxis='y1',
                    line=dict(color=color_px[i]),
                    visible='legendonly'  # Default visibility set to legendonly
                )
            )
            
            # Next color in the list
            i = i+1

    # Add Rain data (bars)
    #if 'rain' in selected_groups:
    # rain_df = df[df['Type'] == 'Rain']
    for sensor_id in rain_df['sensor_id'].unique():
        sensor_data = rain_df[rain_df['sensor_id'] == sensor_id]
        fig.add_trace(
            go.Bar(
                x=sensor_data['Date'],
                y=sensor_data['Value'],
                name=f'Rain {sensor_id}',
                yaxis='y2',
                marker_color='blue',
                opacity=0.6,
                width=14400000      # Adjust width in milliseconds (this is 14400000 ms = 4h minutes)
            )
        )

    # Update layout for dual y-axes
    fig.update_layout(
        yaxis=dict(
            title='VWC (%)',
            showgrid=True,
        ),
        yaxis2=dict(
            title='Rain (mm/10min)',
            overlaying='y',
            side='right',
            showgrid=False
        ),
        xaxis=dict(title='Date'),
        legend=dict(title='Select Data'),
        margin=dict(l=40, r=40, t=40, b=40),
    )

    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
