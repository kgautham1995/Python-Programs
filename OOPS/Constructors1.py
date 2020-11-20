# 1. Parameterized Constructor
# 2. Non Parameterized Constructor

# 1. Parameterized Constructor
class student:
    def __init__(self, id, name):
        self.id1=id
        self.name1=name
    def display(self):
        print(self.id1,self.name1)
s=student(101,"vikas")
s.display()


# 2. Non Parameterized Constructor
class student:
    def __init__(self):
        self.id1=102
        self.name1="Vijay"
        print(self.id1, self.name1)
s=student()