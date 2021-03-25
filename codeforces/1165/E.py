n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


bc = []
i, j = 1, len(a)

for k in range(len(a)):
    bc.append(i*j)
    i+=1
    j-=1
c = []

for aa, bb in zip(a, bc):
    c.append(aa*bb)





c.sort()
b.sort(reverse=True)
d = []
for aa, bb in zip(c, b):
    d.append(aa*bb)
print(sum(d) % 998244353)