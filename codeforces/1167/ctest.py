import random
n , m, s = 100000, 200, 500
print(n, m)

for i in range(1,m+1):
    print('{} {}'.format(s, ' '.join(list(map(str, random.sample(range(1, n), s))) )))
