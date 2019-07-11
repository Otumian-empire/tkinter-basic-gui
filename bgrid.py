from tkinter import Tk, Label, mainloop
from random import choice
root = Tk()

b = Label(text="I am using a grid here for the B label", width=70, height=10)
b.grid(row=3,column=3,padx=5, pady=5)
colors = ['black', 'white', 'green', 'red', 'yellow']

for i in range(4):
    for x in range(4):
        bgc = choice(colors)
        fgc = choice(colors)
        print(bgc, fgc, '**')

        if (bgc == fgc):
            bgc, fgc  = choice(colors), choice(colors)

        a = Label(text="I am using a grid here for the A label", fg=fgc, bg=bgc)
        a.grid(row=i,column=x,padx=i, pady=x)
        
        print(bgc, fgc)

mainloop()