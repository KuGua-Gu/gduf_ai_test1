n, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total = sum(B)
diff = []
for i in range(n):
    diff.append(A[i] - B[i])

diff.sort(reverse=True)

for i in range(K):
    total = total + diff[i]

print(total)