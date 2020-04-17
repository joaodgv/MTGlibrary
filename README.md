# MTG Libary

This is a simple program where you can store all the cards you have. You can also create decks and fill those decks with the cards they have. This way you will never loose track of where your cards are.

## Ways to use the program

### Executable file
Simple run the program and fill it with your cards. It's as simple and straight forward as that

### Terminal
To run the program in the terminal you just have to run the python script console.py that is located inside the source folder
Use the command:

```bash
python3 console.py
```
## Program construction
The program is entirely made in python using only the tkinter library to create the Graphical User Interface

## Database system
The database consists of a single json file. There it stores all the cards and decks you create during the execution of the program.
the Database has the following format. Each card is stored has a dictionary and the key is its name. It is case insensitive

```JSON
{
	"cards": {},
	"decks": {
		lands:{},
		creatures: {},
		spells: {},
		side: {}
	},
	"n_cards": 0
}
```
