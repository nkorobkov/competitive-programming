a = input().split()

n, m, k = list(map(int, a))

a = list(map(int, input().split()))
h = []
for i in range(len(a)-1):
    h.append(a[i+1] - a[i])

h.sort()
#print(h)
ans = -100

if n <= (k):
    ans = n
else:
    ans = n + sum(h[:(n-k)]) - (n-k)

print(ans)