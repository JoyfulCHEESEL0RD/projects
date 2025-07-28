import math

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number."
    return math.sqrt(x)
def power(x, y):
    return x ** y
def modulus(x, y):
    return x % y
def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number is undefined."
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
def calculator():
    print("Welcome to the Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Modulus")
    print("8. Factorial")
    while True:
        choice = input("Enter choice (1-8): ")
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
            if choice in ['1', '2', '3', '4', '6', '7']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                if choice == '1':
                    print(f"{x} + {y} = {add(x, y)}")
                elif choice == '2':
                    print(f"{x} - {y} = {subtract(x, y)}")
                elif choice == '3':
                    print(f"{x} * {y} = {multiply(x, y)}")
                elif choice == '4':
                    print(f"{x} / {y} = {divide(x, y)}")
                elif choice == '6':
                    print(f"{x} ^ {y} = {power(x, y)}")
                elif choice == '7':
                    print(f"{x} % {y} = {modulus(x, y)}")
            elif choice == '5':
                x = float(input("Enter number: "))
                print(f"Square root of {x} = {square_root(x)}")
            elif choice == '8':
                x = int(input("Enter a non-negative integer: "))
                print(f"Factorial of {x} = {factorial(x)}")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 8.")
if __name__ == "__main__":
    calculator()