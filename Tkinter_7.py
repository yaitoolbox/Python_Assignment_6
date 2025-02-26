### MESSAGE BOX

#Step 1 Importing Module and Message Box

from tkinter import *
import tkinter.messagebox

#Step 2 GUI Interaction
window = Tk()


#Step 3 Adding INPUTS

tkinter.messagebox.showinfo('Info', 'Running out time')
tkinter.messagebox.showwarning('Info', 'Running out time')
tkinter.messagebox.showerror('Info', 'Running out time')
question = tkinter.messagebox.askyesno('Weather', 'Will it rain')

if question == True:
    print('Take an Umbrella')
else:
    print('Okay')

#Step 4 Mainloop

mainloop()
