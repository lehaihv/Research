from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('E:/OneDrive/Research Ideas/Python/Intro-To-TKinter-Youtube-Course-master/codemy.ico')

# centre the window
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int((ws/2) - (w/2))
y = int((hs/2) - (h/2))

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def show():
	myLabel = Label(root, text=clicked.get()).pack()

options = [
	"Monday", 
	"Tuesday", 
	"Wednesday", 
	"Thursday", 
	"Friday",
	"Saturday"
]	

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()

