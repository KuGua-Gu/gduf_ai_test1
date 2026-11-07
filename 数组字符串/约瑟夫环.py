n, k, m = map(int, input().split())
people = list(range(n))

start = k

while len(people) > 1:
    idx = (start + m - 1) % len(people) # 取模，圆圈，满一圈回到第0个人
    people.pop(idx)

    start = idx

print(people[0])
