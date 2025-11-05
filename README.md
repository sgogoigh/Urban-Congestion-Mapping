# Urban Congestion Mapping

This project visualizes **urban traffic congestion**, **noise pollution**, and **air quality (PM2.5)** across a city grid using **Folium** heatmaps.  
The dataset contains hourly readings for each coordinate on a 20×20 grid (400 points × 24 hours).

## Dataset Structure
Each row in the CSV represents a unique `(latitude, longitude, hour)` reading.

| Column        | Description                         |
|----------------|-------------------------------------|
| latitude       | Coordinate latitude                 |
| longitude      | Coordinate longitude                |
| zonetype       | Area type — residential/commercial/industrial |
| hour           | Hour of day (0–23)                 |
| noise_db       | Average noise level in decibels     |
| trafficindex   | Traffic congestion intensity         |
| pm2.5          | Air particulate concentration (µg/m³) |


## Features
- **Single-hour heatmap** — visualize congestion or pollution for a specific hour (e.g., 8 AM).  
- **24-hour timeline heatmap** — animated visualization showing temporal changes throughout the day.

## Requirements
Install dependencies:
```bash
pip install -r requirements.txt
```

## Execution

### To generate dataset
```bash
python dataset_generator.py
```

### To visualize one hour
```bash
python visualize_grid.py
```

### To visualize 24 hours
```bash
python visualize_24hr_grid.py
```
---

> Made by Sunny Gogoi & Advaith
> You can also skip this part by using your own dataset

