#Aunik Hussain
#05/10/2014
#IF statement practice


age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to vote")
if age < 18:
    print("You are too young to vote")
if age > 65:
    print("You are retired")
    
retirement = 65 - age

if age < 65:


    print("You will retire in {0} years.".format(retirement, age))
