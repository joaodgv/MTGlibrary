#python3 module
from tkinter import *
from tkinter.ttk import Treeview
from cards import *

def destroy(window):
	window.destroy()

def create_layout_list_all(app, lall, db, current_deck):
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
	b1 = Button(lall, text="Add Card",  bg="lightgrey", width=13, height=5, command=lambda:create_add_card_layout(app, db))
	b1.grid(row=0, column=2, padx=10)
	b2 = Button(lall, text="Remove Card", bg="lightgrey", width=13, height=5, command=lambda:remove_card_layout(app, db, tree.item(tree.focus())))
	b2.grid(row=1, column=2, padx=10)
	b3 = Button(lall, text="Update card", bg="lightgrey", width=13, height=5, command=lambda:update_card_layout(app, db, tree.item(tree.focus())))
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

	lall.tkraise()

def create_deck_layout(app, ldeck, db):
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

	ldeck.tkraise()

def create_add_card_layout(app, db):
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

		try:
			card = Card(name.lower(), color.lower(), cost, number, tipe.lower(), deck.lower(), obs)
			db.add_card(card)

			add.destroy()
		except:
			#need to create a window an error
			print("there is an error")

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
	b1 = Button(f2, text="Cancel", command=lambda:destroy(add))
	b1.pack(padx=10, pady=20, side="right", anchor="e")

def remove_card_layout(app, db, option):

	if(option["values"] == ''):
		#opens the prompt to ask for the card
		rem = Toplevel(app)
		rem.title("Remove card")
		rem.resizable(0,0)
		bottom = Frame(rem)
		bottom.pack(padx=5, pady=20, side="bottom")
		lname = Label(rem, text="Name of the card")
		lname.pack(padx=5,pady=20)
		ename = Entry(rem)
		ename.pack(padx=5,pady=20)
		lnumber = Label(rem, text="Number of cards to remove")
		lnumber.pack(padx=5,pady=20)
		enum = Entry(rem)
		enum.pack(padx=5,pady=20)
		b1 = Button(bottom, text="Remove", command=lambda:remove_card(app, rem, db, ename.get(), int(enum.get())))
		b1.pack(side="left")
		b2 = Button(bottom, text="cancel", command=lambda:destroy(rem))
		b2.pack(side="right")
	else:
		#opens prompt to ask if this is to remove
		rem = Toplevel(app)

def remove_card(app, rem, db, name, number):
	try:
		db.remove_card(name, number)
		rem.destroy()
	except:
		#needs a prompt
		print("erro a remover a carta")

def update_card_layout(app, db, option):
	var = IntVar()

	if(option['values'] == ''):
		#opens prompt to change the values of a card
		up = Toplevel(app)
		up.title('Update Card')
		up.resizable(0,0)
		radio = Frame(up)
		radio.pack(pady=10, side="top")
		bottom = Frame(up)
		bottom.pack(side="bottom")
		b1 = Button(bottom, text="Update", command=lambda:update_card(up, db, ename.get(), lentry.get(), var.get()))
		b1.pack(padx=10,side="left")
		b2 = Button(bottom, text="cancel", command=lambda:destroy(up))
		b2.pack(padx=10,side="right")
		lname = Label(up, text="Name of the card")
		lname.pack(padx=5,pady=20)
		ename = Entry(up)
		ename.pack(padx=5,pady=20)
		lchoice = Label(radio, text="Category to update")
		lchoice.pack(side="top")
		rcost = Radiobutton(radio, text="Cost", variable=var, value=1)
		rcost.pack(pady=10, side="left")
		rcolor = Radiobutton(radio, text="color", variable=var, value=2)
		rcolor.pack(side="left")
		rnumber = Radiobutton(radio, text="number", variable=var, value=3)
		rnumber.pack(side="left")
		robs = Radiobutton(radio, text="Comment", variable=var, value=4)
		robs.pack(side="left")
		lvalue = Label(up, text="New Value")
		lvalue.pack(padx=5,pady=20)
		lentry = Entry(up)
		lentry.pack(padx=5,pady=20)
	else:
		up = Toplevel(app)
		up.title('Update Card')
		up.resizable(0,0)
		radio = Frame(up)
		radio.pack(pady=10, side="top")
		label = Label(up, text="Card to update: {}".format(option['values'][0]))
		label.pack(side='top')
		bottom = Frame(up)
		bottom.pack(side="bottom")
		b1 = Button(bottom, text="Update", command=lambda:update_card(up, db, option['values'][0], lentry.get(), var.get()))
		b1.pack(padx=10,side="left")
		b2 = Button(bottom, text="cancel", command=lambda:destroy(up))
		b2.pack(padx=10,side="right")
		lchoice = Label(radio, text="Category to update")
		lchoice.pack(side="top")
		rcost = Radiobutton(radio, text="Cost", variable=var, value=1)
		rcost.pack(pady=10, side="left")
		rcolor = Radiobutton(radio, text="color", variable=var, value=2)
		rcolor.pack(side="left")
		rnumber = Radiobutton(radio, text="number", variable=var, value=3)
		rnumber.pack(side="left")
		robs = Radiobutton(radio, text="Comment", variable=var, value=4)
		robs.pack(side="left")
		lvalue = Label(up, text="New Value")
		lvalue.pack(padx=5,pady=20)
		lentry = Entry(up)
		lentry.pack(padx=5,pady=20)

def update_card(up, db, name, new, value):
	try:
		if(value==1):
			db.update_cost(name, int(new))
		elif(value==2):
			db.update_color(name, new)
		elif(value==3):
			db.update_number(name, int(new))
		elif(value==4):
			db.update_obs(name, new)
		else:
			raise Exception("no button was selected")
	except Exception:
		print("Error updating card")

	up.destroy()
