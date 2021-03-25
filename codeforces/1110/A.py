a = input().split()

b, k = list(map(int, a))

a = list(map(int, input().split()))

if b%2 == 0:
    if a[-1] %2 == 0:
        print('even')
    else:
        print('odd')
else:
    if sum(a) %2 == 0:
        print('even')
    else:
        print('odd')