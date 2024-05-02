print("The Haunted Mansion\n")

# Level 1: Arriving at the Mansion
print("You are driving down a dark, deserted road when you come across an old, abandoned mansion. You decide to take a closer look.")
print("Choice 1:")
print("A. Enter the mansion")
print("B. Turn back and leave")

choice = input().upper()
if choice == "A":
    # Level 2: Exploring the Mansion
    print("You step into the mansion and find yourself in a large room. In front of you, there are two doors.")
    print("Choice 2:")
    print("A. Take the left door")
    print("B. Take the right door")
    print("C. Turn back and leave the mansion")

    choice = input().upper()
    if choice == "A":
        # Level 3: Encountering a ghost
        print("You enter a dark room and suddenly a ghost appears.")
        print("Choice 3:")
        print("A. Try to communicate with the ghost")
        print("B. Run back to the main room")

        choice = input().upper()
        if choice == "A":
            print("The ghost was friendly and offered to help you find your way out of the mansion.")
        elif choice == "B":
            print("You run back to the main room and quickly leave the mansion.")
        else:
            print("Invalid choice. Please choose A or B.")
    elif choice == "B":
        # Level 3: Finding a secret room
        print("You enter a secret room filled with treasure.")
        print("Choice 3:")
        print("A. Take some of the treasure")
        print("B. Leave the treasure and leave the room")

        choice = input().upper()
        if choice == "A":
            print("You take some of the treasure and leave the mansion.")
        elif choice == "B":
            print("You leave the treasure and quickly leave the mansion.")
        else:
            print("Invalid choice. Please choose A or B.")
    elif choice == "C":
        print("You leave the mansion and drive away.")
    else:
        print("Invalid choice. Please choose A, B or C.")
elif choice == "B":
    print("You leave the mansion and drive away.")
else:
    print("Invalid choice. Please choose A or B.")
