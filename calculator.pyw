from tkinter import*
import math
root = Tk()
root.title('Калькулятор')
root.geometry("270x230")

def sorry():
    en.delete(0,END)
    en.insert(END, "Извините, временно не работает")

def clean1():
    en.delete(0,END)
def clean2():
    n=en.get()
    en.delete(len(n)-1)

ce = Button(root, text = 'CE', width = 5, height = 1, command = clean1)
ce.grid(row = 3, column = 1)

c = Button(root, text = 'C', width = 5, height = 1, command = clean2)
c.grid(row = 3, column = 2)

en = Entry(root, width = 42, justify = RIGHT)
en.grid(row = 0, rowspan = 2, columnspan = 5, pady = 10, padx = 7)
###
def factorial():
    f1 = int(en.get())
    f2 =  1
    for i in range(1,f1+1):
        f2*=i
    en.delete(0,END)
    en.insert(0,f2)
    

fact = Button(root, text = 'n!', width = 5, height = 1,command = factorial)
fact.grid(row = 2, column = 0, padx = 5)

###


s1 = Button(root, text = '(', width = 5, height = 1, command = lambda:number_button("("))
s1.grid(row = 2, column = 1,padx = 5)

s2 = Button(root, text = ')', width = 5, height = 1, command = lambda:number_button(")"))
s2.grid(row = 2, column = 2,padx = 5)



    
    
pl = Button(root, text = '^', width = 5, height = 1, command = sorry)
pl.grid(row = 2, column = 3,padx = 5)

###
mini = Button(root, text = 'M-', width = 4, height = 1, command = sorry)
mini.grid(row = 2, column = 4, padx = 5)
###

s = Button(root, text = '←', width = 5, height = 1, command = sorry)
s.grid(row = 3, column = 0, padx = 5, pady = 5)

###


pl_min = Button(root, text = '±', width = 5, height = 1,command = sorry)
pl_min.grid(row = 3, column = 3)
def sqrt():
    sc = int(en.get())
    sc = math.sqrt(sc)
    en.delete(0,END)
    en.insert(0,sc)
sqrt = Button(root, text = '√', width = 4, height = 1, command = sqrt)
sqrt.grid(row = 3, column = 4)

def number_button(num):
    en.insert(END, str(num))
b7 = Button(root, text = '7', width = 5, height = 1, command = lambda:number_button(7))
b7.grid(row = 4, column = 0)

b8 = Button(root, text = '8', width = 5, height = 1, command = lambda:number_button(8))
b8.grid(row = 4, column = 1)

b9 = Button(root, text = '9', width = 5, height = 1, command = lambda:number_button(9))
b9.grid(row = 4, column = 2)

sep = Button(root, text = '/', width = 5, height = 1, command = lambda: number_button("/"))
sep.grid(row = 4, column = 3)

per = Button(root, text = '%', width = 4, height = 1, command = sorry)
per.grid(row = 4, column = 4)

b4 = Button(root, text = '4', width = 5, height = 1, command = lambda:number_button(4))
b4.grid(row = 5, column = 0)

b5 = Button(root, text = '5', width = 5, height = 1, command = lambda:number_button(5))
b5.grid(row = 5, column = 1)

b6 = Button(root, text = '6', width = 5, height = 1, command = lambda:number_button(6))
b6.grid(row = 5, column = 2)

mult = Button(root, text = '*', width = 5, height = 1, command = lambda: number_button("*"))
mult.grid(row = 5, column = 3, padx = 5, pady = 5)

btn = Button(root, text = '1/x', width = 4, height = 1, command = sorry)
btn.grid(row = 5, column = 4)

b1 = Button(root, text = '1', width = 5, height = 1, command = lambda:number_button(1))
b1.grid(row = 6, column = 0)

b2 = Button(root, text = '2', width = 5, height = 1, command = lambda:number_button(2))
b2.grid(row = 6, column = 1)

b3 = Button(root, text = '3', width = 5, height = 1, command = lambda:number_button(3))
b3.grid(row = 6, column = 2)

minus = Button(root, text = '-', width = 5, height = 1, command = lambda: number_button("-"))
minus.grid(row = 6, column = 3)
def isny():
    dd = en.get()
    if dd[0] and dd[1] == "0":
        en.delete(0,END)
        en.insert(0,"error")
    else:
        try:
            result = eval(dd)
            en.delete(0,END)
            en.insert(0,result)
        except Exception:
             en.delete(0,END)
             en.insert(0, "Error")

isn = Button(root, text = '=', width = 4, height = 3, command = isny)
isn.grid( row = 6, column = 4,rowspan = 2)

b0 = Button(root, text = '0', width = 12, height = 1, command = lambda:number_button(0))
b0.grid(row = 7, column = 0, columnspan = 2)

k = Button(root, text = ',', width = 5, height = 1)
k.grid(row = 7, column = 2)

plusi = Button(root, text = '+', width = 5, height = 1, command = lambda: number_button("+"))
plusi.grid(row = 7, column = 3, pady = 5,padx = 5)

root.mainloop()
