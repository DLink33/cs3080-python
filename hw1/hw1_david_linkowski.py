''' Homework 1
Name: David Linkowski
Date: 2/1/2023
Description: Game of Hangman. A random word is selected from a list of words and the player
must guess the correct word within the given amount of guesses. If they do, they win. If they can't
they lose. Have fun!
'''

import random

DEFAULT_WORDS = ['apple', 'blade', 'cranky', 'darling', 'elephant', 'foster', 'glamorous','holster','ingot','jasmine', 'knuckle', 'limp', 'monster', 'onion', 'plague', 'quarrel', 'robust', 'starry', 'tomato', 'umbrella', 'whisky', 'xenomorph', 'yam', 'zim']
NUM_GUESSES = 12

def loadWords(fileName):
    wordList = []
    with open(fileName, 'r') as words:
        for word in words:
            wordList.append(word.strip())
    return wordList

def revealWord(revealed, ansWord, charGuess):
    correct = 0
    for i, char in enumerate(ansWord):
        if char == charGuess:
            revealed[i] = 1
            correct +=1
    if correct == 1:
        print(f"There is 1 '{charGuess}' in the word.")
        return True
    elif correct > 1:
        print(f"There are {correct} '{charGuess}'s in the word.")
        return True
    else:
        print(f"There are no '{charGuess}'s in the word. =c")
        return False          

def printRevealedWord(revealed, ansWord):
    length = len(ansWord)
    for i in range(length):
        if revealed[i] == 1:
            print(ansWord[i].upper(), end="")
        else:
            print("_", end="")
    print("")
        
def getUserCharGuess():
    guess = str(input("Enter the letter you would like to guess: "))
    return guess.upper()[0]

def getUserWordGuess():
    response = ' '
    while response != 'y' or response != 'n':
        response = str(input("Would you like to guess the word? Enter '(Y)es' or '(N)o': ")).lower()
        if response[0] == 'y':
            guess = str(input("Enter the word you would like to guess: "))
            return guess.upper()
        elif response[0] == 'n':
            return ""

def checkWinCond(wordGuess, ansWord):
    return True if wordGuess == ansWord else False

def checkLoseCond(numGuesses):
    return True if numGuesses >= NUM_GUESSES else False

def initGame():
    print("\nWelcome to Hangman!\n")
    print("Loading words...")
    try:
        words = loadWords("words.txt")
    except FileNotFoundError:
        print(f'Words not loaded from file. File "words.txt" not found in path.')
        print("Using default word list.")
        words = DEFAULT_WORDS
    except:
        print("Words not loaded. Error occurred loading the file.")
        print("Using default word list.")
        words = DEFAULT_WORDS
    print("Words loaded.\n")

    ansIndex = int((float(random.random()) * len(words)) % len(words))
    ansWord = words[ansIndex]
    print("Answer word selected!")
    return ansWord.upper()

# the game loop 
def gameLoop(ansWord):
    print(f"\nThe word is a {len(ansWord)}-letter word.")
    # init guesses for the user's input guesses
    charGuess = ""
    wordGuess = ""
    # var for returning the result of the game
    gameRslt = False
    # init number of guesses to 0
    numBadGuesses = 0
    # init revealed with a list comprehension to keep track of which chars are correctly guessed
    revealed = [0 for _ in range(len(ansWord))]
    printRevealedWord(revealed, ansWord)
    print(f"You have {NUM_GUESSES} guesses remaining. Good luck!\n")
    # init the win condition to false
    
    # while the win condition is not met, loop 
    while(True):
        # get the user's guess
        charGuess = getUserCharGuess()
        # reveal appropriate letter guessed correctly and increment the number of bad guesses by 1
        if not revealWord(revealed, ansWord, charGuess):
            numBadGuesses += 1 
            
        # print the letters revealed in the answer word
        printRevealedWord(revealed, ansWord)
        
        #check if the user has exceeded the number of guesses permitted by the game
        if checkLoseCond(numBadGuesses):
            return False  # The player loses =c
        
        # get user's word guess if they want to guess
        wordGuess = getUserWordGuess()
        
        # check the win condition
        if checkWinCond(wordGuess, ansWord):
            return True # The player wins!
            
        # Note: The variable wordGuess will be "Truthy" if a non-empty 
        # string is returned from getUserWordGuess(), 
        # and "Falsy" if an empty string is returned
        elif wordGuess:
            print(f'"{wordGuess}" is not the correct word.')
            numBadGuesses += 1
        print(f"You have {NUM_GUESSES - numBadGuesses} guesses remaining.\n")           

def endGame(result, ansWord):
    if result:
        print("Congratulations! You won the game!")
    else:
        print(f'Sorry, but you lost! The answer was "{ansWord}"\nBetter luck next time!')

# main function
def main() -> int:
    # initialize the game and generate answer word
    ansWord = initGame()
    rslt = False
    # start the game loop
    rslt = gameLoop(ansWord)
    # end the game after loop is finished
    endGame(rslt, ansWord)
    return 0
    
# used to emulate the main function in python       
if __name__ == '__main__':
    main()
    