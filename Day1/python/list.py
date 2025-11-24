#!/usr/bin/python3

numbers = []

for i in range(1,6):
    numbers.append(i*10)

print("List elements are ...")
for i in range(5):
    numbers[i]

print("Number of elements in list are ", len(numbers))
print("Max element is list is ", max(numbers))
print("Min element is list is ", min(numbers))
