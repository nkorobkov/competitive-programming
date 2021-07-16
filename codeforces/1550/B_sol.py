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
    n,a,b = line()
    s = inp().strip()
    if b >= 0: 
        print(n * (a+b))
        return
    swaps = 0
    c = s[0]
    for char in s[1:]:
        if char != c:
            swaps +=1
            c = char
    
    if swaps %2 == 0: 
        x = (swaps//2) +1
        print(x* b + n*a)
    else:
        x = (swaps//2) + 2
        print(x* b + n*a)


def main():
    testcase(number())

if __name__ == "__main__":
    main()
