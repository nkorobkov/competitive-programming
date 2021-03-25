
def solve(k):
    s = str(k)
    r = []
    for c in s:
        if c == '4':
            r.append('1')
        else:
            r.append('0')
    one = int(''.join(r))
    return one, k-one


n = int(input())

for i in range(1,n+1):
    c = int(input())
    a, b = solve(c)
    print("Case #{}: {} {}".format(i, a, b))


