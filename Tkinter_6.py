### Creating MENUS

#Step 1 Importing Module

from tkinter import *

#Step 2 GUI Interaction
window = Tk()

#Step 3 Adding Inputs

menu = Menu(window)
file = Menu(menu, tearoff = 0) # if tearoff = 1 - its become floating menu
file.add_command(label = 'New')
file.add_command(label = 'Open')
file.add_command(label = 'Save')
file.add_command(label = 'Save As')
file.add_separator()
file.add_command(label = 'Exit', command = window.quit)

menu.add_cascade(label = 'File', menu = file)
window.config(menu = menu)

#Step 5 Main loop

mainloop()
