"""A prefix-notation calculator.

Using the py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    try:
        user_input = raw_input("> ")
        token = user_input.split(" ")
        num1 = int(token[1])
        if len(token) > 2:
            num2 = int(token[2])
        if len(token) > 3:
            num3 = int(token[3])
        if token[0] == "q":
            break
        elif token[0] == "+":
            print add(num1, num2)
        elif token[0] == "-":
            print subtract(num1, num2)
        elif token[0] == "*":
            print multiply(num1, num2)
        elif token[0] == "*":
            print multiply(num1, num2)
        elif token[0] == "/":
            print divide(num1, num2)
        elif token[0] == "square":
            print square(num1)
        elif token[0] == "cube":
            print cube(num1)
        elif token[0] == "pow":
            print power(num1, num2)
        elif token[0] == "mod":
            print mod(num1, num2)
        elif token[0] == "x+":
            print add_mult(num1, num2, num3)
        elif token[0] == "cubes+":
            print add_cubes(num1, num2)
        else:
            print "That's not a valid entry. Please enter an operand and intergers."
    except IndexError:
        print "That's not a valid entry. Please enter an operand and intergers."
