#python3
#program that handles the connection with the db
import json
from cards import Card

class Error(Exception):
	#Base error class
	pass

class DataEntering(Error):
	#Raised when it fails to write to the db
	pass

class Database:
	def __init__(self):
		with open('db.json', 'r') as json_file:
			self.db = json.load(json_file)

	#-------------------------------------------------------
	#		Functions that handle the db
	#--------------------------------------------------------

	#Function that adds a card to the db
	def add_card(self, card):
		db = self.db
		try:
			if (card.name in self.db["cards"]):
				db["cards"][card.name]["number"] += int(card.n)
			else:
				db["cards"][card.name] = {"name": card.name, "color": card.color, "cost": card.cost, "number": int(card.n), "type": card.type, "deck": [card.deck],  "obs": card.obs}
				db["n_cards"] += int(card.n)

			self.update_db()
		except DataEntering:
			print("There was an error addin your card")

	#Function that removes a card from the db
	def remove_card(self, name):
		if (name in self.db["cards"]):
			self.db["cards"].pop(name)
		self.db["n_cards"] -= 1
		self.update_db()

	#Function that updates a card information
	def update_card(self, card):
		if(card.name in self.db["cards"]):
			self.db["cards"][card.name] = {"name": card.name, "color": card.color, "cost": card.cost, "type": card.type, "deck": card.deck,  "obs": card.obs}
		self.update_db()

	#function that adds a deck to the db
	def add_deck(self, name):
		if(name in self.db["decks"]):
			print("Deck is already in the database")
		else:
			self.db["decks"][name] = {"land":{}, "creature": {}, "spell":{}, "side": {},  "n_cards": 0, "n_side": 0}
			self.update_db()

	#function that removes a deck from the db
	def remove_deck(self, name):
		if(name in self.db["decks"]):
			self.db["decks"].pop(name)

	#function that adds a card to a deck
	def add_card_to_deck(self, deck, name, num):
		n = int(num)
		for d in self.db["decks"]:
			if(deck == d):
				card = self. search_by_name(name)
				if(card != None and name not in self.db["decks"][d]["land"] and name not in self.db["decks"][d]["creature"] and name not in self.db["decks"][d]["spell"]):
					lcard = card[0]
					lcard["number"] = n

					if(card[0]["type"] == "land"):
						self.db["decks"][d]["land"][lcard["name"]] = lcard
					elif(card[0]["type"] == "creature"):
						self.db["decks"][d]["land"][lcard["name"]] = lcard
					else:
						self.db["decks"][d]["spell"][lcard["name"]] = lcard

					print(d)

					if(d not in self.db["cards"][lcard["name"]]["deck"]):
						self.db["cards"][lcard["name"]]["deck"].append(d)
				else:
					lcard = card[0]
					if(card[0]["type"] == "land"):
						self.db["decks"][d]["land"][lcard["name"]]["number"] += n
					elif(card[0]["type"] == "creature"):
						self.db["decks"][d]["land"][lcard["name"]]["number"] += n
					else:
						self.db["decks"][d]["spell"][lcard["name"]]["number"] += n
		self.update_db()

	#function that removes a card from a deck
	def remove_card_from_deck(self, deck, name, nnum):
		n = int(num)
		for d in self.db["decks"]:
			if(deck == d):
				for t in self.db["decks"][d]:
					for c in self.db["decks"][d][t]:
						if(c == name and  self.db["decks"][d][t][c]["number"] >= n):
							 self.db["decks"][d][t][c]["number"] -= n
						else:
							self.db["decks"][d][t].pop(c)
							self.db["cards"][name]["deck"].pop(deck)

		self.update_db()

	#--------------------------------------------------------------------------
	#
	#		    Functions that respond to the app
	#
	#	The data returned by the query functions is of the form: [dict]
	#
	#--------------------------------------------------------------------------

	#query functions that  search the database
	def search_by_name(self, name):
		for n in self.db["cards"]:
			if(name in n):
				return [self.db["cards"][n]]
		else:
			return None

	def search_by_type(self, type):
		cards = []
		for card in self.db["cards"]:
			if(type == self.db["cards"][card]["type"]):
				cards.append(self.db["cards"][card])

		return cards

	def search_by_cost(self, cost):
		cards = []
		for card in self.db["cards"]:
			if (cost == self.db["cards"][card]["cost"]):
				cards.append(self.db["cards"][card])
		return cards

	def get_deck(self, deck):
		for d in self.db["decks"]:
			if(deck == d):
				return [d]
		return None

	#General return functions to return everything in the db
	def get_all_cards(self):
		cards = []
		for card in self.db["cards"]:
			cards.append(self.db["cards"][card])
		return cards

	def get_all_decks(self):
		decks = []
		for deck in self.db["decks"]:
			decks.append(deck)
		return decks

	def get_number_of_cards(self):
		return self.db["n_cards"]

	#function that updates the db
	#Gets called by all other functions that mess with the db
	def update_db(self):
		with open('db.json', 'w') as json_file:
			pretty = json.dumps(self.db, indent=4)
			json_file.write(pretty)
