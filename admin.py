# Import the colors module for text styling
from colors import c

# Define the Admin class to manage inventory


class Admin:
    def __init__(self, inventory):
        # Initialize Admin with an inventory object
        self.inventory = inventory

    def manage_inventory(self):
        # Main loop for admin actions
        while True:
            # Display admin dashboard menu
            print(f"{c.OKBLUE}\nAdmin Dashboard ====================================={c.ENDC}")
            print(f"{c.OKCYAN}[1]{c.ENDC} Add new item")
            print(f"{c.OKCYAN}[2]{c.ENDC} Edit existing items")
            print(f"{c.OKCYAN}[3]{c.ENDC} Delete item in inventory")
            print(f"{c.OKCYAN}[4]{c.ENDC} Display items in stock")
            print(f"{c.OKCYAN}[5]{c.ENDC} Exit to menu")
            print(f"{c.OKBLUE}====================================================={c.ENDC}")

            # Get admin command
            command = input(f"{c.OKGREEN}>> {c.ENDC}Enter command: ").strip()
            if command == "5":
                # Exit the loop if command is 5
                break
            elif command == "1":
                # Add a new item to the inventory
                self.add_inventory()
            elif command == "2":
                # Display inventory, edit an item, and display updated inventory
                self.inventory.display_inventory()
                self.edit_inventory()
                self.inventory.display_inventory()
            elif command == "3":
                # Display inventory and delete an item
                self.inventory.display_inventory()
                self.delete_inventory()
            elif command == "4":
                # Display all items in inventory
                self.inventory.display_inventory()

    def add_inventory(self):
        # Add a new item to the inventory
        name = input(f"\n{c.OKGREEN}>> {c.ENDC}Enter item name: ").strip()
        if self.inventory.get_item(name) is not None:
            # Check if item already exists
            print(f"{c.FAIL}>> Item already exists{c.ENDC}")
            return
        quantity = int(input(f"{c.OKGREEN}>> {c.ENDC}Enter quantity: "))
        price = int(input(f"{c.OKGREEN}>> {c.ENDC}Enter price: "))
        self.inventory.add_item(name, price, quantity)

    def edit_inventory(self):
        # Edit an existing item in the inventory
        name = input(f"\n{c.OKGREEN}>> {c.ENDC}Enter item name: ").strip()
        if self.inventory.get_item(name) is None:
            # Check if item exists
            print(f"{c.FAIL}>> Item does not exist{c.ENDC}")
            return

        while True:
            # Display edit item menu
            print(f"{c.OKBLUE}\nEdit Item ==========================================={c.ENDC}")
            print(f"Which value of {name} would you like to edit?")
            print(f"{c.OKCYAN}[1]{c.ENDC} Name")
            print(f"{c.OKCYAN}[2]{c.ENDC} Price")
            print(f"{c.OKCYAN}[3]{c.ENDC} Quantity")
            print(f"{c.OKCYAN}[4]{c.ENDC} Cancel")
            print(f"{c.OKBLUE}====================================================={c.ENDC}")

            command = input(f"{c.OKGREEN}>> {c.ENDC}Enter command: ").strip()

            if command == "4":
                # Exit edit menu
                break
            if command == "1":
                # Edit item name
                new_name = input(f"{c.OKGREEN}>> {c.ENDC}Enter the new name: ")
                self.inventory.edit_item(name, new_name=new_name)
                break
            elif command == "2":
                # Edit item price
                new_price = float(input(f"{c.OKGREEN}>> {c.ENDC}Enter the new price: "))
                self.inventory.edit_item(name, new_price=new_price)
                break
            elif command == "3":
                # Edit item quantity
                new_quantity = int(input(f"{c.OKGREEN}>> {c.ENDC}Enter the new quantity: "))
                self.inventory.edit_item(name, new_quantity=new_quantity)
                break
            else:
                # Handle invalid command
                print(f"{c.FAIL}>> Invalid choice{c.ENDC}")

    def delete_inventory(self):
        # Delete an item from the inventory
        name = input(f"\n{c.OKGREEN}>> {c.ENDC}Enter item name: ").strip()
        if self.inventory.get_item(name) == None:
            # Check if item exists
            print(f"{c.FAIL}>> Item does not exist{c.ENDC}")
            return
        confirm = input(f"{c.WARNING}>> Are you sure you want to delete {name}? Y/N\n").strip().lower()
        if confirm == "y":
            # Confirm deletion
            self.inventory.delete_item(name)
