# #################### Extra Hard Starting Project ######################
import datetime as dt
import os
import pandas
import random
import smtplib

MY_EMAIL = ""
PASSWORD = ""
PLACEHOLDER = "[NAME]"
now = dt.datetime.now()
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

def check_birthday():
    os.system('clear')
    for birth in birthdays:
        if birth['month'] == now.month and birth['day'] == now.day:
            print(f"Today is a {birth['name']}'s birthday")
            birth_name = birth["name"].strip()
            birth_email = birth["email"].strip()
            with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as data_letter:
                letter = data_letter.read()
                letter_template = letter.replace(PLACEHOLDER, birth_name)

            answer = input("Do you want to send a birthday greeting?(yes or no): ")

            if answer == 'yes':
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()  # make the connection secure
                    connection.login(user=MY_EMAIL, password=PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=birth_email,
                        msg=f"Subject: Happy Birthday {birth_name} :D\n\n{letter_template}"
                    )
                    print("Successfully sent")
            else:
                print("See you")


if __name__ == '__main__':
    usr_answer = int(input("What do you want to do?:\n1.- Add Birthday\n2.- Check Birthday\nType a number: "))
    if usr_answer == 1:
        birthday_update()
    elif usr_answer == 2:
        check_birthday()
    else:
        print("Value out of range")
