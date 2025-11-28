#!/usr/bin/python3

class Stack:
    def __init__(self):
        self.__numbers = []

    def push(self, value):
        self.__numbers.append(value)

    def pop(self):
        if ( len(self.__numbers) == 0 ):
            raise IndexError("Stack empty")
        return self.__numbers.pop()

    def top(self):
        if not self.__numbers:
            return None
        return self.__numbers[-1]

    def isEmpty(self):
        return len(self.__numbers) == 0
