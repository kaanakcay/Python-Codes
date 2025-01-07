# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) #<_csv.reader object at 0x102b9a1f0>
#     print(data)
#     for row in data:
#         print(row) #['day', 'temp', 'condition']

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) #<_csv.reader object at 0x102b9a1f0>
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
#

import pandas

data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))

# average bulma yollari
average = sum(temp_list) / len(temp_list)
#veya pandas kullanarak
average = data['temp'].mean()

#max bulma
maximum = data['temp'].max()
print(maximum)
