import tkinter
root = tkinter.Tk()
from tkinter import*
root.geometry("300x350")
btn1 = Button(root, text = "button 1", width = 25, height = 5, bg = "red", fg = "black")
btn1.pack(side = "left")
btn2 = Button(root, text = "button 2", width = 25, height = 5, bg = "red", fg = "black")
btn2.pack(anchor = "ne")
root.mainloop()
