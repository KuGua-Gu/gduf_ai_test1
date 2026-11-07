def double_pyramid(a):
    for i in range(1,a+1):
        print(' ' * (a - i) + '*' * (2*i - 1))
    for i in range(a-1,0,-1):
        print(' ' * (a - i) + '*' * (2*i - 1))

while True:
    try:
        n = int(input())
        double_pyramid(n)
    except EOFError:
        break