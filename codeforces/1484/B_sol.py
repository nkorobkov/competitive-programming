import sys, math, os
from math import factorial, inf, gcd, pi, sqrt, ceil
from heapq import *
from functools import *
from itertools import *
from collections import *
sys.setrecursionlimit(10**5)

if os.environ.get('HOME') == '/Users/clarity':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    inp = open('B_test.txt', 'r').readline

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
    if n == 1:
        print(0)
        return
    diffs = [a[i+1] - a[i] for i in range(len(a)-1)]
    c = list(set(diffs))
    #debug(c)
    if len(c) > 2:
        print(-1)
    elif len(c) == 1:
        print(0)
    elif 0 in c:
        print(-1)
    else:
        m = abs(c[0] - c[1])
        if m <= max(a):
            print(-1)
        else:
            print(m, max(c))
    

def main():
    #solve()
    testcase(number())

if __name__ == "__main__":
    main()
