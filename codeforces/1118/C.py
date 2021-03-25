from collections import Counter


n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

def printv(v,n,  stri = [], mid=[]):
    if n%2 == 0:
        ans = []
        for i in range(n//2):
            string = []
            for j in range(n//2):
                string.append(v[i*(n//2) + j])
            ans.append(string + string[::-1])
        ans = ans+ans[::-1]
        return ans
    else:
        ans = []
        for i in range(n // 2):
            string = []
            for j in range(n // 2):
                string.append(v[i * (n // 2) + j])
            ans.append(string +[stri[i]]+ string[::-1])

        middle = stri[n//2:] + mid + list(reversed(stri[n//2:]))
        ans = ans+ [middle]+ ans[::-1]
        return ans



def solve(n, c):
    vals = []
    for key in c:
        if c[key]>=4:
            vals.extend([key]*(c[key]//4))
            c[key] = c[key]%4

    if n %2 == 1:

        mid = []
        stri = []
        for key in c:
            if c[key] != 0:

                if c[key] >= 2:
                    stri.append(key)
                    c[key] = c[key]%2

                if c[key]== 1:
                    mid.append(key)

        if len(vals)>(n//2)**2:
            k = 0
            for i in range(len(vals) - (n//2)**2):
                stri.extend([vals[i]]*2)
                k = i
            vals = vals[k+1:]

        if len(vals) != (n//2)**2:
            return 0,1,0,0

        if len(stri)  != n -1:
            return 0,2,0,0
        if len(mid)>1:
            return 0,3,0,0


        return 2, vals, stri, mid


    else:
        if sum(c.values()) > 0:
            return 0,0,0,0
        else:
            return 1, vals,0,0



r, v, s, m = solve(n, c)
if r>0:
    print("YES")
    v = printv(v, n, s, m)
    for i in v:
        for j in i:
            print(j, end=" ")
        print()
else:
    print("NO")
