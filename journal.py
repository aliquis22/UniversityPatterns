import grade
import datetime
class Journal:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Journal, cls).__new__(cls)
            cls._instance.init_journal()
        return cls._instance

    def init_journal(self):
        self.journal = {}
        self.attendance= {}

    def add_student(self, group, subject, student_name, ):
        if subject not in self.journal:
            self.journal[subject] = {}
        if group not in self.journal[subject]:
            self.journal[subject][group] = {}
        if student_name not in self.journal[subject][group]:
            self.journal[subject][group][student_name] = []

    def add_mark(self, subject, group, student, value):
        if subject in self.journal and group in self.journal[subject] and student in self.journal[subject][group]:
            mark = grade.Grade(value,datetime.date, student.student_id, subject)
            self.journal[subject][group][student.student_id].append(mark)

    def add_attendance(self, subject, group, student, value):
        if subject in self.journal and group in self.journal[subject] and student in self.journal[subject][group]:
            att = grade.Attendance(value,datetime.date, student.student_id, subject)
            self.attendance[subject][group][student.student_id].append(grade)

    def get_student_grades(self, student_name, group, subject):
        if subject in self.journal and group in self.journal[subject] and student_name in self.journal[subject][group]:
            return self.journal[subject][group][student_name]
        else:
            return "404 not found"
    def get_average(self, subject, group):
         s = 0
         for i in group.students:
             marks = self.journal[subject][group][i.student_id]
             s += sum(marks)/len(marks)
         s /= len(group.students)
         print("Средний баллы группы: ", s)

