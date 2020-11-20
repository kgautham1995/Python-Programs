print(" T \n T r \n T r i \n T r i a \n T r i a n \n T r i a n g \n T r i a n g l \n T r i a n g l e")
text=input("Enter your name to see in triangle pattern as above: ")
for index in range(len(text)):
    print(*text[:index + 1])
    