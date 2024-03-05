# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.


# list_1 = [1, 3, 2, 6, 5]
# k = 3

# # Введите ваше решение ниже

# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1
# print(count)

from random import randint
my_list = []
list_size = int(input('Введите размер списка: '))
for _ in range(list_size):
    my_list.append(randint(0, 10))
print(my_list)

number = int(input('Введите искомое число: '))
print(my_list.count(number))