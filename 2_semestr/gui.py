from tkinter import *
import random


x=int(random.randint(0, 5))
print("введите факториал {}".format(x))

def factorial(x):
    if x == 1:
        return x
    else:
        return x*factorial(x-1)

n=str(factorial(x))



def sravn():
    g = txt.get()
    if n==g :
        lbl = Label(window, text="Верно")
        lbl.grid(column=25, row=30)
    else:
        lbl = Label(window, text="Неверно")
        lbl.grid(column=25, row=30)


window = Tk()
window.title("Проверка знаний")
window.geometry('800x500')
lbl = Label(window, text="Введите значение факториала для {}".format(x))
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Ввести", command=sravn)
btn.grid(column=2, row=0)




window.mainloop()
