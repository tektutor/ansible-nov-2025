#!/usr/bin/python3

firstString = "Some"
secondString = "String"
print(firstString)
print(secondString)
result = firstString + secondString
print("Cancatenated string is ", result )
print("---------------------------------------")
s = "Advanced Python"
print(s)
length = len(s)
print("Length of string ", s, " is ", length )

#First letter in the string s
print( s[0] ) # Print 'A'

#Last letter in the string s
print( s[length-1] )
print( s[-1] )

#convert to Upper case
print(s.upper())
print(s.lower())

