n = int(input())

a = list(map(int, input().split()))

p = len(list(filter(lambda d: d > 0, a)))

z = len(list(filter(lambda d: d == 0, a)))
n = len(list(filter(lambda d: d < 0, a)))

if p >= (len(a) // 2 + len(a) % 2):
    print(1000)
elif n >= (len(a) // 2 + len(a) % 2):
    print(-1000)
else:
    print(0)
