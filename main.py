import random

while True:
  user_action = input("Enter a choice (R, P, S): ")
  possible_actions = ["R", "P", "S"]    
  while user_action not in possible_actions:
        print("Please enter a valid choice")
        user_action = input("Enter a choice (R, P, S): ")
        
  if user_action == "R":  
      action_name = 'Rock'
  elif user_action == "P":  
      action_name = 'Paper' 
  else:  
      action_name = 'Scissors'

  computer_action = random.choice(possible_actions)
 
  while computer_action == user_action:
       computer_action = random.choice(possible_actions)
  if computer_action == "R":  
      comp_action_name = 'Rock'
  elif computer_action == "P":  
      comp_action_name = 'Paper' 
  else:  
      comp_action_name = 'Scissors'

  print(f"\nPlayer({action_name}) : CPU({comp_action_name})\n")
 
  while user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
    user_action = input("Enter a choice (R, P, S): ")
  if user_action == "R":
    if computer_action == "S":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
  elif user_action == "P":
    if computer_action == "R":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
  elif user_action == "S":
    if computer_action == "P":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

  break