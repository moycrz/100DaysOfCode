# TODO: Create a letter using starting_letter.txt (moycrz version)

content_letter = []
names = []
with open("Input/Names/invited_names.txt") as data:
    name = data.readlines()
    for let in name:
        str_name = ""
        for letter in let:
            if letter != "\n":
                str_name += letter
            elif letter == "\n":
                pass
        names.append(str_name)

print(names)

with open("Input/Letters/starting_letter.txt") as file:
    content_letter = file.readlines()

on = True
n = 0

for actual_name in names:

    content_letter[0] = f'Dear  {actual_name},\n'
    str_content_letter = "".join(content_letter)

    with open(f"Output/ReadyToSend/letter_for_{actual_name}.txt", mode="w") as file:
        file.write(str_content_letter)

# ------------------------------------------------------------------------------------------
# TODO: Create a letter using starting_letter.txt (class version)
PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
            file.write(new_letter)