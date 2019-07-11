from tkinter import *
root = Tk()

inputlabel = Label(text='enter your name: ')
entry = Entry()
name = entry.get()
outlabel = Label(text='Hello {}.. Nice to meet you '.format(name))

inputlabel.grid(row=0, column=0)
entry.grid(row=0, column=1)



mainloop()
