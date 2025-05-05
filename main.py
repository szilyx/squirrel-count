from traceback import print_tb

import csv
import pandas

data = pandas.read_csv("../2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squarell = len(data[data["Primary Fur Color"] == "Gray"])
red_squarell = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squarell= len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[gray_squarell, red_squarell, black_squarell]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirel_count.csv")
