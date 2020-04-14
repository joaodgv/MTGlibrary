#python 3
#--------------------------------------------------------
#			Imports
#--------------------------------------------------------
from back import *
from cards import *

#This is the python class that handles the search loop
class Search:
	def __init__(self):
		self.current_card = {}

	#This function prints the info for the loop
	def print_info(self):
		print("This is the search menu")
		print("a- print all cards")
		print("n - Search by name")
		print("t - search by type")
		print("c - search by cost ")
		print("ld - list current deck")
		print("ad - add card to selected deck")
		print("rd - remove a card from the selected deck")
		print("b - back to the main screen")

	#------------------------------------------------
	#		Functions
	#-----------------------------------------------

	def print_list(self, cards):
		print("name | color | cost | decks")
		for i in cards:
			string = "{} | {} | {} | ".format(i["name"], i["color"], i["cost"])
			for j in i["deck"]:
				string = string +"{} ".format(j)

			print(string)

	#Function that gets the list of cards with that name
	def search_by_name(self, db):
		print("What card are you looking for?")
		name = input("name: ")
		cards = db.search_by_name(name)
		if(cards != None):
			self.print_list(cards)
		else:
			print("There are no cards that match your requirements")

	def search_by_type(self, db):
		print("What type are you looking for?")
		name = input("type: ")
		cards = db.search_by_type(name)
		if(cards != None):
			self.print_list(cards)
		else:
			print("There are no cards that match your requirements")

	def search_by_cost(self, db):
		print("What is the cost you are looking for?")
		cost = input("cost: ")
		cards = db.search_by_cost(cost)
		if(cards != None):
			self.print_list(cards)
		else:
			print("There are no cards that match your requirements")

	def add_to_deck(self, db, deck):
		print("What is the name of the card that you want to add to the deck?")
		card = input("card: ")
		n = input("number of cards to add: ")

		if(deck[0] != ""):
			db.add_card_to_deck(deck[0], card, n)
		else:
			print("you have no deck selected")
	def add_to_deck(self, db, deck):
		print("What is the name of the card that you want to add to the side deck?")
		card = input("card: ")
		n = input("number of cards to add: ")

		if(deck[0] != ""):
			db.add_card_to_deck(deck[0], card, n, True)
		else:
			print("you have no deck selected")

	def get_all_cards(self, db):
		card = db.get_all_cards()
		self.print_list(card)

	def remove_card_from_deck(self, db, deck):
		if(deck):
			print("What is the name of the card you want to remove")
			name = input("name: ")
			n = input("number of cards to remove: ")
			db.remove_card_from_deck(deck, name, n);
		else:
			print("you have no deck selected")

	def list_deck(self, db, deck):
		d = db.get_deck(deck)
		for i in d[0]:
			print("{}:".format(i))
			self.print_list(d[0][i])

	#this is the main loop
	def loop(self, db, deck):
		self.print_info()

		while(True):
			print("Make an action")
			c = input()

			if(c == "n"):
				#searches by name
				self.search_by_name(db)
			elif(c == "t"):
				#searches by type
				self.search_by_type(db)
			elif(c == "c"):
				#searches by cost
				self.search_by_cost(db)
			elif(c == "ad"):
				#adds a card to a deck
				self.add_to_deck(db, deck)
			elif(c == "asd"):
				#adds a card to the side deck
				self.add_to_side_deck(db, deck)
			elif(c == "rd"):
				#removes card from deck
				self.remove_card_from_deck(db, deck)
			elif(c == "ld"):
				#lists the current deck
				self.list_deck(db, deck)
			elif(c == "a"):
				#lists all the cards in the db
				self.get_all_cards(db)
			elif(c == "b"):
				#goes back to the original menu
				break
