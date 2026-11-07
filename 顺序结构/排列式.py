result = []

for a in range(1,100):
    max_b = 9999 // a;
    for b in range(a,max_b+1):
        count = a * b;
        all = str(a) + str(b) + str(count);
        if len(all)!= 9 or '0' in  all:
            continue
        if len(set(all))== 9:
            result.append((count,a,b))

result.sort()

for count,a,b in result:
    print("{count} = {a} x {b}".format(count=count,a=a,b=b))








