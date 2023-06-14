import tempfile
import win32api
import win32print
import os

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.configure(background='lightblue')
#root.iconbitmap('E:/OneDrive/Research Ideas/Python/Intro-To-TKinter-Youtube-Course-master/codemy.ico')

# centre the window
w = 600#root.winfo_reqwidth()
h = 400#root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int((ws/2) - (w/2))
y = int((hs/2) - (h/2))
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def openfile():
	global filename
	root.filename = filedialog.askopenfilename(initialdir="E:/", title="Select A File", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
	my_label = Label(root, text=root.filename).pack()
	filename = root.filename
	os.startfile(filename)
	#my_image = ImageTk.PhotoImage(Image.open(root.filename))
	#my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=openfile, padx=50, pady=10).pack()

#filename = 'E:/print1.txt' ##tempfile.mktemp (".txt")
#open (filename, "w").write ("This is a test")
def opentextfile():
	os.system("C:/Program Files (x86)/Adobe/Acrobat Reader DC/Reader/AcroRd32.exe E:/print1.pdf") ##+ filename)
	#os.startfile(filename)	##open file using default system software(Word-*.docx, Notepad for *.txt, Acrobat reader for *.pdf)

def printfile():	
	win32api.ShellExecute (
  		0,
  		"printto",
  		filename,
  		'"%s"' % win32print.GetDefaultPrinter (),
  		".",
  		0
	)

myButton = Button(root, text="Press to Print", command=printfile).pack()
myQuitButton = Button(root, text="Exit Program", command=root.quit).pack()
myOpenButton = Button(root, text="Display file", command=opentextfile).pack()

root.mainloop()


