def gcd(x, y):
    while (y):
        x, y = y, x % y

    return x

for i in range(2, 26):

    a = 2**i -1
    mingcd = -10**12

    for b in range(1, a-1):
        mingcd = max(mingcd, gcd(b,a-b))

    print("{}:{},".format(a, mingcd))
