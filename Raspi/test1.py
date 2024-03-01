from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO
import time

# Pin Definitions
pwmPin = 18
ledPin = 23
butPin = 17

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        value2 = float(counter.get())
        counter.set(value2 + 1.5)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()
counter = DoubleVar()
#counter.set(0)

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

ttk.Label(mainframe, text="Button pressed").grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=str(counter)).grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, text="times").grid(column=3, row=3, sticky=(W, E))


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
