from tkinter import*

root = Tk()
root.geometry("500x100")

btn1 = Button(root, text = "button1")

btn1.grid(row = 0)

ent1 = Entry(root)

ent1.grid(row = 0, column = 1)

btn2 = Button(root, text = "button2",height = 2)
btn2.grid(row = 1,rowspan = 2)

ent1 = Entry(root)

ent1.grid(row = 1, column = 1)

