# Найдите сумму цифр трехзначного числа. 

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


n = 123
res = 0
while n > 0:
    m = n % 10
    res = res + m
    n = n // 10
    
print(res)