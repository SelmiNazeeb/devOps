class Person:
    def __init__(self,fname='default_name',age=0):
        self.fname=fname
        self.age=age
        self.skills=[]
    def printing(self):
        return f'fname:{self.fname}, age:{self.age}, skills:{self.skills}'
    def add_skills(self,skill):
        self.skills.append(skill)

p=Person("Selmi",22)
p1=Person()
#print(p.fname," ",p.age)
print(p1.fname," ",p1.age)
p.add_skills("python")
print(p.printing())


