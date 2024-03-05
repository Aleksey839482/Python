# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# Пример

# На входе:
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# На выходе:
# 3 5

from random import randint as rnum

# m = int(input('Введите колочество элементов первого множества чисел: '))
# n = int(input('Введите колочество элементов второго множетсва через: '))

# m, n = map(int, input('Введите количество элементов первого и второго множества через пробел: ').split())


# var1 = [m, n]
# print(var1)
# var2 = []
# var3 = []

var1 = '5 4'
var2 = '14 30 5 7 9'
var3 = '2 30 14 5'

# # var4 = var2 & var3
# print(var2 & var3)

# for _ in range(var1[0]):
#     var2.append(rnum(0, 10))
# for _ in range(var1[1]):
#     var3.append(rnum(0, 10))

# print(var2, var3)
var2 = [i for i in var2.split()]    # Конвертирует в список используя пробел чтобы разделить элементы
var3 = [i for i in var3.split()]

var4 = []
for i in var2:
    if i in var3:
        var4.append(i)
        
# var4 = [i for i in var4 if i.strip()]   # Удаляет лишние пробелы сейчас не нужна
var4 = " ".join(str(element) for element in var4)   # Конвертирует список в строку с выбором разделителя в " " - разделитель пробел.

print(var4)




# Пример с автотестов:
# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')