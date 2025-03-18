namebook = {"name": [], "hobby": [], "age": []}

while True:
    print("What would you like to do?\n1. Add new user\n2. Display current users\n3. Remove user\n4. Exit")

    choice = input("Select your option:")

    if choice == '1':
        # Capture new user information
        name = input("What is your name?")
        hobby = input("What is your favourite hobby?")
        age = input("What is your age?")

        # Append new user information to namebook
        namebook["name"].append(name),
        namebook["hobby"].append(hobby),
        namebook["age"].append(age)

        print("User updated successfully.")

    elif choice == '2':
        # Display current users:
        if not namebook["name"]:
            print("User not found in system.")
        else:
            print("Current users:")
            for i, (name, hobby, age) in enumerate(zip(namebook["name"],
                                                       namebook["hobby"],
                                                       namebook["age"])):
                print(f"{i+1}. {name}, {hobby}, {age}")
    elif choice == '3':
        if not namebook["name"]:
            print("No user to remove.")
        else:
            print("Current users:")
            for i, (name, hobby, age) in enumerate(zip(namebook["name"], 
                                                       namebook["hobby"], 
                                                       namebook["age"])):
                   print(f"{i+1}. {name}, {hobby}, {age}")
            try:
                index_to_remove = int(input("Enter the index of the user:")) - 1
                if 0 <= index_to_remove < len(namebook["name"]):
                    del namebook["name"][index_to_remove]
                    del namebook["hobby"][index_to_remove]
                    del namebook["age"][index_to_remove]
                    print("User removed successfully.")
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == '4':
        # Exit the program
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
