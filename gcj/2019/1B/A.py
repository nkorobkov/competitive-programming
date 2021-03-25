from itertools import accumulate

def solve(p, q):

    X = [0]*(q+1)
    Y = [0]*(q+1)

    for k in range(p):
        xi, yi, d  = input().split()
        xi, yi = int(xi), int(yi)
        if d =="N":
            Y[yi+1] +=1
        if d == "S":
            Y[0] += 1
            Y[yi] -= 1
        if d =="E":
            X[xi+1] +=1
        if d == "W":
            X[0] += 1
            X[xi] -= 1


    Y = list(accumulate(Y))
    X = list(accumulate(X))

    y = Y.index(max(Y))
    x = X.index(max(X))

    return x, y




n = int(input())

for i in range(1,n+1):
    p, q = list(map(int, input().split()))

    x, y = solve(p, q)
    print("Case #{}: {} {}".format(i, x, y))
