
__author__ = 'Шонтукова Арина Артуровна'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import random

FAMILY = ('Иванов','Петров','Кузнецов','Цой','Ким','Алексеев','Лунин','Волков','Михайлов')
IO = ('И. В.','М. А.','Л. Б.','Н. С.','Р. М.','Г. В.','П. П.','С. О.','Н. Г.')
SUBJECT = ('рус. яз.', 'литература', 'математика', 'информатика', 'физика', 'химия', 'биология')

class School():
    def __init__(self,name):
        self.name = name
        self.Classes = []
    def addClass(self, Clas):
        self.Classes.append(Clas)
    def showClasses(self):
        print('В школе {}'.format(self.name))
        for itm in self.Classes:
            print('классов {}'.format(itm.name))
    def showClass(self, name):
        for itm in self.Classes:
            if itm.name == name: itm.showClass()
    def showStudentsInfo(self, name):
        for cl in self.Classes:
            for s in cl.Student:
                if s.name == name:
                    for teach in cl.Teachers:
                        print('Ученик {} класс {} преподаватель {} предмет {}'.format(s.name, cl.name, teach.name, teach.subject))
    def showStudentParents(self, name):
        for cl in self.Classes:
            for s in cl.Students:
                if s.name == name: s.showParents()
    def genSchool(self, classes, student, subjects):
        for idx in range(int(classes)):                 
            xclass = Class(str(random.randint(1,11))+random.choice(('A', 'B', 'C', 'D')))
            self.addClass(xclass)
            for i in range(int(students)):
                xclass.addStudent(Student(random.choice(FAMILY)+' '+random.choice(IO)+random.choice(IO),
                                      random.choice(FAMILY)+' '+random.choice(IO)+random.choice(IO),
                                      random.choice(FAMILY)+'а '+random.choice(IO)+random.choice(IO)))
            for i in range(int(subjects)):
                xclass.addTeacher(random.choice(FAMILY)+random.choice(NAME)+random.choice(NAME), random.choice(SUBJECT))
            
class Class():
    def __init__(self, name):
        self.name = name
        self.Students = []
        self.Teachers = []
    def addStudent(self, student):
        self.Students.append(student)
    def addTeacher(self, name, subject):
        self.Teachers.append(Teacher(name, subject))
    def showClass(self):
        print('В классе {}'.format(self.name))
        for itm in self.Student:
            print('учеников {}'.format(itm.name))

class Students():
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother
    def showParents(self):
        print('Отец - {}, Мать - {}'.format(self.father, self.mother))

class Teacher():
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject