import folium
import random

# Inicializa o mapa centralizado em uma coordenada específica
m = folium.Map(location=[28.6, 77.2], zoom_start=11)

# Loop para criar 20 marcadores aleatórios
for i in range(20):
    # Gera um valor aleatório para simular um sensor (entre 20 e 100)
    val = random.randint(20, 100)
    
    # Adiciona um marcador circular ao mapa
    folium.CircleMarker(
        location=[
            28.6 + random.uniform(-0.1, 0.1), 
            77.2 + random.uniform(-0.1, 0.1)
        ],
        radius=6,
        color="green" if val < 50 else "red",
        fill=True,
        popup=f"Sensor Value: {val}"
    ).add_to(m)

# Salva o mapa em um arquivo HTML
m.save("mapa_sensores.html")

print("Arquivo 'mapa_sensores.html' gerado com sucesso!")