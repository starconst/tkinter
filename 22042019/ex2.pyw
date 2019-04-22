from tkinter import*
from random import *
root = Tk()
canv = Canvas(root,width=800,height=550, bg='white')
canv.pack()

colors = ["green", "orange","yellow"]

color = choice(colors)


R = randint(10, 40) 
x = randint(R, 400 - R)
y = randint(R, 400 - R)
canv.create_oval(x-R, y-R, x+R, y+R,fill=color)
                 

root.mainloop()
