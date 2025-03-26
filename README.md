# Python Web Development Techdegree  
### Project 3 - Phrase Hunters  
**Author** - Hans Steffens  

---

## Project Overview

Phrase Hunters is a word guessing game written in Python using Object-Oriented Programming (OOP) principles. The player attempts to guess a hidden phrase one letter at a time. The game ends when the player successfully guesses the entire phrase or makes five incorrect guesses.

---

## How It Works

- A random phrase is selected from a predefined list.
- The player is shown a series of underscores representing the letters in the phrase.
- The player guesses one letter at a time.
- Correct guesses reveal the letter's position(s) in the phrase.
- Incorrect guesses reduce the number of available lives (maximum of 5).
- The player wins by revealing the full phrase, or loses after 5 incorrect guesses.
- The player can choose to play again after a game ends.
- Pressing `Ctrl + C` exits the game gracefully at any time.

---

## Features

- OOP implementation using two custom classes: `Game` and `Phrase`
- Input validation to prevent repeated or invalid guesses
- Graceful handling of keyboard interruptions (`Ctrl + C`)
- Option to replay the game after it ends

---

## Files and Structure

```text
.
├── app.py                 # Entry point to start the game
├── phrasehunter/
│   ├── __init__.py
│   ├── game.py            # Contains the Game class
│   └── phrase.py          # Contains the Phrase class
└── README.md              # Project documentation
```

## How to Run

This project requires `Python 3` to run. No additional packages are needed, as it is built using Python’s standard library. Then from your terminal:

```sh
python3 app.py
```
## Acknowledgments
This project is part of the Python Web Development Techdegree from Treehouse.
The game was built to practice class design, data validation, control flow, and interactive console applications.