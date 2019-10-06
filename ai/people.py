# 과제 2 - people.py

class Person:

    def __init__(self, name='', age=0, department=''):
        self.name = name
        self.age = age
        self.department = department

    def get_name(self):
        print(self.name)


class Student(Person):
    def __init__(self, name='', age=0, department='', stu_id=0, GPA=0.0):
        Person.__init__(self, name=name, age=age, department=department)
        self.stu_id=stu_id
        self.GPA=GPA
        self.advisor = ""

    def print_info(self):
        print("'제 이름은 %s, 나이는 %d, 학과는 %s, 지도교수님은 %s 입니다.'" %(self.name, self.age, self.department, self.advisor))

    def reg_advisor(self, P):
        self.advisor = P.name

class Professor(Person):

    def __init__(self, name='', age=0, department='', position='', laboratory=''):
        Person.__init__(self, name=name, age=age, department=department)
        self.student = []
        self.position = position
        self.laboratory = laboratory

    def print_info(self):
        s=''
        for i in self.student:
            s += ", "+ i
        s = s[2:]
        print("'제 이름은 %s, 나이는 %d, 학과는 %s, 지도학생은 %s 입니다.'" %(self.name, self.age, self.department, s))

    def reg_student(self, S):
        self.student.append(S.name)


stu1 = Student('Kim', 30, 'Computer', 20001234, 4.5)
stu2 = Student('Lee', 22, 'Computer', 20101234, 0.5)
prof1 = Professor('Lee', 55, 'Computer', 'Full', 'KLE')

stu1.reg_advisor(prof1)
stu2.reg_advisor(prof1)
prof1.reg_student(stu1)
prof1.reg_student(stu2)

stu1.print_info()
stu2.print_info()
prof1.print_info()