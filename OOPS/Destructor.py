class student():
    def __init__(self):
        print("I am a constructor")
    def show(self):
        print("I am show")
    def __del__(self):
        print("I am Destructor")
s=student()
s.show()
del s
s.show()