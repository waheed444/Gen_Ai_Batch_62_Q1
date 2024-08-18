
#WAHEED AHMAD  (Roll no: PIAIC-245268)
print("<----- Simple Calculator ----->")
num1 = float(input("Enter your first number: "))  
num2 = float(input("Enter your second number: "))
print("Operations available:")
print("Press 1. for  Addition")
print("Press 2. for Subtraction")
print("Press 3. for Multiplication")
print("Press 4. for Division")
choice = input("Enter your choice (1/2/3/4): ")
if choice == '1':
    result = num1 + num2        #Addition Operation
    print(f"Result: {result}")
elif choice == '2':
    result = num1 - num2       #Subtraction Operation
    print(f"Result: {result}")
elif choice == '3':
    result = num1 * num2       #Multiplication Operation
    print(f"Result: {result}")
elif choice == '4':       
    if num2 != 0:               #Division Operation 
        result = num1 / num2  
        print(f"Result: {result}")
    else:
        print("Error: Division by zero")   #Divsin by zero is not possible
else:
    print("Invalid input. Please enter a valid operation number (1/2/3/4).")


