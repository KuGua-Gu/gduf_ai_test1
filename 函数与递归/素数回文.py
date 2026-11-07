import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

t = int(input())
pal = t
temp = t // 10

while temp > 0:
    digit = temp % 10
    pal = pal * 10 + digit
    temp = temp // 10

# 判断回文数是否为素数
if is_prime(pal):
    print("prime")
else:
    print("noprime")
