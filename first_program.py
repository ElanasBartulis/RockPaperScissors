import random
player_wins = 0
computer_wins = 0
score = 3

while player_wins < score and computer_wins < score:
	print(f"Player score : {player_wins} Computer score {computer_wins}")
	print("...rock...")
	print("...paper...")
	print("...scissors...")

	player = input("Enter Something: ").lower()
	if player == "quit" or player == "q":
		break
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
			player_wins += 1
		else:
			print("Computer Wins!")
			computer_wins += 1
	elif player == "scissors":
		if computer == "paper":
			print("Player Wins!")
			player_wins += 1
		else:
			print("Computer Wins!")
			computer_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("Player Wins!")
			player_wins += 1
		else:
			print("Computer Wins!")
			computer_wins += 1
	else:
		print("Something went wrong!")

if player_wins > computer_wins:
	print("CONGRATS , YOU WON!")
elif player_wins == computer_wins:
	print("IT'S A TIE")
else:
	print("BUMMER , YOU LOST :(")
