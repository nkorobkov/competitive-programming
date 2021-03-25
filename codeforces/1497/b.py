from collections import Counter


def solve(m, l):
    l = map(lambda x: x % m, l)
    c = Counter(l)
    res = 0
    #print(c)
    if m % 2 == 0:
        for i in range(1, (m // 2)):
            sm = c[i]
            lg = c[m - i]
            if sm == lg and sm != 0:
                res += 1
            elif abs(sm - lg) == 1:
                res += 1
            else:
                if sm == 0 and lg == 0:
                    pass
                elif sm == 0 or lg == 0:
                    res += max(sm, lg)
                else:
                    res += 1
                    res += max(sm, lg) - (min(sm, lg) + 1)
            print i, m - i, sm, lg, res
        if c[m // 2] > 0:
            res += 1
    else:
        for i in range(1, (m // 2) + 1):
            sm = c[i]
            lg = c[m - i]
            if sm == lg and sm != 0:
                res += 1
            elif abs(sm - lg) == 1:
                res += 1
            else:
                if sm == 0 and lg == 0:
                    pass
                elif sm == 0 or lg == 0:
                    res += max(sm, lg)
                else:
                    res += 1
                    res += max(sm, lg) - (min(sm, lg) + 1)
        #print(i, sm,lg, res)
    if c[0] > 0:
        res += 1
    return res


cases = int(input())
for ii in range(cases):
    _, m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    print(solve(m, l))
