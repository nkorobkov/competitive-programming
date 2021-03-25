import random
from  collections import Counter

n = 80


counters = []
sor_vals = []
ml = 0
for j in range(30):
    a = []
    for i in range(n-1):
        a.append(random.randint(1, 20))
    c = Counter(a)
    counters.append(c)
    ml = max(len(c.values()), ml)
    b = sorted(c.values())
    b.extend([0]*(20-len(b)))
    sor_vals.append(b)


for k in range(len(sor_vals)):
    random.shuffle(sor_vals[k])
    print(sor_vals[k])
    for i in range(12):
        sor_vals[k][i] = sor_vals[k][i] + 5
    sor_vals[k].sort()
    for i in range(1, 8):
        sor_vals[k][i] += 4

for j in range(ml):


    print(str(j).center(3), end='')


    for l in sor_vals:

        print('{:2}'.format(l[j]), end='  ')

    print()

