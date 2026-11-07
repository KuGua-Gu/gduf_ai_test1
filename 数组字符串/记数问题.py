n, x = map(int, input().split())
target = str(x)
count = 0

for num in range(1, n + 1):
    count += str(num).count(target)

print(count)
