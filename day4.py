# Grade Calculator (input marks, calculate average, show grade, pass/fail).
def Grade_calculator():
    marks = int(input("Enter the marks of total: "))
    if marks >= 90:
        print("o")
        print("Pass")
    elif marks > 80 and marks < 90:
        print("A+")
        print("Pass")
    elif marks > 70 and marks <= 80:
        print("A")
        print("Pass")
    elif marks > 60 and marks <= 70:
        print("B+")
        print("Pass")
    elif marks > 50 and marks <= 60:
        print("B")
        print("Pass")
    elif marks > 40 and marks <= 50:
        print("C")
        print("Pass")
    elif marks > 35 and marks <= 40:
        print("c+")
        print("Pass")
    else:
        print("fail")


Grade_calculator()
