# Section 3: Conditionals (Q19–28)
# 19. Write a program to check if a number is positive, negative, or zero.


def num_check():
    number = int(input("Enter: "))
    if number < 0:
        print("Negetive")
    elif number > 0:
        print("Positive")
    else:
        print("zero")


num_check()

# //using ternary operator


def num_check():
    number = int(input("Enter: "))
    # Nested ternary: value_if_true if condition else (value_if_elif if condition else value_if_else)
    result = "Negetive" if number < 0 else ("Positive" if number > 0 else "zero")
    print(result)


num_check()


# 20. Check if a given year is a leap year.


def year():
    year = int(input("Enter the year: "))
    print(
        "Leap year"
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        else print("Non leap year")
    )


year()


# 21. Take three numbers and print the largest using if-elif-else .
def largest():
    f_number = int(input("Enter 1st number: "))
    s_number = int(input("Enter 2nd number: "))
    t_number = int(input("Enter 3rd number: "))

    if f_number >= s_number and f_number >= t_number:
        print(f"Largest is {f_number}")
    elif s_number >= f_number and s_number >= t_number:
        print(f"Largest is {s_number}")
    else:
        print(f"Largest is {t_number}")


largest()


# 22. Take marks as input and print a grade (A/B/C/D/F) using if-elif-else .


def Marks_calculator():
    s1 = int(input("Enter s1 marks:(0-25)"))
    s2 = int(input("Enter s2 marks:(0-25)"))
    s3 = int(input("Enter s3 marks:(0-25)"))
    s4 = int(input("Enter s4 marks:(0-25) "))
    total_marks = s1 + s2 + s3 + s4
    if total_marks >= 90:
        print("o")
        print("Pass")
    elif total_marks > 80 and total_marks < 90:
        print("A+")
        print("Pass")
    elif total_marks > 70 and total_marks <= 80:
        print("A")
        print("Pass")
    elif total_marks > 60 and total_marks <= 70:
        print("B+")
        print("Pass")
    elif total_marks > 50 and total_marks <= 60:
        print("B")
        print("Pass")
    elif total_marks > 40 and total_marks <= 50:
        print("C")
        print("Pass")
    elif total_marks > 35 and total_marks <= 40:
        print("c+")
        print("Pass")
    else:
        print("fail")


Marks_calculator()
