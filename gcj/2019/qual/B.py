def solve(k):

    r = []
    for c in k:
        if c == 'S':
            r.append('E')
        else:
            r.append('S')
    one = (''.join(r))
    return one


n = int(input())

for i in range(1,n+1):
    ms = int(input())
    path = input()

    s = solve(path)
    print("Case #{}: {}".format(i, s))
