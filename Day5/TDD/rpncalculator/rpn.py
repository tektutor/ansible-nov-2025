#!/usr/bin/python3

from stack import Stack

class RPNError(Exception):
    """Custom exception for RPN Calculator exceptions."""
    pass

class RPNCalculator:

    def __init__(self):
        self.numberStack = Stack()

    # "10 3 * 100 20 / -"
    def evaluate( self, rpnMathExpression ):
        firstNumber  = 0
        secondNumber = 0
        result       = 0

        tokens = rpnMathExpression.split()
        #print(tokens)
        count = len(tokens)

        for index in range(count):
            if tokens[index].isdigit():
                self.numberStack.push( int(tokens[index]) )
            elif tokens[index] == "+":
                secondNumber = self.numberStack.pop()
                firstNumber = self.numberStack.pop()
                result = firstNumber + secondNumber 
                self.numberStack.push( result )
            elif tokens[index] == "-":
                secondNumber = self.numberStack.pop()
                firstNumber = self.numberStack.pop()
                result = firstNumber - secondNumber 
                self.numberStack.push( result )
            elif tokens[index] == "*":
                secondNumber = self.numberStack.pop()
                firstNumber = self.numberStack.pop()
                result = firstNumber * secondNumber 
                self.numberStack.push( result )
            elif tokens[index] == "/":
                secondNumber = self.numberStack.pop()
                firstNumber = self.numberStack.pop()
                result = firstNumber / secondNumber 
                self.numberStack.push( result )


        if not self.numberStack.isEmpty():
            return self.numberStack.pop()
        else:
            return 0
