from tkinter import *
root = Tk()


scaleobj = Scale(from_=0, to_=50,length=700, orient='vertical', label='My scale', showvalue='Yes', tickinterval=3)
scaleobj.grid()

mainloop()