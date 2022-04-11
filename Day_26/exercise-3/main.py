
with open("file-1.txt") as data:
    list_1 = data.readlines()

with open("file-2.txt") as data:
    list_2 = data.readlines()

result = [int(content) for content in list_1 if content in list_2]

# Write your code above 👆

print(result)


