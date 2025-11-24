#!/usr/bin/python3

x = int( input ("Enter a number: " ) )
reverse = 0

while x > 0:
    digit = x % 10 
    reverse = reverse * 10 + digit
    x = x // 10

print("Reversed number is :", reverse )
