class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intro(self):
        print(f'Hello my name is {self.name} and I\'m {self.age} years old ')
    
stud1 = Student("Raza",21)

stud1.intro()