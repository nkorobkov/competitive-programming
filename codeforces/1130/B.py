n = int(input())

a = list(map(int, input().split()))

i, j = 0, 0
dist = 0

pos = [0]*(n*2)
for ii in range(len(a)):
    k =  pos[a[ii]]
    if k == 0:
        pos[a[ii]] = [ii, 0]
    else:

        pos[a[ii]][1] = ii

for t in range(1, n+1):

    t1 = pos[t][0]
    t2 = pos[t][1]

    i1 = abs(i-t1) + abs(j-t2)
    i2 = abs(i-t2) + abs(j-t1)
    if i1<i2:
        dist += i1
        i = t1
        j = t2
    else:
        dist += i2
        i = t2
        j = t1

print(dist)
