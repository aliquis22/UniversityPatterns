from users import *
from university import  *
from school import *
from group import *
from journal import *
from Schedule import *

tpu = University("Томский Политехнический Университет", 'г.Томск, пр.Ленина 30', '8-800-555-35-35')
schl1 = School('Инженерная школа информационных технологий и робототехники', 'Информационные технологии')
grp1 = Group('8К13', schl1, 'Титаренко Екатерина Юрьевна')
schl1.courses[3].append(grp1)
std1 = Student('Владислав', 'Зарубин', '02-01-2003', 13261, 'vaz30@tpu.ru', grp1, '3')
std2 = Student('Олег', 'Семченко', '16-03-2003', 13262, 'ops5@tpu.ru', grp1, '3')
std3 = Student('Алексей', 'Донела', '01-07-2003', 13263, 'agd8@tpu.ru', grp1, '3')
jrnl1 = Journal()

#ЛБ12
tpu.add_applicant("Дарья", "Дмитрийчук", "08-08-2003",'did7@tpu.ru',schl1)
tpu.add_applicant("София", "Нижегородцева", "17-09-2003",'son1@tpu.ru',schl1)
enrl2021 = Enrolle(tpu, schl1)
enrl2021.create_students()
course = schl1.get_corses()
print("Студенты 8К13:")
grp1.add_student(std1, std2)
grp1.get_students()
print("Студенты 8К11:")
grp = course[1][0]
grp.get_students()

#ЛБ13
proxy = Employee("Михаил",'Малышев', '23-11-2003', 'mym10@tpu.ru', 'Системный Администратор')
proxy.view_student_details(std1)

#ЛБ14
tchr = Teacher("Ефремова", "Оксана", "01-01-1970", "fedor@tpu.ru", 'старший перподаватель', 'Математика')
schdl = Schedule()
schdl.create_class(tchr, tchr.subjects[0],grp, 1,1,1,'ГК',227)
schdl.schedule[1][1][1]['8К11'].get_info()
tchr.cancel_class(schdl,1,1,1,grp)
schdl.schedule[1][1][1]['8К11'].get_info()


