n, k = map(int, input().split())



def move_byte(s, times):
    k = s[0]
    if s[0] < times:
        s = move_byte(s, k)
        return move_byte(s, times-k)
    if s[0] == times:
        #if len(s) == 1 ?
        s[1] += s[0]*2
        s = s[1:]
        return s
    elif times == 0:
        return s
    else:
        s[1] += times*2
        s[0] -= times
        return s

def s2print(s):
    top_byte = len(s)
    tv = 2 ** (top_byte - 1)
    k = []
    for n in s:
        k.extend([tv] * n)
        tv = tv//2
    return ' '.join(map(str, k))

binn = "{0:b}".format(n)
s = list(map(int, binn))

ones = sum(s)


if ones > k or k > n:
    print('NO')
else:
    s = move_byte(s, k - ones)
    print('YES')
    print(s2print(s))

