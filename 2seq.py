str_numbers = input('Введите элементы списка: ')
numbers = str_numbers.split(',')
numbers = [int(x) for x in numbers]
result = []
for number in numbers:
    if numbers.count(number) == 1:
        result.append(number)
print(result)
