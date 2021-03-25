from collections import deque

n, k = list(map(int, input().split()))
ans = 0

pos_c = k*(k-1)

if n<= pos_c:
    print("YES")
    ans = deque()
    round = 1
    for i in range((n//2)):

        ans.append((i%k+1, (i+round)%k+1))
        ans.appendleft(((i+round)%k+1, (i)%k+1))
        if (i + 1) % (k // round) == 0:
            round += 1
    i = (n//2)+1
    if n%2 == 1:
        ans.append((i % k + 1, (i + round) % k + 1))
        t = ans[-1]
        ans[-1] = ans[-2]
        ans[-2] = t
    for a in ans:
        print(a[0], a[1])


else:
    print("NO")