from tkinter import *
root = Tk()

x = 0

def increase():
    global x
    x += 1
    label.configure(text=x)

def decrease():
    global x
    x -= 1
    label.configure(text=x)


label = Label(text=x)
sendbutton = Button(text="increase", command=increase)
deletebutton = Button(text="decrease", command=decrease)

sendbutton.grid()
label.grid()
deletebutton.grid()

mainloop()