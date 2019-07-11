from tkinter import *
from random import choice
root = Tk()

color = ['red', 'yellow', 'green']

label1 = Label(text='What is your name? ', bg=choice(color))
label2 = Label(text='Where do you come from? ', bg=choice(color))
label3 = Label(text='what do you do? ', bg=choice(color))

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
mainloop()