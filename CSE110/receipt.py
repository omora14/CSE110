import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    compound_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[key_column_index]
            values = row
            compound_dict[key] = values
    return compound_dict

def print_receipt():
    try:
        products_dict = read_dictionary('products.csv', 0)
        print("Pacalow\n")

        ordered_items = []
        subtotal = 0

        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first line (column headings)
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                if product_number in products_dict:
                    product = products_dict[product_number]
                    product_name = product[1]
                    price = float(product[2])
                    total_price = price * quantity
                    subtotal += total_price
                    ordered_items.append(f"{product_name}: {quantity} @ {price}")
                else:
                    raise KeyError(f"Unknown product ID in the request.csv file: '{product_number}'")

        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print('\n'.join(ordered_items))
        print("\nNumber of Items:", len(ordered_items))
        print("Subtotal:", subtotal)
        print("Sales Tax:", sales_tax)
        print("Total:", total)
        print("\nThank you for shopping at the Pacalow")
        print(datetime.now().strftime("%c"))

        # Print an invitation for online survey
        print("\nWe value your feedback! Please take a moment to complete our online survey:")
        print("www.pacalow/survey.com")

    except FileNotFoundError:
        print("Error: missing file\n[Errno 2] No such file or directory: 'products.csv'")
    except PermissionError:
        print("Error: insufficient permissions to access the file.")
    except KeyError as e:
        print("Error: " + str(e))

if __name__ == '__main__':
    print_receipt()
