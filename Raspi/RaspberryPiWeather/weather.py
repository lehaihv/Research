#!/usr/bin/python3

from urllib.request import urlopen
import json

apikey="5d9cb52a19b8b5f9e31edef7b882e8b6" # get a key from https://developer.forecast.io/register
# Latitude & longitude - current values are central Basingstoke.
#lati="51.2673665"
#longi="-1.0817624"
lati = "-37.721319"
longi = "145.048809"
# Add units=si to get it in sensible ISO units not stupid Fahreneheit.
url="https://api.forecast.io/forecast/"+apikey+"/"+lati+","+longi+"?units=si"

meteo=urlopen(url).read()
meteo = meteo.decode('utf-8')
weather = json.loads(meteo)

print (weather['currently'])