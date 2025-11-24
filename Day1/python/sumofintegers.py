#!/usr/bin/python3

#Converting string input to integer - type casting 
min_value = int( input ("Enter the lower bound of the range of integers: ") )
max_value = int( input ("Enter the upper bound of the range of integers: ") )

print ( "Minimum value of the range is :", min_value )
print ( "Maximum value of the range is :", max_value )

print ( "Type of min_value is ", type(min_value) )
print ( "Type of max_value is ", type(max_value) )

sum = 0
for i in range(min_value, max_value):
    sum = sum + i

print("The sum of range(",min_value,",", max_value, ")", " is ", sum )
