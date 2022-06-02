from tkinter import *
from random import*

num = randint(1, 100)
r = 100
l = 0
count = 0

def bolshe():
    global click
    click = ">"

def menshe():
    global click
    click = "<"

def ugadal():
    global click
    click = "="

def main():
    global num, r, l, click, count
    count += 1
    t3.config(text = str(count))
    if click == "=":
        t2.config(text = "Я угадал")
    else:
        if click == ">":
            l = num
            num = (r + l) // 2
        else:
            r = num
            num = (r + l) // 2
        t2.config(text = str(num))


win=Tk()
win.geometry("300x400")
win.title("Двоичный поиск")


t2 = Label(win, text=str(num), fg='violet')
t2.config(font=('Verdana', 25))
t2.pack()

go = Button(win, text = 'Дальше', width=10, height=1, command = main)
go.config(bg='green', fg='blue')
go.config(font=('Verdana', 25))
go.pack()

bolshe = Button(win, text = 'Больше', width=10, height=1, command = bolshe)
bolshe.config(bg='red', fg='blue')
bolshe.config(font=('Verdana', 25))
bolshe.pack()

menshe = Button(win, text = 'Меньше', width=10, height=1, command = menshe)
menshe.config(bg='orange', fg='blue')
menshe.config(font=('Verdana', 25))
menshe.pack()

win2 = Button(win, text = 'Угадал', width=10, height=1, command = ugadal)
win2.config(bg='violet', fg='yellow')
win2.config(font=('Verdana', 25))
win2.pack()

t3 = Label(win, text=str(count), fg='violet')
t3.config(font=('Verdana', 25))
t3.pack()

win.mainloop()
