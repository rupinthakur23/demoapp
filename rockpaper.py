import random
x=random.randint(0,3)
computer=None 
player_score=0
computer_score=0
winning_score=2
if x==1:
	computer="Rocks"
elif x==2:
	computer="Scissors"
else:
	computer="Paper"


while player_score<winning_score and computer_score<winning_score:
	print(f"player1 score is {player_score}, computer score is{computer_score} ")
	print("Player1 enter your choice")
	player1=input()

	print("Computer chooses " + computer)
	if player1==computer:
		print("It;s a tie!")
	elif player1 =="Rocks":
		if computer== "Scissors":
			print("Player1 wins")
			player_score+=1
		
		elif computer=="Paper":
			print("Computer wins!")
			computer_score+=1
	elif player1=="Scissors":
		if computer=="Rocks":
			print("computer wins!")
			computer_score+=1

		elif computer=="Paper":
			print("Player1 wins Wins")
			player_score+=1
	elif player1=="Paper":
		if computer=="Scissors":
			print("computer wins!")
			computer_score+=1

		elif computer=="rocks":
			print("Player1 Wins")
			player_score+=1
	else:
		print("Invalid input")









