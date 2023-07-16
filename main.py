import random 

def get_choices():
    options = ['rock', 'paper', 'scissors']
    player_choice = input("Enter a choice (paper, rock, scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    
    return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == "rock" or player == "paper" or player == "scissors":
    
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
  else:
      return "You must chose rock, paper or scissors, nothing else"
  
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)



