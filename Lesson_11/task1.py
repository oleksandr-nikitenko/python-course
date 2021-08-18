"""
Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute, while salary
 should only be available to the teacher.
"""


class Person:
    
    def __init__(self, fname: str, lname: str):
        self.first_name = fname
        self.last_name = lname
        
    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def display_full_info(self):
        pass
    
    
class Student(Person):
    role = 'Student'
    count = 0
    
    def __init__(self, fname: str, lname: str, age: int, class_number: str, subjects_for_study: list = []):
        super().__init__(fname, lname)
        self.age = age
        self.class_number = class_number
        self.subjects_for_study = subjects_for_study
        Student.count += 1
        
    def add_subject_study(self, item: str) -> None:
        self.subjects_for_study.append(item)
        
    def delete_subject_study(self, item: str) -> None:
        if item in self.subjects_for_study:
            self.subjects_for_study.remove(item)
            
    def display_full_info(self):
        return f'{Student.role}: {self.get_full_name()},{self.age}, {self.class_number},{self.subjects_for_study}'
        
        
class Teacher(Person):
    role = 'Teacher'
    count = 0
    
    def __init__(self, fname, lmame, office, subjects_for_teaching=[]):
        super().__init__(fname, lmame)
        self.office = office
        self.subjects_for_teaching = subjects_for_teaching
        self.salary = 10
        self.students_list = []
        Teacher.count += 1
    
    def add_student(self, student_obj):
        self.students_list.append(student_obj)

    def display_full_info(self):
        return f'{Teacher.role}: {self.get_full_name()},{self.office}, {self.salary*len(self.students_list)}, ' \
               f'students: {str([i.first_name for i in self.students_list])}'


# Create 1 student
stud1 = Student('John', 'Smith', 12, '7-B', ['physics', 'mathematics'])
stud1.delete_subject_study('physics')
stud1.add_subject_study('biology')
print(stud1.display_full_info())
# Create 2 student
stud2 = Student('Tomas', 'Smith', 11, '6-A', [])
stud2.add_subject_study('chemistry')
stud2.add_subject_study('mathematics')
print(stud2.display_full_info())
# Create teacher
teach1 = Teacher('Robert', 'Langdon', '100', ['mathematics'])
teach1.add_student(stud1)
teach1.add_student(stud2)
print(teach1.display_full_info())

#print(Teacher.count, Student.count)




