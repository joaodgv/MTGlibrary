#python3
#Functions that are going to be called by the program that deal with the db
from cards import *
import tkinter

def add_card(name, color, cost, number, tipe, obs, db):
    try:
        card = Card(name, color, cost, number, tipe, obs)
        db.add_card(card)
    except:
        ## displays a menu saying something went wrong
        return 0