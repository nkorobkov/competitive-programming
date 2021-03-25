n = int(input())
a = list(map(int, input().split()))

c = max(a)
ml = 0
k, z = 0, 0
u = []
for i in range(len(a)):
    if a[i] == c:
        ml+=1

    if (ml >0 and a[i] != c) or i == len(a)-1:
        u.append(ml)
        ml = 0


t = max(u)
print(t)