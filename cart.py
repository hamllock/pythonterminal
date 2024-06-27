from colors import c
from item import Item


class Cart:
    # Initialize the Cart with an empty list of items
    def __init__(self):
        self.items = []

    # Retrieve an item by its name
    def get_item(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None  # Return None if item not found

    # Add a new item to the cart
    def add_item(self, name, quantity, price):
        self.items.append(Item(name, price, quantity))  # Create and add new item object to items list

    # Edit an existing item's details in the cart
    def edit_item(self, name, new_price=None, new_quantity=None):
        item = self.get_item(name)  # Find the item by name
        if new_quantity == 0:
            self.delete_item(name)  # Delete the item if new quantity is 0
        else:
            # Update item's quantity and price if provided
            item.quantity = new_quantity if new_quantity is not None else item.quantity
            item.price = new_price if new_price is not None else item.price

    # Delete an item from the cart
    def delete_item(self, name):
        self.items = [item for item in self.items if item.name != name]  # Remove item by name

    # Display the cart items in a formatted manner
    def display_cart(self):
        print(f"\n{c.OKBLUE}Your cart ==========================================={c.ENDC}")
        print(f"{c.WARNING}{'Name':<20}{'Quantity':<15}{'Price':<10}{c.ENDC}")
        for item in self.items:
            # Print each item's details
            print(f"{item.name:<20}{item.quantity:<15}{item.price:<10.2f}")
        print(f"{c.OKBLUE}====================================================={c.ENDC}")
