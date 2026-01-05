print(r"""
                                 |--__
                                 |
                                 X
                        |-___   / \       |--__
                        |      =====      |
                        X      | .:|      X
                       / \     | O |     / \
                      =====   |:  . |   =====
                      |.: |__| .   : |__| :.|
                      |  :|. :  ...   : |.  |
              __   __W| .    .  ||| .      :|W__  --
            -- __  W  WWWW_______________WWWW   W -----  --
        -  -     ___  ---    ____     ____----       --__  -
            --__    --    --__     -___        __-   _
""")

print("Welcome to the Wizard Castle!")
print("Your mission is to graduate from the Magic Academy.")

subject = input("Choose your first subject (swordsmanship or spells): ").lower()

if subject == "swordsmanship":
    print("The Professor hands you a magical sword.\n")
    explore = input("Do you want to explore the surroundings of the academy? (Y/N): ").lower()

    if explore == "y":
        print("A gargoyle appears! You fight bravely but fall into a ravine...\nGame Over!")
    else:
        print("You continue your studies as a magic knight, but an ancient demon emerges and destroys the academy.\nGame Over!")

elif subject == "spells":
    print("The Professor gives you an ancient grimoire.\n")
    study_spell = input("Do you want to uncover the secrets of the grimoire? (Y/N): ").lower()

    if study_spell == "y":
        print("You learn how to summon an ancient sealed demon.\n")
        continue_grimoire = input("Do you want to keep studying the grimoire? (Y/N): ").lower()

        if continue_grimoire == "y":
            print("The demon escapes your control and destroys the entire academy.\nGame Over!")

        elif continue_grimoire == "n":
            print("You settle for what you've learned and return to class.\n")
            print("Two years later, the academy is under attack!")
            final_choice = input("Choose 'grimoire' or 'war': ").lower()

            if final_choice == "war":
                print("You fight bravely, but there are too many enemies. You were defeated.\nGame Over!")

            elif final_choice == "grimorie":
                print("You summon the demon, who obliterates all enemies.\n")
                print("The professor awards you a medal of honor!")
                print("You graduated! Congratulations, you won!")

    else:
        print("You didn't study enough and were expelled.\nGame Over!")

else:
    print("Invalid option! The castle gates close. Try again.")
