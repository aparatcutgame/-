from random import randint

print("Rock.....".lower())
print("Paper.....".lower())
print("Scissors.....".lower())




randomNumber = randint(0, 2)
computerMove = "rock"

if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
elif randomNumber == 2:
    computerMove = "scissors"



Player_1 = input("player_1 , Make your move : ").lower()
Player_2 = input(f"player_2 , Make your move : {computerMove}")
Player_2 = computerMove

if Player_1 == Player_2:
    print("thats a tie.....")
if Player_1 == "rock":
    if Player_2 == "scissors":
          print("Player_1 wins!.....")
    elif Player_1 == "paper":
            print("Player_2 wins!.....")

elif Player_1 == "scissors":
    if Player_2 == "paper":
        print("Player_1 wins!.....")
    elif Player_2 == "rock":
        print("Player_2 wins!.....")
else:
    print("something went wrong....")

if Player_1 == "rock" and Player_2 == "scissors":
   print("Player_1 wins!.....") 
elif Player_1 == "rock" and Player_2 == "paper":
    print("Player_2 wins!.....")
elif Player_1 == "paper" and Player_2 == "rock":
    print("Player_1 wins!.....") 
elif Player_1 == "paper" and Player_2 == "scissors":
    print("Player_2 wins!.....") 
elif Player_1 == "scissors" and Player_2 == "peper":
    print("Player_1 wins!.....") 
elif Player_1 == "scissors" and Player_2 == "rock":
    print("Player_2 wins!.....")
elif Player_1 == Player_2:
    print("thats a tie") 
else:
    print("something went wrong....")