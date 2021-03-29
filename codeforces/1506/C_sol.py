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

def findLongestEqualString(a,b):
    if len(a) != len(b):
        debug('error', a,b)
    k = 0
    maxx = -1
    for i in range(len(a)):
        if a[i] == b[i]:
            k +=1
        else:
            maxx = max(maxx, k)
            k = 0
    return max(maxx, k)
   
def solve():
    a = inp().split()[0]
    b = inp().split()[0]
    tot_len = len(a)+len(b)-1

    add_to_a_left = tot_len-len(a)
    add_to_a_right = 0
    add_to_b_left = 0
    add_to_b_right = tot_len-len(b)
    debug(tot_len,add_to_a_left,add_to_a_right,add_to_b_left,add_to_b_right)
    max_c_substr = -1

    for i in range(len(a) + len(b) -1):
        aa = ('1'*add_to_a_left)+a+('1'*add_to_a_right)
        bb = ('2'*add_to_b_left)+b+('2'*add_to_b_right)
        #
        # debug(aa,bb)
        m = findLongestEqualString(aa, bb)
        max_c_substr = max(max_c_substr, m)
        if(add_to_a_left != 0):
            add_to_a_left  -=1
            add_to_a_right +=1
        else:
            add_to_b_left  +=1
            add_to_b_right -=1
    
    op = len(a) - max_c_substr + len(b) - max_c_substr
    print(op)


def main():
    #solve()
    testcase(number())

if __name__ == "__main__":
    main()
