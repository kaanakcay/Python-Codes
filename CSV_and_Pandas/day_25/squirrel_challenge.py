#based on Primary Fur Color of squirells (gray, cinnamon, black) calculate count of each and create new csv col: fur color and count

import pandas

data=pandas.read_csv("squirrel_count.csv")


print(data["Primary Fur Color"])

# Ezik yontem
grey_count = 0
black_count = 0
cinnamon_count = 0

for color in data["Primary Fur Color"]:
    print(color)
    if color == "Gray":
        grey_count += 1
    elif color == "Cinnamon":
        cinnamon_count += 1
    elif color == 'Black':
        black_count += 1

data_dict = {
    'Fur Color': ["Gray", "Cinnamon", 'Black'],
    'Count': [grey_count, cinnamon_count, black_count]
}

output_data = pandas.DataFrame(data_dict)
output_data.to_csv('squirrel_output')

#Ezik olmayan yontem
grey_count = len(data[data["Primary Fur Color"] == 'Gray'])
black_count = len(data[data["Primary Fur Color"] == 'Black'])
cinnamon_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])

