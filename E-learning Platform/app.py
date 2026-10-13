class Course:
    def __init__(self, title, description, instructor):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.lessons = []

    def display_info(self):
        print(f"Courses: {self.title}")
        print(f"Description: {self.description}")
        print(f"Instructor: {self.instructor}")
        print(f"Number of Lessons: {len(self.lessons)}")

python_course = Course(
    "Python Fundamentals," \
    "Learn Python programming as a beginner," \
    "Alex"
)