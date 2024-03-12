# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.

def sum_deviders(num):
    dev = [1, ]
    for i in range(2, num//2 + 1):
        if not num % i:
            dev.append(i)
    return sum(dev)


for i in range(1, 10000):
    j = sum_deviders(i)
    if i == sum_deviders(j) and i < j:
        print(i, j)
            
            
# def sum_del(num):
#     count = 1 # Суммма делителей, начинаем считать со 2 -го
#     for i in range(2, int(num ** 0.5) + 1): #для числа 100: 1 2 4 5 10 20 25 50
#         if num % i == 0:
#             count += i
#             if i != num // i:
#                 count += num // i
#     return (count)

# for n in range(1, 100_000):
#     m = sum_del(n)
#     if n < m and (n == sum_del(m)):
#         print(n, m)