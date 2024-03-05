# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# n = 700
# m = 750

import math

per_day = int(input('Машина презжает за 1 день: '))
total = int(input('Машине неоходимо проехать: '))

result = -((-total)//per_day)
print(result)
result = math.ceil(total/per_day)
print(result)
result = (total + per_day -1)//per_day
print(result)