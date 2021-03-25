import random


def f(n, d):
    p = []
    to_resolve = 1

    for i in range(n):
        candidates = d[to_resolve]
        if candidates[1] in d[candidates[0]]:
            to_resolve = candidates[0]
        else:
            to_resolve = candidates[1]
        p.append(to_resolve)

    return p


def gen_data(n):
    l = range(1, n + 1)
    p = random.sample(l, n)
    d = {}
    for i in range(1, n + 1):
        d[p[i%n]] = tuple(random.sample([p[(i+1) %n], p[(i+2) % n]], 2))

    return n, d, p


def compare(p1, p2):
    n = len(p1)
    i1 = p1.index(1)
    i2 = p2.index(1)

    for i in range(len(p1)):
        if p1[i1] != p2[i2]:
            return False
        i1 = (i1 + 1) % n
        i2 = (i2 + 1) % n

    return True


def test(k, n):
    for i in range(k):
        n, d, p = gen_data(n)

        p2 = f(n, d)
        if not compare(p, p2):
            print(p)



n, d, p = gen_data(4)

p2 = f(n, d)
print(p2, p, d)
print(compare(p, p2))

test(100, 4)