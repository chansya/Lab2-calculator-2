"""CLI application for a prefix-notation calculator."""

from secrets import token_urlsafe
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cube)

while True:
    user_input = input("Enter equation: ")
    token = user_input.split()
    if len(token) >= 2:
        num1 = float(token[1])
    if len(token) >= 3:
        num2 = float(token[2])
    if len(token) >= 4:
        num3 = float(token[3])

    if token[0] == "q" or token[0] == "quit":
        break
    elif token[0] == "+":
        print(add(num1, num2))
    elif token[0] == "-":
        print(subtract(num1, num2))
    elif token[0] == "*":
        print(multiply(num1, num2))
    elif token[0] == "/":
        print(divide(num1, num2))
    elif token[0] == "square":
        print(square(num1))
    elif token[0] == "cube":
        print(cube(num1))
    elif token[0] == "pow":
        print(power(num1, num2))
    elif token[0] == "mod":
        print(mod(num1, num2))
    elif token[0] == "+*":
        print(add_mult(num1, num2, num3))
    elif token[0] == "+cube":
        print(add_cube(num1, num2))
    else:
        print("Invalid input")
# Replace this with your code
