
def solve():
    n = int(input())
    a = []
    for i in range(n):
        s, e = input().split()
        a.append((int(s), int(e)))

    a = list(enumerate(a))
    #print(a)
    a.sort(key = lambda x: x[1][0])
    #print(a)

    r = ''
    c_f = True
    j_f = True
    cft = 25*60
    jft = 25*60

    for task in a:
        start = task[1][0]
        end = task[1][1]

        if start >= cft:
            c_f = True
            cft = 25*60
        if start >= jft:
            j_f = True
            jft = 25*60

        if c_f:
            r += ('C')
            c_f = False
            cft = end
        elif j_f:
            r +=('J')
            j_f = False
            jft = end
        else:
            return 'IMPOSSIBLE'
    #print(r)
    ts = [(a[i][0], r[i]) for i in range(len(a))]
    ts.sort()
    #print(ts)
    r = ''.join([j[1]for j in ts])
    #print(r)
    return r




n = int(input())

for i in range(1,n+1):
    a = solve()
    print("Case #{}: {}".format(i, a))


