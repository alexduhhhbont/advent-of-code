# Advent of Code 2024
# Day 1: Historian Hysteria

#read the input file
f = open('input.txt', 'r');
input = f.read().split("\n")
input = [i.split() for i in input]

#split the input into two arrays
arrayA = []
arrayB = []
for i in range(len(input)):
    arrayA.append(input[i][0])
    arrayB.append(input[i][1])

#sort the arrays
arrayA = sorted(arrayA)
arrayB = sorted(arrayB)

#
# Part 1
#

#calculate the absolute sum difference between the two arrays
sum = 0
for i in range(len(arrayA)):
    sum += abs(int(arrayA[i]) - int(arrayB[i]))

print(sum)

#
# Part 2
#

#calculate the how many times each number from the first array appears in the second array
#store count per number in a dictionary
count = {}
def storeCount(number):
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

for i in range(len(arrayA)):
    for j in range(len(arrayB)):
        if arrayA[i] == arrayB[j]:
            storeCount(arrayA[i])

#in count, multiply the key by the value and sum all the values
sumCount = 0
for key, value in count.items():
    sumCount += int(key) * value

print(sumCount)