import numpy as np
import pandas as pd
import random

# choosing a focal point
city_center = (28.6139, 77.2090)

# 10x10 km bounding box around the center
lat_min, lat_max = city_center[0] - 0.045, city_center[0] + 0.045
lon_min, lon_max = city_center[1] - 0.045, city_center[1] + 0.045

# Generate 20 x 20 grid -> 400 points
n_points = 20
lats = np.linspace(lat_min, lat_max, n_points)
lons = np.linspace(lon_min, lon_max, n_points)
coordinates = [(lat, lon) for lat in lats for lon in lons]


zone_types = ['MainRoad', 'Residential', 'Industrial', 'Market', 'Park']
zone_distribution = [0.25, 0.35, 0.20, 0.15, 0.05]  # must sum to 1
base_noise = {
    'MainRoad': 80,
    'Residential': 55,
    'Industrial': 75,
    'Market': 70,
    'Park': 45
}
variance_noise = {
    'MainRoad': 10,
    'Residential': 5,
    'Industrial': 8,
    'Market': 6,
    'Park': 4
}

# Assign each coordinate a zone
zones = np.random.choice(zone_types, size=len(coordinates), p=zone_distribution)


def time_factor(hour, zone):
    """Return noise adjustment based on time and zone type."""
    if 0 <= hour <= 5:
        return {'MainRoad': -15, 'Residential': -5, 'Industrial': -10, 'Market': -10, 'Park': -5}[zone]
    elif 6 <= hour <= 9:
        return {'MainRoad': +10, 'Residential': +3, 'Industrial': +5, 'Market': +6, 'Park': 0}[zone]
    elif 10 <= hour <= 16:
        return {'MainRoad': 0, 'Residential': 0, 'Industrial': +3, 'Market': +2, 'Park': 0}[zone]
    elif 17 <= hour <= 20:
        return {'MainRoad': +12, 'Residential': +4, 'Industrial': +5, 'Market': +8, 'Park': 0}[zone]
    else:
        return {'MainRoad': -5, 'Residential': -3, 'Industrial': -4, 'Market': -2, 'Park': -2}[zone]

# generating data
records = []
for (lat, lon), zone in zip(coordinates, zones):
    for hour in range(24):
        base = base_noise[zone]
        tf = time_factor(hour, zone)
        noise = np.random.normal(base + tf, variance_noise[zone])
        noise = np.clip(noise, 35, 100)

        # Optional correlated variables
        traffic_index = np.clip((noise - 40) / 60, 0, 1) + np.random.normal(0, 0.05)
        traffic_index = np.clip(traffic_index, 0, 1)
        pm25 = np.clip(0.8 * noise + np.random.normal(0, 10), 20, 250)

        records.append({
            'Latitude': lat,
            'Longitude': lon,
            'ZoneType': zone,
            'Hour': hour,
            'Noise_dB': round(noise, 2),
            'TrafficIndex': round(traffic_index, 3),
            'PM2.5': round(pm25, 1)
        })

df = pd.DataFrame(records)

# validating dataset
print(df.head())
print("\nRows:", len(df))
print("\nNoise_dB range:", (df['Noise_dB'].min(), df['Noise_dB'].max()))
print("\nAverage Noise by Zone:")
print(df.groupby('ZoneType')['Noise_dB'].mean())

# saving to csv file
df.to_csv("synthetic_city_noise.csv", index=False)
