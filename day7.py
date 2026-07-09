# Section 2: Operators & Expressions (Q11–18)
# 11. Take two numbers and print the result of + , - , * , / , // , % , ** between them.
num1 = int(input("input1: "))
num2 = int(input("input1: "))
plus = num1 + num2
minus = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2
other = num1 // num2
other2 = num1**num2
print(
    f"All operators are performed \n{plus}\n{minus}\n{mult}\n{div}\n{mod}\n{other}\n{other2}"
)


#  2.Check if a number is even or odd using the modulo operator (just print True / False ,
# no if-statement yet).

number = int(input("Enter the number:"))
modulo = "True" if number % 2 == 0 else "False"
print(modulo)

# 13. Given x = 5 , predict and verify: x += 3 , x -= 1 , x *= 2 , x /= 4 .
x = 5
x += 3
x -= 1
x *= 2
x /= 4
print(x)


# 14. Compare two numbers using all six comparison operators ( == , != , > , < , >= , <= )
# and print each result.


def math():
    num1 = int(input("Enter the number:"))
    num2 = int(input("enter the number:"))
    a = num1 == num2
    b = num1 != num2
    c = num1 > num2
    d = num1 < num2
    e = num1 >= num2
    f = num1 <= num2
    print(f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}")


# math()

# 15. Use and , or , not to check if a number is between 10 and 20 (inclusive).

secret_no = 12
if secret_no >= 10 and secret_no <= 20:
    print("Yes")
else:
    print("NO")


secret_no = 12
if secret_no > 10 or secret_no < 20:
    print("Yes")
else:
    print("NO")

# 16. Predict the output of 10 // 3 , 10 % 3 , -10 // 3 , -10 % 3 before running — then
# verify.

output = 10 // 3
print(output)

output = -10 % 3
print(output)


output = -10 // 3
print(output)

# 17..Check operator precedence: predict the result of 2 + 3 * 4 ** 2 // 2 before
# running.

output = 2 + 3 * 4**2 // 2
print(output)

# 18.Use the walrus operator ( := ) to assign and print a value inside a single expression,
# e.g. inside a print() call.

print(x := 25 * 25)

if print(x := 25):
    print(x)
