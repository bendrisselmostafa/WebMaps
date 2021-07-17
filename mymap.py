import folium
import pandas


def color_pop(pop):
    if pop < 100000000:
        return "green"
    elif pop < 200000000 and pop > 100000000:
        return "orange"
    return "red"


def color_marker(elev):
    if elev < 1000:
        return "green"
    elif elev > 1000 and elev < 2000:
        return "orange"
    return "red"


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            radius=6,
            color=color_marker(el),
            fill_opacity=0.7,
            fill=True,
            popup=folium.Popup(iframe),
        )
    )

fg.add_child(
    folium.GeoJson(
        data=(open("world.json", "r", encoding="utf-8-sig").read()),
        style_function=lambda x: {"fillColor": color_pop(x["properties"]["POP2005"])},
    )
)

map.add_child(fg)
map.save("Map.html")
