"""
File Name: all_sm.py
Author: Carlos Vidal
Date Created: 2024-09-25
Last Modified: 2024-09-25
Version: 1.0
Description:
    Plot all datasets.
"""

import pandas as pd
import plotly.graph_objects as go

# Create DataFrames
# df_moisture_sm2 = pd.DataFrame(data_moisture_temp)
# df_rain = pd.DataFrame(data_rain)
df_moisture_sm1 = pd.read_csv('csv_files/SM1.csv')
df_moisture_sm2 = pd.read_csv('csv_files/SM2.csv')
df_moisture_sm3 = pd.read_csv('csv_files/SM3.csv')
df_moisture_sm4 = pd.read_csv('csv_files/SM4.csv')
df_moisture_sm5 = pd.read_csv('csv_files/SM5.csv')
df_rain = pd.read_csv('csv_files/rain.csv')

# Convert 'Date' columns to datetime
df_moisture_sm1["Date"] = pd.to_datetime(df_moisture_sm1["Date"])
df_moisture_sm2["Date"] = pd.to_datetime(df_moisture_sm2["Date"])
df_moisture_sm3["Date"] = pd.to_datetime(df_moisture_sm3["Date"])
df_moisture_sm4["Date"] = pd.to_datetime(df_moisture_sm4["Date"])
df_moisture_sm5["Date"] = pd.to_datetime(df_moisture_sm5["Date"])
df_rain["Date"] = pd.to_datetime(df_rain["Date"])

# Create figure
fig = go.Figure()

# SM1
# Add 10cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_sm1["Date"], 
    y=df_moisture_sm1["SM1_10cm"], 
    mode='lines', 
    name='SM1_10cm',
    line=dict(color='rgb(255,0,0)'),    # Bright red
    opacity=0.7,       # Adjust transparency if needed
    yaxis="y1"  # left axis
))

# Add 30cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_sm1["Date"], 
    y=df_moisture_sm1["SM1_30cm"], 
    mode='lines', 
    name='SM1_30cm',
    line=dict(color='rgb(200,0,0)'),    # Dark red
    yaxis="y1"  # left axis
))

# SM2
# Add 10cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_sm2["Date"], 
    y=df_moisture_sm2["SM2_10cm"], 
    mode='lines', 
    name='SM2_10cm',
    line=dict(color='rgb(0,120,0)'),    # Light green
    opacity=0.7,       # Adjust transparency if needed
    yaxis="y1"  # left axis
))

# Add 30cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_sm2["Date"], 
    y=df_moisture_sm2["SM2_30cm"], 
    mode='lines', 
    name='SM2_30cm',
    line=dict(color='rgb(0,70,0)'),     # Dark green
    yaxis="y1"  # left axis
))

# SM3
# Add 10cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_sm3["Date"], 
    y=df_moisture_sm3["SM3_10cm"], 
    mode='lines', 
    name='SM3_10cm',
    line=dict(color='rgb(60,40,0)'),    # Light brown
    opacity=0.7,       # Adjust transparency if needed
    yaxis="y1"  # left axis
))

# Add 30cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_sm3["Date"], 
    y=df_moisture_sm3["SM3_30cm"], 
    mode='lines', 
    name='SM3_30cm',
    line=dict(color='rgb(60,40,0)'),     # Dark brown
    yaxis="y1"  # left axis
))

# SM4
# Add 10cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_sm4["Date"], 
    y=df_moisture_sm4["SM4_10cm"], 
    mode='lines', 
    name='SM4_10cm',
    line=dict(color='rgb(130,0,130)'),     # Light purple
    opacity=0.7,       # Adjust transparency if needed
    yaxis="y1"  # left axis
))

# Add 30cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_sm4["Date"], 
    y=df_moisture_sm4["SM4_30cm"], 
    mode='lines', 
    name='SM4_30cm',
    line=dict(color='rgb(130,0,130)'),     # Dark purple
    yaxis="y1"  # left axis
))

# SM5
# Add 10cm as a line trace (4-hour intervals)       Commented out: No data (Ctrl K + Ctrl C)
# fig.add_trace(go.Scatter(
#     x=df_moisture_sm5["Date"], 
#     y=df_moisture_sm5["SM5_10cm"], 
#     mode='lines', 
#     name='SM5_10cm',
#     line=dict(color='rgb(170,50,0)'),     # Dark orange
#     yaxis="y1"  # left axis
# ))

# Add 30cm as a line trace (4-hour intervals)
fig.add_trace(go.Scatter(
    x=df_moisture_sm5["Date"], 
    y=df_moisture_sm5["SM5_30cm"], 
    mode='lines', 
    name='SM5_30cm',
    line=dict(color='rgb(240,90,0)'),     # Orange
    yaxis="y1"  # left axis
))

# Rain
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
    title="Soil Moisture and Rain Over Time",
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
