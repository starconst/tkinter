from tkinter import*
from random import *
root = Tk()
canv = Canvas(root,width=800,height=550, bg='white')
canv.pack()

colors = ["green", "orange","yellow", "orange", "red"]

color = choice(colors)



for i in range(12):
    R = randint(10, 40)  # radius
    x = randint(R, 400 - R)
    y = randint(R, 400 - R)
    color = choice(colors)
    canv.create_oval(x-R, y-R, x+R, y+R, fill=color)

root.mainloop()
