#  Section 1: Variables, Data Types, Input/Output (Q1–10)
# 1.Print your name, age, and city on three separate lines using three print()
# statements.

print("Karan")
print(int(25))
print("bombay")

# 2.Store your name, age, and GPA in three variables of appropriate types and print them
# using an f-string in one sentence.
name = "Karan sharma"
age = 22
gpa = 9.4
print(f"name is {name}\n age:{age}\n student gpa is {gpa}")

# 3.Take a user's name as input and print "Hello, <name> !"
name = input("Enter the name: ")
print(f"name is {name}")

# 4.Take two numbers as input (as strings by default) and print their sum as integers.
num1 = "2"
num2 = "4"
print(int(num1 + num2))

# 5.Swap the values of two variables a and b without using a third variable.

a = 2
b = 5
a, b = b, a
print(a, b)

# 6. Check and print the data type of: 5 , 5.0 , "5" , True , [5] using type() .
print(type(5))
print(type(5.0))
print(type("5"))
print(type(True))
print(type([5]))

# 7. Convert a float 3.99 to an int and print it. Explain (in a comment) what happens to
# the decimal part.

gpa = 3.99
print(int(gpa))
# The float is converted into the integer using the keyword int


# 8.Take the radius of a circle as input and print its area (use 3.14159 for pi), formatted to
# 2 decimal places.

radius = float(input("Enter the radius of the circle: "))
pi = 3.14159
area = pi * (radius**2)
print(f"The area of the circle is: {area:.2f}")

# 9.Create variables a, b, c = 10, 20, 30 in a single line and print their sum.

sum = a, b, c = 10, 20, 30
print(sum)


# Take a temperature in Celsius as input and convert it to Fahrenheit.
# formula: °F = °C × 9/5 + 32.
def temp():
    ctemp = int(input("Enter the tempeature:"))
    temp = ctemp * 9 / 5 + 32
    print(f"The present temperature is {temp}")


temp()
