#python3
#Main program
from tkinter import *
from tkinter.ttk import Treeview
from back import *
from guiFunctions import *

#Declaration of functions
def donothing():
	x = 0

#Starting the tkinter app
app = Tk()
app.tk.call('wm', 'iconphoto', app._w, PhotoImage(file='assets/logo.png'))
app.geometry("800x800")
app.title("Magic The Gathering Storage Program")
app.resizable(0, 0)

db = Database()
current_deck = ""

#Declaring the frames
lall = Frame(app, height=800, width=800)
ldeck = Frame(app, height=800, width=800)

#positioning the frames
lall.grid(row=0, column=0, ipadx=0, ipady=0, sticky='news')
ldeck.grid(row=0, column=0, ipadx=0, ipady=0, sticky='news')

#populating the frames
create_deck_layout(app, ldeck, db)
create_layout_list_all(app, lall, db, current_deck)

#Implementing the navbar
menubar = Menu(app, font=10)
library = Menu(menubar, font=5, tearoff=0)
library.add_command(label="Add card", command=lambda:create_add_card_layout(app, db))
library.add_command(label="Remove card", command=lambda:remove_card_layout(app, db, {'values':''}))
library.add_command(label="Update card", command=lambda:update_card_layout(app, db, {'values':''}))
library.add_separator()
library.add_command(label="Search card", command=lambda:search_layout(app, db))
library.add_command(label="List all cards", command=lambda:create_layout_list_all(app, lall, db, current_deck))
deck = Menu(menubar, font=5, tearoff=0)
deck.add_command(label="Add Deck", command=lambda:add_deck_layout(app, db))
deck.add_command(label="Remove Deck", command=lambda:remove_deck_layout(app, db, {'values':''}))
deck.add_command(label="List Decks", command=lambda:create_deck_layout(app, ldeck, db))
helpmenu = Menu(menubar, font=5, tearoff=0)
helpmenu.add_command(label="about", command=donothing)

#adds menus to the menubar
menubar.add_cascade(label="Library", menu=library)
menubar.add_cascade(label="Deck", menu=deck)
menubar.add_cascade(label="Help", menu=helpmenu)

#Runs the mainloop of the app
app.config(menu=menubar)
app.mainloop()
