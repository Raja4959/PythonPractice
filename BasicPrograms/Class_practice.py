a=["raja","naresh","chandu","raja","chandu"]
unique = [i for i in a if a.count(i)==1]
print(unique)



class College():
    def __init__(self,name):
        self.college_name = name
        self.students = []

    def add_students(self,roll,name,group):
        self.students.append((roll,name,group))

    def remove_student(self,roll):
        for i in self.students:
            if roll == i[0]:
                self.students.remove(i)

c1 = College("College")
c1.add_students(1,"raja","cse")
c1.add_students(2,"naresh","ece")
print(c1.students)