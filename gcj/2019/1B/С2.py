
def find_index_right(x, minv):
    for i in range(len(x)):
        if x[i]<= minv:
            return i+1
    return -1

def find_index_left(x, minv):
    for i in range(1,len(x)+1):
        if x[-i]<= minv:
            return i
    return -1



# [l, r)
def solve_part(x, y,l, r):

    print(l, r)
    if l == r:
        return 0
    ans = 0
    maxx = max(x[l: r])
    maxy = max(y[l: r])

    maxxi = l + x[l: r].index(maxx)
    maxyi = l + y[l: r].index(maxy)



    if maxx>maxy:
        minpy = maxx-k
        if maxy >= minpy:
            left_index = maxxi - find_index_left(y[l: maxxi], minpy)
            right_index = maxxi + find_index_right(y[maxxi: r], minpy)
            ans += (left_index-l)*(r-right_index)


        return solve_part(x, y,l, maxxi) + solve_part(x, y, maxxi + 1, r) + ans
    else: #y>x
        minpx = maxy - k

        if maxx >= minpx:

            left_index = maxxi - find_index_left(x[l: maxyi], minpx)
            right_index = maxxi + find_index_right(x[maxyi: r], minpx)
            ans += (left_index - l) * (r - right_index)

        return solve_part(x, y, l, maxyi) + solve_part(x, y, maxyi + 1, r) + ans



def solve(n, k):

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    ans = solve_part(x, y, 0, n)
    return ans



n = int(input())

for i in range(1,n+1):
    n, k = list(map(int, input().split()))

    y = solve(n, k)
    print("Case #{}: {}".format(i, y))
