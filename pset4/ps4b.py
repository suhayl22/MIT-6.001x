from ps4a import *
import time

def isInHand(hand, word):
    '''
    given a word, tell if the word can be made from the hand
    
    word: string which we assume is in the word list
    hand: dict (string -> int) mapping letters to the qty of them in the hand
    '''
    # copy the hand to avoid unexpected mutation
    handcpy = hand.copy()
    for char in word:
        try:
            # ensure the hand has this letter
            if (handcpy[char] > 0):
                handcpy[char] -= 1
            else:
                return False
        except KeyError:
            return False
    # since we've gotten here without returning false (key error or
    # not enough copies of a character) must be true
    return True

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    max_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if (isInHand(hand, word)):
            # Find out how much making that word is worth
            cur_score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if cur_score > max_score:
                # Update your best score, and best word accordingly
                max_score = cur_score
                max_word = word

    # return the best word you found.
    return max_word


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    score = 0
    
    comp_word = ''
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
    
        # Display the hand
        displayHand(hand)
        # get word for computer to play
        comp_word = compChooseWord(hand, wordList, n)
        # If computer is unable to choose a word:
        if (comp_word == None):
            # End the game (break out of the loop)
            break
            
        # computer chooses a word:
        else:
            # If the word is not valid (defensive prgmming):
            if not isValidWord(comp_word, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print "Invalid word, please try again."
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                cur_score = getWordScore(comp_word, n)
                score += cur_score
                print "\"" + comp_word + "\" earned " + str(cur_score) + ". Total score: " + str(score)
                print('')
                
                # Update the hand 
                hand = updateHand(hand, comp_word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print "Thanks for playing!  Total Score: " + str(score)
    print ''
    
def getPlayerChoice ():
    '''
    Asks the user to enter a 'u' or 'c' to choose if the user will
    play a hand or the computer will play a hand
    
    returns: string
    '''
    msg = "Enter u to have yourself play, c to have the computer play: "
    u_in = ''
    while (True):
        u_in = str(raw_input(msg))
        if u_in == 'u' or u_in == 'c':
            break
        else:
            print "Invalid comand."
    return u_in
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    stored_hand = None
    while (True):
        game_input = str( raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end the game: ") )
        if (game_input == 'e'):
            break
        elif (game_input == 'n'):
            stored_hand = dealHand(HAND_SIZE)
            player = getPlayerChoice()
            assert player == 'u' or player == 'c'
            if (player == 'u'):
                playHand(stored_hand, wordList, HAND_SIZE)
            else:
                compPlayHand(stored_hand, wordList, HAND_SIZE)
        elif (game_input == 'r'):
            if stored_hand == None:
                print 'You have not played a hand yet.  Please play a hand first!'
                continue
                
            player = getPlayerChoice()
            assert player == 'u' or player == 'c'
            if player == 'u':
                playHand(stored_hand, wordList, HAND_SIZE)
            else:
                compPlayHand(stored_hand, wordList, HAND_SIZE)
        else:
            print "Invalid input."
            
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


