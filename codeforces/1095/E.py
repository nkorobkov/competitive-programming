n = input()
s = input()

o = s.count('(')
c = s.count(')')
if abs(o-c) == 2:
    if o > c:
        fo = s.find('(')+1
        lc = s.rfind(')')
        numo = s[fo:lc].count('(')
        print(numo)
    else:
        fc = s.find(')')+1
        lo = s.rfind('(')
        numc = s[fc:lo].count(')')
        print(numc)
else:
    print(0)
