n = 2
f = 2000
d = 2000
from random import sample

print(n)
for i in range(n): 
    print(f, d)
    for k in range(d):
        print(i, ' '.join(sample(list(map(str, list(range(1, f)))),f-4)))
