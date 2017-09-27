# import pytest
# import random
# import string
# # secretWord = "apples"
# # letterList = list(secretWord)
# # print(letterList, "-> Turn word to array of letters")


# # # def showGuessLines(): ==========================================================================
# # countLines = len(letterList)
# # showGuessLines = (countLines * " _ ")
# # print(showGuessLines, "-> Player guess display | made into function")

# # # ================================================================================================

# # gussedList = []
# # playerInput = "p"

# # # def convertListIntToString(): =================================================================
# # if playerInput in letterList:

# #     letterListIndex = letterList.index(playerInput)
# #     print(letterListIndex, "-> Index number of letter")
# # indexConversionArray = []
# # for indexNum in letterList:
# #     indexConversionArray.append(letterList.index(indexNum))
# # letterToValue = indexConversionArray
# # print(letterToValue, "-> Convert letter to value")
# # # ================================================================================================


# # # def showCurrentResults(): ===============================================================================
# # showGuessedResult = [playerInput if entry == letterList.Index else entry for entry in letterToValue]
# # print(showGuessedResult, "-> Show guessed results")
# # showRemainingGuesses = [" _ " if isinstance(entry, int) else entry for entry in showGuessedResult]
# # print(showRemainingGuesses, "-> Prints out display in array with underline")
# # currentResults = " ".join(showRemainingGuesses)
# # print(currentResults)
# # # =======================================================================================================

# # def first():
# #     x = 47
# #     y = 11
# #     z = 12
# #     return x, y, z
    
# # def second(x1, y1, z1):
# #     print(x1, y1, z1)

# # x1, y1, z1 = first()
# # second(*first())


# # showRemainingGuesses = ['a', 'p', 'p', 'l', 'e', 's']
# # if showRemainingGuesses == letterList:
# #     print("success")
# # else:
# #     print("keep guessing")

# secretWord = "apples"
# secretWord = list(secretWord) # ['a', 'p', 'p', 'l', 'e', 's']
# lettersGuessed = ['a', 'e', 'l']

# # availableLetters = list(string.ascii_lowercase)
# # showRemainingGuesses = []

# def isWordGuessed(secretWord, lettersGuessed):
#     lettersGuessed.sort() # ['a', 'e', 'l', 'p', 'p', 's'] - sorted array
#     secretWord.sort() # ['a', 'e', 'l', 'p', 'p', 's'] - sorted array

#     if secretWord == lettersGuessed: 
#         print("All matches")
#     else:
#         print("not a match")


# def getGuessedWord(secretWord, lettersGuessed):
#     for letter in secretWord:
#         underscrolls = [" _ " if letter not in lettersGuessed else letter for letter in secretWord]
#         # underScrolls = secretWord.replace(letter, " _ ")
#         underscrollDisplay = " ".join(underscrolls)
    
#     return underscrollDisplay

#     # for letter in secretWord:
#     #     if letter not in lettersGuessed:
#     #         underScrolls = [" _ " if not in lettersGuessed else letter for letter in secretWord]
#     #         # underScrolls = secretWord.replace(letter, " _ ")
#     #         print(underScrolls)
#     # for x in lettersGuessed:
#     #     if set(lettersGuessed).issubset(set(secretWord)): 
    
#     #     print("yes")
#     # else:
#     #     print("no")
    
#     # while letter in secretWord:
#     #     print(letter)
#     #     indexOfNotMatch = secretWord.index(letter)
#     #     print(indexOfNotMatch, "ok")
#     #     lettersGuessed.insert(indexOfNotMatch, " _ ")

#     # print(z)


# def getAvailableLetters(lettersGuessed):
#     availableLetters = list(string.ascii_lowercase) # Pass
#     for letter in lettersGuessed:
#         if letter in availableLetters:
#             availableLetters.remove(letter)
#     availableLetters = ' '.join(availableLetters) # Pass
    
#     return availableLetters

# getGuessedWord(secretWord, lettersGuessed)
# isWordGuessed(secretWord, lettersGuessed)
# getAvailableLetters(lettersGuessed)
# temp = []
# lettersGuessed = ["a", "p", "p"]
# # for i in lettersGuessed:
# #     temp.append(lettersGuessed.index(i))
# # print(temp)

# print(a)

# def checkTryLimit():
#     for i in lettersGuessed:
#                 x = lettersGuessed.count(i) 
#             if x >= 8:
#                 isWordGuessed(secretWord, lettersGuessed)

    
# lettersGuessed = list(set(lettersGuessed)) 
# print(lettersGuessed)
# x = list(set(temp))
# print(x)
# print(type(x))
# def something():
#     for x in lettersGuessed:
#         if x == x:
#             lettersGuessed.remove(x)
#         else:
#             print("all good")
        
# something()

# x = set(len(lettersGuessed))
# print(x)

# x = ["a", "p", "p"].count
# print(x)

# countOf(lettersGuessed, "a")
# print(lettersGuessed)

for x in lettersGuessed:
    if set(lettersGuessed).issubset(set(secretWord): 
        print("yes")
    else:
        print("no")