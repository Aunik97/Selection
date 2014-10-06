#Aunik Hussain
#06-10-2014
#revision ex 4

number1 = int(input("please enter a number"))
number2 = int(input("please enter a second number"))
number3 = int(input("please enter a third number"))


if number1 > number2 and number1 > number3:
    print("the number {0} is bigger".format(number1))
if number2 > number1 and number2 > number3:
    print("the number {0} is bigger".format(number2))
if number3 > number1 and number3 > number1:
    print("the number {0} is bigger".format(number3))
    

    
