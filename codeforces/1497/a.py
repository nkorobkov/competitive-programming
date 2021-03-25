from collections import Counter


def solve(l):
    c = Counter(l)
    #print(c.keys())
    ll = list(c.keys())
    for g in ll:
        l.remove(g)

    return ' '.join(map(str, sorted(ll) + l))


cases = int(input())
for ii in range(cases):
    m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    print(solve(l))
