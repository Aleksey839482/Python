# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

length = int(input('Введите число: '))
def sequence(num):
    if not num:
        return ''
    ch = input('Введите символ: ')
    return sequence(num - 1) + ch

print(sequence(4))
    