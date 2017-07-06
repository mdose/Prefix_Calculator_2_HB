"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input("> ")
    token = user_input.split(" ")
    if token[0] == "q":
        break
    else:
        if user_input[0] == "+":
            print arithmetic.add(user_input[1:])

