n = int(input())
anss= []
for i in range(n):
    ans = 0

    q, a, b= list(map(int, input().split()))

    if a*2 <= b:
        ans = a*q
    else:
        ans = (q//2) * b
        if q % 2 == 1:
            ans += a

    anss.append(ans)

for a in anss:
    print(a)