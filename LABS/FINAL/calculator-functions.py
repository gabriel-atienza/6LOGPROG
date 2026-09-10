#functions final lab activity

def add_num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
    print("The sum is:", result)

def subtract_num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 - num2
    print("The difference is:", result)

def multiply_num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 * num2
    print("The product is:", result)    

def divide_num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("The quotient is:", result)

#main program
print("Welcome to the Calculator Program!")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1-4): ")

match choice:
    case "1":
        add_num()
    case "2":
        subtract_num()
    case "3":
        multiply_num()
    case "4":
        divide_num()
    case _:
        print("Invalid choice. Please select a valid operation.")
        