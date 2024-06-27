from colors import c


class Customer:
    def __init__(self, inventory, cart):
        # Initialize Customer with inventory and cart objects
        self.inventory = inventory
        self.cart = cart

    def customer_selection(self):
        # Main loop for customer actions
        while True:
            # Display customer menu
            print(f"{c.OKBLUE}\nWelcome, customer ================================={c.ENDC}")
            print(f"{c.OKCYAN}[1]{c.ENDC} Purchase item")
            print(f"{c.OKCYAN}[2]{c.ENDC} Edit Cart")
            print(f"{c.OKCYAN}[3]{c.ENDC} View Cart")
            print(f"{c.OKCYAN}[4]{c.ENDC} Checkout")
            print(f"{c.OKCYAN}[5]{c.ENDC} Exit")
            print(f"{c.OKBLUE}====================================================={c.ENDC}")

            # Get customer command
            command = input(f"{c.OKGREEN}>> {c.ENDC}Enter command: ").strip()
            if command == "5":
                # Exit the loop if command is 5
                break
            elif command == "1":
                # Display inventory and prompt to add item to cart
                self.inventory.display_inventory()
                self.add_cart()
            elif command == "2":
                # Display cart and prompt to edit cart
                self.cart.display_cart()
                self.edit_cart()
            elif command == "3":
                # Display cart
                self.cart.display_cart()
            elif command == "4":
                # Proceed to checkout
                self.checkout_cart()
                break

    def add_cart(self):
        # Add an item to the cart
        name = input(f"\n{c.OKGREEN}>> {c.ENDC}Enter item name: ").strip()
        inventory_item = self.inventory.get_item(name)
        if inventory_item is None:
            # Item not found in inventory
            print(f"{c.FAIL}>> Item does not exist. Are you sure you used the right name?{c.ENDC}")
            return

        if self.cart.get_item(name):
            # Item already in cart, prompt to add more
            confirm = input(
                f"\n{c.WARNING}>> This item already exists in your cart! Would you like to add more of this item?: Y/N\n{c.ENDC}").strip().lower()
            if confirm == "y":
                added_quantity = int(
                    input(f"\n{c.OKGREEN}>> {c.ENDC}How many more of this item will you buy?: ").strip())
                # Adjust quantity if it exceeds available stock
                available_quantity = inventory_item.quantity
                if added_quantity > available_quantity:
                    print(f"{c.WARNING}>> Only {
                          available_quantity} items available. Adjusting quantity to available stock.{c.ENDC}")
                    added_quantity = available_quantity
                new_quantity = self.cart.get_item(name).quantity + added_quantity
                new_price = inventory_item.price * added_quantity
                self.cart.edit_item(name, new_price, new_quantity)
        else:
            # New item, prompt for quantity and add to cart
            desired_quantity = int(input(f"\n{c.OKGREEN}>> {c.ENDC}How many of this item will you buy?: ").strip())
            # Adjust quantity if it exceeds available stock
            available_quantity = inventory_item.quantity
            if desired_quantity > available_quantity:
                print(f"{c.WARNING}>> Only {available_quantity} items available. Adjusting quantity to available stock.{c.ENDC}")
                desired_quantity = available_quantity
            total_price = inventory_item.price * desired_quantity
            self.cart.add_item(name, desired_quantity, total_price)

    def edit_cart(self):
        # Edit an item in the cart
        name = input(f"\n{c.OKGREEN}>> {c.ENDC}Enter item name: ").strip()
        inventory_item = self.inventory.get_item(name)
        if self.cart.get_item(name) is None or inventory_item is None:
            # Item not found in cart or inventory
            print(f"{c.FAIL}>> Item does not exist{c.ENDC}")
            return
        new_desired_quantity = int(input(f"{c.OKGREEN}>> {c.ENDC}Edit desired quantity of {name}: ").strip())
        # Adjust quantity if it exceeds available stock
        available_quantity = inventory_item.quantity
        if new_desired_quantity > available_quantity:
            print(f"{c.WARNING}>> Only {available_quantity} items available. Adjusting quantity to available stock.{c.ENDC}")
            new_desired_quantity = available_quantity
        new_total_price = inventory_item.price * new_desired_quantity
        self.cart.edit_item(name, new_total_price, new_desired_quantity)

    def checkout_cart(self):
        # Process checkout
        while True:
            # Prompt for amount paid
            paid_amount = float(input(f"{c.OKGREEN}>> {c.ENDC}Enter amount paid: "))
            if paid_amount < 0:
                # Validate paid amount
                raise ValueError("Paid amount cannot be negative.")
            break

        total_cost = sum(item.price for item in self.cart.items)
        if paid_amount < total_cost:
            # Check if paid amount covers total cost
            print(f"{c.FAIL}Error: Paid amount is less than total cost. Cannot proceed with checkout.{c.ENDC}")
            return

        # Subtract purchased items from inventory
        for item in self.cart.items:
            self.inventory.subtract_item(item.name, item.quantity)

        print(f"{c.OKGREEN}>> Checkout complete!{c.ENDC}")
        confirm = input(f"{c.OKGREEN}>> {c.ENDC}Would you like to print a receipt? Y/N\n").strip().lower()

        if confirm == "y":
            # Print receipt to file if confirmed
            with open("receipt.txt", "w") as file:  # Open receipt.txt in write mode, replace if exists
                file.write(f"=====================================================\n")
                file.write(f"{'Name':<20}{'Quantity':<15}{'Inventory Price':<15}{'Subtotal':<15}\n")
                for item in self.cart.items:
                    inventory_price = self.inventory.get_item(item.name).price
                    subtotal = item.price
                    file.write(f"{item.name:<20}{item.quantity:<15}{inventory_price:<15.2f}{subtotal:<15.2f}\n")
                file.write(f"=====================================================\n")
                file.write(f"{'Total Cost':<50}{total_cost:<15.2f}\n")
                file.write(f"{'Paid Amount':<50}{paid_amount:<15.2f}\n")
                change = paid_amount - total_cost
                file.write(f"{'Change':<50}{change:<15.2f}\n")
                file.write(f"=====================================================\n")
            print("Receipt has been printed to receipt.txt")
        self.cart.items.clear()  # Clear cart after checkout
