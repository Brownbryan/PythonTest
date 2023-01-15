two_digit_number=input("")

# Check the data type of two_digit_number
# print(type(two_digit_number))
#converting first and second digits from str to int
first_digit=int(two_digit_number[0])
second_digit=int(two_digit_number[1])
#add the two digits number
two_digit_number=first_digit+second_digit
print(two_digit_number)