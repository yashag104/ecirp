import os
import calc_art


def operate(n1, operator, n2):
    def add(n1, n2):
        r = n1+n2
        return r

    def multiply(n1, n2):
        return n1 * n2

    def subtract(n1, n2):
        r = n1-n2
        return r

    def divide(n1, n2):
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Cannot divide by zero."
    if operator == "+":
        return add(n1, n2)
    elif operator == "*":
        return multiply(n1, n2)
    elif operator == "/":
        return divide(n1, n2)
    elif operator == "-":
        return subtract(n1, n2)
    else:
        return "Enter a valid operator."


print(calc_art.logo)
result = float(input("What's your first number? "))
print("+\n-\n/\n*\n")
key = True
while key:
    operator = input("Pick an operator: ")
    n2 = float(input("What's the next number? "))
    result = operate(result, operator, n2)
    print(result)
    choice = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'end' to end the program: ")
    if choice.lower() == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        result = float(input("What's your first number? "))
    elif choice.lower() == "end":
        key = False
        os.system('cls' if os.name == 'nt' else 'clear')