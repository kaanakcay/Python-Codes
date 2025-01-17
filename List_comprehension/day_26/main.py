 #Challange: 1 ile 5 arasinda range olsutur ve listedeki elemanlar range in iki kati olsuin
range_list =  [n*2 for n in range(1,5)]

#Challenge 4 harfden buyuk olanlari uppercase yap
names = ['kaan', 'veysel', 'ece', 'pinar', 'deniz']

upper_names = [name.upper() for name in names if len(name) > 4]

print(upper_names)


