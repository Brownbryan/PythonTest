height=float(input("enter your height in m: "))
weight=float(input("enter your weight in kg: "))
# round of to the whole number
bmi=round(weight/height**2)
print(type(bmi))
if bmi<18.5:
    print(f"You have a BMI of {bmi}, you are underweight")
elif bmi<25:
    print(f" You have a BMI of {bmi}, you have a normal weight")
elif bmi<30:
    print(f"You have a BMI of {bmi}, you are overweight")
elif bmi<35:
    print(f"You have a BMI of {bmi}, you are obese")
else:
    print(f"You have a BMI of {bmi}, you are clinically obese")