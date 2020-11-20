# def doublit(x):
#     return x*2
# l1=list(map(doublit, [10,20,30,40,50]))
# print(l1)

# l2=list(map(lambda x:x*2, [10,20,30,40,50]))
# print(l2)

f_marks=[90,85,72,95,65,85]
s_marks=[80,50,45,60,92,65]
t_marks=list(map(lambda x,y:x+y,f_marks,s_marks))
print(t_marks)