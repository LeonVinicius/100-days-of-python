import random
from arts import stage, logo
from palavras import lista_de_palavras


word = random.choice(lista_de_palavras)
word = word.lower()

print(logo)


display = "_" * len(word)
print(display)

correct_letters = []
wrong_letters = []
lives = 6
game_over = False


print(stage[lives])

while not game_over:
    guess = input("Guess a letter: ").lower()


    if guess in correct_letters or guess in wrong_letters:
        print(f"You already guessed the letter '{guess}'. Try another one.")
        continue


    new_display = ""
    for letter in word:
        if letter == guess:
            new_display += letter
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"


    if guess in word:
        correct_letters.append(guess)
        display = new_display
        print(display)

        if "_" not in display:
            print("--------------------------------------")
            print("You won! Congratulations!")
            print(f"The word was: {word}")
            print("--------------------------------------")
            game_over = True

    else:

        wrong_letters.append(guess)
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
        print(stage[lives])

        if lives == 0:
            print("--------------------------------------")
            print("Game Over! You lost!")
            print(f"The word was: {word}")
            print("--------------------------------------")
            game_over = True
