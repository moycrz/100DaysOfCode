import random
import os
from Day_7_art import logo, stages
from Day_7_words import word_list

chosen_word = random.choice(word_list)
display = ["_" for i in range(0, len(chosen_word))]
game = True
lives = 7
pos_display = 6
lives_stage = stages[pos_display]

#Step 3

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ["_" for _ in range(len(chosen_word))]

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while game:
    os.system("clear")
    print(logo)
#     print(f"The word is: {chosen_word}")
    print(f"You have {lives} lives\n{lives_stage}\n{display}\n")
    guess = input("Guess a letter: ").lower()


    #Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
            if lives > 0:
                lives -= 1
                pos_display -= 1

    print("\n")

    if lives == 0:
            answer = input("You lost, Would you like to play again?, Yes or No: ").lower()
            if answer == "yes":
                chosen_word = random.choice(word_list)
                display = ["_" for i in range(0, len(chosen_word))]
                os.system("clear")
            else:
                game = False
                os.system("clear")
                print("\n\n\tSee you next time\n\n")

