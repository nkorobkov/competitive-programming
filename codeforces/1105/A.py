
n = int(input())


a = list(map(int, input().split()))

m = sum(a)/n
dists = {}
for pm in range(min(a), max(a)+1):
    c = 0
    for i in a:
        dist = abs(i-pm)
        if dist > 1:
            c += dist-1

    dists[c] = pm


mk = min(dists.keys())
print(dists[mk], mk)