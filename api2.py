import folium
from geopy.distance import geodesic

def calculate_path_length(coords):
    total_distance = 0
    for i in range(len(coords) - 1):
        total_distance += geodesic(coords[i], coords[i + 1]).meters
    return total_distance

def display_path_on_map(coords):
    path_map = folium.Map(location=coords[0], zoom_start=12)
    folium.PolyLine(coords, color="blue", weight=2.5, opacity=1).add_to(path_map)

    # Средняя точка
    middle_index = len(coords) // 2
    middle_point = coords[middle_index]
    folium.Marker(location=middle_point, popup="Средняя точка").add_to(path_map)

    path_map.save("path_map.html")
    print("Карта пути создана: path_map.html")

coords = [(55.715551, 37.554191), (55.818015, 37.440262), (55.791540, 37.559809)]
display_path_on_map(coords)
print(f"Общая длина пути: {calculate_path_length(coords):.2f} м")
