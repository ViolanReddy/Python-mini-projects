# Inventory Management System

A lightweight Python inventory management script for tracking products, updating stock, checking availability, and calculating sales revenue.

## Overview

This project uses a simple in-memory inventory dictionary to store product information such as:

- product name
- unit price
- quantity in stock

It is designed for small-scale inventory tracking and can be extended into a CLI app, GUI app, or database-backed solution.

## Features

- Add a new item to inventory
- Update stock quantity
- Check current stock for an item
- Process sales and calculate total revenue
- Validate common stock and input errors

## Project Structure

```text
Inventory Management System/
├── app.py
├── README.md
```

## Code Details

The main logic is in `app.py` and includes:

- `add_item(item, price, stock)`
  - Adds a new item to the inventory
  - Prevents duplicates by overwriting existing entries

- `update_stock(item, quantity)`
  - Adds or subtracts stock based on the provided quantity
  - Prevents negative stock values

- `check_availability(item)`
  - Prints the current stock value for an item

- `sales_report(sales)`
  - Accepts a dictionary of sold items and quantities
  - Validates stock before each sale
  - Deducts sold stock from inventory
  - Returns total revenue as a formatted dollar value

## Example Usage

```python
from app import inventory, add_item, update_stock, check_availability, sales_report

add_item("Laptop", 999.99, 10)
add_item("Mouse", 25.50, 50)

update_stock("Laptop", 3)
check_availability("Laptop")

sales = {"Laptop": 2, "Mouse": 5}
print(sales_report(sales))
```

## Example Output

```python
Item 'Laptop' added successfully!
Item 'Mouse' added successfully!
13
Total revenue: $2049.98
```

## Notes

- The current version stores inventory data in memory only.
- Data is lost when the program exits.
- The script uses print statements for user feedback instead of a graphical interface or external database.

## Future Enhancements

Possible improvements include:

- Save data to JSON or CSV files
- Add a command-line menu interface
- Support product deletion
- Track sales history
- Add search and filter features
- Use a database such as SQLite

## How to Run

1. Open the project folder.
2. Run the Python file:

```bash
python app.py
```

If you want to use the functions in another script, import them from `app.py` as shown in the example above.

## License

This project is provided as a simple educational example and may be modified freely for learning and personal use.
