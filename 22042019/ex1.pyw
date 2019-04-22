from tkinter import*
from random import*
root = Tk()
canv = Canvas(root,width=800,height=550, bg='white')
canv.pack()
colors = ["green", "orange","yellow"]

color = choice(colors)
canv.create_oval(30,30,90,90, fill = color)
root.mainloop()
