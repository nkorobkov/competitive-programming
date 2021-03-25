n, m = list(map(int, input().split()))

stations = [0]*n
for i in range(n):
    stations[i] = list()
for i in range(m):

    s, d = list(map(int, input().split()))
    s, d = s-1, d-1


    stations[s].append(d)

#print(stations)
max_s = 0
for s in stations:
    max_s = max(max_s, len(s))

loaded_s = []
for i in range(len(stations)):
    if len(stations[i]) == max_s:
        loaded_s.append(i)

sloaded_s = []
for i in range(len(stations)):
    if len(stations[i]) == max_s-1:
        sloaded_s.append(i)

def distance(s, d):
    if d>=s:
        return d-s
    else:
        return d+n - s


finald = []
for si in loaded_s:
    mind = n+n
    for d in stations[si]:
        dist = distance(si, d)
        mind = min(dist, mind)
    finald.append((si, mind))

subfd = []

for si in sloaded_s:
    mind = n+n
    for d in stations[si]:
        dist = distance(si, d)
        mind = min(dist, mind)
    subfd.append((si, mind))


minr = []
for i in range(n):
    rmax = 0
    for d in finald:
        r = distance(i, d[0])+d[1]
        rmax = max(rmax, r)
    for d in subfd:

        r = (d[1] - distance(d[0], i)) if i != d[0] else 0
        print(d[0], i, r)
        rmax = max(rmax, r)

    minr.append(rmax + (max_s-1)*n)

print(' '.join(list(map(str, minr))))



