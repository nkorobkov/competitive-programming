import sys


def check(x, y):
    print(x, y)
    sys.stdout.flush()

    r = input()
    if r == 'HIT':
        return 'H'
    if r == 'MISS':
        return 'M'
    if r == 'CENTER':
        return 'C'
    else:
        exit(0)

def find_p(fy,fx,sy,sx):
    dely = fy - sy
    delx = fx - sx

    # [ )
    # bin search here to find center
    while abs(delx) > 1 and abs(dely) > 1:

        cx = sx + delx//2
        cy = sy + dely//2
        r = check(cx, cy)
        if r == 'H':
            fx = cx
            fy = cy
        elif r == 'M':
            sx = cx
            sy = cy
        elif r == 'C':
            return 'end'
        dely = fy - sy
        delx = fx - sx

    return (fx+sx)//2, (fy+sy) // 2


def find_ccenter(x1, y1, x2, y2, x3, y3):
    x12 = x1 - x2
    x13 = x1 - x3

    y12 = y1 - y2
    y13 = y1 - y3

    y31 = y3 - y1
    y21 = y2 - y1

    x31 = x3 - x1
    x21 = x2 - x1

    # x1^2 - x3^2
    sx13 = pow(x1, 2) - pow(x3, 2)

    # y1^2 - y3^2
    sy13 = pow(y1, 2) - pow(y3, 2)

    sx21 = pow(x2, 2) - pow(x1, 2)
    sy21 = pow(y2, 2) - pow(y1, 2)

    f = (((sx13) * (x12) + (sy13) *
          (x12) + (sx21) * (x13) +
          (sy21) * (x13)) // (2 * ((y31) * (x12) - (y21) * (x13))))

    g = (((sx13) * (y12) + (sy13) * (y12) +
          (sx21) * (y13) + (sy21) * (y13)) //
         (2 * ((x31) * (y12) - (x21) * (y13))))

    # eqn of circle be x^2 + y^2 + 2*g*x + 2*f*y + c = 0
    # where centre is (h = -g, k = -f) and
    # radius r as r^2 = h^2 + k^2 - c
    h = round(-g)
    k = round(-f)
    return h, k


def solve():
    center = False
    to_check = [[0, 0],
                [-(10 ** 9) // 2, 0],
                [0, -(10 ** 9) // 2],
                [0, (10 ** 9) // 2],
                [(10 ** 9) // 2,0],
                [-(10 ** 9) // 2, -(10 ** 9) // 2],
                [-(10 ** 9) // 2, (10 ** 9) // 2],
                [(10 ** 9) // 2, -(10 ** 9) // 2],
                [(10 ** 9) // 2, (10 ** 9) // 2]]

    i = 0
    f = 0
    while f < 2 and i< 9:
        r = check(to_check[i][0], to_check[i][1])
        if r == 'H':
            f += 1
            if f == 1:
                center = to_check[i]
            else:
                center = [(center[0] + to_check[i][0])//2, (center[1] + to_check[i][1])//2 ]
        i+=1
        if r == 'C':
            return

    # have our center.
    #print('found center', center)
    # need to find 3 points on the circle.
    point1 = find_p(center[0],center[1], - (10**9) -3, - (10**9) -3 )
    if point1 == 'end':
        return
    point2 = find_p(center[0], center[1], -(10**9) -3, (10**9) -3)
    if point2 == 'end':
        return
    point3 = find_p(center[0], center[1], (10**9 -3), (10**9 -3))
    if point3 =='end':
        return


    # now have 3 points got to find middle of the circle
    center_x , center_y = find_ccenter(point1[0], point1[1], point2[0], point2[1],point3[0], point3[1])
    sys.stderr.write(str(center_x) + '  ' + str(center_y) + ' ' + str(point1)+ ' ' + str(point2)+ ' ' + str(point3) + '\n\n')
    # now need to fire in spiral untill hit

    for i in range(center_x - 5, center_x + 6):
        for j in range(center_y - 5, center_y + 6):
            #sys.stderr.write(str(i) + str(j) +  '\n\n')

            if check(i, j) == 'C':
                return

    return



n = input().split()
n = int(n[0])
for i in range(1, n+1):
    solve()

