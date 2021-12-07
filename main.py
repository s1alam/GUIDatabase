import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("Database")
root.geometry("520x200")

idlabel = tk.Label(root,text = "StudentID")
idlabel.grid(row = 1, column = 0)
idbox = tk.Entry(root, )
idbox.grid(row = 1,column = 1)

fnamelabel = tk.Label(root,text = "FirstName")
fnamelabel.grid(row = 2, column = 0)
fnamebox = tk.Entry(root, )
fnamebox.grid(row = 2,column = 1)

lnamelabel = tk.Label(root,text = "LastName")
lnamelabel.grid(row = 3, column = 0)
lnamebox = tk.Entry(root, )
lnamebox.grid(row = 3,column = 1)

agelabel = tk.Label(root,text = "Age")
agelabel.grid(row = 4, column = 0)
agebox = tk.Entry(root, )
agebox.grid(row = 4,column = 1)

insertbutton = tk.Button(root,text = "INSERT", bg= "lightblue")
insertbutton.grid(row = 5, column = 1)

def insertfunction():
  idinfo = idbox.get()
  nameinfo = fnamebox.get()
  sinfo = lnamebox.get()
  ageinfo = agebox.get()

  con = sqlite3.connect('students.db')
  c = con.cursor()
  c.execute("INSERT INTO students VALUES(?,?,?,?)",(idinfo,nameinfo,sinfo,ageinfo))
  c.execute("SELECT * FROM students")
  print(c.fetchall())
  con.commit()
  con.close()

def show():
  con = sqlite3.connect('students.db')
  c = con.cursor()
  c.execute("SELECT * FROM students")
  print(c.fetchall())
  con.commit()
  con.close()

insertbutton = tk.Button(root,text = "INSERT", bg= "lightblue", command = insertfunction)
insertbutton.grid(row = 5, column = 1)


showbutton = tk.Button(root, text = "SHOW",command = show, bg = "lightblue")
showbutton.grid(row = 5, column = 0)

root.mainloop()