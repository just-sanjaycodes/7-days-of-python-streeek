# Open VS Code. Write a for loop that prints 1 to 10. Run it. Change it to print 1 to 100. Run it again.
for i in range(1, 51):
    print(i)
# Write these 5 programs using loops only — no googling:
#  print multiplication table of 5,
# sum of 1 to 100,
# print all even numbers from 1 to 50,
# reverse print 10 to 1,
# print "your name" 7 times

for i in range(1, 11):
    print(f"5X{i}={5 * i}")

for i in range(1, 101):
    print(f"sum of 1 to 100 is {i * i}")

for num in range(1, 51):
    if num % 2 == 0:
        print(num)

for i in range(10, 0, -1):
    print(i)

for i in range(0, 7):
    print("sanjay")

# Learn functions —
#  write def add(a,b): return a+b.
#  Call it.
# Then write 3 more functions yourself: subtract, multiply, check if number is even


def add(a, b):
    return a + b


print(add(2, 5))


def multiply(x, y, z):
    return f"The return value is {x * y * z}"


print(multiply(1, 2, 3))


# check the number is even or odd
def eve_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


print(eve_or_odd(5))


# Combine loops and functions —
# write a function that takes a number and prints its multiplication table using a loop inside


def table():
    number = int(input("Enter the table u want: "))

    for i in range(1, 11):
        print(f"{number}X{i}={number * i}")


table()
