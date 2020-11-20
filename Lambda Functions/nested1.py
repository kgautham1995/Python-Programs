# def outer():
#     x=100
#     print("outer Function")
#     print(x)
#     print("------------------")
#     def inner():
#         global x
#         x=200
#         print("Inner Function")
#         print(x)
#     inner()
#     print(x)
def outer():
    print("i am outer")
    x=lambda :print("I am Lambda")
    x()