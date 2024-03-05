# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

from random import randint
my_list = []
list_size = int(input('Введите размер списка: '))
for _ in range(list_size):
    my_list.append(randint(0, 100))
print(my_list)

number = int(input('Введите искомое число: '))
min_distance = abs(my_list[0] - number)
nearest_item = my_list[0]
for i in range(1, len(my_list)):
    if abs(my_list[i] - number) < min_distance:
        min_distance = abs(my_list[i] - number)
        nearest_item = my_list[i]
print(nearest_item)