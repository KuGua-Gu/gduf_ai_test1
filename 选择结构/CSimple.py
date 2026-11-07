X, Y = map(int, input().split())
if Y % X == 0:
    print(X + Y)
else:
    print(Y - X)