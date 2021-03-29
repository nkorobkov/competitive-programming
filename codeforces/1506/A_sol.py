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

# y from 1 --- line
# x from 1 -- position

def col_to_cor(n,m,xx):

    #n -- lines
    line = ((xx-1)%n)+1
    col = (xx-1)//n +1 
    return col, line

def cor_to_row(n,m,x,y):
    return m*(y-1) + x 

def solve():
    n, m , x = line()

    xx, yy = col_to_cor(n,m,x)

    print (cor_to_row(n,m,xx,yy))




def main():
    #solve()
    testcase(number())

if __name__ == "__main__":
    main()
