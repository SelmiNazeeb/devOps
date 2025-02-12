class Person:
    def __init__(self,fname='default_name',age=0):  #giving the values by default if no input is given 
        self.fname=fname
        self.age=age
        self.skills=[]
    
    def printing(self):
        return f'fname:{self.fname}, age:{self.age}, skills:{self.skills}'
    
    def add_skills(self,skill):
        self.skills.append(skill)

class Student(Person):
    def __init__(self, fname='default_name', age=0,studentId=0):
        super().__init__(fname, age)    #calls the constructor of the parent class ,ie call methods from the parent class
        self.studentId=studentId
    def printing(self):
        return f'{super().printing()},studentID:{self.studentId}'

s1=Student("selmi",22)
print(s1.printing())