# Section 4: Loops (Q29–40)
# 29.Print numbers from 1 to 20 using a for loop.

for i in range(1, 21):
    print(i)

# 30.Print numbers from 20 to 1 (reverse) using a for loop with range() .
for i in range(20, 1, -1):
    print(i)

# Print only even numbers from 1 to 50 using range() with a step.
for i in range(0, 20):
    if i % 2 == 0:
        print(i)


# Calculate the sum of numbers from 1 to 100 using a while loop.


num = 1
total = 0
while num <= 100:
    total = total + num
    num = num + 1
print(total)

# Calculate the factorial of a number using a loop.
