class Group:
    def __init__(self, name, school, curator = None):
        self.name = name
        self.school = school
        self.curator = curator
        self.students = []

    def get_students(self):
         for i in self.students:
             print(i.first_name, i.last_name)

    def add_student(self, *args):
        for i in args:
            self.students.append(i)


