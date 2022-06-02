from tkinter import *
from tkinter import messagebox as mb


def start_1():
    global middle, left, right, n
    left = 0
    right = 1000
    n = 1
    if EntryA.get() == '':
        mb.showerror('Ошибка', 'Введите искомое число')
    else:
        middle = (left + right) // 2
        variant.configure(text = str(middle))
        kol.configure(text = str(n))

def bigger_1():
    global middle, left, right, n
    left = middle
    middle = (left + right) // 2
    variant.configure(text = str(middle))
    n = n + 1
    kol.configure(text = str(n))    

def less_1():
    global middle, left, right, n
    right = middle
    middle = (left + right) // 2
    variant.configure(text = str(middle))
    n = n + 1
    kol.configure(text = str(n))    

def equals_1():
    global middle, left, right, n
    n = n + 1
    kol.configure(text = str(n))    

def clear_1():
    EntryA.delete(0, END)
    kol.configure(text = '')
    variant.configure(text = '')
 
def help_1():
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'grey'
    Label(a, text="Binary search").pack(expand=1)
    
win=Tk()
win.title("Бинарная угадайка")
win.geometry('450x440')

rows = 0
while rows < 11:
    win.rowconfigure(rows, weight=1)
    win.columnconfigure(rows, weight=1)
    rows += 1
    
l1 = Label(win, text = 'Введите задуманное число', font=('Verdana', 14, "bold"))
l1.grid(row = 0, column = 0, columnspan = 2, sticky = W)

EntryA = Entry(win, width = 10, font = 'Arial 14', justify = "center")
EntryA.grid(row = 0, column = 2, padx = 5, pady = 5)

start = Button(win, text = 'Запустить бинарный поиск', width=30, height=3, bg='sky blue', command = start_1)
start.grid(row = 2, columnspan = 3)

l2 = Label(win, text = 'Предлагаемый вариант:', font=('Verdana', 14, "bold"))
l2.grid(row = 4, column = 0, columnspan = 2, sticky = W)

variant = Label(win, font=('Verdana', 14, "bold"), fg = 'steel blue')
variant.grid(row = 4, column = 2, sticky = W)

bigger = Button(win, text = 'Больше', width=20, height=3, bg='cadet blue', command = bigger_1)
bigger.grid(row = 6, column = 0, sticky='NESW')

less = Button(win, text = 'Меньше', width=20, height=3, bg='cadet blue', command = less_1)
less.grid(row = 6, column = 1, sticky='NESW')

equals = Button(win, text = 'Угадал', width=20, height=3, bg='cadet blue', command = equals_1)
equals.grid(row = 6, column = 2, sticky='NESW')

l4 = Label(win, text = 'Количество попыток:', font=('Verdana', 14, "bold"))
l4.grid(row = 8, column = 0, columnspan = 2, sticky = W)

kol = Label(win, font=('Verdana', 14, "bold"), fg = 'steel blue')
kol.grid(row = 8, column = 2, sticky = W)

clear = Button(win, text = 'Очистить', width=20, height=3,  bg='light blue', command = clear_1)
clear.grid(row = 10, column = 2, sticky = W + E)

help = Button(win, text = 'Об алгоритме', width=20, height=3,  bg='light blue', command = help_1)
help.grid(row = 10, column = 0, columnspan = 2, sticky = W + E)


win.mainloop()
