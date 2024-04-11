import os
from art import logo_calculator


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo_calculator)
    is_over = False
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while not is_over:

        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        if num2 == 0 and operation == "/":
            print("Error: Cannot divide by zero. please try again.")
            return

        result = operations[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result},"
                       f"or type 'n' to start a new calculation,"
                       f"or type 'q' to quit: ").lower()

        if choice == 'y':
            num1 = result
        elif choice == 'n':
            is_over = True
            os.system('cls')  # Clearing the Screen
            calculator()
        elif choice == 'q':
            is_over = True
            print("Goodbye")
        else:
            print("Wrong input, please try again.")
            is_over = True


calculator()
