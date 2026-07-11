# 23. Check if a character is a vowel or consonant.
def vowels():

    name = input("Enter name: ").strip()
    if len(name) != 1 or not name.isalpha():
        return

    if name in "aeiouAEIOU":
        print("yes")
    else:
        print("no")


vowels()
#

# 24. Take a number and check if it's divisible by both 3 and 5, only 3, only 5, or neither.


def num():
    number = int(input("Enter number: "))
    if number % 5 == 0 and number % 3 == 0:
        print(f"The number {number} is only divisble by 3&5 ")
    elif number % 3 == 0:
        print(f"The number {number} is only divisble by 3 ")
    elif number % 5 == 0:
        print(f"The number {number} is only divisble by 5 ")
    else:
        print(f"The number {number} is not divisible by 3 and 5")


num()


# 25. Write a simple ticket-price calculator: age < 5 free, age < 18 half price, else full price —
# using nested or chained conditionals.


def film():
    Movie_name = input("Which movie would u like to watch today:")
    age = int(input("Enter age: "))
    half_price = 100
    full_price = 200

    if age <= 5:
        print("Its Free")
        print(f"Enjoy your movie {Movie_name}")
    elif age <= 18:
        print(f"half_price {half_price}")
        print(f"Enjoy your movie {Movie_name}")
    else:
        print(f"Full price {full_price}")
        print(f"Enjoy your movie {Movie_name}")


film()


# 26. Rewrite Q19 using Python's ternary conditional expression ( x if cond else y ).
def check():
    num = int(input("Enter "))
    result = "Negetive" if num < 0 else ("zero" if num == 0 else "positive")
    print(result)


check()
# 27. Take a username and password, check both against fixed values, and print "Login
# successful" or "Login failed."


def passcheck():
    Admin_name = "suraj"
    password = "pass@123"
    # user name
    name = input("Enter name ")
    if name == Admin_name:
        print("Success")
    else:
        print("Incorrect")
        return
    passcode = input("Enter password:")
    if passcode == password:
        print("success")
    else:
        print("Password incorrect:")
        print("Login Success")


passcheck()


# 28. Use a match-case statement to print the name of a day given its number (1–7).
def get_day_name(day_number):
    # 1. MATCH: Evaluate the expression ONCE.
    # Think of this as handing your ID to the bouncer.
    match day_number:
        # 2. CASE: Check specific patterns.
        # If day_number is 1, run this block.
        case 1:
            return "Monday"

        # You can stack multiple values with '|' (OR)
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"

        # 3. WILDCARD (_): The "Else" equivalent.
        # Matches ANYTHING that didn't fit above.
        case _:
            return "Invalid day number"


# Usage
print(get_day_name(1))  # Output: Monday
print(get_day_name(9))  # Output: Invalid day number
