
def solve():
    k = input().split()
    x, y = int(k[0]), int(k[1])

    valid = {
        '01': 'N',
        '03':'NN',
        '23':'SEN',
        '12':'NE',
        '34':'NNE',
        '10': 'E',
        '30': 'EE',
        '32': 'WNE',
        '21': 'EN',
        '43': 'EEn',
    }

    if str(abs(x)) + str(abs(y)) in valid:
        r = valid[str(abs(x)) + str(abs(y))]
        if x<0:
            r = r.replace('N','S')
        if y<0:
            r = r.replace('E','W')
    else:
        r = "IMPOSSIBLE"
    return r



n = int(input())

for i in range(1,n+1):
    a = solve()
    print("Case #{}: {}".format(i, a))


