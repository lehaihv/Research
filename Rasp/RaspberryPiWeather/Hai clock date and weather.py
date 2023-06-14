# -*- coding: utf-8 -*-

from tkinter import *
import tkinter as tk
import Adafruit_DHT as dht
import threading
import tkFont
import time
from PIL import ImageTk
#import ImageTk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.HIGH)

root = tk.Tk()

image = PhotoImage(file="background.gif")

background=Label(root, image=image)
background.place(x=0,y=0,relwidth=1, relheight=1)

temperature = StringVar()
temperature.set("----"+" °C")       

humidity = StringVar()
humidity.set("----"+" %")

timenow = StringVar()
timenow.set(time.strftime("%H:%M:%S"))

datenow = StringVar()
datenow.set(time.strftime("%m:%d:%Y"))

temperatureLabel = Label(root, fg="white", background="#00dbde", textvariable=temperature, font=("Helvetica", 30,"bold"))
temperatureLabel.place(x=20, y=80)

humidityLabel = Label(root, fg="white", background="#00dbde", textvariable=humidity, font=("Helvetica", 30,"bold"))
humidityLabel.place(x=290, y=80)

timeLabel = Label(root, fg="red", background="#00dbde", textvariable=timenow, font=("Helvetica", 40,"bold"))
timeLabel.place(x=120, y=180)

dateLabel = Label(root, fg="red", background="#00dbde", textvariable=datenow, font=("Helvetica", 20,"bold"))
dateLabel.place(x=320, y=10)

root.attributes("-fullscreen",True)
root.bind("<1>",exit)

def exit():
	root.quit()

def readSensor():
	root.after(2000, readSensor)
		#h,t = dht.read_retry(dht.DHT22,20)
	temp = str(30)#"%.1f" %t
	temperature.set(temp+" °C") 
	hum = str(65)#"%.1f" %h
	humidity.set(hum+" %")
	datenow.set(time.strftime("%d/%m/%Y"))

def show_time():
		timenow.set(time.strftime("%H:%M:%S"))
		root.after(1000, show_time)
		
root.after(1000, show_time)
root.after(2000, readSensor)

root.mainloop()