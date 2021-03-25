n = int(input())
a = list(map(int, input().split()))

res = 0
j = 1

a.sort()

for k in a:
    #print(k, j)
    if k >= j:
        res += 1
        j += 1

print(res)
