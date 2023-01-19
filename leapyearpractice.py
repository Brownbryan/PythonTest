year=int(input("Enter a year you would like to check: "))
if year % 4==0:
    if year %100==0:
        if year%400==0:
            print("This ia a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")