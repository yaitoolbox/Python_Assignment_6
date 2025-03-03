
from tkinter import *

window = Tk()
window.geometry('500x500')

e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

b = Button(window, text='1', width=12, command=lambda: click(1))
b.place(x=10, y=60)
b = Button(window, text='2', width=12, command=lambda: click(2))
b.place(x=80, y=60)
b = Button(window, text='3', width=12, command=lambda: click(3))
b.place(x=170, y=60)
b = Button(window, text='4', width=12, command=lambda: click(4))
b.place(x=10, y=120)
b = Button(window, text='5', width=12, command=lambda: click(5))
b.place(x=80, y=120)
b = Button(window, text='6', width=12, command=lambda: click(6))
b.place(x=170, y=120)
b = Button(window, text='7', width=12, command=lambda: click(7))
b.place(x=10, y=180)
b = Button(window, text='8', width=12, command=lambda: click(8))
b.place(x=80, y=180)
b = Button(window, text='9', width=12, command=lambda: click(9))
b.place(x=170, y=180)
b = Button(window, text='0', width=12, command=lambda: click(0))
b.place(x=10, y=240)

def operate(operation):
    try:
        n1 = float(e.get())
        global math, i, operation_pending, previous_math
        math = operation
        if 'operation_pending' in globals() and operation_pending:
            i = perform_operation(i, n1, previous_math)
        else:
            i = n1
        e.delete(0, END)
        operation_pending = True
        previous_math = math
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")

def perform_operation(num1, num2, op):
    if op == 'addition':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'division':
        if num2 == 0:
            raise ZeroDivisionError
        else:
            return num1 / num2
    else:
        return num1

def add():
    operate('addition')

def sub():
    operate('subtract')

def mult():
    operate('multiply')

def div():
    operate('division')

def equal():
    try:
        n2 = float(e.get())
        e.delete(0, END)
        global i, math, operation_pending
        if 'operation_pending' in globals() and operation_pending:
            i = perform_operation(i, n2, math)
        else:
            i = n2
        e.insert(0, i)
        if 'operation_pending' in globals():
            del operation_pending
    except (ValueError, NameError, ZeroDivisionError):
        e.delete(0, END)
        e.insert(0, "Error")

b = Button(window, text='+', width=12, command=add)
b.place(x=80, y=240)
b = Button(window, text='-', width=12, command=sub)
b.place(x=170, y=240)
b = Button(window, text='*', width=12, command=mult)
b.place(x=10, y=300)
b = Button(window, text='/', width=12, command=div)
b.place(x=80, y=300)
b = Button(window, text='=', width=12, command=equal)
b.place(x=170, y=300)

def clear():
    e.delete(0, END)
    if 'operation_pending' in globals():
        del operation_pending
    if 'previous_math' in globals():
        del previous_math

b = Button(window, text='Clear', width=12, command=clear)
b.place(x=10, y=350)

mainloop()