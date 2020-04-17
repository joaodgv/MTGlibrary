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
				
				if(card.deck not in db["cards"][card.name]["deck"] and self.get_deck(card.deck)!= None):
					db["cards"][card.name]["deck"].append(card.deck)
				elif(self.get_deck(card.deck)== None and card.deck != ""):
					raise Exception()

				db["n_cards"] += int(card.n)
			else:
				db["cards"][card.name] = {"name": card.name, "color": card.color, "cost": card.cost, "number": int(card.n), "type": card.type, "deck": [card.deck],  "obs": card.obs}
				db["n_cards"] += int(card.n)

			self.update_db()
		except DataEntering:
			print("There was an error adding your card")

	#Function that removes a card from the db
	def remove_card(self, name, n):
		if (name in self.db["cards"]):
			if(n >= self.db["cards"][name]["number"]):
				self.db["cards"].pop(name)
			else:
				self.db["cards"][name]["number"] -= n
		self.db["n_cards"] -= n
		self.update_db()

	#returns a card
	def get_card(self, name):
		try:
			card = self.db["cards"][name]

			return {"name": card["name"], "color": card["color"], "cost": card["cost"], "number": card["number"], "type": card["type"], "deck": card["deck"],  "obs": card["obs"]}
		except:
			print("There is no card with that name")

	#Function that updates a card information
	def update_card(self, card):
		if(card["name"] in self.db["cards"]):
			self.db["cards"][card[name]] = {"name": card["name"], "color": card["color"], "cost": card["cost"], "number": card["number"], "type": card["type"], "deck": card["deck"],  "obs": card["obs"]}
		self.update_db()

	def update_cost(self, name, cost):
		self.db["cards"][name]["cost"] = cost
		self.update_db()
	
	def update_color(self, name, color):
		self.db["cards"][name]["color"] = color
		self.update_db()
	
	def update_number(self, name, number):
		self.db["cards"][name]["number"] = number
		self.update_db()
	
	def update_obs(self, name, obs):
		self.db["cards"][name]["obs"] = obs
		self.update_db()
	

	#function that adds a deck to the db
	def add_deck(self, name, desc):
		if(name in self.db["decks"]):
			print("Deck is already in the database")
		else:
			self.db["decks"][name] = {"name": name, "main": {}, "side": {}, "desc": desc, "n_cards": 0, "n_side": 0}
			self.update_db()

	#function that removes a deck from the db
	def remove_deck(self, name):
		if(name in self.db["decks"]):
			self.db["decks"].pop(name)

	#function that adds a card to a deck
	def add_card_to_deck(self, deck_name, name, num, side=False):
		card = self.get_card(name)
		for d in self.db['decks']:
			if(d == deck_name):
				if(side):
					if(card['name'] in self.db['decks'][d]['side']):
						self.db['decks'][d]['side'][card['name']]['number'] += num
						self.db['decks'][d]["n_side"] += num
					else:
						lcard = card
						lcard['number'] = num
						self.db['decks'][d]['side'][card['name']] = lcard
						self.db['decks'][d]["n_side"] += num
				else:
					if(card['name'] in self.db['decks'][d]['main']):
						self.db['decks'][d]['main'][card['name']]['number'] += num
						self.db['decks'][d]["n_cards"] += num
					else:
						lcard = card
						lcard['number'] = num
						self.db['decks'][d]['main'][card['name']] = lcard
						self.db['decks'][d]["n_cards"] += num

		self.update_db()

	#function that removes a card from a deck
	def remove_card_from_deck(self, deck, name, num, side=False):
		n = int(num)
		for d in self.db["decks"]:
			if(deck == d):
				for t in self.db["decks"][d]:
					for c in self.db["decks"][d][t]:
						if(c == name and self.db["decks"][d][t][c]["number"] >= n):
							self.db["decks"][d][t][c]["number"] -= n
							if(not side):
								self.db["decks"][d]["n_cards"] -= n
							else:
								self.db["decks"][d]["n_side"] -= n
						else:
							if(not side):
								self.db["decks"][d]["n_cards"] -= self["decks"][d]["number"]
							else:
								self.db["decks"][d]["n_side"] -= self["decks"][d]["number"]
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
			decks.append(self.db["decks"][deck])
		return decks

	def get_number_of_cards(self):
		return self.db["n_cards"]

	#function that updates the db
	#Gets called by all other functions that mess with the db
	def update_db(self):
		with open('db.json', 'w') as json_file:
			pretty = json.dumps(self.db, indent=4)
			json_file.write(pretty)
