N = int(input())
from  collections import deque

a1, a2 = list(map(int, input().split()))
b1, b2 = list(map(int, input().split()))
a1, a2, b1, b2 = a1-1, a2-1, b1-1, b2 -1


map = []
for i in range(N):
    p = list(input())
    map.append(p)


comp1 = [(a1, a2)]
comp2 = [(b1, b2)]

def neib(x, y):
    ns = []
    if x+1 < N:

        ns.append((x+1, y))
    if x != 0:
        ns.append((x-1, y))

    if y+ 1 < N:
        ns.append((x , y+ 1))
    if y != 0:
        ns.append((x , y- 1))
    return ns
c1 = deque(comp1)
c1seen = []
c1e = []

while c1:
    gn = 0
    g = c1.pop()
    nb = neib(g[0], g[1])
    for n in nb:
        if n not in c1seen:
            if map[n[0]][n[1]] != '1':
                c1.append(n)
                gn+=1
    c1seen.append(g)
    if gn<4:
        c1e.append(g)

c2 = deque(comp2)
c2seen = []
c2e = []
while c2:
    g = c2.pop()
    nb = neib(g[0], g[1])
    gn = 0
    for n in nb:
        if n not in c2seen:
            if map[n[0]][n[1]] != '1':
                gn+=1
                c2.append(n)
    c2seen.append(g)
    if gn<4:
        c2e.append(g)


#print(c1e, c2e)
distt = 10**5

def dist(a, b):
    return (a[0]-b[0])**2 + (b[1]-a[1])**2

for a in c2e:
    for b in c1e:
        distt = min(distt, dist(a, b))

print(distt)