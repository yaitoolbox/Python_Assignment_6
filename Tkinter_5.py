
# CREATING BUTTONS AND giving a function to the button
#Step 1 Importing Module

from tkinter import *
#Step 2 Interacting GUI

window = Tk()

window.title('Simple')
window.geometry('500x500')
#Step 3 Adding Inputs

def log_entry():
    print('Logged In')

button1 = Button(window, text = 'Login', command = log_entry, width = 12, bg = 'red', fg='white', font ='bold', activebackground = 'black', activeforeground = 'white')
button1.pack()

#Step 4 Main Loop

mainloop()
