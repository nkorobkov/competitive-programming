import sys


def solve():
    r = [0, 0, 0, 0, 0, 0]

    print('42')
    sys.stdout.flush()

    d42 = int(input())
    if d42 < 0:
        sys.exit()

    print('210')
    sys.stdout.flush()

    d210 = int(input())
    if d210 < 0:
        sys.exit()

    two42 = 2 ** 42
    two52 = 2 ** 52

    r[0] = d42 // two42
    r[1] = d42 % (2 ** 42) // (2 ** 21)

    r[3] = d210 // two52
    r[4] = d210 % two52 // two42
    r[5] = d210 % two42 // (2 ** 35)

    r[2] = (d42 % (2 ** 21) - (r[3] * (2 ** 10) + r[4] * (2 ** 8) + r[5] * (2 ** 7))) // (2 ** 14)

    return r


n, w = list(map(int, input().split()))

for i in range(1, n + 1):

    r = solve()

    print(" ".join(list(map(str, r))))
    sys.stdout.flush()

    a = int(input())
    if a < 0:
        sys.exit()
