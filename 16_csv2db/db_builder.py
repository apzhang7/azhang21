# Team Snaps (Emma Buller, Theo Fahey, Angela Zhang)
# SoftDev
# K16 -- All About Database
# 2021-10-22

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
c.execute("CREATE TABLE roster (name TEXT, age INTEGER, id INTEGER)")

with open('students.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter= ",")
    for row in reader:
        name = row[0]
        age = row[1]
        id = row[2]
        if(age != "age"):
            command = "INSERT INTO roster VALUES ('" + name + "'," + age + "," + id + ")"
            c.execute(command);

c.execute("CREATE TABLE classes (code TEXT, mark INTEGER, id INTEGER)")
with open('courses.csv') as file:
    r = csv.reader(file, delimiter= ",")
    for row in r:
        code = row[0]
        mark = row[1]
        id = row[2]
        if(mark != "mark"):
            command = "INSERT INTO classes VALUES ('" + code + "'," + mark + "," + id + ")"
            c.execute(command);
# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
