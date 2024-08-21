
import folium
from folium.plugins import Draw
map = folium.Map(location=[23.7808405,90.419689],zoom_start=10)

# Add drawing tools to the map
draw = Draw(
    draw_options={
        'polyline': False,
        'polygon': False,
        'circlemarker': False,
        'rectangle': True,  # Enable rectangle drawing
        'circle': True,      # Enable circle drawing
        'marker': False,
    },
    edit_options={
        'edit': True,
        'remove': True
    }
)
draw.add_to(map)

map.save('run.html')

