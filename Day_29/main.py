from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website.title()}", message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    passwd_let = [choice(letters) for _ in range(nr_letters)]
    passwd_sym = [choice(symbols) for _ in range(nr_symbols)]
    passwd_num = [choice(numbers) for _ in range(nr_numbers)]

    password = passwd_let + passwd_num + passwd_sym
    shuffle(password)
    password = "".join(password)

    pass_entry.delete(0, END)
    pass_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

# LOGO
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website LABEL and ENTRY
website_label = Label(text="Website:")
website_entry = Entry(width=26)
website_entry.focus()
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1)

# Email/Username LABEL and ENTRY
email_label = Label(text="Email/Username:")
email_entry = Entry(width=44)
email_entry.insert(0, "moises.c.alcala@gmail.com")
email_label.grid(column=0, row=2)
email_entry.grid(column=1, row=2, columnspan=2)

# Password LABEL and ENTRY
pass_label = Label(text="Password:")
pass_entry = Entry(width=26)
pass_label.grid(column=0, row=3)
pass_entry.grid(column=1, row=3)

# Password BUTTON
pass_button = Button(text="Generate Password", command=generate_password, width=14)
pass_button.grid(column=2, row=3)

# Website BUTTON
website_button = Button(text="Search", command=find_password, width=14)
website_button.grid(column=2, row=1)

# ADD BUTTON
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, )

window.mainloop()
