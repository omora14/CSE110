import datetime

# Get input from user :D
width = float(input("Enter tire width in mm: "))
aspect_ratio = float(input("Enter tire aspect ratio: "))
diameter = float(input("Enter wheel diameter in inches: "))

# Calculate volume of tire
pi = 3.14159
radius = ((width * aspect_ratio) / 2540) + (diameter / 2)
volume = pi * radius ** 2 * (width / 25.4) * 0.000264172

# Print tire volume 
print("The volume of the tire is:", round(volume, 2), "cubic inches.")

# Ask if user wants to buy tires
answer = input("Do you want to buy tires with these dimensions? (yes or no): ")

if answer.lower() == "yes":
    # Get phone number from user
    phone_number = input("Please enter your phone number: ")

    # Get current date
    current_date = datetime.date.today()

    # Append data to volumes.txt file
    with open("volumes.txt", "a") as f:
        f.write(str(current_date) + "," + str(width) + "," + str(aspect_ratio) + "," + str(diameter) + "," + str(volume) + "," + phone_number + "\n")
