class Phrase():
    """This class handles the phrase to be guessed."""
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        """Display the phrase with guessed letters and underscores."""
        display_phrase = ""
        for letter in self.phrase:
            if letter in guesses:
                display_phrase += letter + " "
            else:
                display_phrase += "_ "
        print(f'{display_phrase} \n')
    
 
    def check_guess(self, guess):
        """Check if the guess is in the phrase."""
        return guess in self.phrase
    
    def check_complete(self, guesses):
        """Check if all letters in the phrase have been guessed."""
        for letter in self.phrase:
            if letter not in guesses and letter != " ":
                return False
        return True