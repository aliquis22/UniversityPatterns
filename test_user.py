import unittest
from users import Student

class TestStudentClass(unittest.TestCase):
    def test_valid_student_creation(self):
        student = Student("John", "Doe", "1998-01-01", 12345, "john@example.com", "Group A", "Course X")
        self.assertIsInstance(student, Student)

    def test_invalid_student_creation(self):
        with self.assertRaises(ValueError):
            student = Student(123, "Doe", "1998-01-01", 12345, "john@example.com", "Group A", "Course X")

    def test_get_marks(self):
        student = Student("John", "Doe", "1998-01-01", 12345, "john@example.com", "Group A", "Course X")
        # Тестирование метода get_marks, например, проверка вывода на экран
        # Вместо print, можно использовать assert, чтобы сравнивать вывод с ожидаемым результатом.

    def test_get_table(self):
        student = Student("John", "Doe", "1998-01-01", 12345, "john@example.com", "Group A", "Course X")
        # Тестирование метода get_table, аналогично проверка вывода на экран

if __name__ == '__main__':
    unittest.main()
