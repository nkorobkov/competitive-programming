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
    n,k = line()
    s = inp()
    debug(s.split()[0].strip('.'))
    s = s.split()[0].strip('.') 

    #..***..*.*.
    last_x = -1
    distance_since_last_x = 0
    setx = 0
    probable_x = -1 
    for i in range(len(s)):
        c = s[i]
        distance_since_last_x= i-last_x if last_x >= 0 else -1
        debug(i,c,last_x,probable_x)

        if i == len(s)-1:
            setx +=1 
            break

        if last_x == -1 and c == '.':
            continue
        if last_x != -1 and c == '*':
            probable_x = i
        if last_x == -1 and c == '*':
            setx+=1
            last_x = i
            continue
            
        if distance_since_last_x >= k:
            if probable_x == -1:
                debug('error', i, c, last_x)
            last_x = probable_x
            probable_x = -1
            setx+=1

    print(setx)



def main():
    #solve()
    testcase(number())
if __name__ == "__main__":
    main()
