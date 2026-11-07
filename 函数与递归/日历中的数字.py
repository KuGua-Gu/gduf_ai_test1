while True:
    try:
        y, m, x = map(int, input().split())
        # 平年每个月的天数，索引0对应1月，索引1对应2月，以此类推
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # 判断闰年
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            month_days[1] = 29  # 闰年2月有29天

        total = 0
        target = str(x)
        days = month_days[m - 1]  # 当月总天数

        # 遍历当月每一天
        for d in range(1, days + 1):
            # 不足2位前面补0
            date_str = f"{y:04d}{m:02d}{d:02d}"
            total += date_str.count(target)

        print(total)
    except EOFError:
        break
