from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
from  PIL import Image, ImageTk
import numpy as np

import os

# All functions
def donothing():
    print("HELLO WORLD")



def openfile():
    filename = askopenfilename(parent=root)
    img = ImageTk.PhotoImage(Image.open(filename))
    print(filename)
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    Image.show()


def savefile():
    filename = asksaveasfilename(parent=root)
    Image.save(filename)


def exitfile():
    root.destroy()

def Fourier():
    filename = askopenfilename(parent=root)
    img = Image.open(filename)
    fft = np.log(np.abs(np.fft.fftshift(np.fft.fft(img))))
    panel = Label(root, image = ImageTk.PhotoImage(fft))
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    Image.show()

root = Tk()
frame = Frame(root)
frame.pack()

# Menubars
menu = Menu(root)
root.config(menu=menu)

# The file menu
Filemenu = Menu(menu)
menu.add_cascade(label = "File", menu=Filemenu)    # A cascaded file menu.
Filemenu.add_command(label = "New...", command=donothing)
Filemenu.add_command(label = "Open...", command=openfile)
Filemenu.add_command(label = "Save", command=savefile)
Filemenu.add_separator()
Filemenu.add_command(label = "Exit", command=exitfile)


# The edit menu
Editmenu = Menu(menu)
menu.add_cascade(label = "Edit", menu=Editmenu)    # A cascaded file menu.
Editmenu.add_command(label = "Cut", command=donothing)
Editmenu.add_command(label = "Copy", command=donothing)
Editmenu.add_command(label = "Undo", command=donothing)
Editmenu.add_command(label = "Redo", command=donothing)

# The view menu
Viewmenu = Menu(menu)
menu.add_cascade(label = "View", menu=Viewmenu)    # A cascaded file menu.
Viewmenu.add_command(label = "Flat", command=donothing)
Viewmenu.add_command(label = "Bias", command=donothing)


# The arithemetic menu
Arithmenu = Menu(menu)
menu.add_cascade(label = "Arithmetic", menu=Arithmenu)    # A cascaded file menu.
Arithmenu.add_command(label = "Add", command=donothing)
Arithmenu.add_command(label = "Subtarct", command=donothing)
Arithmenu.add_command(label = "Multiplication", command=donothing)
Arithmenu.add_command(label = "Division", command=donothing)



# The Image menu
Imagemenu = Menu(menu)
menu.add_cascade(label = "Image", menu=Imagemenu)    # A cascaded file menu.
Imagemenu.add_command(label = "FFT", command=Fourier)
Imagemenu.add_command(label = "Spectrum", command=donothing)


bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)


root.mainloop()
