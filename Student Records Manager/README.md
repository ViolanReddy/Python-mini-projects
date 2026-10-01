# Student Records Manager

A simple Python project for storing and managing student information in memory. It uses a dictionary to keep track of students, their ages, grades, and course data.

## Overview

This project demonstrates a basic student records system with functions for:

- adding a new student
- adding a grade for a student
- checking whether a student is enrolled in a course
- calculating the average grade for a student
- listing students enrolled in a course
- finding students whose average grade exceeds a threshold

## Project Structure

- `app.py` — contains the student record logic and supporting functions

## Functions

### `add_student(name, age, courses)`
Adds a student to the records if they do not already exist.

### `add_grade(name, grade)`
Adds a grade to a student's record.

### `is_enrolled(name, course)`
Checks whether a student is currently marked as enrolled in a specific course.

### `calculate_average_grade(name)`
Returns the average of a student's grades. If no grades exist, it returns `0`.

### `list_students_by_course(course)`
Returns a list of students enrolled in the given course.

### `filter_top_students(threshold)`
Returns students whose average grade is greater than the provided threshold.

## Example Usage

```python
import app

app.add_student("Alice", 18, ["Math", "Science"])
app.add_student("Bob", 17, ["History"])

app.add_grade("Alice", 90)
app.add_grade("Alice", 85)
app.add_grade("Bob", 78)

print(app.calculate_average_grade("Alice"))
print(app.is_enrolled("Alice", "Math"))
print(app.list_students_by_course("Math"))
print(app.filter_top_students(80))
```

## Notes

- This project stores data in memory only, so records are lost when the program exits.
- The code is a simple educational example and can be expanded with features like course enrollment, student removal, editing records, or a file-based database.

## Running the Project

Since this is a module-based example, you typically import it into another Python script or run commands interactively in a Python shell:

```bash
python
>>> import app
```

## Future Improvements

Possible enhancements include:

- adding student removal and updating functionality
- storing records in JSON or CSV files
- adding a simple command-line interface (CLI)
- validating input values such as age and grade ranges
