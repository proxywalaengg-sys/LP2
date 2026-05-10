# Expert System for Information Management

# Dictionary to store information
database = {}


# Add Information
def add_information():

    key = input("Enter information title: ")
    value = input("Enter information details: ")

    database[key] = value

    print("Information added successfully!")


# View Information
def view_information():

    if len(database) == 0:
        print("No information available!")
        return

    print("\nStored Information:\n")

    for key, value in database.items():
        print("Title :", key)
        print("Details :", value)
        print()


# Search Information
def search_information():

    key = input("Enter title to search: ")

    if key in database:
        print("\nInformation Found!")
        print("Title :", key)
        print("Details :", database[key])

    else:
        print("Information not found!")


# Delete Information
def delete_information():

    key = input("Enter title to delete: ")

    if key in database:

        del database[key]

        print("Information deleted successfully!")

    else:
        print("Information not found!")


# Main Menu
def main():

    while True:

        print("\n===== Information Management Expert System =====")

        print("1. Add Information")
        print("2. View Information")
        print("3. Search Information")
        print("4. Delete Information")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        # Add
        if choice == 1:
            add_information()

        # View
        elif choice == 2:
            view_information()

        # Search
        elif choice == 3:
            search_information()

        # Delete
        elif choice == 4:
            delete_information()

        # Exit
        elif choice == 5:
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice!")


# Run Program
if __name__ == "__main__":
    main()