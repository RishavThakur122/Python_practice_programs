import sqlite3
mybooks=sqlite3.connect('books.db')
mybookname=input("give the name of the book ")
noofcopies=int(input("guve no of copies you required:"))
sql="SELECT * from BOOKS WHERE NAME='"+mybookname+"';"
curbooks=mybooks.cursor()
curbooks.execute(sql)
record=curbooks.fetchone()
print (record)                 

