from cgitb import html
from itertools import count
from turtle import color, fillcolor
import folium
import pandas

#importing data frame
data=pandas.read_csv("COVIDDATA.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
num=list(data["ACTIVECASES"])

#creating a function for marker color based on number o cases
def color_producer(cases):
   if cases<10000:
       return 'lightgreen'
   elif 10000<= cases <100000:
        return 'green'
   elif 100000<= cases <200000:
        return 'orange'
   else:
        return 'red' 


html="""<h4>Covid Active Cases:</h4>"""

#creating a featuregroup
map=folium.Map(location=[11.94,79.88],zoom_start=6,tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="My Map")

#using for loop to send the data
for lt,ln,N in zip(lat, lon, num):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=10,popup=str(N),fill_color=color_producer(N),color='grey',fill_opacity=0.7))
#the marker design can be changed,search for in help

#calling child function
map.add_child(fg)
map.save("MapRandom.html")