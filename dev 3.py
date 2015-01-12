hours = int(input("please enter the number of hours you have worked this week"))
rate = float(input("please enetr your rate of pay"))
pay = hours * rate
if hours >= 0 and hours <= 60:
    print("your hours is within the range")
    if hours <= 40:
        print("your pay is.....")
        print(pay)
    elif hours > 40:
        overtime_rate = rate * 1.5
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * overtime_rate
        normal_hours = 40
        normal_pay = 40 * rate
        total = normal_pay + overtime_pay
        print(total)
else:
    print("hours is invalid")
        


