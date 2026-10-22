class Course:
    def __init__(self, title, description, instructor):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)
        print(f"Lesson {lesson.title} added successfully.")

    def display_lessons(self):
        if not self.lessons:
            print("No lessons available for this course")
            return

        print(f"Lessons in {self.title}:")

        for index, lesson in enumerate(self.lessons, start=1):
            print(f"{index}. {lesson.title}")

    def display_info(self):
        print(f"Courses: {self.title}")
        print(f"Description: {self.description}")
        print(f"Instructor: {self.instructor}")
        print(f"Number of Lessons: {len(self.lessons)}")

    def has_lesson(self, lesson):
        return lesson in self.lessons


class Lesson:
    def __init__(self, title, description, duration):
        self.title = title
        self.description = description
        self.duration = duration

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Duration: {self.duration} minutes.")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.enrolled_courses = []
        self.completed_lessons = []

    def enrol(self, course):
        if course in self.enrolled_courses:
            print("You are already enrolled in {course.title}.")
            return

        self.enrolled_courses.append(course)
        print(f"Successfully enrolled in {course.title}.")

    def display_enrolled_courses(self):
        if not self.enrolled_courses:
            print("You are not enrolled in any courses")

        print(f"Courses enrolled by: {self.name}")

        for index, course in enumerate(self.enrolled_courses, start=1):
            print(f"{index}. {course.title}")

    def complete_lesson(self, lesson):
        enrolled = False

        for course in self.enrolled_courses:
            if course.has_lesson(lesson):
                enrolled = True
                break

        if not enrolled:
            print("You must enrol in this course before completing the lesson.")
            return
        
        if lesson in self.completed_lessons:
            print(f"You have already completed {lesson.title}")
            return
        
        self.completed_lessons.append(lesson)

        print(f"Lesson {lesson.title} completed successfully.")

    def display_progress(self, course):
        if course not in self.enrolled_courses:
            print("You are not enrolled in this course")
            return

        total_lessons = len(course.lessons)

        if total_lessons == 0:
            print("this course has no lessons yet")
            return

        completed = 0

        for lesson in course.lessons:
            if lesson in self.completed_lessons:
                completed += 1

        percentage = (completed / total_lessons) * 100

        print(f"Student: {self.name}")
        print(f"Course: {course.title}")
        print(f"Completed lessons: {completed}/{total_lessons}")
        print(f"Progress: {percentage:.2f}%")

class ElearningPlatform:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def display_platform_info(self):
        print(f"Platform: {self.name}")
        print(f"Total Students: {len(self.students)}")
        print(f"Total Courses: {len(self.courses)}")

    def add_course(self, course):
        if course in self.courses:
            print(f"Course '{course.title}' already exists.")
            return
        
        self.courses.append(course)
        print(f"Course '{course.title}' successfully added to Platform.")

    def register_student(self, student):
        if student in self.students:
            print(f"{student.name} is already registered.")
            return

        self.students.append(student)
        print(f"Student '{student.name}' registered successfully.")

    def display_courses(self):
        if not self.courses:
            print("No courses are currently available.")
            return

        print(f"\nCourses available in {self.name}: ")

        for index, course in enumerate(self.courses, start=1):
            print(f"{index}. {course.title}")
            print(f"    Instructor: {course.instructor}")
            print(f"    Description: {course.description}")
            print()

"""Testing the Learning Hub"""
platform = ElearningPlatform("LearnHub")

#Create a course
python_course = Course(
    "Python Fundamentals",
    "Learning Python fundamentals",
    "Alexis Rayne"
)

#Create lessons
lesson1 = Lesson("Variables", "learn about variables", 35)
lesson2 = Lesson("Data Types", "Understand python data types", 25)
lesson3 = Lesson("Loops", "Learn for loops and while loops", 35)

#Add lessons to the course
python_course.add_lesson(lesson1)
python_course.add_lesson(lesson2)
python_course.add_lesson(lesson3)

#Add the course to the platform
platform.add_course(python_course)

def display_menu():
    print("\n===== LearnHub =====")
    print("1. View available courses")
    print("2. Register as a student")
    print("3. View registered students")
    print("4. Enrol in a course")
    print("5. View my enrolled courses")
    print("6. View course progress")
    print("7. Exit")

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            platform.display_courses()

        elif choice == "2":
            name = input("Enter your name: ")
            email = input("Enter your email: ")

            student = Student(name, email)

            platform.register_student(student)

        elif choice == "3":
            platform.display_students()

        elif choice == "4":
            if not platform.students:
                print("No students registered yet.")
                continue

            if not platform.courses():
                print("No courses available.")
                continue

            email = input("Enter students email: ")

            student = None

            for registered_student in platform.students:
                if registered_student.email == email:
                    student = registered_student
                    break

            if student is None:
                print("Student not found.")
                continue

            platform.display_courses()

            course_title = input("Enter the course title: ")

            course = None

            for available_course in platform.courses:
                if available_course.title.lower() == course_title.lower():
                    course = available_course
                    break

            if course is None:
                print("Course not found.")
                continue

            student.enrol(course)
        elif choice == "5":
            email = input("Enter your email: ")

            student = None

            for registered_student in platform.students:
                if registered_student.email == email:
                    student = registered_student
                    break

            if student is None:
                print("Student not found.")
                continue

            student.display_enrolled_courses()
        elif choice == "0":
            print("Thank you for using LearnHub!")
            break

        else:
            print("Invalid choice. Please try again.")
                   