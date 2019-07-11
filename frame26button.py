from tkinter import *
root = Tk()

alphabets = 'abcdefghijklmnopqrstuvwxyz'
frame = Frame()
for i in range(26):
    btn = Button(frame, text=alphabets[i])
    btn.grid(row=0, column=i)

okbtn = Button(text='OK')
okbtn.grid(row=1)
frame.grid(row=0, column=0)
mainloop()