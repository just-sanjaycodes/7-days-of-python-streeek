# Calculate the factorial of a number using a loop.
number = 5
factorial = 1

if number < 0:
    print("Factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}")


# Print the multiplication table of a given number (1 to 10).
n = int(input("Enter:1-10"))
for i in range(1, 10):
    print(f"{n}X{i}={n * i}")
