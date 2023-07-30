
'''
При аналізі даних часто виникає необхідність позбавитися екстремальних значень,
перш ніж почати працювати з даними далі. Напишіть функцію prepare_data, яка видаляє з переданого списку найбільше та найменше значення, 
сортує його в порядку зростання і повертає змінений список як результат.
'''
#  data = [5, 8, -10, 0.58754, 1, 3, 3.1415, 41]
#
#
# def prepare_data(data):
#     # let's set the minimum and maximum value
#     min_number = data[0]
#     max_number = data[0]
#     # We go through the elements of the list and determine the minimum and maximum
#     for number in data:
#         if number < min_number:
#             min_number = number
#         if number > max_number:
#             max_number = number
#     # Remove the minimum and maximum value from the list
#     data.remove(min_number)
#     data.remove(max_number)
#     # We sort the rest of the list by the maximum value
#     new_data = sorted(data)
#     print(min_number)
#     print(max_number)
#     return new_data
#
#
# result = prepare_data(data)
# print(result)


'''
Ми розробляємо кулінарний блог. 
І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами, а перед останнім ставимо союз "and", як у прикладі нижче:
2 eggs, 1 liter sugar, 1 tsp salt and vinegar
Напишіть функцію format_ingredients, яка прийматиме на вхід список з інгредієнтів ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] 
та повертатиме рядок зібраний з його елементів в описаний вище спосіб. Ваша функція має вміти обробляти списки будь-якої довжини.

'''
# def format_ingredients(items):
#     if len(items) == 0:
#         return ""  # Повертаємо пустий рядок, якщо список інгредієнтів порожній
#     elif len(items) == 1:
#         return items[0]  # Повертаємо єдиний інгредієнт, якщо список містить тільки один елемент

#     # З'єднуємо всі інгредієнти, крім останнього, комами
#     formatted_string = ", ".join(items[:-1])
#     # Додаємо "and" перед останнім інгредієнтом
#     formatted_string += " and " + items[-1]

#     return formatted_string

# # Приклад використання функції
# ingredients = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
# formatted_result = format_ingredients(ingredients)
# print(formatted_result)  # Виведе: "2 eggs, 1 liter sugar, 1 tsp salt and vinegar"


'''
Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні. Реалізуйте функцію lookup_key для пошуку всіх ключів
 за значенням у словнику. Першим параметром у функцію ми передаємо словник, а другим — значення, що хочемо знайти.
Таким чином, результат може бути як список ключів,так і порожній список, якщо ми нічого не знайдемо.
'''
# def lookup_key(data, value):
#     found_keys = []
#     for key, val in data.items():
#         if val == value:
#             found_keys.append(key)
#     return found_keys


# # Приклад використання функції
# data = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}
# result = lookup_key(data, 2)
# print(result)  # Виведе: ['key2', 'key4']

'''
У нас є список показників студентів групи – це список з отриманими балами з тестування. 
Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список (цілі числа), 
знаходить середнє значення бала у списку та ділить його на два списки.
 У перший потрапляють значення менше середнього, включаючи середнє значення, тоді як у другий — строго більше від середнього.
 Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.
'''
# def split_list(grade):
#     if not grade:
#         return [],[] # Check two empty lists for an empty grade list

#     # Calculating the average value of the balls
#     average_score = sum(grade)/ len(grade)
#     print(average_score)
#     # create two lists
#     lower_average = [] # List with scores less or more than average
#     higher_average = [] # List with higher scores for the average

#     # We divide the balls into two groups: less or more for the average and more for the average
#     for score in grade:
#         if score <= average_score:
#             lower_average.append(score)
#         else:
#             higher_average.append(score)
#     return lower_average, higher_average  # Let's rotate two lists
# # An example of using the function
# our_list = [85, 90, 78, 92, 70, 88, 82, 95, 85, 75]
# result =split_list(our_list)
# print(result)

