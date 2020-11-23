class student:
    def assign(self, id, na):
        self.idno=id
        self.name=na
class school(student):
    def assign_school(self, school):
        self.sch=school
class dip(school):
    def display(self):
        print(self.idno, self.name,self.sch)
d=dip()
d.assign(1001, "Vikas")
d.assign_school("abc school")
d.display()
