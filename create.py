import sqlite3

con = sqlite3.connect('students.db')
c = con.cursor()

# Create table
c.execute('''CREATE TABLE students(
  StudentID integar,
  name text,
  surname text,
  age integar
)''')

con.commit()
con.close()