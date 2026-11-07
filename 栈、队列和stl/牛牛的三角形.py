n = int(input())
nums = list(map(int, input().split()))
nums.sort()

found = False
for i in range(n - 1, 1, -1):
    a = nums[i - 2]
    b = nums[i - 1]
    c = nums[i]
    if a + b > c:
        print(a, b, c)
        found = True
        break

if not found:
    print("No solution")