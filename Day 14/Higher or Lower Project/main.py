import random
from game_data import data
import art

print(art.logo)

def play_game():
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(art.vs)
    print(f"B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    if (followers_a > followers_b and guess == "a") or (followers_b > followers_a and guess == "b"):
        return True
    else:
        return False

score = 0
game_should_continue = True

while game_should_continue:
    if play_game():
        score += 1
        print(f"You got it right! Current score: {score}\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

print("Game over")
