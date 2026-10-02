inventory = {}

def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists!")
    inventory[item] = {"price": float(price),
                       "stock": int(stock)
                       }
    print(f"Item '{item}' added successfully!")

def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")

    try:
        new_stock = inventory[item]["stock"] + int(quantity)
        if new_stock < 0:
            print(f"Error: Insufficient stock for '{item}'")
        else:
            inventory[item]["stock"] = new_stock
    except ValueError:
        print("Error: Quantity must be an integer.")

def check_availability(item):
    if item not in inventory:
        print("Item not found.")
    current_stock = inventory[item]["stock"]
    print(current_stock)

def sales_report(sales):
    total_revenue = 0
    for item, quantity in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue
        if inventory[item]["stock"] < quantity:
            print(f"Error: Insufficient stock for '{item}'.")
            continue
        inventory[item]["stock"] -= quantity
        total_revenue += quantity * inventory[item]["price"]
    return f"Total revenue: ${total_revenue:.2f}"