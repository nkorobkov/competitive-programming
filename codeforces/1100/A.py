
n, k = tuple(map(int, input().split()))
a = list(map(int, input().split()))

kk = sum(a)
difs = []

for ic in range(k):
    c = ic
    dif = 0
    while c < n:

        dif += a[c]
        c += k
    difs.append(abs(kk - dif))

print(max(difs))


