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
        #int_tokens = int(token[1])
        if token[0] == "q":
            break
        elif token[0] == "+":
            print add(int(token[1]), int(token[2]))
        elif token[0] == "-":
            print subtract(int(token[1]), int(token[2]))
        elif token[0] == "*":
            print multiply(int(token[1]), int(token[2]))
        elif token[0] == "*":
            print multiply(int(token[1]), int(token[2]))
        elif token[0] == "/":
            print divide(int(token[1]), int(token[2]))
        elif token[0] == "square":
            print square(int(token[1]))
        elif token[0] == "cube":
            print cube(int(token[1]))
        elif token[0] == "pow":
            print power(int(token[1]), int(token[2]))
        elif token[0] == "mod":
            print mod(int(token[1]), int(token[2]))
        elif token[0] == "x+":
            print add_mult(int(token[1]), int(token[2]), int(token[3]))
        elif token[0] == "cubes+":
            print add_cubes(int(token[1]), int(token[2]))
        else:
            print "That's not a valid entry. Please enter an operand and intergers."
    except IndexError:
        print "That's not a valid entry. Please enter an operand and intergers."
