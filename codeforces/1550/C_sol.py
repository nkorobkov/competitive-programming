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

class Cont:
    ans = 0
    len = -1
    # True = up
    trip_dir= None
    quad_range = None

    def __init__(self, arr) -> None:
        self.arr = arr

    def add(self, v):
        debug(v,self.ans, self.trip_dir, self.quad_range)
        
        if self.quad_range:
            if self.quad_range[0] < v < self.quad_range[1]:
                self.ans +=1 # for quad

        if self.trip_dir is not None:
            notr = False
            if self.trip_dir and v < self.arr[self.len]:
                self.ans +=1 #trips is good
            elif not self.trip_dir and v > self.arr[self.len]:
                self.ans +=1 #trips is good
            else:
                notr = True
            # update quad range
            if notr or (min(self.arr[self.len], self.arr[self.len-1]) <= v <= max(self.arr[self.len], self.arr[self.len-1])):
                self.quad_range = None
            else:
                if self.arr[self.len-1] == v:
                    self.quad_range = None
                else:
                    self.quad_range = [
                        min(self.arr[self.len], v), max(self.arr[self.len], v)
                    ]

       
        if self.len == -1:
            self.ans +=1
        else:
            self.ans +=2 # for 1 and 2
            if v != self.arr[self.len]:
                self.trip_dir = v > self.arr[self.len]
            else:
                self.trip_dir = None
                self.quad_range = None

        self.len +=1 




def solve():
    n = number()
    l = line()
    c = Cont(l)
    for ll in l:
        c.add(ll)
    print(c.ans)

def main():
    testcase(number())

if __name__ == "__main__":
    main()
