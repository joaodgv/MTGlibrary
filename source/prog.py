#python3
#Main program
from tkinter import *
import cards as cards
import back as db
import loop as loop

#Decleration of functions
def donothing():
	x = 0

#Starting the tkinter app
app = Tk()
app.geometry("800x800")
app.title = "Magic The Gathering Storage Program"
app.resizable(0, 0)
app.grid_propagate(False)

#Implementing the navbar
menubar = Menu(app, font=10)
library = Menu(menubar, font=5, tearoff=0)
library.add_command(label="add card", command=donothing)
library.add_command(label="remove card", command=donothing)
library.add_command(label="update card", command=donothing)
library.add_separator()
library.add_command(label="Search card", command=donothing)
deck = Menu(menubar, font=5, tearoff=0)
deck.add_command(label="add Deck", command=donothing)
deck.add_command(label="remove Deck", command=donothing)
deck.add_command(label="list Decks", command=donothing)
helpmenu = Menu(menubar, font=5, tearoff=0)
helpmenu.add_command(label="about", command=donothing)

#adds menus to the menubar
menubar.add_cascade(label="Library", menu=library)
menubar.add_cascade(label="Deck", menu=deck)
menubar.add_cascade(label="Help", menu=helpmenu)

#Initiating the windows
# every menu will have a corresponding frame'
# frame.tkraise()
home = Frame(app)
home.grid(row=1, column=0)

#Runs the mainloop of the app
app.config(menu=menubar)
home.tkraise()
app.mainloop()
