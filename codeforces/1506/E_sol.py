import sys, math, os
from math import factorial, inf, gcd, pi, sqrt, ceil
from heapq import *
from functools import *
from itertools import *
from collections import *
sys.setrecursionlimit(10**5)

if os.environ.get('HOME') == '/Users/clarity':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    inp = open('E_test.txt', 'r').readline

    def debug(*args):
        print(*args, file=sys.stderr)
else:
    inp = sys.stdin.readline

    def debug(*args):
        pass


def line(): return list(map(int, inp().rstrip().split()))
def fline(): return list(map(float, inp().rstrip().split()))
def number(): return int(inp())
def print_array(l): print(' '.join(list(map(str, l))))

def testcase(t):
    for p in range(t):
        solve()

def solve():
    n = number()
    a = line()
    la = len(a)
    ns = set(range(1,la+1))

    minp = [-1] * la
    maxp = [-1] * la
    minp[0] = a[0]
    maxp[0] = a[0]
    curmax = a[0]-1
    ns.remove(a[0])
    curmin = 1 if a[0] != 1 else 2
    for i in range(1,la):
        if a[i] != a[i-1]:
            maxp[i] = a[i]
            minp[i] = a[i]
            curmax = a[i]-1
            while curmax not in ns:
                curmax-=1
            ns.remove(a[i])
        else:
            minp[i] = curmin
            ns.remove(curmin)
            curmin+=1
            
            maxp[i] = curmax
            curmax-=1
    print_array(minp)
    print_array(maxp)

            






def main():
    #solve()
    testcase(number())

if __name__ == "__main__":
    main()
