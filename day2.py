# Lists- strings --------day2
# simple code of list
def fruits():
    mylist = ["mangos", "bananas", "apples"]
    for items in mylist:
        print(items)


fruits()


# same problem
# using inputs
def fruits():
    n = int(input("Enter the number of inputs: "))
    # Creates the list in a single line
    mylist = [input(f"Enter the fruit you want {i + 1}: ") for i in range(n)]
    print(mylist)


fruits()


# Strings — learn and use: the following
def length():
    name = "sanjay"
    print(len(name))
    print(name.split("s"))


length()


def name():
    #   len(),
    name = "kapil sharma"
    print(len(name))


name()


def name():
    #  upper(),
    name = "kapil sharma"
    print(name.upper())


name()


def name():
    #   lower()
    name = "kapil sharma"
    print(name.lower())


name()


def name():
    #    len(),
    name = "kapil sharma"
    print(name.replace("kap", "an"))


name()


def name():
    # split()
    name = "kapil sharma"
    print(name.split("kapil"))


name()


def name():
    # reverse() : s[::-1] to reverse.
    name = "kapil sharma"
    print(name[::-1])


name()
