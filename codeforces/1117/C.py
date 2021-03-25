x, y = list(map(int, input().split()))
x1, y1 = list(map(int, input().split()))

a = list(map(int, input().split()))

s = list(input().split())

wind = [0, 0]

for el in s:
    if el == 'U':
        wind[1] +=1
    if el == 'D':
        wind[1] -= 1
    if el == 'L':
        wind[0] -= 1
    if el == 'R':
        wind[0] += 1

dest = [x1-x, y1-y]

a = sum(dest)
b = dest[0]-wind[0] + dest[1] - wind[1]

improve_pt = a-b + len(s)




