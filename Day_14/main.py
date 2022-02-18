import random
import os
from art import logo, vs
from game_data import data


def random_number():
    n_data = len(data) - 1
    random_n = random.randint(0, n_data)
    return random_n


def random_people():
    n_rand = random_number()
    d_people = data[n_rand]
    return d_people


def compare_followers(a, b):
    if a > b:
        return "a"
    elif b > a:
        return "b"


def play():
    score = 0
    print(logo)
    while True:
        people_1 = random_people()
        people_2 = random_people()

        name_1 = people_1['name']
        description_1 = people_1['description']
        country_1 = people_1['country']
        followers_1 = people_1['follower_count']

        name_2 = people_2['name']
        description_2 = people_2['description']
        country_2 = people_2['country']
        followers_2 = people_2['follower_count']

        print(f"Compare A: {name_1}, a {description_1}, from {country_1}.\n{vs}\nCompare B: {name_2}, a {description_2}, from {country_2}")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer == compare_followers(followers_1, followers_2):
            score += 1
            os.system('clear')
            print(logo)
            print(f"You're right! Current score: {score}.")

        else:
            os.system('clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            break


if __name__ == '__main__':
    os.system('clear')
    play()