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

lesson1 = Lesson("Introduction to Python",
                 "learn the basics",
                 "50")

lesson2 = Lesson(
    "DSA",
    "Python data structures",
    "45"
)

lesson3 = Lesson(
    "Information systems",
    "learning basic system design",
    "50"
)

course1 = Course("Python Fundamentals",
                  "Learning Python Programming",
                  "Alex")

course1.add_lesson(lesson1)
course1.add_lesson(lesson2)
course1.add_lesson(lesson3)

valorie = Student("Valorie", "valorieR@icloud.com")

valorie.enrol(course1)

print(f"Initial Progress: {valorie.display_progress(course1)}")

print(f"Completing first lesson: {valorie.complete_lesson(lesson1)}")

print(f"Updated progress: {valorie.display_progress(course1)}")