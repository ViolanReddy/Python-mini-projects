student_records = {}

def add_student(name, age, courses):
    if name in student_records:
        print(f"Student {name} already exists.")
    else:
        student_records[name] = {"age": age,
                                 "grades": set(),
                                 "courses": set()
                                 }
        print(f"Student {name} added successfully.")

def add_grade(name, grade):
    if name not in student_records:
        print(f"Student {name} not found.")
        return
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student {name} not found.")
        return False
    return course in student_records[name]["courses"]

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student {name} not found.")
        return None
    grades = student_records[name]["grades"]
    if not grades:
        return 0
    return sum(grades) / len(grades)

def list_students_by_course(course):
    students_in_course = []
    for name, details in student_records.items():
        if course in details["courses"]:
            students_in_course.append(name)
    return students_in_course

def filter_top_students(threshold):
    top_students = []
    for name in student_records:
        if calculate_average_grade(name) > threshold:
            top_students.append(name)
    return top_students