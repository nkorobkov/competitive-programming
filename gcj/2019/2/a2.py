
def solve():
    n = int(input())

    m = []

    difs = set()

    for i in range(n):
        c, j = list(map(int, input().split()))
        for mol in m:
            cd = c - mol[0]
            jd = j - mol[1]
            if cd > 0 and jd<0 or (cd<0 and jd>0):
                difs.add(cd/jd)
        m.append((c, j))

    return len(difs) + 1



n = int(input())

for i in range(1,n+1):
    a = solve()
    print("Case #{}: {}".format(i, a))


