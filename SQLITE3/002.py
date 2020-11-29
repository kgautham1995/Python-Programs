import sqlite3 as sql
conn=sql.connect("PWG.sqlite3")
curs=conn.cursor()
idno=int(input("Enter id no"))
name=input("Enter name")
salary=float(input("Enter the salary"))
try:
    curs.execute("insert into employee values(?,?,?)",(idno,name,salary))
    conn.commit()
    print("Data Stored Successfully")
except sql.IntegrityError:
    print("Data already Exists")
conn.close()
print("Thanks")