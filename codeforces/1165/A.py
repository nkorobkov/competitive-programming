n, x,y = list(map(int, input().split()))
s = input()

s =  s[-x:]

#print(s, s[x-y-1])
res = 0

if s[x-y-1] == '0':
    res += 1

#print(s[x-y:])
#print(s[:x-y-1])


res += s[:x-y-1].count('1')
res += s[x-y:].count('1')

print(res)