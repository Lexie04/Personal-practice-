inventory = {"apple":10, "orange":5, "watermelon":6}

def add_item(item, quantity: int):
    if item in inventory:
        inventory[item] += quantity
    else: 
        inventory[item] = quantity

add_item("banana", 10)
add_item("apple", 5)
print(inventory)


    # Function to view all items in the inventory
def view_inventory():
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    for item, quantity in inventory.items():
    # 2. Print each item's name and its quantity.
        print("{item}:{quantity}")
    pass

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity:int):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    if item in inventory:
    # 2. If it does, update its quantity.
        inventory[item] = quantity
        print(f"{item} quantity updated to {quantity}.")
    # 3. If the item doesn't exist, print a message indicating it's not found.
    print(f"{item} not found in inventory.")
    pass

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 2. If the choice is '2', call the view_inventory function.
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        # 4. If the choice is '4', break the loop to exit the program.
        # 5. For any other input, display an error message.
        pass

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()

