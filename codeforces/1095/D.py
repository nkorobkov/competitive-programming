n = int(input())
d = {}
for i in range(n):
    d[i+1] = tuple(map(int, input().split()))


p = [1]
to_resolve = 1

for i in range(n-1):
    candidates = d[to_resolve]
    if candidates[1] in d[candidates[0]]:
        to_resolve = candidates[0]
    else:
        to_resolve = candidates[1]
    p.append(to_resolve)

if n == 3:
    print('1 2 3')
else:
    print(' '.join(map(str, p)))
