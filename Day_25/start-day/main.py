# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# # print(f"The media temperature is: {round(average, 2)}")
#
# mean_temp = data["temp"].mean()
max_temp = data.temp.max()
#
# print(f"Mean: {mean_temp}\nMax: {max_temp}")
# print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
monday_temp = monday.temp * 1.8 + 32
# print(monday_temp)


# TODO: Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

