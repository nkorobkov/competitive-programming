a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))

todig = []
p = [a, b, c]
p.sort(key=lambda x:x[0])
m = p[1]
min_1 = min(a[1], b[1], c[1])
max_1 = max(a[1], b[1], c[1])

for i in range(min_1, max_1+1):
    todig.append((m[0], i))
for d in p:
    if d != m:
        for i in range(m[0], d[0]+1):
            todig.append((i, d[1]))

        for i in range(d[0], m[0]+1):
            todig.append((i, d[1]))

todig = set(todig)

print(len(todig))
for i in todig:
    print('{} {}'.format(i[0],i[1]))