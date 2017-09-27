import random
import string
# underline disappear when letter is guessed
# 8 guesses total

# def loadWord():
#    f = open('hangman_words.txt', 'r')
#    wordsList = f.readlines()
#    f.close()

#    wordsList = wordsList[0].split(' ')
#    secretWord = random.choice(wordsList)
#    return secretWord



# challenge words from makeschool.com
# beautifulsoup


# show user relevant info
# get guess and check if correct
# display correct letter
# increment incorrect guesses

secretWord = "apples"
letterList = list(secretWord)
lettersGuessed = []
availableLetters = list(string.ascii_lowercase)
print(availableLetters, "availableLetters")
showRemainingGuesses = []

print("Welcome to Hangman! \nStart by guessing a letter from A-Z")
print(availableLetters)
playerInput = input("Guess: ")

def getGuessedWord(secretWord, lettersGuessed):
    '''
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
def showGuessLines():
  countLines = len(letterList)
  showGuessLines = (countLines * " _ ")
showGuessLines()

def getAvailableLetters(lettersGuessed):
  '''
  lettersGuessed: list of letters that have been guessed so far
  returns: string, comprised of letters that represents what letters have not
    yet been guessed.
  '''
  availableLetters.remove(playerInput)
  print("What is your next guess?\n", availableLetters)

def isWordGuessed():
  if showRemainingGuesses == letterList:
    print("success")
  else:
    print("keep guessing")

def showCurrentResults():
  if playerInput in letterList:
    print("\nYou got a letter, hooray!\n")
    letterListIndex = letterList.index(playerInput)
    getAvailableLetters(lettersGuessed)
    # print(letterListIndex, "-> Index number of letter")

  indexConversionArray = []
  for indexNum in letterList:
    indexConversionArray.append(letterList.index(indexNum))
  letterToValue = indexConversionArray
  # print(letterToValue, "-> Convert letter to value")

  showGuessedResult = [playerInput if entry == letterListIndex else entry for entry in letterToValue]
  # print(showGuessedResult, "-> Show guessed results")
  showRemainingGuesses = [" _ " if isinstance(entry, int) else entry for entry in showGuessedResult]
  # print(showRemainingGuesses, "-> Prints out display in array with underline")
  currentResults = " ".join(showRemainingGuesses)
  print(currentResults)
  
  isWordGuessed()
showCurrentResults()
    

getGuessedWord(secretWord, lettersGuessed)


    
        
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
  

# secretWord = loadWord()
# hangman(loadWord())

hangman(secretWord)
