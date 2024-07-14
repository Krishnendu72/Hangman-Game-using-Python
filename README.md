# Hangman Game using Python

Welcome to the Hangman Game! This project is a simple tkinter GUI integrated example of the classic word-guessing game Hangman, where players attempt to guess a hidden word one letter at a time. Each incorrect guess results in a loss of a life, and the game continues until either the word is completely guessed or the player runs out of lives.

#### Project Files:
##### project.py
This file contains the main implementation of the Hangman game. It includes the following key functions and their responsibilities:

##### choose_word(wordlist):

This function randomly selects a word from the provided wordlist and returns it in uppercase. It utilizes Python's random.choice method to select a word.
Arguments: wordlist (list of strings)
Returns: A randomly selected word in uppercase (string)

##### display_word(word, correct):

This function creates a string representation of the current state of the word being guessed. Correctly guessed letters are displayed, while the remaining letters are represented by underscores.
Arguments: word (string), correct (set of characters)
Returns: A string with correctly guessed letters and underscores for remaining letters

##### guess_letter(word, letter, correct, incorrect):

This function updates the sets of correct and incorrect guesses based on the player's input. If the guessed letter is in the word, it is added to the correct set; otherwise, it is added to the incorrect set.
Arguments: word (string), letter (string), correct (set of characters), incorrect (set of characters)
Returns: Updated correct and incorrect sets

##### check_game_over(word, correct, attempts):

This function checks whether the game is over. The game is considered over if the player has correctly guessed all letters in the word or if the player has run out of attempts. It returns a boolean indicating whether the game is over and a message describing the outcome.
Arguments: word (string), correct (set of characters), attempts (integer)
Returns: Tuple containing a boolean (game over status) and a message (string)

##### class Hangman :

This function contains the main game loop. It initializes the game state, manages player input, updates the game state based on guesses, and checks for game over conditions. It prints the current state of the game and get the input from the player using the buttons.

##### main():

This function is the entry point of the program. It starts the Hangman game by calling the Hangman class.

#### Design Choices:

Class : Class is used to initalize the GUI and also for the flow of events.

Word List: A small set of words is hardcoded in the hangman_game function. This choice was made for simplicity and ease of testing. In a more advanced version, the word list could be externalized or expanded.

Set Data Structure: Sets are used to track correct and incorrect guesses. This choice provides efficient lookups and ensures that each letter is only stored once, avoiding duplicate guesses.
