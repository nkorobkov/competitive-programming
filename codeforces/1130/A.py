n =int (input())

a = list(map(int, input().split()))

neg = 0
max_n = 0
for e in a:
    if e<=0:
        neg +=1
    if e == -10**3:
        max_n+=1


if neg>(len(a)//2):
    print(0)
else:
    if abs(min(a)) == 10**3:
        if max_n > (len(a) // 2):
            print(0)
        else:
            print(abs(min(a)))
    else:
        print(abs(min(a))+1)