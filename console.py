#python 3
#the console format for the program
#------------------------------------------
#		Imports
#-----------------------------------------
import cards
from back import *
from loop import *

#-------------------------------------------
#	    Simple Functions
#------------------------------------------
def help():
	print("This is the help command")
	print("a - Adds a card to the database or increases its number")
	print("r - removes a card from the database or decreases its number")
	print("ad - Adds a deck to the database")
	print("rd - Removes a deck from the database")

def add_card():
	print("to add a card you must give the following information:")
	print("Card Name")
	print("color in the form (red/blue/green/white/black) always in that order\n\tex.: my card is red/black")
	print("total mana cost")
	print("number of cards")
	print("type(land, creature, instant, sorcery, enchantment): ")
	print("deck")
	print("observations")
	print("--------------------------------")
	name = input("name: ")
	color = input("color: ")
	cost = input("mana cost: ")
	n = input("number of cards: ")
	type = input("type(land, creature, spell, ...): ")
	deck = input("deck(this can be empty): ")
	obs = input("observations: ")

	card = Card(name, color, cost, n, type, deck, obs)

	db.add_card(card)

def remove_card():
	print("To remove a card just write the cards name")
	name = input("name: ")

	db.remove_card(name)

def choose_a_deck():
	print("Write the name of the deck you want (must have been already created)")
	name = input("deck: ")

	deck = db.get_deck(name)

	if (deck == None):
		print("There is no deck with that name")

	return deck

def add_deck():
	print("To create a deck just give it a name")
	name = input("name: ")
	print("You can give a description of the deck if you want")
	desc = input("desc")

	if(name):
		db.add_deck(name, desc)
	else:
		print("The name cannot be empty")

def remove_deck():
	print("To remove a deck just write the name")
	name = input("name: ")

	if(name):
		db.remove_deck(name)
	else:
		print("The name cannot be empty")

#-------------------------------------------
#		Main Loop
#-------------------------------------------

print("welcome to the card manager")
print("a - Add a card")
print("r - remove a card")
print("s - search")
print("d - choose a deck")
print("ad - Add a deck")
print("rd - Remove a deck")
print("x - exits program")

db = Database()
current_deck = ""

while (True):
	print("make an action")
	value = input()

	if (value == "h"):
		help()
	elif(value == "a"):
		#calls function that adds gives instrucion to add cards
		add_card()
	elif(value == "r"):
		#calls function that removes cards
		remove_card()
	elif(value == "s"):
		#calls the search menu
		s = Search()
		s.loop(db, current_deck)
	elif(value == "d"):
		#calls a function that stores the current deck
		current_deck = choose_a_deck()
	elif(value == "ad"):
		#calls function that adds decks
		add_deck()
	elif(value  == "rd"):
		#calls funtion that removes decks
		remove_deck()
	elif (value == "x"):
		print("Exiting program \nSaving Data");
		print("done")
		break
