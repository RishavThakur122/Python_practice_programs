import sqlite3
newschool=sqlite3.connect('college.db')
curdcoll=newschool.cursor()
curdcoll.execute('''CREATE TABLE COLUGES(

NAME            STRING  NOT NULL,
AGE            INTEGER  NOT NULL,
QUALIFICATION  INTEGER  NOT NULL
);'''










    )
newschool.close()
