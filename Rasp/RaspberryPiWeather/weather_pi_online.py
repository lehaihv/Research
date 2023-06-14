#!/usr/bin/python3

from urllib.request import urlopen
import json
import datetime 
import time 

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('World Weather Forecast')
root.configure(background='lightblue')
root.iconbitmap('codemy.ico') #E:/

# centre the window
w = 600#root.winfo_reqwidth()
h = 400#root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int((ws/2) - (w/2))
y = int((hs/2) - (h/2))
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

location = StringVar()
location_date = StringVar()
location_temp = StringVar()
location_hum = StringVar()
location_press = StringVar()
city = 0
#cityname = ""

#apikey="5d9cb52a19b8b5f9e31edef7b882e8b6" # get a key from https://developer.forecast.io/register
# Latitude & longitude - current values are central Basingstoke.

#lati="21.045021"#"52.194504"
#longi="105.800690"#"0.134708"
def get_weather():
	global city
	global cityname
	global timenow
	global temp
	global hum, press, epochtime
	apikey = "5d9cb52a19b8b5f9e31edef7b882e8b6" # get a key from https://developer.forecast.io/register
	# Latitude & longitude - current values are central Basingstoke.
	if city == 0: 
		lati = "21.045021"#"52.194504"
		longi = "105.800690"#"0.134708"
		cityname = "Hanoi"
		city = 1
	elif city == 1:
		lati = "51.508089"
		longi = "-0.076208"
		cityname = "London"
		city = 2
	elif city == 2:
		lati = "38.894893"
		longi = "-77.036552"
		cityname = "Washington DC"
		city = 3
	elif city == 3:
		lati = "55.750446"
		longi = "37.617494"
		cityname = "Moscow"
		city = 4    
	else:
		lati = "-37.721319"
		longi = "145.048809"
		cityname = "La Trobe Uni"
		city = 0    
	#if city==1:    
		#lati = "52.194504"
		#longi = "0.134708"
		#city = 0
	#city = city + 1
	#lati="21.045021"#"52.194504"
	#longi="105.800690"#"0.134708"
	
	# Add units=si to get it in sensible ISO units not stupid Fahreneheit.
	url="https://api.forecast.io/forecast/"+apikey+"/"+lati+","+longi+"?units=si"

	meteo=urlopen(url).read()
	meteo = meteo.decode('utf-8')
	weather = json.loads(meteo)
	
	temp = weather['currently']['temperature']
	hum = weather['currently']['humidity']*100
	press = weather['currently']['pressure']
	epochtime = weather['currently']['time']
	#print(weather['currently'])
	a = ' \u2103' # degree celsius sign
	#time = datetime.datetime.utcfromtimestamp(epochtime).replace(tzinfo=datetime.timezone.utc)
	timenow = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epochtime)) #Replace time.localtime with time.gmtime for GMT time "%a, %d %b %Y %H:%M:%S +0000".	
	location.set(cityname)
	#location_date.set(timenow)
	location_temp.set(str(temp)+ a)
	location_hum.set(str(int(hum))+ " %")
	location_press.set(str(press)+ " mbar")

	root.after(5000, get_weather)

e = Entry(root, width=95, background='lightblue', borderwidth=0)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
place_label = Label(root, textvariable=location, background='lightblue', fg="red", borderwidth=5, font=("Arial Bold", 30))
place_label.grid(row = 1, column = 0, columnspan=3, padx=5, pady = 5)
#date_label = Label(root, textvariable=location_date, background='lightblue', borderwidth=5, font=("Arial Bold", 20))
#date_label.grid(row = 2, column = 0, columnspan=3, padx=5, pady = 5)
temp_label = Label(root, textvariable=location_temp, background='lightblue', borderwidth=5, font=("Arial Bold", 20))
temp_label.grid(row = 2, column = 0, columnspan=3, padx=5, pady = 5)
hum_label = Label(root, textvariable=location_hum, background='lightblue', borderwidth=5, font=("Arial Bold", 20))
hum_label.grid(row = 3, column = 0, columnspan=3, padx=5, pady = 5)
press_label = Label(root, textvariable=location_press, background='lightblue', borderwidth=5, font=("Arial Bold", 20))
press_label.grid(row = 4, column = 0, columnspan=3, padx=5, pady = 5)

root.after(5000, get_weather)

root.mainloop()
