import sqlite3 as sql
conn=sql.connect("PWG.sqlite3")
curs=conn.cursor()
try:
    curs.execute("Create table employee(idno number unique, name text, salary real)")
    print("Table is created Successfully")
except sql.OperationalError:
    print("Table already exists")
finally:
    conn.close()
print("Thanks")