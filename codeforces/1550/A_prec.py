res = []
c = 1
for i in range(1, 100):
    res.extend([i]*c)
    c+=2

print (res[:5002])

