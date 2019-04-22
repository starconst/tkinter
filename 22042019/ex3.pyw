from tkinter import*
from random import *
root = Tk()
canv = Canvas(root,width=800,height=550, bg='white')
canv.pack()





for i in range(10):
    R = randint(10, 40)  # radius
    x = randint(R, 400 - R)
    y = randint(R, 400 - R)
    
    canv.create_oval(x-R, y-R, x+R, y+R, fill = "green")

root.mainloop()
