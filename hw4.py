#!/usr/bin/ python
'''
Python v3.7
July 24, 2019
Homework 4 - Kassandra Bethune
hw4.py
'''

#get user input for household item
itemName1 = str(input("Name an item in your house:"))

#get user input for item value
itemValue1 = float(input("What's the value of this item?"))

#store user input in tuple
homeInventory1 = (itemName1, itemValue1)

#get input for an additional item
itemName2 = str(input("Name an additional item in your house:"))

#get the value of the second item
itemValue2 = float(input("What is this item's value?"))

#store second items to new tuple
homeInventory2 = (itemName2, itemValue2)

#create two demensional tuple
allInventory = (homeInventory1, homeInventory2)

#ask user if they want to save/add data to file
userSave = input("Would you like to save your home inventory? Type yes or no. ")

'''
Feedback: when running this block of code which displays the inventory items in a more organized way. 
I am getting a duplicate of the first tuple. Not sure why.

#if userSave.lower() == "yes":
#    outList = []
#    for x in allInventory:
#        print(x)
#        myItem = x[0]
#        myValue = x[1]
#        outLine = "item:{} value:{}\n".format(myItem, myValue)
#        outList.append(outLine)
'''

#if user enters 'yes', we save inventory to file
if userSave.lower() == "yes":
        with open(r"C:\Users\Kass\Documents\HomeInventory.txt", "a") as filetxt:
            filetxt.writelines(str(allInventory))
#any other input from user does not save items
else:
    print("No items saved.")

