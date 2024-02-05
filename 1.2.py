# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

import math

PART = 2

class_1 = int(input('Количество учащихся в первом кабинете: '))
class_2 = int(input('Количество учащихся во втором кабинете: '))
class_3 = int(input('Количество учащихся в третьем кабинете: '))

result = math.ceil(class_1/PART) + math.ceil(class_2/PART) + math.ceil(class_3/PART)
print(f"Всего нужно парт: {result}")