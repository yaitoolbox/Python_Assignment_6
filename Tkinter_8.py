### Drawing Canvas

from tkinter import *

#Step 2 GUI Interaction

window = Tk()

# Step 3 Adding Inputs

c = Canvas(window, height = 500, width = 500)
c.pack()
c.create_line(0,0,500,500, width = 5, fill = 'green', dash = (3,3))
c.create_line(0,500,500,0, width = 5, fill = 'red', dash = (3,3))

#RECTANGLE

c.create_rectangle(150,125,450, 375, fill = 'cyan', outline = 'yellow', width = 5.5)

#Step 4 mainloop

mainloop()