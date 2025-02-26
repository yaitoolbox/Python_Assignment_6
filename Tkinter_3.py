#Step 1 Importing Module

from tkinter import *

#Step 2 Interacting GUI
window = Tk()

window.title('Simple')
window.geometry('250x50')

#Step3 Adding Inputs

label1 = Label(window, text = 'Mail')
label1.grid(row = 0, column = 1)
label2 =Label(window, text ='Password')
label2.grid(row = 1, column = 1)

e1 =Entry(window, width = 35, borderwidth = 5)
e2 =Entry(window, width = 35, borderwidth = 5)

e1.grid(row = 0, column = 2)
e2.grid(row = 1, column = 2)

#Step4 Mainloop
mainloop()