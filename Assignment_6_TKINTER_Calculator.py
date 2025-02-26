#step 1 - Importing the mddule

from tkinter import *

#Step 2 - GUI Interaction [Graphic User Interface]

window = Tk()
window.geometry('500x500') #Height and width should be specified inside the quotes

#Step 3 - Adding Inputs

# Creating the ENTRY BOX

e = Entry(window, width = 56, borderwidth = 5) #Entry box width and borderwidth store in variable 'e'
e.place(x = 0, y = 0)

#Creating Buttons
def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0, str(result) + str(num))


b = Button(window, text = '1', width = 12, command = lambda:click(1))
b.place(x = 10, y =60)

b = Button(window, text = '2', width = 12, command = lambda:click(2))
b.place(x = 80, y =60)

b = Button(window, text = '3', width = 12, command = lambda:click(3))
b.place(x = 170, y =60)

b = Button(window, text = '4', width = 12, command = lambda:click(4))
b.place(x = 10, y =120)

b = Button(window, text = '5', width = 12, command = lambda:click(5))
b.place(x = 80, y =120)

b = Button(window, text = '6', width = 12, command = lambda:click(6))
b.place(x = 170, y =120)

b = Button(window, text = '7', width = 12, command = lambda:click(7))
b.place(x = 10, y =180)

b = Button(window, text = '8', width = 12, command = lambda:click(8))
b.place(x = 80, y =180)

b = Button(window, text = '9', width = 12, command = lambda:click(9))
b.place(x = 170, y =180)

b = Button(window, text = '0', width = 12, command = lambda:click(0))
b.place(x = 10, y =240)

# OPerators

#Addition
def add():
    n1 = e.get()
    global math
    math = 'addition'
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window, text = '+', width = 12, command = add)
b.place(x = 80, y =240)

#Subtraction
def sub():
    n1 = e.get()
    global math
    math = 'subtract'
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = '-', width = 12, command = sub)
b.place(x = 170, y =240)

#Multiplication
def mult():
    n1 = e.get()
    global math
    math = 'multiply'
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = '*', width = 12, command = mult)
b.place(x = 10, y =300)

#Division

def div():
    n1 = e.get()
    global math
    math = 'division'

    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = '/', width = 12, command = div)
b.place(x = 80, y =300)

#Equal to

def equal():
    n2 = e.get()
    e.delete(0,END)

    if math == 'addition':
        e.insert(0, i + int(n2))
    elif math == 'subtract':
        e.insert(0,i - int(n2))
    elif math == 'multiply':
        e.insert(0, i * int(n2))
    elif math == 'division':
        e.insert(0, i / int(n2))



b = Button(window, text = '=', width = 12, command = equal)
b.place(x = 170, y =300)

#CLEAR
def clear():
    e.delete(0, END)

b = Button(window, text = 'Clear', width = 12, command = clear)
b.place(x = 10, y =350)


#Step 4 - Mainloop
mainloop()

