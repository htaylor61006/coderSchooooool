from requests import get
import json
import folium
import os
import webbrowser
import html

url='https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
stations = get(url).json()

#print(stations)    


lons = []
for station in stations['items']:
    lons.append(station['weather_stn_long'])

lats = []
for station in stations['items']:
    lats.append(station['weather_stn_lat'])

wsnames = []
for station in stations['items']:
    wsnames.append(station['weather_stn_name'])


map_ws = folium.Map(location=[0,0],
                    tiles= 'Mapbox Control Room',
                    zoom_start=2,
                    zoom_control=False,
                    max_zoom= 10,
                    min_zoom=2,
                    max_native_zoom= 10,
                    no_touch= True)

map_ws.fit_bounds([[52.193636, -2.221575], [52.636878, -1.139759]])

CWD = os.getcwd()

for n in range(len(lons)):
    folium.Marker([lats[n],lons[n]],
                  popup=wsnames[n],
                  icon=folium.Icon(icon='cloud',
                                   color= 'purple')).add_to(map_ws)


map_ws.save('wsmap1.html')
webbrowser.open_new('file://'+CWD+'/wsmap1.html')

