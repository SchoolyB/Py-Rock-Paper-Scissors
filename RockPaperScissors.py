import random

userAction = input("Enter your choice(Rock,Paper,or Scissors)")


possibleActions = ["Rock" , "Paper", "Scissors"]
compAction = random.choice(possibleActions)

print(f"\nYou chose {userAction}, the computer chose {compAction}. \n")

if userAction == compAction:
    print("Both players selected {userAction}. It's a tie.")
elif userAction == "Rock":
    if compAction == "Scissors":
        print ("Rock smashes scissors. YOU WIN!!!")
    else:
       print ("Paper covers rock. YOU LOSE...")
elif userAction == "Paper":
    if compAction == "Rock":
        print ("Papaer covers rock. YOU WIN!!!") 
    else:
        print ("Scissors cut paper. YOU LOSE...")
elif userAction  == "Scissors":
    if compAction == "Paper":
        print ("Scissors cut paper. YOU WIN!!!")
    else:
        print ("Rock smashes scissors. YOU LOSE...")
