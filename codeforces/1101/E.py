import sys
input = sys.stdin.readline

n = int(input())

mmax = 0
mmin = 0

ans = []
for i in range(n):
    s = input().split()
    a, b = int(s[1]), int(s[2])
    if a > b:
        mx = a
        mn = b
    else:
        mn = a
        mx = b

    if s[0] == '+':
        if mx > mmax:
            mmax = mx
        if mn > mmin:
            mmin = mn
    else:
        if mx >= mmax and mn >= mmin:
            ans.append('YES')
        else:
            ans.append('NO')

print('\n'.join(ans))


