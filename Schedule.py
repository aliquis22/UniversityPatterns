
class Subject():
    def __init__(self, name, teacher, corp, aud):
        self.name = name
        self.teacher = teacher
        self.corp = corp
        self.aud = aud
        self.state = True

    def cancel(self):
        self.state = False

    def get_info(self):
        print(self.name)
        print(f'{self.teacher.first_name} {self.teacher.last_name}')
        print(self.corp)
        print(self.aud)
        if self.state == True:
            print("Занятие состоится")
        else:
            print("Занятие отменено")
class Schedule():
    def __init__(self):
        self.schedule = {i : { i : { i: {} for i in range(1,8)} for i in range(1,8)} for i in range(1,22)}

    def create_class(self, teacher,subject, group, week, day, time, corp, aud):
        self.schedule[week][day][time][group.name] = Subject(subject, teacher,corp,aud ) #[subject, f'{teacher.first_name} {teacher.last_name}', corp, aud, state]
