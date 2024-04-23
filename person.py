import random
from school import School

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)    

    def evaluate_exam(self):
        return random.randint(1, 100)
    
class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classmethod
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None

    def final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            sum += point

