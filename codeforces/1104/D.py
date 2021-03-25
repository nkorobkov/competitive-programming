import sys
from sys import stdout

def send(x):
    print('!', x)
    s = input()
    if s != 'start':
        sys.exit(0)


def check(x, y):
    print("?", x, y)
    s = input()
    if s =='x':
        return 1
    if s == 'e':
        sys.exit(0)
    else:
        return 0


def play():
    r = check(0, 1)
    if r:
        send(1)
    r = check(1,2)
    if r:
        send(2)

    amin = 2

    #  (amin, amax]


    while True:
        r = check(amin, amin*2)
        if r:
            amax = amin*2
            break
        else:
            amin = amin*2


    # binsearch ws amin

    # (l, r]
    base = amin
    l = amin
    r = amax

    while True:
        if l == r:
            return l
        m = (l+r)//2
        if l == m:
            return r
        a = check(base, m)
        # 1 means x <= m

        if a:
            r = m
        else:

            l = m

s = input()
while True:
    send(play())

