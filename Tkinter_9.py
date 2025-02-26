#Displaying a Message Box in the Windows
# importing the tkinter module
from tkinter import *

# Step 2 GUI Interaction
window = Tk()

# Step 3 Adding Inputs

window.geometry('500x500')
#message = Message(window, text = 'Python')

var = StringVar()
message = Message(window, textvariable = var, relief = RAISED, padx = 20, pady = 20)
var.set("Welcome")
message.pack()

#Step 4 mainloop
mainloop()