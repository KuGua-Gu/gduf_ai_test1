mid = {
    (1, 3): 2, (3, 1): 2,
    (4, 6): 5, (6, 4): 5,
    (7, 9): 8, (9, 7): 8,
    (1, 7): 4, (7, 1): 4,
    (2, 8): 5, (8, 2): 5,
    (3, 9): 6, (9, 3): 6,
    (1, 9): 5, (9, 1): 5,
    (3, 7): 5, (7, 3): 5
}

while True:
    try:
        s = input().strip()
        nums = []
        for c in s:
            nums.append(int(c))

        # 重复数字×
        if len(nums) != len(set(nums)):
            print("NO")
            continue

        used = set()
        used.add(nums[0])
        valid = True

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            curr = nums[i]

            if (prev, curr) in mid:
                # 有中间点，检查中间点是否已经被使用
                if mid[(prev, curr)] not in used:
                    valid = False
                    break

            used.add(curr)

        if valid:
            print("YES")
        else:
            print("NO")

    except EOFError:
        break
