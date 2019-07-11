from tkinter import *

root = Tk()

# def fhexcolor(r, g, b):
#     return '#{:.2f}{:.2f}{:.2f}'.format(r/255, g/255, b/255)

# def hexcolor(r, g, b):
#     return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def phexcolor(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(int(r*2.55), int(g*2.55), int(b*2.55))

label = Label(text='michael', fg=phexcolor(80, 50, 34))
label.grid()

mainloop()