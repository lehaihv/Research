from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('E:/OneDrive/Research Ideas/Python/Intro-To-TKinter-Youtube-Course-master/codemy.ico')


def openfile():
	global my_image
	root.filename = filedialog.askopenfilename(initialdir="/gui/images", title="Select A File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
	my_label = Label(root, text=root.filename).pack()
	#my_image = ImageTk.PhotoImage(Image.open(root.filename))
	#my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=openfile).pack()


root.mainloop()
