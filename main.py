import random 

def get_choices():
    options = ['rock', 'paper', 'scissors']
    player_choice = input("Enter a choice (paper, rock, scissors): ")
    computer_choice = random.choice(options)
    choices = {"user": player_choice, "computer": computer_choice}
    
    return choices

def check_win(player, computer):
    print("You chose " + player + ", Computer chose " + computer)
    if player == computer:
        return "It's a tie!"


