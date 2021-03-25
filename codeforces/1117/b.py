n,m ,k = list(map(int, input().split()))
a = list(map(int, input().split()))


a.sort()
best = a[-1]
second = a[-2]

times_s = m//(k+1)

times_best = m - times_s

ans = times_best*best + times_s*second

print(ans)