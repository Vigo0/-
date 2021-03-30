from tkinter import *


def clicked():
    res = txt.get()
    lbl = Label(window, text=res)
    lbl.grid(column=100, row=100)


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
lbl = Label(window, text="Привет",font=("Arial ", 25),bg="black", fg="red")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Клик!",font=("Arial", 15),bg="pink", fg="blue", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
