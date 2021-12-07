import sqlite3
from sqlite3 import *
con = sqlite3.connect('students.db')
c = con.cursor()

c.execute("INSERT INTO students VALUES(1,'ksi','ola','21')")

c.fetchall()

# Save (commit) the changes
con.commit()
con.close()