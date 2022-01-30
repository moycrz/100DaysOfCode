import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
print("Welcome to Rock Paper Scissors")
usr_choose = int(input("What do you choose?\n0 - Rock\n1 - Paper\n2 - Scissors.\nChoose: "))
random_choose = random.randint(0, 2)

print(game_images[usr_choose])
print(f"Computer chose:\n{game_images[random_choose]}")

if usr_choose == random_choose:
    print("It's a draw")

elif usr_choose  > random_choose:
    print("You win!")

elif usr_choose  < random_choose:
    print("You lose")