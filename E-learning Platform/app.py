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
        self.enrolled_course = []

    def enrol(self, course):
        if course in self.enrolled_course:
            print("You are already enrolled in {course.title}!")