# Import necessary modules for the main functionality
from admin import Admin
from cart import Cart
from colors import c
from customer import Customer
from inventory import Inventory

# Define the main function to run the application


def main():
    # Initialize inventory and cart objects
    inventory = Inventory()
    cart = Cart()
    # Main loop for user selection
    while True:
        # Display the main menu options
        print(f"{c.OKBLUE}\nSelection ==========================================={c.ENDC}")
        print(f"{c.OKCYAN}[1]{c.ENDC} Order as a Customer")
        print(f"{c.OKCYAN}[2]{c.ENDC} Access Inventory as Admin")
        print(f"{c.OKCYAN}[3]{c.ENDC} Exit")
        print(f"{c.OKBLUE}====================================================={c.ENDC}")

        # Get user command
        command = input(f"{c.OKGREEN}>> {c.ENDC}Enter command: ").strip()
        if command == "3":
            # Exit the program if command is 3
            break
        elif command == "1":
            # Create a Customer object and enter customer selection if command is 1
            customer = Customer(inventory, cart)
            customer.customer_selection()
            break  # Exiting after customer selection; might need to loop instead
        elif command == "2":
            # Create an Admin object and enter admin management if command is 2
            admin = Admin(inventory)
            admin.manage_inventory()
        else:
            # Handle invalid command input
            print(f"{c.FAIL}>> Invalid choice{c.ENDC}")


# Check if the script is run directly and call main function
if __name__ == "__main__":
    main()
