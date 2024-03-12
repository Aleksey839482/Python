# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

from random import randint as rnum

num_1 = int(input('Введите количество чисел в списке: '))
numbers = [rnum(1, 5) for _ in range(num_1)]
print(numbers)


# spisok = set(numbers)
# count = 0
# for item in spisok:
#     count += numbers.count(item) // 2
count = sum([numbers.count(item)//2 for item in set(numbers)])
print(count)