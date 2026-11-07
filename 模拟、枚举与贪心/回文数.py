counts = list(map(int, input().split()))
total = sum(counts)

odd_count = 0
mid_digit = -1

for i in range(10):
    if counts[i] % 2 != 0:
        odd_count += 1
        mid_digit = i

# 奇数次超过1
if odd_count > 1:
    print(-1)
    exit()

if total == 1:
    print(mid_digit)
    exit()

# 对数
pair = [x // 2 for x in counts]

first = -1
for i in range(1, 10):
    if pair[i] > 0:
        first = i
        break

if first == -1:
    print(-1)
    exit()

left = []
left.append(str(first))
pair[first] -= 1

for i in range(10):
    if pair[i] > 0:
        left.append(str(i) * pair[i])

left_str = ''.join(left)

mid_str = str(mid_digit) if odd_count == 1 else ''

result = left_str + mid_str + left_str[::-1]

print(result)
