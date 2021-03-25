n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))

b = sorted(a, reverse=True)
middle = b[m*k-1]
nm = b[:m*k].count(middle)
sum = sum(b[:m*k])

ind = []
c = 0
cut = 0
cm = 0

for i  in range(len(a)):
    if a[i]>= middle:
        if a[i] == middle:
            if cm < nm:
                cm+=1
                c+=1
        else:
            c+=1
    if c == m:
        c = 0
        cut +=1
        ind.append(i+1)
    if cut == k-1:
        break

print(sum)
print(' '.join(list(map(str, ind))))




