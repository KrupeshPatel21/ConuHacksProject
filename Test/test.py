import pandas as pd
import plotly.express as px

# Reads the dataset of "Acte Criminels"
dataset1 = pd.read_csv(r"C:\Users\chris\Downloads\ConuHacksProject\actes-criminels.csv", nrows=300)
dataset2 = pd.read_csv(r"C:\Users\chris\Downloads\ConuHacksProject\actes-criminels.csv", nrows=300)


# Ensure your dataset has latitude and longitude columns
# Replace 'latitude_column' and 'longitude_column' with your actual column names
latitude_column = 'LATITUDE'
longitude_column = 'LONGITUDE'

fig = px.scatter_geo(dataset1, lat=latitude_column, lon=longitude_column)
fig.show()

fig.write_html('dot_map.html')


# Use cases
# 1. Gather the crime type and display that crime type
# 


