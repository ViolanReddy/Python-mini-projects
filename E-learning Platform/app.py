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

        
course1 = Course("DSA",
                  "Data structures and algorithms in Python",
                  "Alex")

sarah = Student("sarah", "sarah@example.com")
sarah.enrol(course1)
sarah.display_info()
sarah.display_enrolled_courses()
sarah.enrol(course1)