class Inventory:
    def __init__(self):
        self.items = {}
        self.inventory_file = "inventory.txt"
        self.load_inventory()

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        print(f"Added {quantity} {name}(s).")
        self.save_inventory()

    def remove_item(self, name, quantity):
        if name not in self.items or self.items[name] < quantity:
            print(f"Cannot remove {quantity} {name}(s). Not enough stock.")
        else:
            self.items[name] -= quantity
            if self.items[name] == 0:
                del self.items[name]
            print(f"Removed {quantity} {name}(s).")
            self.save_inventory()

    def delete_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} deleted from inventory.")
            self.save_inventory()
        else:
            print(f"{name} not found in inventory.")

    def show_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for name, quantity in self.items.items():
                print(f"{name}: {quantity}")

    def save_inventory(self):
        with open(self.inventory_file, 'w') as file:
            for name, quantity in self.items.items():
                file.write(f"{name}:{quantity}\n")

    def load_inventory(self):
        try:
            with open(self.inventory_file, 'r') as file:
                for line in file:
                    name, quantity = line.strip().split(':')
                    self.items[name] = int(quantity)
        except FileNotFoundError:
            print("Inventory file not found, starting with an empty inventory.")


def main():
    inventory = Inventory()
    while True:
        print("\nCommands: add, remove, delete, show, exit")
        command = input("Enter command: ").strip().lower()
        if command == "exit":
            break
        elif command == "add":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(name, quantity)
        elif command == "remove":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.remove_item(name, quantity)
        elif command == "delete":
            name = input("Enter item name to delete: ")
            inventory.delete_item(name)
        elif command == "show":
            inventory.show_inventory()
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
