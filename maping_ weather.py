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


map_ws = folium.Map(location=[0,0],zoom_start=2)

CWD = os.getcwd()

map_ws.save('wsmap1.html')
webbrowser.open_new('file://'+CWD+'/wsmap1.html')
