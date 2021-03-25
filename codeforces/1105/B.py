from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = tuple(map(int, input().split()))
s = input()

pl = s[0]
c = 1
d = defaultdict(int)

for l in s[1:]:
    if l == pl:
        c += 1
    if l!= pl:
        c = 1
        pl = l
    if c == k:
        d[l] += 1
        c = 0

#print(d)
if d.values():
    print(max(d.values()))
else:
    if len(s) == 1:
        if k == 1:
            print(1)
        else:
            print(0)
    else:
        print(0)

