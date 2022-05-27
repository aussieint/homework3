str_numbers = input('Введите элементы первого списка: ')
first_numbers = str_numbers.split(',')
first_numbers = [int(x) for x in first_numbers]
str_numbers = input('Введите элементы второго списка: ')
second_numbers = str_numbers.split(',')
second_numbers = [int(x) for x in second_numbers]
first_numbers_copy = first_numbers.copy()
for number in first_numbers_copy:
    if number in second_numbers:
        first_numbers.remove(number)
print(first_numbers)
