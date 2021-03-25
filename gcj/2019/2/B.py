import sys

def put(v, p):
    print(v, p)
    sys.stdout.flush()

def check(v):

    print(v, 0)

    sys.stdout.flush()

    n = input().split()
    return int(n[0])

def solve():
    vv = list(range(1, 13)) * 5
    for p, v in zip(range(1, 61), vv):
        a = input()
        put( v, 100)

    vv = list(range(13, 21))
    mini = -1
    minv = 100
    for p, v in zip(range(61, 69), vv):
        a = input()
        n = check(v) + ((69-p)/20)

        if n<minv:
            mini = v
            minv = n

    a = input()
    put(mini, 100)

    vv.remove(mini)

    for p, v in zip(range(70,98), vv*4):
        a = input()
        put(v, 100)

    a = input()
    put(vv[0],100)
    a = input()
    put(vv[2],100)
    a = input()
    put(vv[1], 100)







n = int(input())

for i in range(1,n+1):

    solve()

