elem_numbers = int(input('Введите количество элементов списка: '))
new_list = []
for i in range(elem_numbers):
    new_list.append(int(input(f'Введите {i+1} элемент: ')))
new_list.sort()
print(new_list)
