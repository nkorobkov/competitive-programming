n, m, ta, tb, k = list(map(int, input().split()))

a = list(map(lambda x: int(x) + ta, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

i = 0

bless = []
for bb in b:

    while i < len(a) and bb >= a[i]:
        i += 1

    bless.append(i)

#print(bless)
ans = -1
for j in range(len(b)):

    # fly  on ith
    canc = bless[j]
    lefc = k - canc
    if lefc < 0:
        break
    if j + lefc + 1 >= len(b):
        ans = -1
        break

    # print(b[j+lefc])
    ans = max(ans, b[j + lefc + 1])

if ans == -1:
    print(ans)
else:
    print(ans + tb)
