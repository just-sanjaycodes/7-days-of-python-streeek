def name():
    # knowing the customer name
    while True:
        name = input("Enter the name plz: ")
        if name:
            print(f"hello & welcome to the coffie hub {name}")
            break
        else:
            print("name cannot be empty")


name()

# menu items

menu_items = ["Latte", "Espresso", "Cappuccino", "Mocha", "Americano"]

prize = {
    "Latte": 200,
    "Espresso": 100,
    "Cappuccino": 300,
    "Mocha": 400,
    "Americano": 250,
}


def menuitems():
    print("--- Coffee Menu ---")
    for i, coffee in enumerate(menu_items, start=1):
        print(f"{i}. {coffee} = {prize[coffee]}rs")


menuitems()


# selecting the coffie

choice = int(input("Enter the number of coffee u want: "))
index = choice - 1
selected_coffee = menu_items[index]
selected_prize = prize[selected_coffee]

print("You selected:", selected_coffee, "for", selected_prize, "rs")

# paying the order
while True:
    payment = input("Would u like to pay it in cash / card:")
    if payment == "cash":
        print(f"Thank you for paying rs {selected_prize}")
        break
    elif payment == "card":
        print(f"pay using this scanner rs {selected_prize}")
        break
    else:
        print("U have not selected mode of payment")
        break


print("thank u for visiting coffee hub")
