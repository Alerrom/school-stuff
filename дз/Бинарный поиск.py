from tkinter import *
from tkinter import messagebox as mb 

def start():
    global mid, left, right, n
    left = 0
    right = 1000
    n = 1
    if EntryA.get() == '':
        mb.showerror('Ошибка','Введите число меньше 1000')
    else:
        mid = (left + right)//2
        variant.configure(text = str(mid))
        kol.configure(text = str(n))

def bigger():
    global mid, left, right, n
    left = mid
    mid = (left + right)//2
    variant.configure(text = str(mid))
    n += 1
    kol.configure(text = str(n))

def less():
    global mid, left, right, n
    right = mid
    mid = (left + right)//2
    variant.configure(text = str(mid))
    n += 1
    kol.configure(text = str(n))

def stop():
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'gold'
    Label(a, text="Ура!  Ты победил!").pack(expand=1)

def help1():
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'gold'
    Label(a, text="Binary search").pack(expand=1)


def ster():
    EntryA.delete(0, END)
    variant.configure(text = '')
    kol.configure(text = '') 



win=Tk() 
win.title('Бинарный поиск')
win.geometry('450x440')

rows = 0
while rows < 11:
    win.rowconfigure(rows, weight=1)
    win.columnconfigure(rows, weight=1)
    rows += 1



l1 = Label(win, text = 'Введите задеманное число', font=('Verdana', 14, 'bold'))
l1.grid(row = 0, column = 0, columnspan = 2, sticky = W)

EntryA = Entry(win, width = 10, font = 'Arial 14', justify = 'center')
EntryA.grid(row = 0, column = 2, padx = 5, pady = 5)

start = Button(win, text = 'Запустить программу', width = 30, height = 3, command = start)
start.grid(row = 2, columnspan = 3)

l2 = Label(win, text = 'Это Ваше число?', font=('Verdana', 14, 'bold'))
l2.grid(row = 4, column = 0, columnspan = 2, sticky = W)

variant = Label(win, width = 10, font = 'Arial 14', justify = 'center')
variant.grid(row = 4, column = 2, padx = 5, pady = 5)

bigger = Button(win, text = 'Больше', width = 30, height = 3, command = bigger)
bigger.grid(row = 6, column = 0)

less = Button(win, text = 'Меньше', width = 30, height = 3, command = less)
less.grid(row = 6, column = 1)

stop = Button(win, text = 'Угадал', width = 30, height = 3, command = stop)
stop.grid(row = 6, column = 2)

l3 = Label(win, text = 'Колличество попыток', font=('Verdana', 14, 'bold'))
l3.grid(row = 7, column = 0, columnspan = 2, sticky = W)

kol = Label(win, width = 10, font = 'Arial 14', justify = 'center')
kol.grid(row = 7, column = 2, padx = 5, pady = 5)

help1 = Button(win, text = 'Об алгоритме', width = 30, height = 3, command = help1)
help1.grid(row = 10, column = 0, columnspan  = 2,sticky = W)

ster = Button(win, text = 'Стереть', width = 30, height = 3, command = ster)
ster.grid(row = 10, column = 2)
