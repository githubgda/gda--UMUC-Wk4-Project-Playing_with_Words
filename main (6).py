### Setup Section ###

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):
  #index = 0
  #print(guess, actual)  #TEST
  # Loop through each index/position
  for index in range(6):
  #for guessChar in guess:
    #for actualChar in actual:
    # Grab the letter from the guess
    letter = guess[index]
      #print(letter)  #TEST
    
    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    #if guessChar == actualChar:
        #print(f"{letter} is in {actual}")
        
    position = index
    secret = actual
    numberOfTimes = 0

    #for numChars in range(len(userGuess)):
    for guessChar in letter:
      #for guessChar in userGuess
      if guessChar in actual:
        numberOfTimes = actual.count(guessChar)
    
    # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
    if (letter == actual[position]):
    
            # Then print it out with a green background
      printColorfulLetter(letter, True, True)
    
          # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
    else:
      if numberOfTimes > 0:
            #for correctChar in guess:
            #  if correctChar == guess:
            #nextChar = index +1
            #if guessChar == actualChar:
      # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True)
      # ...but if the letter is not in the word at all...
      else:
        # ...print it out with a red background
        printColorfulLetter(letter, False)
  
    # Don't worry about the line of code below, it works. It just handles the transition between colors
  print(Style.RESET_ALL + " ", end="")

# TO-DO: Write a Function that takes in a six-lettered word from the user
#getSixLetterInput() function
def getSixLetterInput(): 
  secretGuess = ""
  
  while(len(secretGuess) != 6):
    secretGuess = input("Try to guess the secret word by entering a six letter word: ")
    
 # print(secretGuess)
  #print("A six letter secret word was enter")
  return secretGuess
  
# This marks the end of the function definitions, below this is where the program will actually start!

### Main Program ###

# TO-DO: Write the logic of the game here!
tries = 5
while (tries != 0):
  secretWord = "python"
  userGuess = getSixLetterInput()
  if(userGuess != secretWord):
    printGuessAccuracy(userGuess, secretWord)
    tries = tries - 1
    if tries == 0:
      print()
      print (f"Sorry, all five (5) of you tries have been used up. Game Over!!!  :)")
    else:
      print()
  else:
    printGuessAccuracy(userGuess, secretWord)
    print()
    print (f"Congratulations you guessed the secret word: {secretWord}")
    tries = 0