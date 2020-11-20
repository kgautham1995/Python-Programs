# A-Z=65-91
# a-z=97-122

# A----a
# for x in range(26):
#     print(x+1,"----",chr(x+65),"----",chr(x+97))

x=int(input("Enter the number to print the table:"))
for z in range(1,x):
    print(x,"*",z,"=",x*z)