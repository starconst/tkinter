import tkinter
root = tkinter.Tk()
from tkinter import*
root.geometry("200x100")
fr1 = Frame(root)
fr1.pack(side = TOP, fill = BOTH)
fr2 = Frame(root)
fr2.pack(side = BOTTOM,fill = BOTH)

btn1 = Button(fr1, text = "button 1", width = 5, height =1, bg = "red", fg = "black")
btn1.pack(side = "left")
btn2 = Button(fr1, text = "button 2", width = 5, height = 1, bg = "red", fg = "black")
btn2.pack(side = "right")
btn3 = Button(fr2, text = "button 3", width = 5, height =1, bg = "red", fg = "black")
btn3.pack(side = "left")
btn4 = Button(fr2, text = "button 4", width = 5, height = 1, bg = "red", fg = "black")
btn4.pack(side = "right")

root.mainloop()
