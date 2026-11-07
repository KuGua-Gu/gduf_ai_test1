L, M = map(int, input().split())
tree = [True] * (L + 1)

for _ in range(M):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        tree[i] = False

# True相当于1，False相当于0，sum直接统计剩余树的数量
print(sum(tree))
