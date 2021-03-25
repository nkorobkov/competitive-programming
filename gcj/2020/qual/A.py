
def solve():
    k = int(input())
    trace = 0
    lines = [set() for i in range(k)]
    rows = [set() for i in range(k)]
    for i in range(k):
        s = list(map(int, input().split()))
        for j in range(k):
            e = s[j]
            lines[i].add(e)
            rows[j].add(e)
            if i==j: 
                trace += e


    dlines = len(list(filter(lambda x: len(x)<k, lines)))
    drows = len(list(filter(lambda x: len(x)<k, rows)))

    return trace, drows, dlines



n = int(input())

for i in range(1,n+1):
    a, b, d = solve()
    print("Case #{}: {} {} {}".format(i, a, b, d))


