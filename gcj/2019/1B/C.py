
def solve(n, k):

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    ans = 0

    for i in range(n+1):
        for j in range(i+1, n+1):
            #print(i, j)
            xm = max(x[i:j])
            ym = max(y[i:j])
            if abs(xm-ym) <=k:
                ans +=1
    return ans



n = int(input())

for i in range(1,n+1):
    n, k = list(map(int, input().split()))

    y = solve(n, k)
    print("Case #{}: {}".format(i, y))
