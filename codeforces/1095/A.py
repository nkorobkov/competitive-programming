n = int(input())
s = input()
k = ''
cs = 0
for i in range(n):
    try:
        k += s[cs + i]
    except IndexError:
        break
    cs += i+1

print(k)
