class student:
    def assign(self, id, na):
        self.idno=id
        self.name=na
class school(student):
    def assign_school(self, school):
        self.sch=school
    def display(self):
        print("Student Name:", self.name)
        print("Student Id no:", self.idno)
        print("Student School:", self.sch)
s=school()
s.assign(1001,"Vijay")
s.assign_school("abc High School")
s.display()