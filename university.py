from users import User
class University():
    def __init__(self, name, adress, phone, *schools):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.schools = list(schools)
        self.teachers = []
        self.admin = []
        self.applicants = []
    def add_school(self, school):
        self.schools.append(school)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def add_applicant(self, first_name, last_name, birthday, email, school):
        applicant = User(first_name, last_name, birthday, email)
        data = [applicant, school]
        self.applicants.append(data)
    def get_schools(self):
        return self.schools
    def get_teachers(self):
        return self.teachers
    def get_applicants(self):
        return self.applicants
class School():
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.courses = {1: [], 2: [], 3: [], 4: []}




