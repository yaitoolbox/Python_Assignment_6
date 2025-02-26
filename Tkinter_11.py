## CREATING CHECKBOX

from tkinter import *

window = Tk()

window.geometry('500x500')

check_box_1 = IntVar()
check_box_2 = IntVar()
check_box_3 = IntVar()

chk_btn_1 = Checkbutton(window, text = 'Apple', onvalue = 1, offvalue = 0, height = 2, width = 10)
chk_btn_2 = Checkbutton(window, text = 'Banana', onvalue = 1, offvalue = 0, height = 2, width = 10)
chk_btn_3 = Checkbutton(window, text = 'Plum', onvalue = 1, offvalue = 0, height = 2, width = 10)

chk_btn_1.pack()
chk_btn_2.pack()
chk_btn_3.pack()

mainloop()