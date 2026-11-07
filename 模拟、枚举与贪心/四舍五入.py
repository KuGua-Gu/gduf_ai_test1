n, t = map(int, input().split())
num = list(input().strip())

if '.' not in num:
    print(''.join(num))
    exit()

dot_idx = num.index('.')

# 只要还有次数，就继续尝试进位
while t > 0:
    # 标记：有没有找到可以进位的位置
    found = False
    for i in range(dot_idx + 1, len(num)):
        if int(num[i]) >= 5:
            for k in range(i, len(num)):
                num[k] = '0'

            # 第二步：从i-1开始往前处理进位
            carry = 1
            j = i - 1
            while carry and j >= 0:
                # 遇到小数点就跳过，继续往左
                if num[j] == '.':
                    j -= 1
                    continue

                # 当前位数字 + 进位
                new_digit = int(num[j]) + carry
                if new_digit >= 10:
                    # 满10了，保留个位，继续进位
                    num[j] = str(new_digit % 10)
                    carry = 1
                else:
                    # 没满10，进位结束
                    num[j] = str(new_digit)
                    carry = 0
                j -= 1

            # 如果进位还没结束，说明整数部分最前面还要补1
            if carry:
                num.insert(0, '1')
                dot_idx += 1  # 小数点位置后移

            found = True
            break

    # 没找到可以进位的位置，提前结束
    if not found:
        break
    # 用掉一次机会
    t -= 1

# 去掉小数末尾多余的0
while num[-1] == '0':
    num.pop()
if num[-1] == '.':
    num.pop()

print(''.join(num))
