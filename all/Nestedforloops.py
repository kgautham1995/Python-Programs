# for x in seq:
#     _________________
#     for y in seq:
#         _____________________
#         ________________________
#     _______________________
#     _______________________
#
# 1 1 1
# 2 2 2
# 3 3 3
# print("1 1 1")
# print("2 2 2")
# print("3 3 3")
# for x in range(1,10,1):
#     for y in range(10):
#         print(x, end=" ")
#     print()
for x in range(26):
    for y in range(x+1):
        print(chr(y+65), end=" ")
    print()

# A
# A B
# A B C