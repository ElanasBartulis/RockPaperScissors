import random

print("...rock...")
print("...paper...")
print("...scissors...")

player = input("enter Player choice: ").lower()
random_num = random.randint(0,2)

#Comp logika
if random_num == 0:
	computer = "rock"
elif random_num == 1:
	computer = "paper"
else:
	computer = "scissors"
print(f"Computer showed ----> {computer} <----")

if player == computer:
	print("It's a draw")
elif player == "rock":
	if computer == "scissors":
		print("Player Wins!")
	else:
		print("Computer Wins!")
elif player == "scissors":
	if computer == "paper":
		print("Player Wins!")
	else:
		print("Computer Wins!")
elif player == "paper":
	if computer == "rock":
		print("Player Wins!")
	else:
		print("Computer Wins!")
else:
	print("Something went wrong!") 

#	p1 = input("Player 1: rock, paper, or scissors ")
#p2 = input("Player 2: rock, paper, or scissors ")
 
#if p1 == p2:
#    print("Draw")
#elif p1 == "rock" and p2 == "scissors":
#   print("p1 wins")
#elif p1 == "paper" and p2 == "rock":
#    print("p1 wins")
#elif p1 == "scissors" and p2 == "paper":
#    print("p1 wins")
#else:
#    print("p2 wins")