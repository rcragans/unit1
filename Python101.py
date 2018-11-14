import random
userName = raw_input("What is your name? ")
secret_number = random.randint(1,10)
gameOn = True
allowedGuesses = 5
userGuesses = 0
keepPlaying = True

while(keepPlaying):

    while(gameOn):
        userGuess = input("Guess a number between 1 and 10: ")
        userGuesses += 1
        if (int(userGuess) == secret_number):
            gameOn = False
            print ("Great job %s. Game Over" % userName)
        else:
            if (userGuesses == allowedGuesses):
                gameOn = False
                print ("You are out of guesses! The number was %i" % secret_number)
            elif (int(userGuess) > int(secret_number)):
                print ("%s, %i is too high" % (userName,userGuess))
                print ("You have %i guesses left!") % (int(allowedGuesses)-int(userGuesses))
            else:
                print ("%s, %i is too low" % (userName, userGuess))
                print ("Guess again...")  
                print ("You have %i guesses left!") % (int(allowedGuesses)-int(userGuesses)) 
    playAgain = raw_input("Would you like to play again? Y or N")
    if (playAgain == "N"):
        keepPlaying = False
        print ("Thanks for playing, %s" % userName)
    elif(playAgain == "Y"):
        secret_number = random.randint(1,10)
        userGuesses = 0
        gameOn = True
    else:
        print ("Huh?")    
