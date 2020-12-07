import sqlite3 as sql
conn=sql.connect("PWG.sqlite3")
curs=conn.cursor()
curs.execute("select * from employee where idno=102")
result=curs.fetchall()
for x in result:
    for y in x:
        print(y)
conn.close()

