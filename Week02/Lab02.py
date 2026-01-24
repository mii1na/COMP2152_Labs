import random

choices = ["Rock", "Paper", "scissors"]

playerChoice= input("Enter the number 1 to 3 for the folloing choices 1-Rock, 2-paper, 3-scisseors: ")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice >3:
    print("Error: Choice shoud be between 1 and 3!")
else: 
    
    # Develop the game logic use if/elif/else
    computerChoice = random.randint(1, 3)

    if playerChoice == computerChoice:
        print("It's tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors -- You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock -- You win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper -- You win!")
    else:
        print("You lose!")