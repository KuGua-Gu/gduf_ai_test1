s = input().strip()
count = 0

for c in s:
    if c == 'a':
        count += 1
    elif c == 'b':
        count -= 1

        if count < 0:
            print('Bad')
            exit()

    else:
        print('Bad')
        exit()

if count == 0:
    print('Good')
else:
    print('Bad')