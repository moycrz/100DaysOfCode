# #################### Extra Hard Starting Project ######################
import datetime as dt
import os
import pandas
import random
import smtplib

MY_EMAIL = "moises.crza@gmail.com"
PASSWORD = "J@maicanegra2708"
PLACEHOLDER = "[NAME]"
now = dt.datetime.now()
random_letter = []
new_birthday = {}

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")


# TODO: 1. Update the birthdays.csv
def birthday_update():
    global new_birthday

    while True:
        try:
            name = input("What is her/his name?: ").title()
            day = int(input("In what day she/he was born?: "))
            month = int(input("In what month she/he was born?: "))
            year = int(input("In what year she/he was born?: "))
        except ValueError:
            print("You can only use numbers in 'day', 'month' and 'year', try again")
            birthday_update()
        else:
            email = input("What is her/his email?: ")
            new_birthday = {
                'name': f'{name}',
                'email': f'{email}',
                'year': f'{year}',
                'month': f'{month}',
                'day': f'{day}'
            }
            birthdays.append(new_birthday)
            data_frame = pandas.DataFrame(birthdays)
            data_frame.to_csv("birthdays.csv", index=False)

        if input("Do you want to add any birthdays?(yes or no): ").lower() == 'no':
            break
        else:
            os.system('clear')
            pass


# TODO: 2. Check if today matches a birthday in the birthdays.csv
# TODO: 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
#  name from birthdays.csv
# TODO: 4. Send the letter generated in step 3 to that person's email address.

for birth in birthdays:
    if birth['month'] == now.month and birth['day'] == now.day:
        birth_name = birth["name"].strip()
        birth_email = birth["email"].strip()
        with open("letter_templates/letter_1.txt") as data_letter:
            letter = data_letter.read()
            letter_1 = letter.replace(PLACEHOLDER, birth_name)
            random_letter.append(letter_1)
        with open("letter_templates/letter_2.txt") as data_letter:
            letter = data_letter.read()
            letter_2 = letter.replace(PLACEHOLDER, birth_name)
            random_letter.append(letter_2)
        with open("letter_templates/letter_3.txt") as data_letter:
            letter = data_letter.read()
            letter_3 = letter.replace(PLACEHOLDER, birth_name)
            random_letter.append(letter_3)

        letter = random.choice(random_letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # make the connection secure
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birth_email,
                msg=f"Subject: Happy Birthday {birth_name} :D\n\n{letter}"
            )
            print("Successfully sent")
