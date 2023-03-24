import csv

class InventoryManager:
    def __init__(self):
        self.inventory = {}
        self.db_file = 'inventory.csv'

    def add_item(self, item, quantity):
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer")
            if item in self.inventory:
                self.inventory[item] += quantity
                print("Item list updated \n")
            else:
                self.inventory[item] = quantity
                print("Item added\n")
        except ValueError as e:
            print(str(e))

    def remove_item(self, item, quantity):
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer")
            if item in self.inventory:
                if self.inventory[item] >= quantity:
                    self.inventory[item] -= quantity
                    print("Item list updated \n")
                else:
                    print(f"Error: Not enough {item} in inventory\n")
            else:
                print(f"Error: {item} not found in inventory\n")
        except ValueError as e:
            print(str(e))

    def display_inventory(self):
        if self.inventory:
            print("\nInventory List")
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}\n")
        else:
            print("Inventory is empty")

    def save_inventory(self):
        with open(self.db_file, mode='w') as csv_file:
            fieldnames = ['item', 'quantity']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for item, quantity in self.inventory.items():
                writer.writerow({'item': item, 'quantity': quantity})

    def load_inventory(self):
        try:
            with open(self.db_file, mode='r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.inventory[row['item']] = int(row['quantity'])
            print("Inventory loaded from database")
        except FileNotFoundError:
            print("Inventory database not found. Creating a new one.")

def handle_request(manager):
    while True:
        print("Hey welcome to Inventtx\n")
        print("To add items to inventory press 1 | \n To remove item press 2 | \n press 3 to display| \n press 0 to kill program\n")
        user_input = int(input("User: "))

        if user_input == 1:
            print("what would you like to add\n")
            inp = input("Name: ")
            inp_2 = int(input("Quantity: "))
            manager.add_item(inp, inp_2)
            
        elif user_input == 2:
            print("what would you like to remove\n")
            inp = input("Name: ")
            inp_2 = int(input("Quantity: "))
            manager.remove_item(inp, inp_2)
            
        elif user_input == 3:
            manager.display_inventory()
            
        elif user_input == 0:
            manager.save_inventory()
            break
            
        else:
            print("Invalid input. Please try again.")

manager = InventoryManager()
manager.load_inventory()
handle_request(manager)

