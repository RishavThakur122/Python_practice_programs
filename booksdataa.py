import sqlite3
mybooks=sqlite3.connect('books.db')
mynumber=int(input("give the number of your book or the book number:"))
mybookname=input("give the name of the book :")
myprice=input("give the price of the book ")   
curbooks=mybooks.cursor()
curbooks.execute('''INSERT INTO BOOKS(NUMBER,NAME,PRICE)VALUES(?,?,?);''',(mynumber,mybookname,myprice)
)
print("data added succesfullly")
mybooks.commit()



    
