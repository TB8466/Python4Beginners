#Combine the lists
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

clothes = [(color, size) for color in colors for size in sizes]
print(clothes)

#Create a new list only containing ("Black","m") & ("White","s")
soldout = [(color, size) for (color, size) in clothes if (color, size) == ('Black', 'm') or (color, size) == ('White', 's')]

print("Sold out:",soldout)