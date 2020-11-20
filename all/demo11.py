# Functions without arguments and without return
def add():
    a=int(input("enter the value of a "))
    b=int(input("enter the value of b "))
    print("addition of",a ,b, "is" ,a+b)
add()




# Functions with arguments and without return
def add(a,b):
    print("addition of",a ,b, "is" ,a+b)
add(1500,21545)






# Functions without arguments and with return
def add():
    global a, b
    a=int(input("enter the value of a "))
    b=int(input("enter the value of b "))
    return a+b
addition=add()
print("addition of", a, b, "is ",addition)

# function with arguments and with return
def math1(a,b=541):
    return a+b
print("Addition is ", math1(154))










