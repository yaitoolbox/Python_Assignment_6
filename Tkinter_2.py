# Step 1 import tkinter - For GUI
from tkinter import *

# Step 2 GUI interaction

window = Tk()


#Step 3 Adding Inputs

window.title('Simple') #Title
window.geometry('500x700')#Dimension
window.config(bg = 'yellow') #Background colour

#frame1 = Frame(window, bg = 'red', width = 300, height = 300, cursor = 'dot')
#frame2 = Frame(window, bg ='green', width = 300, height = 300, cursor ='dotbox')

frame1 = Frame(window, width = 300, height = 300, cursor = 'dot')
frame2 = Frame(window, width = 300, height = 300, cursor ='dotbox')

button1 = Button(frame1, text = 'Button1', bg = 'blue')
button2 = Button(frame2, text ="Button2", bg ='green')
button3 = Button(frame1, text ='Logged', fg ='Red')

frame1.pack(side = TOP)
frame2.pack(side = BOTTOM)
button1.pack()
button2.pack()
button3.pack()




#Step4 : Main Loop

mainloop()

