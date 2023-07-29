# If умова
# Перевірити чи a менше за b
# a = 7
# b = 5

# if a < b:
#     print(f"{a} is less than {b}")
# print("end of code")


# Перевірити чи a менше за b i c
# a = 2
# b = 5
# c = 4

# if a < b and a < c:
#     print(f"{a} is less than {b} and {c}")

# Перевірити a на рівність нулю
# a = 0
# if a:
#     print(f'{a} is not zero')

# print("End of code")

# a = -2
# if a < 0 or a > 0:
#     print(f'{a} is not zero')

# print("End of code")

# Перевірити а на рівність нулю
# a = 0
# if a != 0:
#     print(f"{a} is not zero")
# if a == 0:
#     print(f"{a} is zero")
# print("End of code")

# Перевірка а по декількох умовах
# a = int(input("Enter value a: "))

# if not a % 2 and not a % 3:
#     print("a not divides by 2 and 3")
# if not a % 4 and  a % 5:
#     print("a not divides by 4 and  divides by 5")
# if a < 0 or a > 3:
#     print("а not belong to range from 0 to 3")
# if a >= -2 and a <= 0:
#     print("а belong to range from -2 to 0")   

# Перевірити а на рівність нулю
# a = 0
# if a:
#     print(f"{a} is not zero")
# else:
#     print(f"{a} is zero")

# Перевірити чи a менше за b
# a =6
# b =4
# if a < b:
#   print(f'{a} is less than {b}')
# else:
#   print(f'{a} is not less than {b}')

# def say_hello():
#     print('Привіт, Світ!')   # блок, що належить функції
#     # Кінець функції say_hello()


# say_hello()

x = 50

def func():
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2

func()
print('x як і раніше', x)   # x як і раніше 50

