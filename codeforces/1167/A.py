

def solve(a):

    i  = a.find('8')
    if i == -1:
        return "NO"
    if len(a)-i >=11:
        return "YES"
    return "NO"

n = int(input())

for i in range(1, n+1):
    k = int(input())
    a = input()

    x = solve(a)


    print(x)
