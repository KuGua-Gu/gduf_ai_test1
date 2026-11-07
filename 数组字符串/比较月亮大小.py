moon = list(range(16)) + list(range(14, 0, -1))

n = int(input())
a = list(map(int, input().split()))

starts = []
for s in range(30):
    match = True
    for i in range(n):
        if moon[(s + i) % 30] != a[i]:
            match = False
            break
    if match:
        starts.append(s)

# 判断
ans = None
for s in starts:
    last = moon[(s + n - 1) % 30]
    next_day = moon[(s + n) % 30]

    if next_day > last:
        res = "UP"
    else:
        res = "DOWN"

    # 第一次赋值，后续如果和之前不一致，直接标记为无法判断
    if ans is None:
        ans = res
    elif ans != res:
        ans = -1
        break

print(ans)
