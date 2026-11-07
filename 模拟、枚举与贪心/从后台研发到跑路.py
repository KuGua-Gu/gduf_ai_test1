import sys


def main():
    s = sys.stdin.read()
    res = []
    n = len(s)
    i = 0

    in_string = False
    in_comment = False
    comment_buf = []

    while i < n:
        if in_comment:
            # 只寻找结束符 */
            if i + 1 < n and s[i] == '*' and s[i + 1] == '/':
                in_comment = False
                comment_buf.clear()
                i += 2
            else:
                comment_buf.append(s[i])
                i += 1
        elif in_string:
            #  \" 为转义
            if s[i] == '\\' and i + 1 < n and s[i + 1] == '"':
                res.append(s[i])
                res.append(s[i + 1])
                i += 2
            elif s[i] == '"':
                res.append(s[i])
                in_string = False
                i += 1
            else:
                res.append(s[i])
                i += 1
        else:
            if i + 1 < n and s[i] == '/' and s[i + 1] == '*':
                in_comment = True
                comment_buf.append('/')
                comment_buf.append('*')
                i += 2
            elif s[i] == '\\' and i + 1 < n and s[i + 1] == '"':
                res.append(s[i])
                res.append(s[i + 1])
                i += 2
            elif s[i] == '"':
                res.append(s[i])
                in_string = True
                i += 1
            else:
                res.append(s[i])
                i += 1

    if comment_buf:
        res.extend(comment_buf)

    print(''.join(res), end='')


if __name__ == "__main__":
    main()
