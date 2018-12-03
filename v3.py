import random


rand_num = random.randint(0,2)
# print(rand_num)

if rand_num ==0:
    computer = "rock"
elif rand_num ==1:
    computer = "paper"
else:
     computer = "scissors"


player = input("Player what's your input")
# # computer = input("Player2 make your move ")
# # print(player)
# print( f"Computer plays {computer}")
#
# if player == computer:
#     print("It's a tie")
# elif (player == "rock" and computer == "scissors"): {
#         print ('player wins!!')
#         }
# elif (player== "paper" and computer == "rock"):{
#             print ('The winner is computer')
#  }
# elif (player== "scissors" and computer == "paper"):{
#             print ('The winner is computer')
#  }
# else:
#     print("Computer wins!!")
#
# #
# #
# # print("SHOOT!")
