#Shriya Anand and Angela Zhang
# SoftDev
# Classwork- Class Names
# POW WOW SUMMARY : When you call the printName() function, it asks you which period you want the student from.
# SUMMARY OF TRIO DISCUSSION : Originally, the code would provide a random student from the list or ask you to input a number;
# after talking to my partner, however, we have changed it so that it reads a file for both first period and second period, makes 
# the names into a list each, and then spits out a random name from those periods.
# QUESTIONS
# Is there a way this can be done with last names as well as first names like "Name, Test"? Since commas wouldn't work 
# correctly anymore as a splitting device? -- Angela
# COMMENTS
# Python is not that much different from java, but it certainly feels like a different language -- Angela
        
    try:
        
        period = int(input("Period 1 or 2? (only type number)"))
        
        if period == 1:           
            print (dictionary["one"][random.randint(0,len(pd2)-1)])
        elif period == 2:
            print (dictionary["two"][random.randint(0,len(pd2)-1)])
        else:
            print ("This input is not valid")
       
    except: print ("This input is not valid")


import random # allows you to use random

def printName(): # function 
    try: # attempts and if it doesn't work it sends an error and doesn't break things
        file = open("pd1.txt", "r") # just reads "r" the txt 
        contents1 = (file.read())
        pd1 = (contents1.split(", ")) # splits it, make it into list

        file = open("pd2.txt", "r") # does same here as ^^^
        contents2 = (file.read())
        pd2 = (contents2.split(", "))
        
        dictionary = {} # creates a dictionary instance
        dictionary["one"] = pd1 # puts it into a dictionary under "one" and defines it
        dictionary["two"] = pd2
        
    except: print ("One or more files are not valid") # if there is only one file, or none at all, this message is printed
        
    try:  
        period = int(input("Period 1 or 2? (only type number)")) # asks for number, and turns it from string input to int in one line
        
        if period == 1:
            print (dictionary["one"][random.randint(0,len(pd2)-1)])
        elif period == 2:  # this is an else if, written as elif
            print (dictionary["two"][random.randint(0,len(pd2)-1)])
        else:
            print ("This input is not valid")
       
    except: print ("This input is not valid") # for errors like numbers that aren't 1 or 2
