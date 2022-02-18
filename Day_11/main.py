from art import logo, goodbye
import random
import os
import time

def compare(computer_cards, usr_cards):
    if sum(computer_cards) > sum(usr_cards) or sum(usr_cards) > 21:
        return "You went over. You lose 😭"

    elif sum(computer_cards) > 21:
        return "Opponent went over. You win 😁"
        
    elif sum(usr_cards) > sum(computer_cards) and sum(usr_cards) <= 21:
        return "You win 😁"

    elif sum(computer_cards) == sum(usr_cards):
        return "Draw 🙃"


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def play_game():
    while True:
        os.system("clear")
        computer_cards = []
        usr_cards = []

        for _ in range(2):
            usr_cards.append(deal_card())
            computer_cards.append(deal_card())


        print(logo,f"\n\tYour cards: {usr_cards}, current score: {sum(usr_cards)}\n\tComputer's first card: {computer_cards[0]}")

        while sum(usr_cards) <= 21:    
            usr_desicion = input("\nType 'y' to get another card, type 'n' to pass: ")

            if usr_desicion == "y":
                usr_cards.append(deal_card())
                computer_cards.append(deal_card())

                print(f"Your cards: {usr_cards}, current score: {sum(usr_cards)}\n\tComputer's first card: {computer_cards[0]}")


            elif usr_desicion == "n":
                break                

        print(f"\tYour final hand: {usr_cards}, final score: {sum(usr_cards)}\n\tComputer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print(compare(computer_cards, usr_cards))
        
        
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
            continue

        else:
            os.system("clear")
            print(goodbye)
            time.sleep(2)
            os.system("clear")
            break


if __name__ == '__main__':
    os.system("clear")
    usr_answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if usr_answer == "y":
        play_game()   

    else: 
        os.system("clear")
        print(goodbye)
        time.sleep(2)
        os.system("clear")