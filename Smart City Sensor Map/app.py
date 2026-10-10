import folium
import random

# Servidor de mapas da Esri (ArcGIS) - Gratuito, rápido e não bloqueia scripts[cite: 5]
esri_tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}'
esri_attr = 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'

# Coordenadas do Rio de Janeiro[cite: 5]
m = folium.Map(
    location=[-22.9068, -43.1729], 
    zoom_start=11, 
    tiles=esri_tiles, 
    attr=esri_attr
)

# Adiciona os marcadores espalhados ao redor do Rio de Janeiro[cite: 5]
for i in range(20):
    val = random.randint(20, 100)
    folium.CircleMarker(
        location=[-22.9068 + random.uniform(-0.1, 0.1), -43.1729 + random.uniform(-0.1, 0.1)],
        radius=6,
        color="green" if val < 50 else "red",
        fill=True,
        popup=f"Sensor Value: {val}"
    ).add_to(m)

# Salva o mapa definitivo centralizado no Rio de Janeiro[cite: 5]
m.save("mapa.html")
