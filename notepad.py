from tkinter import*
from tkinter.messagebox import*
from tkinter.filedialog import asksaveasfile, askopenfile

FILE_NAME = NONE
def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', END)

def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name

    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

def save_file():
    data = text.get('1.0', END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Oops!", message="Unable to save file....")

def close_file():
    root.destroy()

def clear():
    text.delete(1.0, END)

def show_about():
    # второе окно (форма о программе)
    second = Tk()
    second.title('About')
    # this removes the maximize button
    second.resizable(0, 0)
    second.geometry('300x200')
    lb1 = Label(second, text="Это программа блокнот нужна для записей")
    lb2 = Label(second, text="Версия программы 1.0")
    bt1 = Button(second, text="Закрыть", command=lambda: second.destroy())
    lb1.pack()
    lb2.pack()
    bt1.pack()

def show_help():
    showinfo(title="Help", message="Данная справка вам не поможет")

root=Tk()
root.title('My note 1')

#Ограничиваем работу кнопки разворота окна
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

#Область для ввода текста
text = Text(root, font='Arial 20')
text.pack()
#Создать объект Меню на главном окне
menuBar =Menu(root)

#Создать пункт меню
fileMenu = Menu(menuBar)

#Пункт меню будет выпадающим
menuBar.add_cascade(label="File", menu=fileMenu)

#формируется список команд пункта меню
fileMenu.add_command(label = "New", command=new_file)
fileMenu.add_command(label = "Open...", command=open_file)
fileMenu.add_command(label="Save...", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)

#разделительная линия
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = close_file)

#Создаем второй выпадающий пункт меню
editMenu = Menu(menuBar)
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label = "Clear", command=clear)

#Создаем третий выпадающий пункт меню
helpMenu = Menu(menuBar)
menuBar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Help", command=show_help)
helpMenu.add_command(label="About", command=show_about)

#Закрепляем объект Меню на главном окне
root.config(menu=menuBar)

root.mainloop()    
 




    
