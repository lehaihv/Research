# Copyright (c) 2017 Adafruit Industries
# Author: Tony DiCola & James DeVito
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from tkinter import *
import time

from urllib.request import urlopen
import json
import datetime 
import time 

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

root = Tk()
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int((ws/2) - (w/2))
y = int((hs/2) - (h/2))
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#timenow = StringVar()
#timenow.set(time.strftime("%H:%M:%S"))

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
city = 0
# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Alternatively you can specify an explicit I2C bus number, for example
# with the 128x32 display you would use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_bus=2)

# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Alternatively you can specify a software SPI implementation by providing
# digital GPIO pin numbers for all the required display pins.  For example
# on a Raspberry Pi with the 128x32 display you might use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, sclk=18, din=25, cs=22)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
#Bfont = ImageFont.load_default()
font = ImageFont.truetype('Retro Gaming.ttf', 13)
# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

def myClick():
    #global hello
    hello = "Hello " + e.get() + "   " # 
    myLabel = Label(root, text=hello)
    myLabel.pack()
    e.delete(0,END)
    # Clear display.
    disp.clear()
    #disp.display()
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,top+16), outline=0, fill=0)
    # Display image.
    draw.text((x, top), hello, font=font, fill=255)
    disp.image(image)
    disp.display()
    #time.sleep(.05)

def weatherupdate():
    global city
    global cityname
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

    print (weather['currently'])
    print ("**********************************")
    temp = weather['currently']['temperature']
    hum = weather['currently']['humidity']
    press = weather['currently']['pressure']
    epochtime = weather['currently']['time']

    a = ' \u2103' # degree celsius sign
    #time = datetime.datetime.utcfromtimestamp(epochtime).replace(tzinfo=datetime.timezone.utc)
    timecur = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epochtime)) #"%a, %d %b %Y %H:%M:%S"Replace time.localtime with time.gmtime for GMT time "%a, %d %b %Y %H:%M:%S +0000".
    print ("Time: "+str(timecur))
    print ("Temp: "+str(temp)+ a)
    print ("Hum : "+str(hum*100)+" %")
    print ("Pres: "+str(press)+" mbar")
    disp.clear()
    #disp.display()
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,top+15), outline=0, fill=0)
    draw.rectangle((0,top+33,width,height), outline=0, fill=0)
    # Display image.
    draw.text((x, top), cityname+"  ", font=font, fill=255)
    #font = ImageFont.truetype('Retro Gaming.ttf', 16)
    #timecurshort = timecur[0:7:1] + " "+timecur[17:]
    #draw.text((x, top+16), timecurshort+"   ", font=font, fill=255)
    draw.text((x, top+33), "Temp: "+str(temp)+" C  ", font=font, fill=255)
    draw.text((x, top+50), "Hum  : "+str(hum*100)+" %  ", font=font, fill=255)
    #draw.text((x, top+52), "Pres: "+str(press)+" mbar  ", font=font, fill=255)
    
    disp.image(image)
    disp.display()

def show_time():
    timesys = time.strftime("%H:%M:%S") #"%d/%m/%Y %H:%M:%S")# for date and time
    disp.clear()
    #disp.display()
    # Draw a black filled box to clear the image.
    draw.rectangle((0,top+16,width,top+32), outline=0, fill=0)
    # Display image.
    draw.text((x, top+16), "Time : "+str(timesys)+"  ", font=font, fill=255)
    
    disp.image(image)
    disp.display()
    root.after(1000, show_time)
        

e = Entry(root, width=50)
e.pack()

myButton = Button(root, text="Enter Your Full Name", command=myClick)
myButton.pack()
myweatherButton = Button(root, text="Update current weather", command=weatherupdate)
myweatherButton.pack()

root.after(1000, show_time)
root.mainloop()



