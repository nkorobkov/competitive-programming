import sys, math, os
from math import factorial, inf, gcd, pi, sqrt, ceil
from heapq import *
from functools import *
from itertools import *
from collections import *
sys.setrecursionlimit(10**5)

if os.environ.get('HOME') == '/Users/clarity':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    inp = open('A_test.txt', 'r').readline

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
    ss = []
    for i in range(n):
        a,b = line()
        ss.append([a,b])
    t = line()

    in_time = 0
    if len(ss) >= 2:
        in_time = ss[-2][1] + t[-1] 
    else:
        in_time = ss[-1][0] + t[0]
    
    prev_dep_delay = 0
    for i in range(n):
        at_st_s = ss[i][0]
        depart_s = ss[i][1]
        delay = t[i]

        at_st_r = at_st_s + delay + prev_dep_delay
        depart_r = max(depart_s, at_st_r + ceil((depart_s-at_st_s)/2))

        prev_dep_delay = depart_r - depart_s

    print(at_st_r)

def main():
    #solve()
    testcase(number())

if __name__ == "__main__":
    main()
