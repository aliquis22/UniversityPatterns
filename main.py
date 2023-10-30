from users import *
from university import  *
from group import *
from journal import *

tpu = University("Томский Политехнический Университет", 'г.Томск, пр.Ленина 30', '8-800-555-35-35')
schl1 = School('Инженерная школа информационных технологий и робототехники', 'Информационные технологии')
grp1 = Group('8К13', schl1, 'Титаренко Екатерина Юрьевна')
schl1.courses[3].append(grp1)
std1 = Student('Vladislav', 'Zarubin', '02-01-2003', 13261, 'vaz30@tpu.ru', '8K13', '3')
std2 = Student('Oleg', 'Semchenko', '16-03-2003', 13262, 'ops5@tpu.ru', '8K13', '3')
grp1.add_student(std1, std2)
grp1.get_students()
jrnl1 = Journal()
jrnl2 = Journal()
print(hash(jrnl1))
print(hash(jrnl2))

