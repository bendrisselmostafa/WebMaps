import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lon = list(data["LON"])
lat = list(data["LAT"])

map = folium.Map(
    location=[33.57, -7.59],
    zoom_start=12,
    tiles="Stamen Terrain",
)

fg = folium.FeatureGroup(name="My map")

for lt, ln in zip(lat, lon):
    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup="Im a Volcano",
            icon=folium.Icon(color="green"),
        )
    )

map.add_child(fg)

map.save("Map.html")
