from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

# Create the Dash app
app = Dash(__name__)

# Load combined data from CSV
# CSV format: Date, Value, Type, sensor_id
df = pd.read_csv('csv_files/combined_data.csv')

# Define the app layout
app.layout = html.Div([
    html.H4('Soil Moisture and Rain Data'),
    dcc.Graph(
        id="graph",
        style={'width': '80vw', 'height': '80vh'}
    ),
    dcc.Checklist(
        id="checklist",
        options=[
            {'label': 'Show Soil Data', 'value': 'soil'},
            {'label': 'Show Rain Data', 'value': 'rain'}
        ],
        value=[],  # Start with no data displayed
        inline=True
    ),
])

# Define the callback to update the graph based on the selected checklist values
@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value")
)
def update_chart(selected_groups):
    fig = go.Figure()

    # Add Soil Moisture data (lines)
    if 'soil' in selected_groups:
        soil_df = df[df['Type'] == 'Soil Moisture']
        for sensor_id in soil_df['sensor_id'].unique():
            sensor_data = soil_df[soil_df['sensor_id'] == sensor_id]
            fig.add_trace(
                go.Scatter(
                    x=sensor_data['Date'],
                    y=sensor_data['Value'],
                    mode='lines',
                    name=f'Soil Moisture {sensor_id}',
                    yaxis='y1'
                )
            )

    # Add Rain data (bars)
    if 'rain' in selected_groups:
        rain_df = df[df['Type'] == 'Rain']
        for sensor_id in rain_df['sensor_id'].unique():
            sensor_data = rain_df[rain_df['sensor_id'] == sensor_id]
            fig.add_trace(
                go.Bar(
                    x=sensor_data['Date'],
                    y=sensor_data['Value'],
                    name=f'Rain {sensor_id}',
                    yaxis='y2',
                    opacity=0.6
                )
            )

    # Update layout for dual y-axes
    fig.update_layout(
        yaxis=dict(
            title='Soil Moisture',
            showgrid=True,
        ),
        yaxis2=dict(
            title='Rain',
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
