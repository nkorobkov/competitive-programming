def solve(c, n):
    decode = [0]* (len(c)+1)
    cm = min(c)
    pff = 0

    for i  in range(len(c)):
        if c[i] == cm and pff == 0:
            #factorize
            start = cm//n - int(cm//n % 2 == 0)
            for pf in range(start, n,2):
                if cm % pf == 0:
                    pff = pf
                    decode[i] = cm/pff
        if pff != 0:
            decode[i+1] =  pff

    pass


nn = int(input())

for i in range(1,nn+1):
    n, l = list(map(int, input().split()))
    c = list(map(int, input().split()))

    s = solve(c, n)
    print("Case #{}: {}".format(i, s))
