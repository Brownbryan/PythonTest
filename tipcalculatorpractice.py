print("Welcome to the tip calculator.")
bill=input("What was the total bill? $")
new_bill=float(bill)
percent=input("What percetage tip would you like to give? 10, 12, or 15? ")
new_percent=float(percent)/100
people=input("How many people to split the bill? ")
new_people=int(people)
each_people=new_bill/new_people
total_bill=(each_people*new_percent ) + each_people
final_perperson= "{:.2f}".format(total_bill)
final_perperson=round(total_bill, 2)
print(f"Each person should pay: ${final_perperson}")
