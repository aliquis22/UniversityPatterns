import unittest
from university import University, School

class TestStudentClass(unittest.TestCase):
    def test_get_schools_returns_collection(self):
        schl1 = School('ИШИТР', 'Программирование и информационные технологии')
        university = University("Томский Политех", "пр.Ленина 30", "8-800-555-35-35", schl1)
        schools = university.get_schools()
        self.assertIsInstance(schools, list)

if __name__ == '__main__':
    unittest.main()
