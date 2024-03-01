# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint as rnum              # импорт функции randint и назвать ее в переменную rnum для простоты

list_size = int(input('Введите размер списка: '))
my_list = []
for _ in range(list_size):                  # _ перечисление элементов если мы их не используем
    my_list.append(rnum(-10, 10))
print(my_list)

count = 0

for i in range(list_size - 1):           # или range(1, list_size)                              # потому что перебирает индексы и последний будет больше самого списка
    if my_list[i] < my_list[i + 1]:      # if my_list[i] > my_list[i - 1]
        count += 1
print(count)
