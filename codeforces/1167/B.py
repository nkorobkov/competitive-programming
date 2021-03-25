def check(a, b):
    print("?", a, b)
    return int(input())


pos_vals = {
    32: (8, 4),
    60: (4, 15),
    64: (4, 16),
    92: (4, 23),
    168: (4, 42),

    120: (8, 15),
    128: (8, 16),
    184: (8, 23),
    336: (8, 42),
    240: (15, 16),
    345: (15, 23),
    630: (15, 42),
    368: (16, 23),
    672: (16, 42),
    966: (23, 42),
}

a = []
for i in range(7):
    a.append(set())

c12 = check(1, 2)

a[1].add(pos_vals[c12][0])
a[1].add(pos_vals[c12][1])

a[2].add(pos_vals[c12][0])
a[2].add(pos_vals[c12][1])

c23 = check(2, 3)

if pos_vals[c23][0] in a[1]:
    a[1].remove(pos_vals[c23][0])
if pos_vals[c23][1] in a[1]:
    a[1].remove(pos_vals[c23][1])
a1 = a[1].pop()
a[2].remove(a1)
a2 = a[2].pop()

a[3].add(pos_vals[c23][0])
a[3].add(pos_vals[c23][1])
a[3].remove(a2)
a3 =  a[3].pop()


c34 = check(4, 3)


a[4].add(pos_vals[c34][0])
a[4].add(pos_vals[c34][1])
a[4].remove(a3)
a4 = a[4].pop()
c45 = check(4, 5)

a[5].add(pos_vals[c45][0])
a[5].add(pos_vals[c45][1])
a[5].remove(a4)
a5= a[5].pop()

all_vals = {4, 8, 15, 16, 23, 42}


all_vals.remove(a1)
all_vals.remove(a2)
all_vals.remove(a3)
all_vals.remove(a4)
all_vals.remove(a5)

a6 = all_vals.pop()

print("!", a1,a2,a3,a4,a5,a6)

