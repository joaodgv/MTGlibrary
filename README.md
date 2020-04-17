(https://github.com/joaodgv/MTGlibrary/archive/v0.2.0.zip)

## Ways to use the program

### Terminal
To run the program in the terminal you just have to run the python script console.py that is located inside the source folder

```bash
python3 console.py
```

### Executable file
still has to be done

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
