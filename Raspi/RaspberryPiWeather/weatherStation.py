# -*- coding: utf-8 -*-

from Tkinter import *
import Tkinter as tk
import Adafruit_DHT as dht
import threading
import tkFont
import ImageTk
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

temperatureLabel = Label(root, fg="white", background="#00dbde", textvariable=temperature, font=("Helvetica", 40,"bold"))
temperatureLabel.place(x=580, y=100)

humidityLabel = Label(root, fg="white", background="#00dbde", textvariable=humidity, font=("Helvetica", 40,"bold"))
humidityLabel.place(x=580, y=200)
 
root.attributes("-fullscreen",True)
root.bind("<1>",exit)

def exit():
	root.quit()

def readSensor():
	root.after(2000, readSensor)
        h,t = dht.read_retry(dht.DHT22,20)
        temp = "%.1f" %t
	temperature.set(temp+" °C")	
	hum = "%.1f" %h
	humidity.set(hum+"  %")
		
root.after(2000, readSensor)

root.mainloop()