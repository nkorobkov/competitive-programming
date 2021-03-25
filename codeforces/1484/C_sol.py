import sys, math, os
from math import factorial, inf, gcd, pi, sqrt, ceil
from heapq import *
from functools import *
from itertools import *
from collections import *
sys.setrecursionlimit(10**5)
from io import BytesIO,IOBase


BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


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
    friends, days = line()
    f = []
    daysets = []
    d_options_c = defaultdict(int)
    frienddays = [list() for x in range(friends+1)]
    all_friends = list(range(1, friends+1))
    for i in range(days):
        l = line()
        f.extend(l[1:])
        daysets.append(set(l[1:]))
        d_options_c[i] = len(l)-1
        for friend in l[1:]:
            frienddays[friend].append(i)

     #daysets[4] -- friends avaliable on day 4
     #frienddays[9] -- days when friend 9 is avaliable
    f_avaliability_c = Counter(f)
    #debug(f_avaliability_c,d_options_c)
    solution = [0]*days
    ok_treshold = ceil(days/2)
    used = defaultdict(int)

    least_avaliable_friends = sorted(all_friends, key= lambda x: - f_avaliability_c.get(x,0))


    for (day, options) in sorted(d_options_c.items(), key=lambda x: x[1]):
        # fill the day with the least avaliable friend
        avaliable_friends = list(least_avaliable_friends)

        while solution[day] == 0:
            if len(avaliable_friends) == 0: 
                print('NO')
                return 
            least_avaliable_friend = avaliable_friends.pop()
            if least_avaliable_friend not in daysets[day]:
                continue
            if f_avaliability_c[least_avaliable_friend] < ok_treshold - used[least_avaliable_friend]:
                for d in frienddays[least_avaliable_friend]:
                    solution[d] = least_avaliable_friend
                least_avaliable_friends.remove(least_avaliable_friend)
                continue
            if used[least_avaliable_friend] < ok_treshold:
                solution[day] = least_avaliable_friend
                used[least_avaliable_friend] += 1

    print('YES') 
    print_array(solution)


    


def main():
    #solve()
    testcase(number())
if __name__ == "__main__":
    main()
