two_digit_number=input("")

# Check the data type of two_digit_number
# print(type(two_digit_number))
#converting first and second digits from str to int
# first_digit=int(two_digit_number[0])
# second_digit=int(two_digit_number[1])
# #add the two digits number
# two_digit_number=first_digit+second_digit
# print(two_digit_number)


# weight_pound=input("Your weight in pounds: ")
# weight_kg=float(weight_pound)*0.453592
# print(type(weight_pound))
# print("you are " + str(weight_kg) + " kg")

 
height=input("enter your height in m: ")
weight=input("enter your weight in kg: ")
bmi=int(weight)/float(height)**2
bmi_int=int(bmi)
print(bmi_int) 

# using the f-strings

import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

answer = bmi_int
print(f"Your answer is {answer}")

age=input("Whats your current age?" )
age_int=int(age)
years_remaining=96-age_int
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
