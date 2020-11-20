# Identity Operators(is, is not)

a=10
b=10
print(a is b)
print(id(a))
print(id(b))

a=[10,20]
print(id(a))
b=[10,20,30]
print(id(b))
print(a is b)
print(a==b)