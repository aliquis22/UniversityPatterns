class University():
    def __init__(self, name, adress, phone, *schools):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.schools = list(schools)
    def add_school(self, school):
        self.schools.append(school)
    def get_schools(self):
        return self.schools
class School():
    def __init__(self, name, specialization, *courses):
        self.name = name
        self.specialization = specialization
        self.course = list(courses)



