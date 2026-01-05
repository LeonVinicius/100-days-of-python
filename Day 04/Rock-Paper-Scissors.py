import random


rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
"""

scissors_art = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
"""

print("Let's play Rock, Paper, Scissors!")

player_choice = int(input("Choose 0 = Rock, 1 = Paper, 2 = Scissors: "))

computer_choice = random.randint(0, 2)

choices = ["Rock", "Paper", "Scissors"]

if player_choice == 0:
    print(rock_art)
elif player_choice == 1:
    print(paper_art)
elif player_choice == 2:
    print(scissors_art)
else:
    print("Invalid choice.")


print("You chose:", choices[player_choice])

print("Computer chose:", choices[computer_choice])

if computer_choice == 0:
    print(rock_art)
elif computer_choice == 1:
    print(paper_art)
else:
    print(scissors_art)

if player_choice == computer_choice:
    print("It's a draw!")

elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
