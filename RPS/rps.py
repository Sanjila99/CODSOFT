# ----------Rock -Paper-Scissors-------------------------------------------------------------------------------
import random
from enum import IntEnum
class Action(IntEnum):
    rock = 0
    paper = 1
    scissors = 2

#set user_action to False 
def get_user_selection():    
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    while True:
        try:
          selection = int(input(f"Enter a choice ({choices_str}): "))
          return Action(selection)
        except ValueError:
            range_str=f"[0, {len(Action)-1}]"
            print(f"Invalid Selection.Enter a value in range{range_str}")
            
def get_computer_selection():
    selection = random.randint(0,len(Action)-1)
    action=Action(selection)
    return action

def determine_winner(user_action,computer_action):
      result=""
      if user_action==computer_action :
            result=f"Both players selected {user_action.name}.It's a tie!"
      elif user_action == Action.rock:
            result = f"You chose {user_action.name}, computer chose {computer_action.name}. "
            result += "Rock smashes scissors! You win!" if computer_action == Action.scissors else "Paper covers rock! You lose."
      elif user_action == Action.paper:
        result = f"You chose {user_action.name}, computer chose {computer_action.name}. "
        result += "Paper covers rock! You win!" if computer_action == Action.rock else "Scissors cuts paper! You lose."
      elif user_action == Action.scissors:
        result = f"You chose {user_action.name}, computer chose {computer_action.name}. "
        result += "Scissors cuts paper! You win!" if computer_action == Action.paper else "Rock smashes scissors! You lose."

      return result

    
while True:
    try:
     user_action = get_user_selection()
    except ValueError as e:
        range_str=f"[0,{len(Action)-1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue    
    
    computer_action = get_computer_selection()
    result_text=determine_winner(user_action,computer_action)
    print(result_text)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing! Goodbye!!")
        break    



   