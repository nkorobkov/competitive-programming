n = int(input())

pos = []
neg = []

for i  in range(n):
    a,  b = list((map(int, input().split())))

    if a  < b:
        pos.append((a, b, i))
    else:
        neg.append((-b, -a, i))



def solve(pairs):
    inds  =  list(map(lambda x:x[2]+1, sorted(pairs, key=lambda x:x[1], reverse=True)))
    return inds

n = solve(neg)
p =  solve(pos)

if len(n)> len(p):
    print(len(n))
    print(' '.join(map(str, n)))
else:
    print(len(p))
    print(' '.join(map(str, p)))
