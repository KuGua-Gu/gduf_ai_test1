L, R = map(int, input().split())
cnt = 0

# 遍历区间 [L, R] 的每一个数字
for num in range(L, R + 1):
    x = num
    # 逐个取出当前数字的每一位
    while x > 0:
        d = x % 10   # 取出个位数字
        if d == 2:
            cnt = cnt + 1
        x = x // 10  # 去掉已经检查过的个位
print(cnt)

