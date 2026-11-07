def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

x, y = map(int, input().split())
# 避免输入的左数比右数大
left = min(x, y)
right = max(x, y)
count = 0

for num in range(left, right + 1):
    if digit_sum(num) % 5 == 0:
        count += 1

print(count)
