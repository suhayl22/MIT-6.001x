# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/home/evan/Work/6.001x/pset3/words.txt"
INIT_GUESSES = 8

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if not (char in lettersGuessed):
            return False
        
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    remainingWord = ''
    for char in secretWord:
        addedChar = ''
        if char in lettersGuessed:
            addedChar = char
        else:
            addedChar = '_ '
        remainingWord = remainingWord + addedChar 
    return remainingWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    avail = ''
    for char in string.ascii_lowercase:
        if not (char in lettersGuessed):
            avail += char
    return avail
    
def newRound(guessesLeft, availableLetters):
    '''
    guessesLeft: int, the number of guesses the user has left
    availableLetters: string, the letters which the user can still guess
    returns: string, the character the user guesses in the new round
    
    prints the first 3 lines (number of guesses left, avail letters,
    and guess prompt) of the game and returns the character which the user
    guesses in this round
    '''
    print "-----------------"
    print "You have " + str(guessesLeft) + " guesses left."
    print "Available letters: " + availableLetters
    guess = raw_input("Please guess a letter: ")
    return guess

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to hangman!"
    print "I am thiking of a word " + str(len(secretWord)) + " letters long."

    # keeps track of the guessed letters
    letters_guessed = []
    # tracks the letters available
    letters_avail = getAvailableLetters(letters_guessed)

    # the first round to setup all the other rounds
    num_guesses = INIT_GUESSES
    
    # continue the game while user has guesses and the word hasn't been guessed
    while (num_guesses > 0 and not isWordGuessed(secretWord, letters_guessed)):
        # the guess character
        g = newRound(num_guesses, letters_avail).lower()
        
        # get the word with correctly guessed characters
        guessed = getGuessedWord(secretWord, letters_guessed)
        
        # check if the character was already guessed
        if g in letters_guessed:
            print "Oops! You've already guessed that letter: " + guessed
        else:
            # must be a new guess
            letters_guessed.append(g)
            letters_avail = getAvailableLetters(letters_guessed)
            guessed = getGuessedWord(secretWord, letters_guessed)
            
            # check if the character was in the secret word
            if g in secretWord:
                print "Good guess: " + guessed
            else:
                num_guesses -= 1
                print "Oops! That letter is not in my word: " + guessed
   
    print "--------------" 
    if (isWordGuessed(secretWord, letters_guessed)):
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses.  The word was " + secretWord


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)