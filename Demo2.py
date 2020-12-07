#
# 1 storing the data
# 1 employee name
# 2 manager name
#
# 2. retrieval function
# emp=[]
# man=[]
# dic= {}
# def store():
#     x= input("Enter the employee's Name")
#     y= input("Enter the Manager's Name")
#     emp.append(x)
#     man.append(y)
#     dic={x:y}
# def ret(a):
#     if a in dic or dic[z]:
#         print(a, dic[a])
#         a = dic[a]
#         ret(a)
# no=int(input("Enter the no of employees you want to enter"))
#
# for a in range(no):
#     store()
# z = input("Enter the employee's name")
# ret(z)


# Order book
# pencil
# shopkeeper is buying and selling
#
# selling at x rs
#
# buy at z vars
#
# quantity also

buying={ }
selling={ }
def buy():
    xprice= input("Enter the Price of the product")
    xqty= input("Enter the Qty of the product")
    buying.update({xprice:xqty})
def sell():
    yprice=input("Enter the price of the product")
    yqty=input("Enter the qty of the product")
    buying.update({yprice: yqty})
no=int(input("enter the no of buying or selling values"))
for x in range(no):
        buy()
        sell()
x = input("Enter the price of the product the buyer wants to buy at")


if buying.keys() in selling.keys():
    a=buying.get(x)
    b=selling.get(x)
    if a==b or a<=b:
        buying.pop(x)
    selling.x=selling.x-b














