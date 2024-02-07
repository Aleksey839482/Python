# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

num = int(input('Введите число: '))

first_num = 0                           # first_num, second_num = 0, 1  - вмест 2 строк кода
second_num = 1
index = 1

while second_num < num:
    sum = first_num + second_num
    first_num = second_num                  # first_num, second_num = second_num, first_num + second_num
    second_num = sum                        # В питоне можно не ввдить третью переменную sum 
    index += 1                              # сначала вычисляет значение в правой части, а потом присваивает в левую

if second_num == num:
    result = index                          # Можно сделать единый оператор:
else:                                       # result = index if second_num == num else -1
    result = -1
    
print(result)