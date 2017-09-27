import random
import string



def loadWord():
    f = open('hangman_words.txt', 'r')
    wordsList = f.readlines()
    f.close()

    wordsList = wordsList[0].split(' ')
    secretWord = random.choice(wordsList)
    secretWord = list(secretWord)
    return secretWord

def isWordGuessed(secretWord, lettersGuessed):
    # print(secretWord, "This is the secretWord")
    
    rightLetters = []
    wrongLetters = []

    for x in lettersGuessed:
        if x in secretWord:
            rightLetters.append(x)
        else: 
            wrongLetters.append(x)

    setOfSecretLetters = list(set(secretWord))
    setOfRightLetters = list(set(rightLetters))
    setOfWrongLetters = list(set(wrongLetters))

    # print(setOfRightLetters, "right")
    # print(setOfWrongLetters, "wrong")
    remainingGuesses = 8 - len(setOfWrongLetters)
    print("You have ",remainingGuesses, " guesses remaning.")
    print("\n====================================================================")

    if setOfSecretLetters == setOfRightLetters:
        print("Congrats! You Won!")
    elif len(setOfWrongLetters) == 8:
        print("You ran out of guesses ): Try again!")
    else:
        getGuessedWord(secretWord, lettersGuessed)
        getAvailableLetters(lettersGuessed)
        isWordGuessed(secretWord, lettersGuessed)
        

def getGuessedWord(secretWord, lettersGuessed):
    playerInput = input("\nYour guess: ")
    lettersGuessed.append(playerInput)
    lettersGuessed = list(set(lettersGuessed))
    # lettersGuessed.sort()
    print("Letters Guessed:", lettersGuessed)


    # its adding doubles and spaces
    for letter in secretWord:
        underscrolls = [" _ " if letter not in lettersGuessed else letter for letter in secretWord]
        underscrollDisplay = " ".join(underscrolls)
    print(underscrollDisplay, "\n")
    return underscrollDisplay


def getAvailableLetters(lettersGuessed):
    availableLetters = list(string.ascii_lowercase) 
    for letter in lettersGuessed:
        if letter in availableLetters:
            availableLetters.remove(letter)
    availableLetters = ' '.join(availableLetters) 
    print("Take another guess from the list:\n", availableLetters)
    return availableLetters

# Extra Helpers ============================================================

def countLetters():
    elementCount = len(secretWord)
    startDisplay = (elementCount * " _ ")
    print(startDisplay)

def ifSetMatchesSubset(secretWord, lettersGuessed):
    for x in lettersGuessed:
        if set(lettersGuessed).issubset(set(secretWord)):
            return True
        else:
            return False

# ==========================================================================
def hangman(secretWord):

    print("Welcome to Hangman! Start by guessing a letter from A to Z.")
    lettersGuessed = []
    isWordGuessed(secretWord, lettersGuessed)



secretWord = loadWord()
hangman(loadWord())
