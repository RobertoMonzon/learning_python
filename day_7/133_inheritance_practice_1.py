# Create a class called Person, which has the following instance attributes: name, age. 
# Create another class, Student, that inherits these attributes from the first.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    pass

student_1=Student("John",15)
print(student_1.name)
print(student_1.age)