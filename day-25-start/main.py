# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# # print(data)
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))# Dataframe
# # print(type(data["temp"]))# Series
# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].to_list()
# # print(temp_list)
# # print(data["temp"].max())
# # print(sum(temp_list)/len(temp_list))
# # print(data.condition)
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
# # monday_row = data[data.day == "Monday"]
# # monday_temp = monday_row.temp
# # monday_f = (monday_temp * 9/5) + 32
# # print(monday_f)
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Primary_Fur_Color = data["Primary Fur Color"]
# print(Primary_Fur_Color)
rows_of_grey = len(data[data["Primary Fur Color"] == "Gray"])
rows_of_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
rows_of_black = len(data[data["Primary Fur Color"] == "Black"])

dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [rows_of_grey, rows_of_red, rows_of_black]
}
data = pd.DataFrame(dict)
data.to_csv("squirrel-count.csv")

