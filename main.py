import random 

def get_choices():
    options = ['rock', 'paper', 'scissors']
    user_choice = input("Enter a choice (paper, rock, scissors): ")
    computer_choice = random.choice(options)
    choices = {"user": user_choice, "computer": computer_choice}
    
    return choices

choice = get_choices()
print(choice)