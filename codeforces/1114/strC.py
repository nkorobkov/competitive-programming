mn = 40
mb = 36
import string
digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)
from C import solve

from math import factorial
for n in range(3, mn+1):
    nf = factorial(n)
    for b in range(3, mb):

        bb  = int2base(nf, b)

        k = len(bb) - len(bb.strip('0'))



        kk = solve(n, b)
        if kk != k:

            print(k, kk,int2base(nf, b), n , b)