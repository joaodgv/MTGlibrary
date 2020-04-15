#python3
#Main program
from tkinter import *
from tkinter.ttk import Treeview
from back import *

#Declaration of functions
def changeFrame(frame):
	frame.tkraise()

def donothing():
	x = 0

def create_layout_list_all(lall, db):
	#-----------------------------------------------------------------
	#				Creating the List all page
	#------------------------------------------------------------------
	tree = Treeview(lall, show="tree headings", height=34)
	tree["columns"]=("name", "color", "cost", "number", "type", "decks")
	tree.column("#0", width=0, stretch=NO)
	tree.column("name", width=80, stretch=NO)
	tree.column("color",width=80, stretch=NO)
	tree.column("cost",width=80, stretch=NO)
	tree.column("number",width=80, stretch=NO)
	tree.column("type",width=80, stretch=NO)
	tree.column("decks",width=150, stretch=NO)
	tree.heading("name", text="name")
	tree.heading("color", text="color")
	tree.heading("cost", text="cost")
	tree.heading("number", text="number")
	tree.heading("type", text="type")
	tree.heading("decks", text="decks")
	tree.grid(row=0, column=0, rowspan=4, padx=30, pady=30)
	b1 = Button(lall, text="Add Card",  bg="lightgrey", width=13, height=5)
	b1.grid(row=0, column=2, padx=10)
	b2 = Button(lall, text="Remove Card", bg="lightgrey", width=13, height=5)
	b2.grid(row=1, column=2, padx=10)
	b3 = Button(lall, text="Update card", bg="lightgrey", width=13, height=5)
	b3.grid(row=2, column=2, padx=10)
	b4 = Button(lall, text="Add to Deck", bg="lightgrey", width=13, height=5)
	b4.grid(row=3, column=2, padx=10)
	label = Label(lall, text="Current Selected deck: {}".format(current_deck))
	label.grid(row=4, column=0)

	cards = db.get_all_cards()
	for i in cards:
		decks = ""
		for j in i["deck"]:
			if(j):
				decks = "{}|{}".format(decks, j)

		tree.insert("", END, values=(i["name"], i["color"], i["cost"], i["number"], i["type"], decks))


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

#positioning the frames
lall.pack(fill = BOTH, ipadx=0, ipady=0)

#populating the frames
create_layout_list_all(lall, db)

#Implementing the navbar
menubar = Menu(app, font=10)
library = Menu(menubar, font=5, tearoff=0)
library.add_command(label="Add card", command=lambda:changeFrame(add))
library.add_command(label="Remove card", command=donothing)
library.add_command(label="Update card", command=donothing)
library.add_separator()
library.add_command(label="Search card", command=donothing)
library.add_command(label="List all cards", command=donothing)
deck = Menu(menubar, font=5, tearoff=0)
deck.add_command(label="Add Deck", command=donothing)
deck.add_command(label="Remove Deck", command=donothing)
deck.add_command(label="List Decks", command=donothing)
helpmenu = Menu(menubar, font=5, tearoff=0)
helpmenu.add_command(label="about", command=donothing)

#adds menus to the menubar
menubar.add_cascade(label="Library", menu=library)
menubar.add_cascade(label="Deck", menu=deck)
menubar.add_cascade(label="Help", menu=helpmenu)

#Runs the mainloop of the app
app.config(menu=menubar)
changeFrame(lall)
app.mainloop()
