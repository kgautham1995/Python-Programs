# lambda functions without arguments and without return

a=lambda : print("Welcome to programming with Gautam")
a()


# lambda functions with arguments and without return

b=lambda x,y : print("The sum of ",x ,"&",y ,"is", x+y)
b(10,20)

# lambda functions without arguments and with return
c=lambda  : 20+50
print("the sum is ",c())

# lambda functions with arguments and with return

d=lambda a=50,b=5 :a*b
print("The Multiplication is",d())
print(type(d))