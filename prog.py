#python3
#Main program
from tkinter import *
import cards as C
import back as B

#Startting the window
window = Tk()
window.geometry("800x800")
window.title = "Magic Card Storage Program"

#code for the window
lbl = Label(window, text="hello")
lbl.grid(row=0, column=0)

window.mainloop()
