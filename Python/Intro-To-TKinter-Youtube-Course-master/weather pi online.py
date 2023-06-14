#!/usr/bin/python3

from urllib.request import urlopen
import json

apikey="api_key_redacted" # get a key from https://developer.forecast.io/register
# Latitude & longitude - current values are central Basingstoke.
lati="21.045021"#"52.194504"
longi="105.800690"#"0.134708"

# Add units=si to get it in sensible ISO units not stupid Fahreneheit.
url="https://api.forecast.io/forecast/"+"5d9cb52a19b8b5f9e31edef7b882e8b6"+"/"+lati+","+longi+"?units=si"

meteo=urlopen(url).read()
meteo = meteo.decode('utf-8')
weather = json.loads(meteo)

print (weather['currently']['temperature']['humidity'])