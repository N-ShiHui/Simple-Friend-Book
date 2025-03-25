import json

try:
    with open('namebook.json', 'r') as fp:
        # Load the dictionary
        namebook = json.load(fp)
except (FileNotFoundError, json.JSONDecodeError):
    namebook = {'name': [], 'hobby': [], 'age': []}
print(namebook)

while True:
    print("What would you like to do?\n1. Add new user.\n2. Display current users.\n3. Remove user.\n4. Search user info.\n5. Edit user info.\n6. Exit")

    choice = input("Select your option (1/2/3/4/5/6):")

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
                print(f"{i}. {name}\n{'   '}Hobby: {hobby}\n{'   '}Age: {age}\n")

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
        search_item = input("Enter user name: ").strip().lower()
        found_users = []
        for i in range(len(namebook["name"])):
            if namebook["name"][i].lower() == search_item:
                found_users.append({
                    "Name": namebook["name"][i],
                    "Hobby": namebook['hobby'][i],
                    "Age": namebook['age'][i]
                })
        
        if found_users:
            print("Users found:".format(search_item))
            for user in found_users:
                print(f"{index}. Name: {user['Name']}, Hobby: {user['Hobby']}, Age: {user['Age']}")
        else:
            print("No such existing user.")

    elif choice == '5':
        if not namebook['name']:
            print("No such existing user.")
        else: 
            for i, (name, hobby, age) in enumerate(zip(namebook['name'],
                                                       namebook['hobby'],
                                                       namebook['age'])):
                print(f"{i}. {name}, Hobby: {hobby}, Age: {age}")
            
            try:
                index = int(input("Enter the index of user: "))
                if 0 <= index < len(namebook['name']):
                    option = input("What would you like to edit?\n1. Name\n2. Hobby\n3. Age")
                    if option == '1':
                        new_name = input("Enter new name: ")
                        namebook['name'][index] = new_name
                        print("User updated successfully.")
                    elif option == '2':
                        new_hobby = input("Enter new hobby: ")
                        namebook['hobby'][index] = new_hobby
                        print("User updated successfully.")
                    elif option == '3':
                        new_age = input("Enter new age: ")
                        namebook['age'][index] = new_age
                        print("User updated successfully.")
                    else:
                        print("Invalid option. please choose a valid option.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '6':
        # Exit the program
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

print("Updating file..")
with open("namebook.json", "w") as file:
    json.dump(namebook, file, indent=4) # Save updated data
print("Data updated successfully.")
