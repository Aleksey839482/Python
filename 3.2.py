# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [3, 4, 5, 1, 2]

# number_1 = [1, 2, 3, 4, 5]
# count = int(input('Введите число сдвига: '))

# number_2 = number_1[-count:] + number_1[:-count]
# print(number_1)
# print(number_2)

# for _ in range(count):
#     number_1.insert(0, number_1.pop())
# print(number_1)

print(my_list := [1, 2, 3, 4, 5])                       # моржовый оператор
shift = int(input('Введите количество шагов: '))
print(result := my_list[-shift:] + my_list[:-shift])