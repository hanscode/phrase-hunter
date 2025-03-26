import random
from phrasehunter.phrase import Phrase

class Game():
    """Game class to manage the Phrase Hunter game."""
    def __init__(self):
        self.missed = 0
        self.phrases = [
            "Hello World",
            "Simple is Better",
            "Python is Fun",
            "Code is Poetry",
            "Keep it Simple"
        ]
        self.active_phrase = None
        self.guesses = [" "]
    
    def get_random_phrase(self):
        """Get a random phrase from the phrases list."""
        return random.choice(self.phrases)
    
    def welcome(self):
        """Display a welcome message."""
        print("======================")
        print("Welcome to Phrase Hunter!")
        print("Guess the phrase letter by letter.")
        print("Good luck!")
        print("======================")
        
    def get_guess(self):
        """Get a guess from the user."""
        guess = input("Guess a letter: ").lower()
       
        while len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please make sure the following is true:")
            print("1. You only input one character.")
            print("2. You only input letters (a-z).")
            print("3. You do not input a space. \n")
            guess = input("Guess a letter: ").lower()
        return guess
    
    def game_over(self):
        """Display a game over message."""
        if self.missed == 5:
            print("Game Over! Better luck next time.")
        else:
            print("Congratulations! You've guessed the phrase!")

    def start(self):
        """Start the game."""

        self.active_phrase = Phrase(self.get_random_phrase())

        self.welcome()
        # Loop until the user has guessed the phrase or has missed 5 times.
        # The loop should print the number of misses and the phrase with guessed letters and underscores.
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):

            # printing the phrase with guessed letters and underscores
            self.active_phrase.display(self.guesses)

            user_guess = self.get_guess()
            self.guesses.append(user_guess)

            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
                print(f'You have {5 - self.missed} out of 5 lives remaining!')
                
        self.active_phrase.display(self.guesses)
        
        # Display the game over message
        self.game_over()
   