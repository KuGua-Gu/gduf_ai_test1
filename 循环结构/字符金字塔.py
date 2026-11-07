c = input().strip()
n = ord(c) - ord('A') + 1

for i in range(1, n + 1):
    #回文字母串
    asc = ''.join(chr(ord('A') + j) for j in range(i))
    chars = asc + asc[:-1][::-1]
    line = ' ' * (n - i) + chars
    print(line)

