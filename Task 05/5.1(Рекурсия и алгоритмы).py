# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., 
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fib(n):
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

# n = int(input('Введите число феббоначи: '))
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i - 2))

print(fib(5))
