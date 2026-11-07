import itertools

for perm in itertools.permutations(range(1, 9)):  #全排列函数
    print(' '.join(map(str, perm)))
