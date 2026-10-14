class Course:
    def __init__(self, title, description, instructor):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.lessons = []

    def add_lesson(self, lesson_title):
        self.lessons.append(lesson_title)
        print(f"Lesson {lesson_title} added successfully.")

    def display_lessons(self):
        if not self.lessons:
            print("No lessons available for this course")
            return

        for index, lesson in enumerate(self.lessons, start=1):
            print(f"{index}.{lesson}")

    def display_info(self):
        print(f"Courses: {self.title}")
        print(f"Description: {self.description}")
        print(f"Instructor: {self.instructor}")
        print(f"Number of Lessons: {len(self.lessons)}")
