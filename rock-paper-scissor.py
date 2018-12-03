print("...rock...")
print("...paper...")
print("...scissors...")

# test = input('name)
player1 = input("Player1 make your move ")
player2 = input("Player2 make your move ")
# print(player1)

if (player1== "rock" and player2 == "scissors"): {
        print ('The winner is player1')
        }
elif (player1== "rock" and player2 == "paper"):{
            print ('The winner is player2')
 }
elif player1 == "paper" and player2 =="rock":
    print("player1 wins!!")
elif player1 == "paper" and player2 =="scissors":
        print("player2 wins!!")
elif player1 == "scissors" and player2 =="rock":
    print("player2 wins!!")
elif player1 == "scissors" and player2 =="paper":
        print("player1 wins!!")
elif player1 == player2:
            print("It's a tie")
else:
    print("something went wrong")


print("SHOOT!")
