import folium

map = folium.Map(
    location=[33.57, -7.59],
    zoom_start=12,
    tiles="Stamen Terrain",
)

fg = folium.FeatureGroup(name="My map")

fg.add_child(
    folium.Marker(
        location=[33.60881457164729, -7.632757310367674],
        popup="Here Is Hassan II Mosque",
        icon=folium.Icon(color="green"),
    )
)

map.add_child(fg)

map.save("Map.html")
