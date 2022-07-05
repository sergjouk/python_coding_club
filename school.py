class student:

    def __init__(self, name = "noname", last_name = "something"):
        print("this runs when ...")
        self.name = name
        self.last_name = last_name

    def get_full_name(self):
        return self.name + self.last_name

class classroom:

    def __init__(self, students: list):
        print("creating a classroom")
        self.students = students

    def print_student_names(self):
        for student in self.students:
            print(student.get_full_name())