This program is meant to emulate the game Hangman.  

The program will select a random word from the attached words.txt file.  If not file is found, it 
will randomly pick a word from a list of defaults found in main.

The program will tell the user how many letters are in the word and how many guesses they have to 
solve it.

The user will then be prompted to guess a letter.  If the letter they guess is somewhere in the word
the program will reveal the locations of that letter in the word.  If the user's letter is not found
then the program will inform the user and will decrement the number of guesses the user has remaining. 

The user will then be asked if they would like to guess the word. If they respond no, the game loop
will repeat. IF they answer yes, then the program will ask for a word from the user.  If the guess 
is correct the user wins and the program will terminate.  If the guess is wrong, then the program
will decrement the number of guesses the user has remaining. 

This Game loop will repeat until either the user has guessed the right word, or they have run out of
guesses. 