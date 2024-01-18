def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def calculator():
    print("select operation:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")

    choice = input("Enter choice (1/2/3/4):")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result: ", add(num1,num2))
    elif choice == "2":
        print("Result: ", subtract(num1,num2))
    if choice == "3":
        print("Result: ", multiply(num1,num2))
    if choice == "4":
        print("Result: ", divide(num1,num2))

calculator()

