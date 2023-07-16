import random 

def get_choices():
    options = ['rock', 'paper', 'scissors']
    player_choice = input("Enter a choice (paper, rock, scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    
    return choices

def check_win(player, computer):
    #print("You chose " + player + ", Computer chose " + computer)
    print(f"You choose {player} and computer choose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock" and computer == "scissors":
        return "Rock smashed scissors! You win!"
    elif player == "rock" and computer == "paper":
        return "Paper covers rock! You lose."
    elif player == "paper" and computer == "rock":
        return "Paper covers rock! You win!" 
    elif player == "paper" and computer == "scissors":
        return "Scissors cuts paper! You lose."
    elif player == "scissors" and computer == "paper":
        return "Scissors cuts paper! You win!"
    elif player == "scissors" and computer == "rock":
        return "Rock smashed scissors! You lose."
    
check_win("rock", "scissors")


