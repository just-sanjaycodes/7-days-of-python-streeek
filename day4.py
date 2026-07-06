# Pick your project right now — To-Do app (add task, view tasks, delete task, mark done) OR Grade Calculator (input marks, calculate average, show grade, pass/fail). Pick in 2 minutes. Don't overthink.
# 2 min · To-Do app recommended — shows more logic
# Write the full plan on paper — what does it do, what are the features, what functions do you need, what data does it store
# 30 min · paper only. No laptop. Planning before coding saves hours.
# Create a new GitHub repo for the project. Name it clearly — "todo-app-python". First commit with empty README.
# 15 min
# Start coding the core feature only — for To-Do: make "add task" and "view all tasks" work perfectly first
# 2 hrs · only core. No extra features until core works.
# Push whatever you have to GitHub end of day — even incomplete
# 15 min · incomplete code committed is better than perfect code not committed


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
