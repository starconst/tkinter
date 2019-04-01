from tkinter import*
root = Tk()
root.title('Калькулятор')
root.geometry("270x230")

en = Entry(root, width = 42, justify = RIGHT)
en.grid(row = 0, rowspan = 2, columnspan = 5, pady = 10, padx = 7)

mc = Button(root, text = 'n!', width = 5, height = 1)
mc.grid(row = 2, column = 0, padx = 5)

mr = Button(root, text = '(', width = 5, height = 1)
mr.grid(row = 2, column = 1,padx = 5)

ms = Button(root, text = ')', width = 5, height = 1)
ms.grid(row = 2, column = 2,padx = 5)

pl = Button(root, text = 'M+', width = 5, height = 1)
pl.grid(row = 2, column = 3,padx = 5)

mini = Button(root, text = 'M-', width = 4, height = 1)
mini.grid(row = 2, column = 4, padx = 5)


s = Button(root, text = '←', width = 5, height = 1)
s.grid(row = 3, column = 0, padx = 5, pady = 5)

ce = Button(root, text = 'CE', width = 5, height = 1)
ce.grid(row = 3, column = 1)

c = Button(root, text = 'C', width = 5, height = 1)
c.grid(row = 3, column = 2)

pl_min = Button(root, text = '±', width = 5, height = 1)
pl_min.grid(row = 3, column = 3)

sqrt = Button(root, text = '√', width = 4, height = 1)
sqrt.grid(row = 3, column = 4)

b7 = Button(root, text = '7', width = 5, height = 1)
b7.grid(row = 4, column = 0)

b8 = Button(root, text = '8', width = 5, height = 1)
b8.grid(row = 4, column = 1)

b9 = Button(root, text = '9', width = 5, height = 1)
b9.grid(row = 4, column = 2)

sep = Button(root, text = '/', width = 5, height = 1)
sep.grid(row = 4, column = 3)

per = Button(root, text = '%', width = 4, height = 1)
per.grid(row = 4, column = 4)

b4 = Button(root, text = '4', width = 5, height = 1)
b4.grid(row = 5, column = 0)

b5 = Button(root, text = '5', width = 5, height = 1)
b5.grid(row = 5, column = 1)

b6 = Button(root, text = '6', width = 5, height = 1)
b6.grid(row = 5, column = 2)

mult = Button(root, text = '*', width = 5, height = 1)
mult.grid(row = 5, column = 3, padx = 5, pady = 5)

btn = Button(root, text = '1/x', width = 4, height = 1)
btn.grid(row = 5, column = 4)

b1 = Button(root, text = '1', width = 5, height = 1)
b1.grid(row = 6, column = 0)

b2 = Button(root, text = '2', width = 5, height = 1)
b2.grid(row = 6, column = 1)

b3 = Button(root, text = '3', width = 5, height = 1)
b3.grid(row = 6, column = 2)

minus = Button(root, text = '-', width = 5, height = 1)
minus.grid(row = 6, column = 3)

isn = Button(root, text = '=', width = 4, height = 3)
isn.grid( row = 6, column = 4,rowspan = 2)

b0 = Button(root, text = '0', width = 12, height = 1)
b0.grid(row = 7, column = 0, columnspan = 2)

k = Button(root, text = ',', width = 5, height = 1)
k.grid(row = 7, column = 2)

plusi = Button(root, text = '+', width = 5, height = 1)
plusi.grid(row = 7, column = 3, pady = 5,padx = 5)

root.mainloop()
