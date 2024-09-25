"""
File Name: sm_rain.py
Author: Carlos Vidal
Date Created: 2024-09-25
Last Modified: 2024-09-25
Version: 1.0
Description:
    Plot two (or more) data sets, from csv files.
"""

import pandas as pd
import plotly.graph_objects as go

# Sample Soil Moisture and Temperature data (4-hour intervals)
data_moisture_temp = {
    "Date": ["2024-01-01 00:00", "2024-01-01 04:00", "2024-01-01 08:00", "2024-01-01 12:00"],
    "Soil Moisture": [20, 30, 25, 35],
    "Temperature": [15, 18, 20, 22]
}

# Sample Rain data (10-minute intervals)
data_rain = {
    "Date": ["2024-01-01 00:00", "2024-01-01 00:10", "2024-01-01 00:20", "2024-01-01 00:30",
             "2024-01-01 00:40", "2024-01-01 00:50", "2024-01-01 01:00", "2024-01-01 01:10"],
    "Rain": [0, 1, 0, 2, 3, 0, 1, 2]
}

# Create DataFrames
# df_moisture_temp = pd.DataFrame(data_moisture_temp)
# df_rain = pd.DataFrame(data_rain)
df_moisture_temp = pd.read_csv('csv_files/SM1.csv')
df_rain = pd.read_csv('csv_files/rain.csv')

# Convert 'Date' columns to datetime
df_moisture_temp["Date"] = pd.to_datetime(df_moisture_temp["Date"])
df_rain["Date"] = pd.to_datetime(df_rain["Date"])

# Create figure
fig = go.Figure()

# Add 10cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_temp["Date"], 
    y=df_moisture_temp["SM1_10cm"], 
    mode='lines+markers', 
    name='10cm',
    line=dict(color='orange'),
    yaxis="y1"  # left axis
))

# Add 30cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_temp["Date"], 
    y=df_moisture_temp["SM1_30cm"], 
    mode='lines', 
    name='30cm',
    line=dict(color='brown'),
    yaxis="y1"  # left axis
))

# Add Rain as a line trace (10-minute intervals)
fig.add_trace(go.Bar(
    x=df_rain["Date"], 
    y=df_rain["Rain"],
    name='Rain',
    marker_color='blue',
    yaxis="y2",         # right axis
    opacity=0.99,       # Adjust transparency if needed
    width=14400000      # Adjust width in milliseconds (this is 14400000 ms = 4h minutes)
))

# Update layout with titles
fig.update_layout(
    title="10cm , 30cm, and Rain Over Time",
    xaxis_title="Date",

    yaxis=dict(
        title="Soil Moisture (%)",  # Left y-axis title
        titlefont=dict(color="blue"),
        tickfont=dict(color="blue"),
        gridcolor="lightgray"
    ),
    
    yaxis2=dict(
        title="Rain (mm)",  # Right y-axis title
        titlefont=dict(color="green"),
        tickfont=dict(color="green"),
        overlaying="y",     # Overlay the second y-axis with the first y-axis
        side="right",       # Display the second y-axis on the right
        showgrid=False      # Disable grid lines for the right y-axis
    ),

    legend_title="Variable",
    barmode='overlay',  # Overlay bars with the line traces

    # Set white background for the plot and the paper
    plot_bgcolor='white',  # Inside the plotting area
    paper_bgcolor='white' # Outside the plotting area
)

# Show plot
fig.show()
