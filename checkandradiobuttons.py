from tkinter import *
root = Tk()

def color():
    global textc

    if checkc.get() == 1:
        fav = 'red'
    elif checkc.get() == 2:
        fav = 'yellow'
    else:
        fav = 'green'
    
    labelc.configure(text='{}{}'.format(textc, fav))

def married():
    global text
    if check.get() == 1:
        text = 'married'
    else:
        text = 'not married'

    label.configure(text=text)
    
text = 'marriage status'

check = IntVar()

checkbutton = Checkbutton(text='married', var=check, command=married)
checkbutton.grid(row=0, column=0)

label = Label(text="{}".format(text))
label.grid(row=1, column=0)
# ###############################


textc = 'your fav color is '

labelc = Label(text=textc)
labelc.grid(row=2, column=0)

checkc = IntVar()

redbtn = Radiobutton(text="red", var = checkc, value = 1, command=color)
redbtn.grid(row=3, column=0)

yellowbtn = Radiobutton(text="yellow", var = checkc, value = 2, command=color)
yellowbtn.grid(row=3, column=1)

greenbtn = Radiobutton(text="green", var = checkc,  value = 3, command=color)
greenbtn.grid(row=3, column=2)


mainloop()