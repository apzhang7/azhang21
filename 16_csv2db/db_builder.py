# Team Snaps (Emma Buller, Theo Fahey, Angela Zhang)
# SoftDev
# K16 -- All About Database
# 2021-10-22

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db" #This is the file you do sqlite commands on. Remove it before you run the file again

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
c.execute("CREATE TABLE roster (name TEXT, age INTEGER, id INTEGER)") #NEW TABLE

with open('students.csv') as csvfile: #open file
    reader = csv.reader(csvfile, delimiter= ",") #splits line for text
    for row in reader:
        name = row[0] #row is split into a list of strings
        age = row[1]
        id = row[2]
        if(age != "age"): #skips first line
            command = "INSERT INTO roster VALUES ('" + name + "'," + age + "," + id + ")" #quotes around name = TEXT/strng; no quotes = INTEGER
            c.execute(command); #rows inserted into table

c.execute("CREATE TABLE classes (code TEXT, mark INTEGER, id INTEGER)") #NEW TABLE
with open('courses.csv') as file: #same as first table, but with different variable names
    r = csv.reader(file, delimiter= ",")
    for row in r:
        code = row[0]
        mark = row[1]
        id = row[2]
        if(mark != "mark"):
            command = "INSERT INTO classes VALUES ('" + code + "'," + mark + "," + id + ")"
            c.execute(command);
# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


# command = ""          # test SQL stmt in sqlite3 shell, save as string
# c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
