# WAHEED AHMAD  (Roll no: PIAIC-245268)
def add(num1, num2):
    return num1 + num2  # Addition

def subtract(num1, num2):
    return num1 - num2  # Subtraction

def multiply(num1, num2):
    return num1 * num2  # Multiplication

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2  # Division
    else:
        return "Error: Division by zero"

# Main calculator function
def calculator():
    print("<----- Simple Calculator ----->")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    
    print("Operations available:")
    print("Press 1. for Addition")
    print("Press 2. for Subtraction")
    print("Press 3. for Multiplication")
    print("Press 4. for Division")
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid input. Please enter a valid operation number (1/2/3/4).")

# Run the calculator Function
calculator()
