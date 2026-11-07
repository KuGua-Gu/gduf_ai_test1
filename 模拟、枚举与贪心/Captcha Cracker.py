word_to_num = {
    'zero': '0',
    'two': '2',
    'four': '4',
    'six': '6',
    'nine': '9'
}
word_list = list(word_to_num.keys())

T = int(input())
for _ in range(T):
    s = input().strip()
    result = []
    i = 0
    n = len(s)

    while i < n:
        # 数字
        if s[i].isdigit():
            if s[i] in {'0', '2', '4', '6', '9'}:
                result.append(s[i])
            i += 1
        else:
            # 单词
            found = False
            for word in word_list:
                w_len = len(word)
                if i + w_len <= n and s[i:i + w_len] == word:
                    result.append(word_to_num[word])
                    i += w_len
                    found = True
                    break

            if not found:
                i += 1

    print(''.join(result))
