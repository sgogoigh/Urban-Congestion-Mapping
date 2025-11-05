import pandas as pd
import folium
from folium.plugins import HeatMap

df = pd.read_csv("synthetic_city_noise.csv")

hour_to_plot = 8                   
value_col = "TrafficIndex"        

sub = df[df["Hour"] == hour_to_plot]

heat_data = sub[["Latitude", "Longitude", value_col]].values.tolist()

# folium map based on location
m = folium.Map(
    location=[sub["Latitude"].mean(), sub["Longitude"].mean()],
    zoom_start=13,
    tiles="cartodbpositron"
)

HeatMap(heat_data, radius=12, blur=10, max_zoom=15).add_to(m)

m.save("heatmap_8AM.html")
