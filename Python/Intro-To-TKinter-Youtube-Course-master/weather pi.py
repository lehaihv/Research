from requests import get
import json
from pprint import pprint
from haversine import haversine

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'
#url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/1648902'

my_lat = 52.194504
my_lon = 0.134708

all_stations = get(stations).json()['items']
#weather = get(url).json()['items']
#pprint(weather)


#21.045021, 105.800690