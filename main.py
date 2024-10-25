# Система управления курсами и студентами

from __future__ import annotations

from abc import abstractmethod

class Person:
      
    def __init__(self, person_id: int , name: str,  email: str):
        self._person_id: int = person_id
        self._name: str = name 
        self._email: str = email    
    
@staticmethod

@abstractmethod

    def from_console()-> Person:
     raise NotImplementedError('нужно реализовать метод')
  
    def __str__(self)-> str:
     return f'{self._person_id} {self._name} ({self._email})'


class Teacher(Person):

  def __init__(self, person_id : int , name : str, email: str, job_title: str):
     super().__init__(person_id, name, email)
     self._job_title: str = job_title
     
@property

def name(self):
     return self._name 
 
@staticmethod

def from_console()-> Teacher:
    person_id: int = int(input('Введите id'))
    name: str = input('Введите Имя ')
    email: str = input('Ведите Почту маил')     
    job_title: str = input('Введите Должность')
    return Teacher (person_id, name, email, job_title)

def __str__(self) -> str:
    return super().__str__() + f', Должность: {self._job_title} '


class Student(Person):
    def __init__(self, person_id: int, name: str, email: str, grade: float):
       super().__init__(person_id, name, email)
       self._grade = grade
       
       
@staticmethod

def from_console() -> Student:
    person_id: int = int(input('Введите id'))
    name:str = input('Введите Имя ')
    email:str = input('Введите почту маил')
    grade: float = float(input('Введите grade'))
    return Student (person_id , name , email, grade)

def __str__(self) -> str:
    return super().__str__() + f', Средняя Оценка: {self._grade}'


class Course:
    def __init__(self, name:str , teacher: Teacher , students: list[Student] = None):
       self.__name:str = name 
       self.__teacher: Teacher = teacher
       self.__student: list[Student]  = students
       if self.__students isNone: 
           self.__students = [] 
           
@property

def name(self):
    return self.__name


def has(self, student: Student) -> bool:
    return student in self.__students


def enrool(self, student: Student) -> None:
    if student in self.__students:
        raise Exception()
    self.__students.append(student) 

    
def __len__(self) -> int:
    return len(self.__students)


def __str__(self)-> str:
    return f'{self.__name} = {self.__teacher.name} ({len(self)})'


class University:
    def __init__(self):
        self.__teachers: list[Teacher] = []
        self.__courses: list[Course] = []
        self.__students: list[Student] = []
        
    def add_person(self, person: Person)-> None:
        if isinstance(person, Student):
            self.__students.append(person)
        elif isinstance (person, Teacher):
            self.__teachers.append(person)   
        else:
            raise Exception('Можно Добавить только Студента или Препода') 
     
    def add_course(self, course: Course)-> None 
         self.__courses.append(course)
         
    def get_students_info(self) -> str :
        students: dict[Student]: list[str] = {}
       
        for student inself.__students:
            students[student]: list[str] = []  
            for course in self.__courses: 
                if course.has(student):
                    students[student].append(course.name)             
                    return '\n'.join([str(student) + f' ({", ".join(courses)})' for student, courses in students.items()])
                
    def info(self) -> None:
		print('Студенты университета:')
		print(self.get_students_info())
		print()
		print('Преподаватели университета:')
		print('\n'.join([str(teacher) for teacher in self.__teachers]))
		print()
		print('Курсы в университете:')
		print('\n'.join([str(course) for course in self.__courses])) 