# Contact Book

A simple command-line contact manager built in Python. This project lets you add, view, edit, delete, and list saved contacts in a small in-memory database using a Python dictionary.

## Features

- Add a new contact
- View a contact's details
- Edit an existing contact
- Delete a contact
- Display all saved contacts
- Exit the application cleanly

## Project Structure

```text
Contact Book/
├── contactBook.py   # Main contact book application
├── test.py          # Separate sample/test script
└── README.md        # Project documentation
```

## How It Works

The application stores contacts in a dictionary where each contact name is the key and the value contains:

- phone
- email
- address

The program runs in a loop and shows a menu for users to choose actions.

## Run the Project

From the project directory, run:

```bash
python contactBook.py
```

## Example Menu

```text
Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit
```

## Notes

- Contacts are stored in memory only, so they are lost when the program closes.
- This is a beginner-friendly Python project designed for learning basic input/output, dictionaries, and control flow.

## Code Review Summary

The current implementation is functional for a simple CLI app, but a few improvements would make it more reliable:

- In `view_contact`, the code reads from `contact_book` instead of the individual `contact` dictionary. This can cause incorrect output or errors.
- The app does not validate user input for empty or malformed data.
- The project does not persist contacts to disk, so data is not saved between runs.
- `test.py` appears unrelated to the contact application and may be a separate learning example.

## Future Improvements

- Save contacts to JSON or a local file
- Add search by name or phone number
- Validate email and phone number format
- Improve menu input handling and error messages
- Add a proper data model and cleaner function structure

## License

This project is provided for learning and personal use.
