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
  # Loop through each index/position
  for index in range(6):
    # Grab the letter from the guess
    letter = guess[index]
         
    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
            
    position = index
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
   #Return the word that user/player entered 
  return secretGuess
  
# This marks the end of the function definitions, below this is where the program will actually start!

### Main Program ###

# TO-DO: Write the logic of the game here!
#Used to establish the number of tries/guesses allow
tries = 5

#While thw five (5) quesses have not been exhausted allow player to enter guesses
while (tries != 0):
  secretWord = "python"
  userGuess = getSixLetterInput()
  # If the guess is not the secret word try again
  if(userGuess != secretWord):
    printGuessAccuracy(userGuess, secretWord)
    tries = tries - 1
    # If five (5) tries have been exhausted terminated game
    if tries == 0:
      print()
      print (f"Sorry, all five (5) of you tries have been used up. Game Over!!!  :)")
     # else give player another guess attempt 
    else:
      print()
  #If player enter the secret word, player wins and game is over    
  else:
    printGuessAccuracy(userGuess, secretWord)
    print()
    print (f"Congratulations you guessed the secret word: {secretWord}")
    tries = 0