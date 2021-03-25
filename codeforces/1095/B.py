n = int(input())
a = list(map(int, input().split()))
b = a.copy()

mx = max(a)
mn = min(a)


a.remove(mx)
b.remove(mn)


amx = max(a)
amn = min(a)


bmx = max(b)
bmn = min(b)

print(min(amx-amn, bmx - bmn))