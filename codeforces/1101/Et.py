n = 500000
print(n)
for i in range(n):
    if i%1:
        print('+', i, i+2)

    else:
        print('?', i+3, i+4)
