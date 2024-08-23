def main():
    print("Welcome to Nneoma's Shop")
    class Item:
    
        def __init__(self, item_id, name, category, quantity, price):
            self.item_id = item_id
            self.name = name
            self.category = category
            self.quantity = quantity
            self.price = price

        def update(self, name=None, category=None, quantity=None, price=None):
            if name is not None:
                self.name = name
            if category is not None:
                self.category = category
            if quantity is not None:
                self.quantity = quantity
            if price is not None:
                self.price = price
            return self.name, self.category, self.quantity, self.price

        def __str__(self):
            return f"Item ID: {self.item_id}, Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}, Price: {self.price}"

    class Inventory:
        def __init__(self, item_list=None):
            if item_list is None:
                self.item_list = []
            else:
                self.item_list = item_list

        def add_item(self, item):
            self.item_list.append(item)
            print(f"Item {item.name} added successfully!")

        def remove_item(self, item_id):
            for item in self.item_list:
                if item.item_id == item_id:
                    
                    self.item_list.remove(item)
                    print(f"Item with ID {item_id} removed successfully!")
                    return
            print(f"Item with ID {item_id} not found!")

        def update_item(self, item_id, **kwargs):
            for item in self.item_list:
                if item.item_id == item_id:
                    item.update(**kwargs)
                    print(f"Item with ID {item_id} updated successfully!")
                   
        def display_items(self):
            if not self.item_list:
                print("No items in inventory!")
            else:
                print("Current Inventory:")
                for item in self.item_list:
                    print(item)

    
    inventory = Inventory()

    while True:
        print("\nInventory Menu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. Display Items")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = input("Enter item ID: ")
            name = input("Enter item name: ")
            category = input("Enter item category: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            new_item = Item(item_id, name, category, quantity, price)
            inventory.add_item(new_item)
        
        elif choice == "2":
            item_id = input("Enter item ID to remove: ")
            inventory.remove_item(item_id)
        
        elif choice == "3":
            item_id = input("Enter item ID to update: ")
            name = input("Enter new item name (press enter to skip): ")
            category = input("Enter new item category or press enter to skip: ")
            quantity = input("Enter new item quantity or press enter to skip: ")
            price = input("Enter new item price (press enter to skip): ")
            kwargs = {}
            if name:
                kwargs["name"] = name
            if category:
                kwargs["category"] = category
            if quantity:
                kwargs["quantity"] = int(quantity)
            if price:
                kwargs["price"] = float(price)
            inventory.update_item(item_id, **kwargs)
        
        elif choice == "4":
            inventory.display_items()
        
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()