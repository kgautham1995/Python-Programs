# open() is ised to open the files in python
# r - read mode
# w -  write mode
# a -append mode

file = open("abc.txt", "r")
text = file.read()
print(text)
file.close()