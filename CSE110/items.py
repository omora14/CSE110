items = []
prices = []

def add_item():
    item_name = input("Enter the name of the item: ")
    item_price = float(input("Enter the price of the item: "))
    items.append(item_name)
    prices.append(item_price)
    print("Item added to cart.")

def display_items():
    if len(items) == 0:
        print("The cart is empty.")
    else:
        print("Shopping Cart:")
        for i in range(len(items)):
            print(f"{i+1}. {items[i]} - ${prices[i]:.2f}")

def display_total():
    total = sum(prices)
    print(f"Total: ${total:.2f}")

def remove_item():
    display_items()
    item_number = int(input("Enter the number of the item you want to remove: "))
    index = item_number - 1
    if index < 0 or index >= len(items):
        print("Invalid item number.")
    else:
        del items[index]
        del prices[index]
        print("Item removed from cart.")

while True:
    print("Menu:")
    print("1. Add a new item")
    print("2. Display items in cart")
    print("3. Display total")
    print("4. Remove an item")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_item()
    elif choice == 2:
        display_items()
    elif choice == 3:
        display_total()
    elif choice == 4:
        remove_item()
    elif choice == 5:
        break
    else:
        print("Invalid choice.")
    print()
