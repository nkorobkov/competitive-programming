import sys, math, os
from math import factorial, inf, gcd, pi, sqrt, ceil
from heapq import *
from functools import *
from itertools import *
from collections import *
sys.setrecursionlimit(10**5)

if os.environ.get('HOME') == '/Users/clarity':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    inp = open('C_test.txt', 'r').readline

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
    res = 0
    tot_add_so_far = 0
    d = {}
    countd = {}
    s = line()
    for i, k in enumerate(s):
        res += tot_add_so_far
        #print(i, k, tot_add_so_far)
        if k in d:
            res += d[k]
            tot_add_so_far += d[k]
            d[k] += i + 1
        else:
            countd[k] = i+1
            d[k] = i+1
        #print(res)
    print(res)

def main():
    testcase(number())

if __name__ == "__main__":
    main()
