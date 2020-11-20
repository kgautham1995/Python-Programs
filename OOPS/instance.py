class student:
    def allot(self,id, na):
        self.idno=id
        self.name=na
    def display(self):
        print("Student id is:",self.idno)
        print("Student name is:",self.name)
a=student()
a.allot(101,"vijay")
a.display()

a.allot(102,"vikas")
a.display()