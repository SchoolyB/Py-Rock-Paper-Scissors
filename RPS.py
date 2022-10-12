#VERSION 2.0.0
#AUTHOR: Marshall Burns a.k.a Schooly B


###IMPORTING THE 'RANDOM' LIBRARY TO ALLOW PYTHON TO MAKE RANDOM CHOICES###
import random
###IMPORTING THE 'SLEEP 'FUCNTION FROM THE 'TIME' LIBRARY TO ALLOW THE THE PROGRAM TO HAVE A TIME DELAY###
from time import sleep

###DECLARING 1ST VARIABLE TO BE USED WITHIN THE GAME() FUNTION. REPRESENTS USERS CHOICE###
userAction = input("Enter your choice(Rock,Paper,or Scissors)")

###DEFINING POSSOBLE CHOICES FOR COMPUTER###
possibleCompActions = [
"Rock", 
"Paper",
"Scissors",
]

###DECLARING 2ND VARIABLE TO BE USED WITHIN THE GAME() FUNTION. REPRESENTS COMPUTERS CHOICE###
compAction = random.choice(possibleCompActions)

###DECLARING A PLAY_AGAIN()FUNCTION###
def Play_Again():

    if playAgain == 'y':
        print('OK! Lets play again!!!')
        game()
    elif playAgain == 'n':
        print('Ok goodbye...') 

###DECLARING A GAME() FUNCTION. THIS FUNCTION CONTAINS THE GAME ITSELF###
def game():

    userAction = input("Enter your choice(Rock,Paper,or Scissors)")
    
    possibleCompActions = [

    "Rock", 
    "Paper",
    "Scissors",
    ]

    compAction = random.choice(possibleCompActions)
    

    if userAction == compAction:
        print('Both players selected ' + userAction  + ' ' + 'ITS A TIE!!!')
    elif userAction == "Rock":
        if compAction == "Scissors":
            print('You chose ' + userAction)
            sleep(2)
            print('The computer chose ' + compAction)
            sleep(2)
            print ("Rock smashes scissors. YOU WIN!!!")
        else:
            print('You chose ' + userAction)
            sleep(2)
            print('The computer chose ' + compAction)
            sleep(2)
            print ("Paper covers rock. YOU LOSE!!!")
    elif userAction == "Paper":
        if compAction == "Rock":
            print('You chose ' + userAction)
            sleep(2)
            print('The computer chose ' + compAction)
            sleep(2)
            print ("Paper covers rock. YOU WIN!!!") 
        else:
            print('You chose ' + userAction)
            sleep(2)
            print('The computer chose ' + compAction)
            sleep(2)
            print ("Scissors cut paper. YOU LOSE!!!")
    elif userAction  == "Scissors":
        if compAction == "Paper":
            print('You chose ' + userAction)
            sleep(2)
            print('The computer chose ' + compAction)
            sleep(2)
            print ("Scissors cuts paper. YOU WIN!!!")
        else:
            print('You chose ' + userAction)
            sleep(2)
            print('The computer chose ' + compAction)
            sleep(2)
            print ("Rock smashes scissors. YOU LOSE!!!")    


###CALLING THE GAME() FUNCTION###
game()

###DECLARING A VARIABLE TO BE USED TO EXECUTE THE PLAY_AGAIN() FUNTION###
playAgain = input('Would you like to play again? y/n ')

###CALLING THE PLAY_AGAIN FUNCTION()###
Play_Again()



