from tkinter import Tk, Label, mainloop

root = Tk()

name = 'michael'
# creating a label
mylabel = Label(text="Hello world", font = ("Vernada", 16, 'roman'), fg='yellow', bg='blue')
mylabel.grid(row=100, column=100)

mylabel2 = Label(text='I am a boy')
mylabel2.grid(row=1, column=0)
mylabel2.configure(text='I love you, {}'.format(name))



mainloop()

