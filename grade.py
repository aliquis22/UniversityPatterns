#ЛБ15
class Grade:
    def __init__(self, value, date, student_id, subject):
        self.value = value
        self.date = date
       # self.student_id = student_id
        self.subject = subject

class GradePool:
    _pool = {}
    @staticmethod
    def get_grade(value, date, student_id, subject):
        # Создание уникального ключа для экземпляра Grade
        key = f"{value}_{date}_{student_id}_{subject}"
        # Если такой объект уже существует, возвращаем его
        if key in GradePool._pool:
            return GradePool._pool[key]
        # Иначе создаем новый объект Grade
        else:
            grade = Grade(value, date, student_id, subject)
            # Добавляем его в пул объектов
            GradePool._pool[key] = grade
            return grade

class Attendance:
    def __init__(self, value, date, student_id, subject):
        self.value = value
        self.date = date
        # self.student_id = student_id
        self.subject = subject

