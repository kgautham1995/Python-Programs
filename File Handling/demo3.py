# w-Write mode:
file=open("python.txt","w")
data=input("Enter the data you want to write in the file")
file.write(data)
file.close()
print("Data written to file successfully")