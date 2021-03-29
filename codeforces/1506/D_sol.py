import sys, math, os
from math import factorial, inf, gcd, pi, sqrt, ceil
from heapq import *
from functools import *
from itertools import *
from collections import *
sys.setrecursionlimit(10**5)

if os.environ.get('HOME') == '/Users/clarity':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    inp = open('D_test.txt', 'r').readline

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
    c = Counter(a)
    max_occ = c.most_common(1)[0][1]
    ll = len(a)
    if max_occ * 2 > ll:
        print(2*max_occ - ll)
    else: 
        print(ll - (2* (ll//2)))

    #         n = number()
    # a = line()
    # c = Counter(a)
    # max_occ = c.most_common(1)[0][1]
    # ll = len(a)
    # other_d = ll - max_occ
    # if other_d >= max_occ:
    #     print(0)
    # else: 
    #     print(max_occ-other_d)


def main():
    testcase(number())

if __name__ == "__main__":
    main()
