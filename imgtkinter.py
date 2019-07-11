from tkinter import *
root = Tk()

def swap():
    global lbl
    lbl.configure(image=imgobj)

imgobj = PhotoImage(file='cat.gif')

btn = Button(image=imgobj, command=swap)
btn.grid()

lbl = Label(text="please click on the image button")
lbl.grid()


mainloop()