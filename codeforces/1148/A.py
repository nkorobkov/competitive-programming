a, b, c = list(map(int,input().split()))

r = c*2
if a ==  b:
    r += a+b
else:
    r +=  2*min(a,b) + 1

print(r)

