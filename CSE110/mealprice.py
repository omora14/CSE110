def calculate_total_price(child_meal_price, adult_meal_price, num_child_meals, num_adult_meals, drink_price, num_drinks, appetizer_price, num_appetizers, sales_tax_rate):
    #Calculate the subtotal before tax
    subtotal = (child_meal_price * num_child_meals) + (adult_meal_price * num_adult_meals) + (drink_price * num_drinks) + (appetizer_price * num_appetizers)
    #Calculate the total sales tax
    tax = subtotal * (sales_tax_rate / 100)
    #Calculate the total price
    total_price = subtotal + tax
    return subtotal, tax, total_price

def calculate_change(total_price, payment_amount):
    change = payment_amount - total_price
    return change

child_meal_price = float(input("Enter the price of a child meal: "))
adult_meal_price = float(input("Enter the price of an adult meal: "))
num_child_meals = int(input("Enter the number of child meals: "))
num_adult_meals = int(input("Enter the number of adult meals: "))
drink_price = float(input("Enter the price of a drink: "))
num_drinks = int(input("Enter the number of drinks: "))
appetizer_price = float(input("Enter the price of an appetizer: "))
num_appetizers = int(input("Enter the number of appetizers: "))
sales_tax_rate = float(input("Enter the sales tax rate (in %): "))

#I know I souldn't go that far but honestly I had the time and the next week I'll be traveling so I did all at once!

print('\n')

subtotal, tax, total_price = calculate_total_price(child_meal_price, adult_meal_price, num_child_meals, num_adult_meals, drink_price, num_drinks, appetizer_price, num_appetizers, sales_tax_rate)
print("The subtotal of the meal is $%.2f" % subtotal)
print("The taxes of the meal is $%.2f" % tax)
print("The total price of the meal is $%.2f" % total_price)

print('\n')

payment_amount = float(input("Enter the payment amount: "))
change = calculate_change(total_price, payment_amount)
print("The change due is $%.2f" % change)
