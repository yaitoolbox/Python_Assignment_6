#Step 1 Importing Module
from tkinter import *

#Step2 Interacting GUI
window = Tk()

window.title('Simple')
window.geometry('500x500')

#Adding Inputs
label1 = Label(window, text = 'Label-1', bg ='red', fg = 'white')
label1.pack(side = TOP, fill = X, expand = False)

label2 = Label(window, text = 'Label-2', bg ='blue', fg = 'white')
label2.pack(side = LEFT, fill = Y, expand = False)

label3 =Label(window, text = 'Label-3', bg = 'green', fg = 'white')
label3.pack(side = RIGHT, fill = Y, expand = False)

#Step 4 Mainloop

mainloop()