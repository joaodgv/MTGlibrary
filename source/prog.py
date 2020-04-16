#python3
#Main program
from tkinter import *
from tkinter.ttk import Treeview
from back import *
import dbmanager

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
	b1 = Button(lall, text="Add Card",  bg="lightgrey", width=13, height=5, command=lambda:create_add_card_layout())
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

def create_deck_layout(ldeck, db):
	#-----------------------------------------------------------------
	#				Creating the List decks page
	#------------------------------------------------------------------
	tree = Treeview(ldeck, show="tree headings", height=34)
	tree["columns"]=("name", "number", "numberside", "obs")
	tree.column("#0", width=0, stretch=NO)
	tree.column("name", width=100, stretch=NO)
	tree.column("number",width=50, stretch=NO)
	tree.column("numberside",width=50, stretch=NO)
	tree.column("obs",width=355, stretch=NO)
	tree.heading("name", text="name")
	tree.heading("number", text="cards")
	tree.heading("numberside", text="side")
	tree.heading("obs", text="comment")
	tree.grid(row=0, column=0, rowspan=4, padx=30, pady=30)
	b1 = Button(ldeck, text="Add Deck",  bg="lightgrey", width=13, height=5)
	b1.grid(row=0, column=2, padx=10)
	b2 = Button(ldeck, text="Remove Deck", bg="lightgrey", width=13, height=5)
	b2.grid(row=1, column=2, padx=10)
	b3 = Button(ldeck, text="See Deck", bg="lightgrey", width=13, height=5)
	b3.grid(row=2, column=2, padx=10)
	b4 = Button(ldeck, text="Choose Deck", bg="lightgrey", width=13, height=5)
	b4.grid(row=3, column=2, padx=10)

	decks = db.get_all_decks()

	for i in decks:
		tree.insert("", END, values=(i["name"], i["n_cards"], i["n_side"], i["desc"]))


def create_add_card_layout():
	def get_data():
		name = e1.get()
		cost = int(e3.get())
		number = int(e4.get())
		tipe = e5.get()
		deck = e6.get()
		obs = e7.get(1.0, END)
		color = ""

		if(r.get()):
			color = "red"
		if(b.get()):
			color = "{},blue".format(color)
		if(g.get()):
			color = "{},green".format(color)
		if(w.get()):
			color = "{},white".format(color)
		if(bk.get()):
			color = "{},black".format(color)
		
		card = Card(name, color, cost, number, tipe, deck, obs)
		db.add_card(card)


	r = IntVar()
	b = IntVar()
	g = IntVar()
	w = IntVar()
	bk = IntVar()


	add = Toplevel(app)
	add.minsize(300,400)
	add.title("Add Card")
	add.resizable(0,0)
	mega = Frame(add)
	f = Frame(mega)
	f1 = Frame(mega)
	f2 = Frame(add)
	mega.grid(row=0, column=0)
	f.pack(fill=BOTH, side="left")
	f1.pack(fill=BOTH, side="right")
	f2.grid(row=1, column=0)
	lname = Label(f, text="Name:")
	lname.pack(padx=0, pady=20, anchor="w")
	lcolor = Label(f, text="Color")
	lcolor.pack(padx=0, pady=20, anchor="w")
	lmana = Label(f, text="Mana Cost:")
	lmana.pack(padx=0, pady=20, anchor="w")
	lnumber = Label(f, text="Number to add:")
	lnumber.pack(padx=0, pady=21, anchor="w")
	ltype = Label(f, text="Type of card:")
	ltype.pack(padx=0, pady=21, anchor="w")
	ldeck = Label(f, text="Deck(1 deck max):")
	ldeck.pack(padx=0, pady=21, anchor="w")
	lobs = Label(f, text="Coments:")
	lobs.pack(padx=0, pady=21, anchor="w")
	e1 = Entry(f1, width=30)
	e1.pack(padx=0, pady=20, anchor="w")
	c = Frame(f1)
	c.pack(padx=0, pady=20, anchor="w")
	c1 = Checkbutton(c, text="red", variable=r)
	c1.pack(side="left")
	c2 = Checkbutton(c, text="blue", variable=b)
	c2.pack(side="left")
	c3 = Checkbutton(c, text="green", variable=g)
	c3.pack(side="left")
	c4 = Checkbutton(c, text="white", variable=w)
	c4.pack(side="left")
	c5 = Checkbutton(c, text="black", variable=bk)
	c5.pack(side="left")
	e3 = Entry(f1, width=30)	
	e3.pack(padx=0, pady=19, anchor="w")
	e4 = Entry(f1, width=30)
	e4.pack(padx=0, pady=20, anchor="w")
	e5 = Entry(f1, width=30)
	e5.pack(padx=0, pady=20, anchor="w")
	e6 = Entry(f1, width=30)
	e6.pack(padx=0, pady=20, anchor="w")
	e7 = Text(f1, height=10, width=34)
	e7.pack(padx=0, pady=20, anchor="w")
	bl = Button(f2, text="Save", command=lambda:get_data())
	bl.pack(padx=10, pady=20, side="left", anchor="w")
	b1 = Button(f2, text="Cancel")
	b1.pack(padx=10, pady=20, side="right", anchor="e")


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
create_layout_list_all(lall, db)
create_deck_layout(ldeck, db)

#Implementing the navbar
menubar = Menu(app, font=10)
library = Menu(menubar, font=5, tearoff=0)
library.add_command(label="Add card", command=lambda:create_add_card_layout())
library.add_command(label="Remove card", command=donothing)
library.add_command(label="Update card", command=donothing)
library.add_separator()
library.add_command(label="Search card", command=donothing)
library.add_command(label="List all cards", command=lambda:changeFrame(lall))
deck = Menu(menubar, font=5, tearoff=0)
deck.add_command(label="Add Deck", command=donothing)
deck.add_command(label="Remove Deck", command=donothing)
deck.add_command(label="List Decks", command=lambda:changeFrame(ldeck))
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
