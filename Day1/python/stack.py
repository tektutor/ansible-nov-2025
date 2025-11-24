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

numberStack = Stack()
numberStack.push(10)
numberStack.push(20)
numberStack.push(30)

print("Is stack empty ", numberStack.isEmpty() )
print("Top most element ", numberStack.top() )
print("Popping out values from stack ....")

while ( not numberStack.isEmpty() ):
    print( numberStack.pop() )

