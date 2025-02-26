# importing the tkinter module
from tkinter import *

# Step 2 GUI Interaction
window = Tk()

#Step 3 Adding Input
var = StringVar()
ent_var = StringVar()

def insert():
    result = ent_var.get()
    var.set(result)

message = Message(window, textvariable = var, relief = RAISED, padx = 50, pady = 50)
entry = Entry(window, textvariable = ent_var)
button = Button(window, text = 'OK', command = insert)

message.pack()
entry.pack()
button.pack()

#Step 4 mainloop
mainloop()