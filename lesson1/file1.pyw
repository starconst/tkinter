import tkinter
root = tkinter.Tk()
from tkinter import*
root.geometry("250x150")
fr1 = Frame(root)
fr1.pack(side = TOP)
btn1 = Button(fr1, text = "button 1", width = 25, height = 5, bg = "red", fg = "black")
btn1.pack(side = "left")
btn2 = Button(fr1, text = "button 2", width = 25, height = 5, bg = "red", fg = "black")
btn2.pack(side = RIGHT, padx = 5)
root.mainloop()
