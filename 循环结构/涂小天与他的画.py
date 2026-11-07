def lingxing(a):
    mid = a // 2
    # 上半部分（包含中间最长行）
    for i in range(1, mid + 2):
        print(' ' * (mid - i + 1) + '*' * (2 * i - 1))
    # 下半部分
    for i in range(mid, 0, -1):
        print(' ' * (mid - i + 1) + '*' * (2 * i - 1))


T = int(input())
for _ in range(T):
    n = int(input())
    lingxing(n)
