# value_a = float(input("Enter value a: "))
# value_b = float(input("Enter value b: "))
# value_x = -value_b/value_a
# print(f"result x equal:{value_x}")

# # sqrt(a^2+b^2) and (a*b)/2
# kat_a, kat_b = float(input("Enter value a: ")), float(input("Enter value b: "))
# area = (kat_a + kat_b)/2
# hypotenuse = (kat_a**2 + kat_b**2)**0.5
# print(f"our figure has:\n a hypotenuse {hypotenuse}\n an area {area}")

# side = float(input("Enter the side of the square: "))
# perimeter =side*4
# print(f"The perimeter of the square is {perimeter} ")
# second way
# side = float(input("Enter the side of the square: "))
# print(f"The perimeter of the square is {side*4} ")

# circle length 2*PI*R  circle area(PI*R**2)/2

# radius = float(input("circle radius= "))
# PI = 3.14
# length = round(2*PI*radius,1)
# area = (PI*radius**2)/2
# print (f"circle has\n length {length}\n area {area}")

# example_5
# first_number = float(input("first number = "))
# second_number = float(input("second number = "))
# third_number = float(input("third number = "))
# sum = first_number + second_number + third_number
# print (f"the sum of three real numbers is equal {sum}")

# example_6
# 2x4-3x3+4X2-5x+6
# number = float(input("let's set the value of the variable= "))
# formula = (2*number*4)-(3*number*3) + (4*number*2) - 5*number + 6
# print("the result of the formula = ",formula)

# ehample_7 sqrt((x2-x1)**2 + (y2-y1)**2)
# variable_1 = float(input("enter variable (1): "))
# variable_2 = float(input("enter variable (2): "))
# variable_3 = float(input("enter variable (3): "))
# variable_4 = float(input("enter variable (4): "))
# formula = round(((variable_2 - variable_1)**2 + (variable_4 - variable_3)**2)**0.5,2)
# print("result = ",formula)

# example_8 to display the arithmetic mean of a four-digit number
# numbers1 =float(input("enter a four digit number = "))
# numbers2 =float(input("enter a four digit number = "))
# numbers3 =float(input("enter a four digit number = "))
# numbers4 =float(input("enter a four digit number = "))
# numbers_sum =numbers1 + numbers2 + numbers3 +numbers4
# formula = numbers_sum/4
# print("the arithmetic mean of a four-digit number = ",formula)

# example_9 : Write a program that enters a three-digit number from the keyboard and displays it on the screen
                                                        # *the sum of the last and penultimate digits
                                                        # *the sum of the last and first digits.

# three_number1 =float(input("Enters a first-digit number = "))
# three_number2 =float(input("Enters a second-digit number = "))
# three_number3 =float(input("Enters a three-digit number = "))
# three_number = str(int(three_number1)) + str(int(three_number2)) + str(int(three_number3))
# three_sum_1 = three_number2 + three_number3
# three_sum_2 = three_number1 + three_number3
# print(f"it is our three-digit number  {three_number}\n the sum of the last and penultimate digits  {three_sum_1 }\n the sum of the last and first digits  {three_sum_2}")

# example_10 In a three-digit number, swap the first and second digits

# three_number1 =float(input("Enters a first-digit number = "))
# three_number2 =float(input("Enters a second-digit number = "))
# three_number3 =float(input("Enters a three-digit number = "))
# three_digit = str(int(three_number1)) + str(int(three_number2)) + str(int(three_number3))
# invers_three_digit = str(int(three_number2)) + str(int(three_number1)) + str(int(three_number3))
# print(f"three-digit number = {three_digit}")
# print("invers_three-digit number =",invers_three_digit)

# sample2
# three_number =int(input("Enters three-digit number = "))
# # (493//100 =  integer divide 4  )
# first_digit_number = three_number // 100
# # remainder  (493//10 =  49 % 10  =4.3we take only 9 )
# second_digit_number = (three_number// 10) % 10
# # remainder after decimal point (493%10 =  49.3 we take only 3 )
# third_digit_number = three_number%10   
# result = str(second_digit_number) +str(first_digit_number) + str(third_digit_number) 
# print("invers_three-digit number =",result )

# # sample3
# numbers = int(input("Enters three-digit number = "))
# # (493 = 4.93 integer divide 4  )
# number1 = numbers//100
# # remainder  (493 -  4*100)//10 = 93//10 =9.3 we take only 9 )
# number2 = (numbers -number1*100)//10
# # 493%10 = 49.3 integer divide 3  )
# number3 =numbers%10
# print(f"three-digit number = {number1}{number2}{number3}")
# sum = str(number2)+str(number1)+str(number3)
# print("invers_three-digit number = ",sum)

# example_11
# number_of_records = int(input("enter the number of records = "))
# RECORD_FOR_PAGE = 10
# pages = (number_of_records -1)//RECORD_FOR_PAGE +1
# print((pages))

# sample2
num = int(input())
# input 12 12//10 = 1
num_1 = num // 10
# he result of the expression num_2 will be 1 (True) if the last digit of num is greater than 0, or 0 (False) if it is false.
# 12%10 =0.2 >0  = True <==> num_2 =1
num_2 = int(num % 10 > 0)
sum = num_1 + num_2
print(sum)

# example_12
# Input - 5000
# Otput_hours - 1
# Otput_minutes - 23
# Otput_seconds - 20

# seconds_sum = int(input("Enter the total number of seconds: "))
# hours = seconds_sum // 3600
# seconds_sum = seconds_sum - hours * 3600
# minutes = seconds_sum // 60
# seconds_sum = seconds_sum - minutes * 60
# seconds_remaining = seconds_sum
# print(f"Number of hours = {hours}, number of minutes = {minutes}, number of seconds = {seconds_remaining}")

# sample2
seconds_sum= int(input('Ener your number: '))
hours = seconds_sum // 3600
seconds_sum -= hours * 3600
minut = seconds_sum// 60
seconds_sum -= minut * 60
seconds_remaining = num
print(f'Otput_hours - {hours}\nOtput_minutes - {minut}\nOtput_seconds - {seconds_remaining}')