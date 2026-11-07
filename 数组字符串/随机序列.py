'''import numpy as np

T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    arr = np.array(nums)

    range_val = int(arr.max() - arr.min())

    var = np.var(arr)
    print(f"{range_val} {var:.3f}")'''


T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    # 计算极差：最大值 - 最小值
    range_val = max(nums) - min(nums)
    # 计算平均值
    avg = sum(nums) / n
    # 计算总体方差：每个数与均值差的平方和 除以 n
    variance = sum((x - avg) ** 2 for x in nums) / n
    # 输出：极差为整数，方差保留3位小数
    print(f"{range_val} {variance:.3f}")

