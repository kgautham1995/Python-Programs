# Constructor: A constructor is a special kind of method which
#  is used to initialize the instance variables of a class
# Constructor should always be "__init__()"
# This kind of method is also called as Dunder method
# (Double underscore) These are also called as Magic Methods
# Constructors will take 'self' as the default parameter:
# def __init__(self):
# Constructor is called automatically when the object is created

class student:
    def __init__(self):
        print("Hello i am a constructor")
    def show(self):
        print("Hello i am a Instance method")
s=student()