from tkinter import *


def send():
    sendbutton.configure(text='sent')

def delete():
    deletebutton.configure(text='deleted', bg='red', fg='yellow')

root = Tk()

sendbutton = Button(text="Send", command=send)
deletebutton = Button(text="Delete", command=delete)

sendbutton.grid()
deletebutton.grid()

mainloop()