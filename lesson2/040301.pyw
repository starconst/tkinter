from  tkinter import*
root = Tk()
root.geometry("500x100")

btn1 = Button(root, text = "Button1")
btn1.grid(row = 0)
ent1 = Entry(root)

ent1.grid(row = 0, column = 2, sticky = W)

btn2 = Button(root,text = "Button2")
btn2.grid(row = 3, column = 0, pady = 10)

ent1 = Entry(root, width = 40)
ent1.grid(row = 3, column = 2, sticky = N, pady = 10)
