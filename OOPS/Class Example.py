class student:
    school_name="ABC high School"
    def allot(self, idno, name):
        self.id=idno
        self.na=name
    def display(self):
        print(student.school_name)
        print(self.id)
        print(self.na)
        print(student.school_no)
    school_no=9595959595
s1=student()
s1.allot(101,"abc")
s1.display()
for x in range(5):
    a=int(input("Enter id no"))
    b=input("Enter Student Name")
    s2 = student()
    s2.allot(a, b)
    s2.display()
