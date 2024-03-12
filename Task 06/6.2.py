# Дан список, состоящий из целых чисел. Напишите программу, которая в данном списке определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в списке
# Далее записаны N чисел — элементы списка. Список состоит из целых чисел.

from random import randint as rnum

num_1 = int(input('Введите количество чисел в первом списке: '))
numbers = [rnum(1, 20) for _ in range(num_1)]
print(numbers)

count = 0
for i in range(1, len(numbers) - 1):
    if numbers[i - 1] < numbers[i] > numbers[i + 1]:
        count += 1
print(count)


def counter(list_n):
    cint = 0
    for i in range(1, len(list_n) - 1):
        if list_n[i - 1] < list_n[i] > list_n[i + 1]:
            cint += 1
    return cint
print(counter(numbers))