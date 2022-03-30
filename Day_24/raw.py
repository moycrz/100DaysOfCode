# Read File
with open("../../../../Users/cam/Desktop/new_file.txt") as file:
    content = file.read()
    print(content)

# Append File
# MODE: 'w' = write; 'a' = append; 'r' = read
with open("../../../../Users/cam/Desktop/new_file.txt", mode="a") as file:
    file.write("\nNew text.")

# Write File
# If doesn't exist a file with the same name, we create this
with open("../../../../Users/cam/Desktop/new_file.txt", mode='w') as file:
    file.write("\nNew text.")

