import  math

n, R = tuple(map(int, input().split()))

al = 2 * math.pi/n

beth = (math.pi - al)/2

sal = math.sin(al)
sbeth = math.sin(beth)

sab = sal/sbeth

r = R * sab / (2. - sab)

print(r)

