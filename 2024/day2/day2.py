# Advent of Code 2024
# Day 2: Red-Nosed Reports

#read the input file
f = open('input.txt', 'r')
input = f.read().split("\n")

output = []

#split rows into arrays
for i in range(len(input)):
    row = input[i].split(" ")

    if(row[0] > row[1]):
        print('larger')

    elif(row[0] < row[1]):
        print('smaller')          

    else:
        output.append(False)

print(output)