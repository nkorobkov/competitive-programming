
def solve():
    s = list(map(int, input()))
    c = 0
    r = ''
    for n in s + [0]: 
        if n != c:
            if n>c:
                r += '('*(n-c)
                c = n
            else:
                r += ')'*(c-n)
                c = n
        r += str(n)

    return r[:-1]

n = int(input())

for i in range(1,n+1):
    a = solve()
    print("Case #{}: {}".format(i, a))


