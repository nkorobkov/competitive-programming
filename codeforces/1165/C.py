n = int(input())
a = input()

odd, even = 0, 0

ps = '1'

chett = []

i = 0
ans = 0
new_s = []
pk = 'c'
for l in a:
    i += 1
    if l == ps:
        if i%2 == 0:
            k = 'n'
        else:
            k = 'c'
        if k == pk:
            new_s.append(l)
        else:
            ans += 1
        pk = k

    else:
        new_s.append(l)
    ps = l

if len(new_s) % 2 == 1:
    new_s = new_s[:-1]
    ans +=1
print(ans )
print( ''.join(new_s))