number = int(input("please enter a whole number integer between 1 and 12: "))
if number >= 1 and number <= 12:
    print("your number is valid")
    if number == 1:
        print("January")
    elif number == 2:
        print("February")
    elif number == 3:
        print("March")
    elif number == 4:
        print("Aprill")
    elif number == 5:
        print("May")
    elif number == 6:
        print("June")
    elif number == 7:
        print("July")
    elif number == 8:
        print("August")
    elif number == 9:
        print("September")
    elif number == 10:
        print("October")
    elif number == 11:
        print("November")
    else:
        print("December")
else:
    print("Your number is invalid")
        
