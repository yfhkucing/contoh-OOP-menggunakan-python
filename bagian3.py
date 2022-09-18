
class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class course :
    def __init__(self,name,max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student (self,student):
        if len(self.students) < self.max_student :
            self.students.append(student)
            return True
        return False

    #akumulator(?), kayak pas matkul progkom
    def average(self,):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

S1 = student("otong",19,20)
S2 = student("pakpol",20,90)
S3 = student("budi",20,80)

course =course("sysdick",2)
course.add_student(S1)
course.add_student(S2)
course.add_student(S3)

print(course.students[1].name)
print(course.average())