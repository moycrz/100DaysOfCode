import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray, red, black]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")

print(data)
