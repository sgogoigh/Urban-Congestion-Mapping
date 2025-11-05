import pandas as pd
import folium
from folium.plugins import HeatMapWithTime

df = pd.read_csv("synthetic_city_noise.csv")
value_col = "TrafficIndex"

data, index_hours = [], []
for hour, g in df.groupby("Hour"):
    data.append(g[["Latitude", "Longitude", value_col]].values.tolist())
    index_hours.append(f"{hour}:00")

# Create map centered on city
m = folium.Map(
    location=[df["Latitude"].mean(), df["Longitude"].mean()],
    zoom_start=13,
    tiles="cartodbpositron"
)

# Temporal heatmap
HeatMapWithTime(
    data,
    index=index_hours,
    auto_play=False,
    max_opacity=0.8,
    radius=10
).add_to(m)

m.save("heatmap_24h.html")
