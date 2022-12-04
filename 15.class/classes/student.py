class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def add_course(self, course):
        self.course = course

    def _get_course(self, course):
        return f"Course: {course}"

    def __str__(self):
        return f"Student: {self.name}, ID: {self.id}"

    def __repr__(self):
        return f"Student({self.name}, {self.id})"
