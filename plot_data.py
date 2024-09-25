"""
File Name: plot_data.py
Author: Carlos Vidal
Date Created: 2024-09-25
Last Modified: 2024-09-25
Version: 1.0
Description:
    Plot one data set, from a csv file.
"""

import pandas as pd
import plotly.express as px

# Sample data (you can replace this with your CSV data)
data = {
    "Date": ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01"],
    "Soil Moisture": [20, 30, 25, 35, 40]
}

# Create a DataFrame
df = pd.read_csv('csv_files/SM1.csv')
# df = pd.DataFrame(data)

# Create a line plot
fig = px.line(df, x="Date", y="SM1_10cm", title="Soil Moisture Over Time")

# Show the plot
fig.show()