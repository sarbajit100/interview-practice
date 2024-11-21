

class Student:
    def __init__(self,no, name, sub):
        self.no = no
        self.name = name
        self.sub = sub
    def display (self):
        print(self.no)
        print(self.name)
        print(self.sub)

s = Student(1,"raj","python")
s.display()
