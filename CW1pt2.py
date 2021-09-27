#Shriya Anand and Angela Zhang
# SoftDev
# Classwork- Class Names
# POW WOW SUMMARY: When you call the printName() function, it asks you which period you want the student from. Originally, the code would then provide a random student from the list; after talking to my partner, however, we have changed it so that the user can input which number student they want from the list.

import random
pd1 = ['emma', 'shriya', 'william']
pd2 = ['a', 'b', 'c']
def printName():
    try: 
        period = int(input("Period 1 or 2? (only type number)"))
        name_index = int (input("Choose a number from 0 to 2"))
        if period == 1:
             print (pd1[name_index])
            #print(pd1[random.randint(0,len(pd1)-1)])
        elif period == 2:
             print (pd2[name_index])
            #print (pd2[random.randint(0,len(pd2)-1)])
        else:
            print ("This input is not valid")
       
    except: print ("This input is not valid")
