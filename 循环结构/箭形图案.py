def jianxing(n):
    # 上升段：空格越来越少，星号越来越多
    for i in range(n + 1):
        print(' ' * (n - i) +' '*(n + 1 - i)+ '*' * (i + 1))
    # 下降段：空格越来越多，星号越来越少
    for i in range(n - 1, -1, -1):
        print(' ' * (n - i) +' '*(n + 1 - i)+ '*' * (i + 1))

# 多组输入读到末尾结束
while True:
    try:
        n = int(input())
        jianxing(n)
    except EOFError:
        break