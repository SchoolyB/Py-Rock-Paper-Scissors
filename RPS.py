import random
from time import sleep

userAction = input("Enter your choice(Rock,Paper,or Scissors)")

possibleCompActions = [

"Rock", 
"Paper",
"Scissors",
]

compAction = random.choice(possibleCompActions)


def Play_Again():

    if playAgain == 'y':
        print('OK! Lets play again!!!')
        game()
    elif playAgain == 'n':
        print('Ok goodbye...') 



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

game()

playAgain = input('Would you like to play again? y/n ')

Play_Again()



