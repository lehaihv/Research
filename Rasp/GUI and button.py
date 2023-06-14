## Toggle an LED when the GUI button is pressed ##
## Read button press from GPIO input ##

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

### HARDWARE DEFINITIONS ###
led=LED(14)
butPin = 18

### Setup GPIO
GPIO.setup(butPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

### GUI DEFINITIONS ###
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


### Event Functions ###
def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"]="Turn LED on" # Change only the button text property
        #value = int(counters.get())
        #counters.set(value + 1)
    else:
        led.on()
        ledButton["text"]="Turn LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
def buttonPressed(channel):
    """This function should be called when butPin has a falling edge event"""
    #global var
    #print("Button was pressed")
    #var.set(var.get() + 1)
    value = int(counters.get())
    counters.set(value + 1)

"""Register the callback"""
GPIO.add_event_detect(butPin, GPIO.FALLING, callback=buttonPressed, bouncetime=300) # bouncetime: to eliminate the bouncing when read key press

### Variable
counters = IntVar()
counters.set(0)

### WIDGETS ###

# Button, triggers the connected command when it is pressed
ledButton = Button(win, text='Turn LED on', font=myFont, command=ledToggle, bg='bisque2', height=1, width=24)
ledButton.grid(row=0,column=2)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
exitButton.grid(row=1, column=2)

pressedLabel = Label(win, text='Press', height=1, width=10)
pressedLabel.grid(row=2, column=1)

pressedLabel = Label(win, textvariable=str(counters), height=1, width=6)
pressedLabel.grid(row=2, column=2)

pressedLabel = Label(win, text='times', height=1, width=10)
pressedLabel.grid(row=2, column=3)

#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4, row=3, sticky=W)


win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

win.mainloop() # Loops forever