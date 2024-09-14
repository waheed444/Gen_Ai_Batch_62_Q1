```python
# Get user's name
name = input("Enter your name: ")
# Get the three favorite numbers one by one from the user
num1 = int(input("Enter your 1st favorite number: "))
num2 = int(input("Enter your 2nd favorite number: "))
num3 = int(input("Enter your 3rd favorite number: "))
# Get the name from the user
print(f"\nHello, {name}! Let's explore your favorite numbers:")
```

```python
# Check if the first number is even or odd
if num1 % 2 == 0:
    print(f"The number {num1} is even.")
else:
    print(f"The number {num1} is odd.")

# Check if the second number is even or odd
if num2 % 2 == 0:
    print(f"The number {num2} is even.")
else:
    print(f"The number {num2} is odd.")

# Check if the third number is even or odd
if num3 % 2 == 0:
    print(f"The number {num3} is even.")
else:
    print(f"The number {num3} is odd.")

```

```python
# Print the number and its square for the first number
print(f"The number {num1} and its square: ({num1}, {num1 ** 2})")

# Print the number and its square for the second number
print(f"The number {num2} and its square: ({num2}, {num2 ** 2})")

# Print the number and its square for the third number
print(f"The number {num3} and its square: ({num3}, {num3 ** 2})")

```

```python
# Calculate the sum of the numbers
total_sum = num1 + num2 + num3
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

```

```python
# Print if the sum is a prime number
if total_sum < 2:
    is_prime = False
elif total_sum == 2:
    is_prime = True
elif total_sum % 2 == 0:
    is_prime = False
else:
    is_prime = True
    i = 3
# using while loop     
    while i * i <= total_sum:    
        if total_sum % i == 0:
            is_prime = False
            break
        i += 2
if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number!")

```