import grade
import datetime

class AverageGradeStrategy:
    def calculate(self, marks):
        return sum(marks) / len(marks)

class MaxGradeStrategy:
    def calculate(self, marks):
        return max(marks)

class Journal:
    _instance = None
    _strategy = AverageGradeStrategy()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Journal, cls).__new__(cls)
            cls._instance.init_journal()
        return cls._instance

    def init_journal(self):
        self.journal = {}
        self.attendance = {}

    @classmethod
    def set_grade_strategy(cls, strategy):
        cls._strategy = strategy

    def add_student(self, group, subject, student_name):
        if subject not in self.journal:
            self.journal[subject] = {}
        if group not in self.journal[subject]:
            self.journal[subject][group] = {}
        if student_name not in self.journal[subject][group]:
            self.journal[subject][group][student_name] = []

    def add_mark(self, subject, group, student, value):
        if subject in self.journal and group in self.journal[subject] and student in self.journal[subject][group]:
            mark = grade.Grade(value, datetime.date, student.student_id, subject)
            self.journal[subject][group][student.student_id].append(mark)

    def add_attendance(self, subject, group, student, value):
        if subject in self.journal and group in self.journal[subject] and student in self.journal[subject][group]:
            att = grade.Attendance(value, datetime.date, student.student_id, subject)
            self.attendance[subject][group][student.student_id].append(att)

    def get_student_grades(self, student_name, group, subject):
        if subject in self.journal and group in self.journal[subject] and student_name in self.journal[subject][group]:
            return self.journal[subject][group][student_name]
        else:
            return "404 not found"

    def get_average(self, subject, group):
        marks = [mark.value for student_marks in self.journal[subject][group].values() for mark in student_marks]
        return self._strategy.calculate(marks)

    def get_max_average_student(self, subject, group):
        students = self.journal[subject][group].keys()
        students_averages = {
            student: self._strategy.calculate([mark.value for mark in marks])
            for student, marks in self.journal[subject][group].items()
        }
        max_student = max(students_averages, key=students_averages.get)
        return max_student, students_averages[max_student]


