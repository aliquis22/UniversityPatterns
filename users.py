class User():
    def __init__(self, first_name, last_name, birthday, email):
        self.first_name = first_name.lower().title()
        self.last_name = last_name.lower().title()
        self.birthday = birthday
        self.email = email
    def get_inform(self):
        print(f'{self.first_name} {self.last_name}')
        print(f'Birthday: {self.birthday}')
        print(f'Email: {self.email}')

class Student(User):
    def __init__(self, first_name, last_name, birthday, student_id, email, group, course):
        super().__init__(first_name, last_name, birthday, email)
        if (not isinstance(first_name, str) or not isinstance(student_id, int)  or not isinstance(last_name, str)
                or not isinstance(birthday, str) or not isinstance(email, str)):
            raise ValueError("Неверные типы данных для аргументов")
        self.student_id = student_id
        self.group = group
        self.course = course
    def get_marks(self):
        print('Оценки')
    def get_table(self):
        print('Расписание')

