import sqlite3

conn = sqlite3.connect('tmp/test.db')

# conn.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
  VALUES (1, 'Paul', 32, 'California', 20000.00 )")
conn.commit()

data_list = [
  (2, 'Allen', 25, 'Texas', 15000.00),
  (3, 'Teddy', 23, 'Norway', 20000.00),
]
conn.executemany("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (?, ?, ?, ?, ?)", data_list)
conn.commit()

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit()

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
  print("ID = ", row[0])
  print("NAME = ", row[1])
  print("ADDRESS = ", row[2])
  print("SALARY = ", row[3])

conn.execute("DELETE from COMPANY where ID>=1;")
conn.commit()

conn.close()